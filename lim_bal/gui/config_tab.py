import tkinter as tk
from tkinter import ttk
from ..config import DEFAULT_BAUDRATES, DEFAULT_BAUDRATE
from ..utils import MockSerial
from ..i18n import t, get_config_manager


class ConfigTab:


    def __init__(self, parent, serial_manager, connection_callback=None, send_callback=None):
        self.frame = ttk.Frame(parent)
        self.serial_manager = serial_manager
        self.connection_callback = connection_callback
        self.send_callback = send_callback
        self.hardware_connected = False
        self.mock_serial = None
        self.config_manager = get_config_manager()

        self._create_widgets()
        self._update_ports()
        self._load_preferences()

    def _create_widgets(self):


        self.config_frame = ttk.LabelFrame(self.frame, text=t("ui.config_tab.configuration_frame"))
        self.config_frame.grid(column=0, row=0, padx=10, pady=10, sticky="ew")


        self.mode_label = ttk.Label(self.config_frame, text=t("ui.config_tab.mode_label"))
        self.mode_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")
        self.mode_combobox = ttk.Combobox(self.config_frame, state="readonly",
                                         values=[t("ui.config_tab.mode_hardware"), t("ui.config_tab.mode_simulated")])
        self.mode_combobox.grid(column=1, row=0, padx=10, pady=10, sticky="w")
        self.mode_combobox.set(t("ui.config_tab.mode_hardware"))
        self.mode_combobox.bind("<<ComboboxSelected>>", self._on_mode_changed)
        self.mode_combobox.bind("<<ComboboxSelected>>", self._on_preference_changed, add="+")


        self.port_label = ttk.Label(self.config_frame, text=t("ui.config_tab.port_label"))
        self.port_label.grid(column=0, row=1, padx=10, pady=10, sticky="w")


        port_frame = ttk.Frame(self.config_frame)
        port_frame.grid(column=1, row=1, padx=10, pady=10, sticky="w")

        self.port_combobox = ttk.Combobox(port_frame, state="readonly")
        self.port_combobox.grid(column=0, row=0, sticky="w")
        self.port_combobox.bind("<<ComboboxSelected>>", self._on_preference_changed)

        self.refresh_button = ttk.Button(port_frame, text="🔄", width=3,
                                       command=self._update_ports)
        self.refresh_button.grid(column=1, row=0, padx=(5, 0), sticky="w")


        port_frame.columnconfigure(0, weight=1)


        self.baudrate_label = ttk.Label(self.config_frame, text=t("ui.config_tab.baudrate_label"))
        self.baudrate_label.grid(column=0, row=2, padx=10, pady=10, sticky="w")
        self.baudrate_combobox = ttk.Combobox(self.config_frame, state="readonly",
                                            values=DEFAULT_BAUDRATES)
        self.baudrate_combobox.grid(column=1, row=2, padx=10, pady=10, sticky="w")
        self.baudrate_combobox.set(DEFAULT_BAUDRATE)
        self.baudrate_combobox.bind("<<ComboboxSelected>>", self._on_preference_changed)


        self.config_frame.columnconfigure(1, weight=1)


        self.info_frame = ttk.LabelFrame(self.frame, text=t("ui.config_tab.connection_info_frame"))
        self.info_frame.grid(column=0, row=1, padx=10, pady=10, sticky="ew")

        self.info_label = ttk.Label(self.info_frame, text="", justify="left",
                                   font=("TkDefaultFont", 9), foreground="darkgreen")
        self.info_label.grid(column=0, row=0, padx=15, pady=15, sticky="w")


        self.info_frame.grid_remove()


        self.connection_controls_frame = ttk.Frame(self.frame)
        self.connection_controls_frame.grid(column=0, row=2, padx=10, pady=10, sticky="w")

        self.connect_button = ttk.Button(
            self.connection_controls_frame,
            text=t("ui.config_tab.connect"),
            command=self._connect
        )
        self.connect_button.pack(side="left", padx=(0, 10))

        self.graph_data_var = tk.BooleanVar(value=True)
        self.graph_data_checkbox = ttk.Checkbutton(
            self.connection_controls_frame,
            text=t("ui.config_tab.graph_data"),
            variable=self.graph_data_var
        )
        self.graph_data_checkbox.pack(side="left", padx=(0, 10))

        self.si_button = ttk.Button(
            self.connection_controls_frame,
            text="SI",
            command=self._send_si,
            state="disabled"
        )
        self.si_button.pack(side="left", padx=(0, 10))

        self.sir_button = ttk.Button(
            self.connection_controls_frame,
            text="SIR",
            command=self._send_sir,
            state="disabled"
        )
        self.sir_button.pack(side="left", padx=(0, 10))

        self.zero_button = ttk.Button(
            self.connection_controls_frame,
            text=t("ui.config_tab.zero_button"),
            command=lambda: self._send_command("Z"),
            state="disabled"
        )
        self.zero_button.pack(side="left", padx=(0, 10))

        self.tare_button = ttk.Button(
            self.connection_controls_frame,
            text=t("ui.config_tab.tare_button"),
            command=lambda: self._send_command("T"),
            state="disabled"
        )
        self.tare_button.pack(side="left")

        self.send_frame = ttk.LabelFrame(self.frame, text=t("ui.config_tab.send"))
        self.send_frame.grid(column=0, row=3, padx=10, pady=10, sticky="ew")

        send_text_frame = ttk.Frame(self.send_frame)
        send_text_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        send_text_frame.columnconfigure(0, weight=1)

        self.send_text = tk.Text(send_text_frame, height=6, wrap="none")
        self.send_text.grid(row=0, column=0, sticky="nsew")
        send_vertical = ttk.Scrollbar(send_text_frame, orient="vertical", command=self.send_text.yview)
        send_vertical.grid(row=0, column=1, sticky="ns")
        send_horizontal = ttk.Scrollbar(send_text_frame, orient="horizontal", command=self.send_text.xview)
        send_horizontal.grid(row=1, column=0, sticky="ew")
        self.send_text.config(yscrollcommand=send_vertical.set, xscrollcommand=send_horizontal.set)

        self.send_button = ttk.Button(
            self.send_frame,
            text=t("ui.config_tab.send_button"),
            command=self._on_send,
            state="disabled"
        )
        self.send_button.grid(row=0, column=1, padx=10, pady=5, sticky="s")
        self.send_frame.columnconfigure(0, weight=1)

        self.receive_frame = ttk.LabelFrame(self.frame, text=t("ui.config_tab.receive"))
        self.receive_frame.grid(column=0, row=4, padx=10, pady=10, sticky="ew")

        receive_text_frame = ttk.Frame(self.receive_frame)
        receive_text_frame.pack(fill="x", padx=5, pady=5)
        receive_text_frame.columnconfigure(0, weight=1)

        self.receive_text = tk.Text(receive_text_frame, height=6, wrap="none", state="disabled")
        self.receive_text.grid(row=0, column=0, sticky="nsew")
        receive_vertical = ttk.Scrollbar(receive_text_frame, orient="vertical", command=self.receive_text.yview)
        receive_vertical.grid(row=0, column=1, sticky="ns")
        receive_horizontal = ttk.Scrollbar(receive_text_frame, orient="horizontal", command=self.receive_text.xview)
        receive_horizontal.grid(row=1, column=0, sticky="ew")
        self.receive_text.config(yscrollcommand=receive_vertical.set, xscrollcommand=receive_horizontal.set)


        self.frame.columnconfigure(0, weight=1)


