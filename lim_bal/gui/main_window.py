import tkinter as tk
from tkinter import ttk
import re
import time
from ..config import DEFAULT_GEOMETRY
from ..core import SerialManager
from ..i18n import t, initialize as init_i18n, get_available_languages, set_language
from .config_tab import ConfigTab
from .data_tab import DataTab
from .graph_tab import GraphTab


class MainWindow:


    def __init__(self):

        init_i18n()

        self.root = tk.Tk()
        self.root.title(t("ui.main_window.title"))
        self.root.geometry(DEFAULT_GEOMETRY)
        self._connection_started_at = None
        self._received_line_count = 0
        self._skip_data_line_after = None

        self._setup_serial_manager()
        self._create_menu()
        self._create_tabs()

    def _setup_serial_manager(self):

        self.serial_manager = SerialManager(
            data_callback=self._on_data_received,
            error_callback=self._on_error
        )

    def _create_menu(self):

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)


        self.language_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Language", menu=self.language_menu)


        self.language_vars = {}

        language_order = ["en", "pt-br", "fr", "es", "de"]
        langs_by_code = {lang['code']: lang for lang in get_available_languages()}
        for code in language_order:
            if code in langs_by_code:
                lang = langs_by_code[code]
                var = tk.BooleanVar()
                self.language_vars[lang['code']] = var
                self.language_menu.add_checkbutton(
                    label=lang['display_name'],
                    variable=var,
                    command=lambda code=lang['code']: self._change_language(code)
                )


        from ..i18n import get_current_language
        current_lang = get_current_language()
        if current_lang in self.language_vars:
            self.language_vars[current_lang].set(True)

    def _change_language(self, language_code):


        for code, var in self.language_vars.items():
            var.set(False)
        self.language_vars[language_code].set(True)


        set_language(language_code)


        from tkinter import messagebox
        messagebox.showinfo(
            "Language Changed",
            t("ui.main_window.restart_required")
        )

    def _create_tabs(self):


        self.tab_control = ttk.Notebook(self.root)


        self.data_tab = DataTab(self.tab_control)
        self.config_tab = ConfigTab(
            self.tab_control,
            self.serial_manager,
            connection_callback=self._on_connection_changed,
            send_callback=self._send_data
        )
        self.graph_tab = GraphTab(
            self.tab_control,
            self.data_tab,
            None,
            send_callback=self._send_data,
            stop_callback=self._stop_data_capture
        )


        self.tab_control.add(self.config_tab.get_frame(), text=t("ui.tabs.configuration"))
        self.tab_control.add(self.data_tab.get_frame(), text=t("ui.tabs.data"))
        self.tab_control.add(self.graph_tab.get_frame(), text=t("ui.tabs.graph"))


        self.tab_control.pack(expand=1, fill="both")

    def _on_data_received(self, line):
        received_at = time.monotonic()
        self.root.after(0, self._display_received_data, line, received_at)

    def _display_received_data(self, line, received_at=None):
        if received_at is None:
            received_at = time.monotonic()
        skip_data_line = (
            self._skip_data_line_after is not None
            and received_at > self._skip_data_line_after
        )
        if skip_data_line:
            self._skip_data_line_after = None

        elapsed = None
        if self._connection_started_at is not None:
            self._received_line_count += 1
            elapsed = time.monotonic() - self._connection_started_at
            self.config_tab.add_serial_data(
                f"{self._received_line_count} {elapsed:.3f} s | {line}"
            )

        is_identification_response = 'I4 A "1126492643"' in line
        if (
            self.config_tab.should_graph_data()
            and not skip_data_line
            and not is_identification_response
        ):
            if elapsed is None:
                self.data_tab.add_data(line)
            else:
                measurements = re.findall(
                    r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?",
                    line
                )
                if measurements:
                    self.data_tab.add_data(
                        f"{self._received_line_count} {elapsed:.3f} {' '.join(measurements)}"
                    )


    def _on_error(self, error_message):
        self.root.after(0, self.data_tab.add_message, error_message)

    def _on_connection_changed(self, connected, mode, port):
        is_hardware = connected and mode == t("ui.config_tab.mode_hardware")
        self._received_line_count = 0
        self._skip_data_line_after = None
        self._connection_started_at = time.monotonic() if is_hardware else None
        self.config_tab.set_hardware_connection(is_hardware, port if is_hardware else "")
        self.graph_tab.set_hardware_connection(is_hardware)

    def _stop_data_capture(self):
        self._skip_data_line_after = time.monotonic()
        if not self._send_data("@"):
            self._skip_data_line_after = None

    def _send_data(self, data):
        try:
            if not self.config_tab.hardware_connected:
                raise ConnectionError("Conecte uma porta no modo Hardware antes de enviar")
            self.serial_manager.send(data)
            return True
        except Exception as error:
            self.data_tab.add_message(t("ui.data_tab.send_error").format(error=error))
            return False

    def run(self):

        import time

        try:

            self._running = True
            self._last_render_time = time.time()


            self._game_loop()


            self.root.mainloop()

        finally:
            self._running = False

            if hasattr(self, 'data_tab'):
                self.data_tab.cleanup()

            self.serial_manager.disconnect()

    def _game_loop(self):

        if not self._running:
            return

        try:

            self.root.update()


            current_time = time.time()
            if hasattr(self.graph_tab, 'should_render_now'):
                if self.graph_tab.should_render_now(current_time):
                    self.graph_tab.render_frame()

        except tk.TclError:

            self._running = False
            return
        except Exception as e:
            print(f"Game loop error: {e}")


        if self._running and self.root.winfo_exists():
            self.root.after(16, self._game_loop)
