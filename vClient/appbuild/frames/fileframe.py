import Tkinter as tk
from functools import partial


class FileTransferFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        """Class constructor."""

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.mode = 'SEND'

        tk.Radiobutton(self, text='Send File To Server', value=1, variable='ftf',
                       command=partial(self._change_mode, 'SEND')).grid(row=0, column=0, sticky=tk.W, pady=(5, 0))
        tk.Radiobutton(self, text='Get File From Server', value=2, variable='ftf',
                       command=partial(self._change_mode, 'GET')).grid(row=1, column=0, sticky=tk.W)

        tk.Label(self, text='Source Path').grid(row=0, column=1, sticky=tk.E, pady=(5, 0))
        tk.Label(self, text='Destination Path').grid(row=1, column=1, sticky=tk.E)

        self.src_entry = tk.Entry(self)
        self.src_entry.grid(row=0, column=2, padx=(0, 5), pady=(5, 0))

        self.dst_entry = tk.Entry(self)
        self.dst_entry.grid(row=1, column=2, padx=(0, 5))

        # self.ftf_button command is configured in mainframe.py
        self.ftf_button = tk.Button(self, text='OK')
        self.ftf_button.grid(columnspan=3, row=2, column=0, pady=(0, 5))

    def _change_mode(self, change_to):
        """Change self.mode from GET to SEND or vice versa."""

        self.mode = change_to


def main():
    root = tk.Tk()
    FileTransferFrame(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()