############################################################################
    def set_hardware_connection(self, connected, port=""):
        self.hardware_connected = connected
        title = t("ui.config_tab.receive")
        if connected and port:
            title = f"{title} - {port}"
        self.receive_frame.config(text=title)

    def should_graph_data(self):
        return self.graph_data_var.get()

    def add_serial_data(self, line):
        if not self.hardware_connected:
            return
        self.receive_text.config(state="normal")
        self.receive_text.insert("end", line + "\n")
        self.receive_text.see("end")
        self.receive_text.config(state="disabled")

    def _on_send(self):
        data = self.send_text.get("1.0", "end-1c")
        if data and self.send_callback and self.send_callback(data):
            self.send_text.delete("1.0", "end")

    def _send_si(self):
        if self.send_callback:
            self.send_callback("SI")

    def _send_sir(self):
        if self.send_callback:
            self.send_callback("SIR")

    def _send_command(self, command):
        if self.send_callback:
            self.send_callback(command)

    def _on_mode_changed(self, event=None):

        mode = self.mode_combobox.get()
        if mode == t("ui.config_tab.mode_simulated"):

            self.port_combobox.config(state="disabled")
            self.baudrate_combobox.config(state="disabled")
            self.refresh_button.config(state="disabled")
            self.port_combobox.set("")
            self.baudrate_combobox.set("")
        else:

            self.port_combobox.config(state="readonly")
            self.baudrate_combobox.config(state="readonly")
            self.refresh_button.config(state="normal")

            if not self.baudrate_combobox.get():
                if hasattr(self.baudrate_combobox, 'config'):
                    self.baudrate_combobox.set(DEFAULT_BAUDRATES[0])
            self._update_ports()

    def _update_ports(self):

        if self.mode_combobox.get() == t("ui.config_tab.mode_hardware"):
            ports = self.serial_manager.get_available_ports()
            self.port_combobox["values"] = ports
            if ports:

                if hasattr(self, '_preferred_port') and self._preferred_port and self._preferred_port in ports:
                    self.port_combobox.set(self._preferred_port)
                else:
                    self.port_combobox.set(ports[0])

    def _connect(self):

        mode = self.mode_combobox.get()

        if self.serial_manager.is_connected:

            self.serial_manager.disconnect()
            self.send_button.config(state="disabled")
            self.si_button.config(state="disabled")
            self.sir_button.config(state="disabled")
            self.zero_button.config(state="disabled")
            self.tare_button.config(state="disabled")
            if self.connection_callback:
                self.connection_callback(False, mode, self.port_combobox.get())
            if self.mock_serial:
                self.mock_serial.stop_data_generation()
                self.mock_serial = None
            self.connect_button.config(text=t("ui.config_tab.connect"))
            self._show_config_interface()
            return


        if mode == t("ui.config_tab.mode_hardware"):
            port = self.port_combobox.get()
            baudrate = self.baudrate_combobox.get()

            if not port:
                return

            if self.serial_manager.connect(port, baudrate):
                self.connect_button.config(text=t("ui.config_tab.disconnect"))
                self._show_connection_info(mode, port, baudrate)
                self.send_button.config(state="normal")
                self.si_button.config(state="normal")
                self.sir_button.config(state="normal")
                self.zero_button.config(state="normal")
                self.tare_button.config(state="normal")
                if self.connection_callback:
                    self.connection_callback(True, mode, port)

        elif mode == t("ui.config_tab.mode_simulated"):
            try:

                self.mock_serial = MockSerial()
                virtual_port = self.mock_serial.create_virtual_port()
                self.mock_serial.start_data_generation()


                if self.serial_manager.connect(self.mock_serial, DEFAULT_BAUDRATE):
                    self.connect_button.config(text=t("ui.config_tab.disconnect"))
                    self._show_connection_info(mode, virtual_port, DEFAULT_BAUDRATE)
                    self.send_button.config(state="disabled")
                    self.si_button.config(state="disabled")
                    self.sir_button.config(state="disabled")
                    self.zero_button.config(state="disabled")
                    self.tare_button.config(state="disabled")
                    if self.connection_callback:
                        self.connection_callback(False, mode, virtual_port)


                    current_ports = list(self.port_combobox["values"])
                    if virtual_port not in current_ports:
                        current_ports.append(f"{virtual_port} (Virtual)")
                        self.port_combobox["values"] = current_ports
                        self.port_combobox.set(f"{virtual_port} (Virtual)")
                else:
                    self.mock_serial.stop_data_generation()
                    self.mock_serial = None

            except Exception as e:
                print(t("errors.virtual_port_error").format(error=e))

    def _show_config_interface(self):

        self.config_frame.grid()
        self.info_frame.grid_remove()
        self._on_mode_changed()

    def _show_connection_info(self, mode, port, baudrate):

        self.config_frame.grid_remove()
        self.info_frame.grid()


        if mode == t("ui.config_tab.mode_hardware"):
            info_text = t("ui.config_tab.connection_status").format(
                mode=mode, port=port, baudrate=baudrate)
        else:
            info_text = t("ui.config_tab.virtual_connection_status").format(
                mode=mode, port=port, baudrate=baudrate)

        self.info_label.config(text=info_text)

    def _load_preferences(self):


        saved_mode = self.config_manager.load_tab_setting('config', 'mode')
        if saved_mode:
            if saved_mode == "Hardware":
                self.mode_combobox.set(t("ui.config_tab.mode_hardware"))
            elif saved_mode == "Simulated":
                self.mode_combobox.set(t("ui.config_tab.mode_simulated"))


        saved_baudrate = self.config_manager.load_tab_setting('config', 'baudrate', DEFAULT_BAUDRATE)
        if saved_baudrate in DEFAULT_BAUDRATES:
            self.baudrate_combobox.set(saved_baudrate)


        saved_port = self.config_manager.load_tab_setting('config', 'port')
        if saved_port:

            self._preferred_port = saved_port
        else:
            self._preferred_port = None


        self._on_mode_changed()

    def _save_preferences(self):


        current_mode = self.mode_combobox.get()
        if current_mode == t("ui.config_tab.mode_hardware"):
            mode_value = "Hardware"
        elif current_mode == t("ui.config_tab.mode_simulated"):
            mode_value = "Simulated"
        else:
            mode_value = "Hardware"

        self.config_manager.save_tab_setting('config', 'mode', mode_value)
        self.config_manager.save_tab_setting('config', 'port', self.port_combobox.get())
        self.config_manager.save_tab_setting('config', 'baudrate', self.baudrate_combobox.get())

    def _on_preference_changed(self, event=None):

        self._save_preferences()

    def get_frame(self):

        return self.frame
