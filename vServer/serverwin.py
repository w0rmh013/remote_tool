import Tkinter as tk

import mainframe


class VisualServerApp:

    def __init__(self):
        """Class constructor."""

        self.root = tk.Tk()
        self.mainframe = mainframe.MainFrame(self.root)

        self.mainframe.pack()
