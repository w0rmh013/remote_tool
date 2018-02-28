import Tkinter as tk


class ConnectFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        """Class constructor."""

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        tk.Label(self, text='Server IP').grid(row=1, column=0, sticky=tk.E, padx=(5, 0), pady=(5, 0))

        self.ip_entry = tk.Entry(self)
        self.ip_entry.insert(tk.END, 'localhost')
        self.ip_entry.grid(row=1, column=1, padx=(0, 5), pady=(5, 0))
        self.ip_entry.focus()

        # self.cf_button command is configured in mainframe.py
        self.cf_button = tk.Button(self, text='Connect')
        self.cf_button.grid(columnspan=2, row=2, column=0, pady=(5, 5))


def main():
    root = tk.Tk()
    ConnectFrame(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()
