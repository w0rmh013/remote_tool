import Tkinter as tk

import mainframe


class VisualClientApp:

    def __init__(self, client):
        """Class constructor."""

        self.root = tk.Tk()
        self.mainframe = mainframe.MainFrame(self.root)
        self.mainframe.client = client

        self.mainframe.pack()
