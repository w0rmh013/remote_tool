import Tkinter as tk

import frames.connectframe as connectframe
import frames.statusframe as statusframe

import raw


class MainFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.geometry('250x85+300+300')
        self.parent.title('Connect To..')
        self.parent.resizable(False, False)

        try:
            self.parent.iconbitmap('logo.ico')
        except:
            pass

        self.parent.bind('<Return>', self._enter_pressed)

        self.client = None

        self.connect_frame = connectframe.ConnectFrame(self)
        self.status = statusframe.StatusBar(self)

        self.connect_frame.cf_button.config(command=self._cf_command)

        self.connect_frame.pack()
        self.status.pack()

    def _enter_pressed(self, event):

        self.connect_frame.cf_button.focus_set()
        self.connect_frame.cf_button.invoke()

    def _cf_command(self):

        ip = self.connect_frame.ip_entry.get()

        try:
            self.client = raw.SpecialClient(ip)
        except:
            self.status.status.config(fg='red')
            self.status.set('Cannot create socket with {}'.format(ip))
        else:
            try:
                self.status.status.config(fg='blue')
                self.status.set('Connecting to {}'.format(ip))
                while self.client.socket.connect_ex(self.client.address):
                    pass

                self.client.on = self.connected = True
                self.status.status.config(fg='green')
                self.status.set('Connected successfully to {}'.format(ip))
                self.parent.destroy()

            except:
                self.status.status.config(fg='red')
                self.status.set('Cannot connect to {}'.format(ip))
