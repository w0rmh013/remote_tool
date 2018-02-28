import Tkinter as tk

import mainframe


class VisualClientConnectWin:

    def __init__(self):
        """Class constructor."""

        self.root = tk.Tk()
        self.main_frame = mainframe.MainFrame(self.root)

        self.main_frame.pack()
