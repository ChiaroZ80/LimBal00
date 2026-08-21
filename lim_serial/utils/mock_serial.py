import os
import threading
import time
import math
import platform
import queue

if platform.system() == "Linux":
    import pty


class MockSerial:
    def __init__(self):
        self.master_fd = None
        self.slave_port = None
        self.is_running = False
        self.data_thread = None
        self._data_queue = queue.Queue()
        self._is_open = False
        self._read_buffer = b""

    def create_virtual_port(self):
        try:
            if platform.system() == "Linux":
                self.master_fd, slave_fd = pty.openpty()
                self.slave_port = os.ttyname(slave_fd)
                os.chmod(self.slave_port, 0o666)
                os.set_blocking(self.master_fd, False)
            else:
                self.slave_port = "COM_VIRTUAL"
            self._is_open = True
            return self.slave_port
        except Exception as e:
            raise Exception(f"Erro ao criar porta virtual: {e}")

    def start_data_generation(self):
        if self.is_running:
            return
        self.is_running = True
        self.data_thread = threading.Thread(target=self._generate_data, daemon=True)
        self.data_thread.start()

    def stop_data_generation(self):
        self.is_running = False
        self._is_open = False
        if self.master_fd:
            try:
                os.close(self.master_fd)
            except:
                pass
            self.master_fd = None
        self.slave_port = None
        while not self._data_queue.empty():
            try:
                self._data_queue.get_nowait()
            except queue.Empty:
                break
        self._read_buffer = b""

    def _generate_data(self):
        index = 0
        while self.is_running:
            try:
                col1 = int(index)
                col2 = col1 * 0.01 + 2
                col3 = math.sin(10 * col2) + 2
                col4 = math.sin(20 * col2) + 0.1 + 2
                col5 = math.sin(30 * col2) + 0.2 + 2
                col6 = math.sin(40 * col2) + 0.3 + 2
                col7 = math.sin(50 * col2) + 0.4 + 2

                data = f"{col1:d} {col2:.2f} {col3:.2f} {col4:.2f} {col5:.2f} {col6:.2f} {col7:.2f}"

                if self.master_fd:
                    os.write(self.master_fd, (data + "\n").encode("utf-8"))
                else:
                    self._data_queue.put((data + "\n").encode("utf-8"))

                index += 1
                time.sleep(0.5)
            except Exception as e:
                print(f"Erro na geração de dados: {e}")
                break

    @property
    def is_open(self):
        return self._is_open

    def close(self):
        self.stop_data_generation()

    def readline(self):
        while b'\n' not in self._read_buffer:
            if self.master_fd:
                try:
                    chunk = os.read(self.master_fd, 1024)
                    if not chunk:
                        return b''
                    self._read_buffer += chunk
                except BlockingIOError:
                    if not self.is_running:
                        return b''
                    time.sleep(0.01)
                    continue
                except (OSError, IOError):
                    return b''
            else:
                try:
                    chunk = self._data_queue.get(timeout=0.1)
                    self._read_buffer += chunk
                except queue.Empty:
                    if not self.is_running:
                        return b''
                    continue

        line, self._read_buffer = self._read_buffer.split(b'\n', 1)
        return line + b'\n'

    @property
    def in_waiting(self):
        if self.master_fd:
            return 0
        return self._data_queue.qsize()

    def get_port(self):
        return self.slave_port
