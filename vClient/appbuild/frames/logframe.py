import Tkinter as tk
import ScrolledText


class LogFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        """Class constructor."""

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        tk.Label(self, text='Server Log').pack(pady=(5, 0))

        self.log_text = ScrolledText.ScrolledText(self, bg='black', fg='green', state=tk.DISABLED, wrap=tk.WORD,
                                                  height=5, bd=5, relief=tk.SUNKEN)

        self.log_text.pack(padx=(10, 10), pady=(5, 5))

        tk.Button(self, text='Clear', font=('', 8, ''), command=self._clear_log)\
            .pack(side=tk.LEFT, padx=(10, 0), pady=(5, 5))

    def append_to_log(self, text):
        """Append text to self.log_text"""

        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, text + '\n')
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def _clear_log(self):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete('1.0', tk.END)
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    LogFrame(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()
