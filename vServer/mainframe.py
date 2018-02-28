import Tkinter as tk
import time
import threading

from server import SpecialServer


class MainFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.geometry('250x85+500+500')
        self.parent.title('VisualServer 0.8')
        self.parent.resizable(False, False)

        try:
            self.parent.iconbitmap('logo.ico')
        except:
            pass

        self.server = SpecialServer()

        tk.Label(self, text='Server is up!', fg='green', font=('', 12, '')).pack(side=tk.TOP, pady=(5, 0))
        tk.Label(self, text='Up-Time', font=('', 10, '')).pack(side=tk.LEFT, padx=(5, 0))

        self.uptime_value = tk.StringVar()
        self.uptime_label = tk.Label(self, textvariable=self.uptime_value, fg='blue', font=('', 10, ''))
        self.uptime_label.pack(side=tk.LEFT)

        self.server_thread = threading.Thread(target=self._manage_server_thread)
        self.server_thread.setDaemon(True)
        self.uptime_thread = threading.Thread(target=self._timer)
        self.uptime_thread.setDaemon(True)

        self.server_thread.start()
        self.uptime_thread.start()

    def _manage_server_thread(self):

        while self.server.on:
            self.server.server_handler()
        self.parent.destroy()

    def _timer(self):

        seconds = minutes = hours = 0
        while self.server.on:
            self.uptime_value.set('{}:{}:{}'.format(hours, minutes, seconds))
            time.sleep(1)
            seconds += 1
            if not seconds % 60:
                seconds = 0
                minutes += 1
                if not minutes % 60:
                    minutes = 0
                    hours += 1
