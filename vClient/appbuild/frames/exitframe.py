import Tkinter as tk


class CloseExitFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        """Class constructor."""

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # disconnect_button & close_button commands are configured in mainframe.py

        self.disconnect_button = tk.Button(self, text='Disconnect')
        self.disconnect_button.pack(side=tk.LEFT, padx=(5, 5), pady=(5, 5))

        self.close_button = tk.Button(self, text='Disconnect And Close Server')
        self.close_button.pack(padx=(5, 5), pady=(5, 5))


def main():
    root = tk.Tk()
    CloseExitFrame(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()
