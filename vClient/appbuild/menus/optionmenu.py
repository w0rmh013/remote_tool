import Tkinter as tk


class OptionMenu(tk.Menu):

    def __init__(self, parent, *args, **kwargs):

        tk.Menu.__init__(self, parent, *args, **kwargs)

        self.parent = parent
