import Tkinter as tk


class StatusBar(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        """Class constructor."""

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.status = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W, width=36)
        self.status.pack(side=tk.BOTTOM)

    def set(self, format_text, *args):

        self.status.config(text=format_text % args)
        self.status.update_idletasks()

    def clear(self):

        self.status.config(text='')
        self.status.update_idletasks()
