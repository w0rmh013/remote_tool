import Tkinter as tk
import ttk


class CommandHandlerFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        """Class constructor."""

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        tk.Label(self, text='Command').grid(row=0, column=0, padx=(5, 0), pady=(5, 0), sticky='E')

        self.cmd_combobox = ttk.Combobox(self)
        self.cmd_combobox.grid(row=0, column=1, padx=(0, 5), pady=(5, 0), sticky='WE')

        self.chf_button = tk.Button(self, text='SEND')
        self.chf_button.grid(columnspan=2, row=1, column=0, pady=(0, 5))

        self.columnconfigure(1, weight=1)

    def update_cbox(self):

        history = self.cmd_combobox['values']
        new_cmd = self.cmd_combobox.get()

        if len(history) is 0:
            if new_cmd is not '':
                self.cmd_combobox['values'] = (new_cmd, )

        else:
            if new_cmd is not '' and new_cmd not in history:
                history = list(history)
                history.insert(0, new_cmd)
                self.cmd_combobox['values'] = tuple(history)

        self.cmd_combobox.set('')

    def clear_cbox(self):

        self.cmd_combobox.set('')
        self.cmd_combobox['values'] = tuple()


def main():
    root = tk.Tk()
    CommandHandlerFrame(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()
