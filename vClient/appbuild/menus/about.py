import Tkinter as tk


class About(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent

        with open('docs\\about.txt', 'rb') as f:
            self.raw_about = f.read()

        self.about_content = tk.Text(self)
        self.about_content.insert(tk.END, self.raw_about)
        self.about_content.config(state=tk.DISABLED)
        self.about_content.pack(fill=tk.BOTH, expand=1)
