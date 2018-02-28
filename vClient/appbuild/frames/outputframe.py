import Tkinter as tk
import ScrolledText


class OutputFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        """Class constructor."""

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        tk.Label(self, text='Server Output').pack(pady=(5, 0))
        self.output_text = ScrolledText.ScrolledText(self, bg='black', fg='green', state=tk.DISABLED,
                                                     wrap=tk.WORD, height=10, bd=5, relief=tk.SUNKEN)
        self.output_text.pack(padx=(10, 10), pady=(5, 5))

        tk.Button(self, text='Clear', font=('', 8, ''), command=self._clear_output)\
            .pack(side=tk.LEFT, padx=(10, 0), pady=(5, 5))

    def append_to_output(self, cmd, output):
        """Append text to self.output_text"""

        self.output_text.tag_config('side', foreground='white')

        self.output_text.config(state=tk.NORMAL)

        self.output_text.insert(tk.END, 'You:\n  ', 'side')
        self.output_text.insert(tk.END, cmd + '\n\n')
        self.output_text.insert(tk.END, 'Server:\n\n', 'side')
        self.output_text.insert(tk.END, output + '\n')

        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)

    def _clear_output(self):

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    OutputFrame(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()
