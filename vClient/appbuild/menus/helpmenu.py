import Tkinter as tk
import Tix as tx

import manual
import about


class HelpMenu(tk.Menu):

    def __init__(self, parent, *args, **kwargs):

        tk.Menu.__init__(self, parent, *args, **kwargs)

        self.parent = parent

        self.add_command(label='Manual', command=self._show_manual)
        self.add_command(label='About', command=self._show_about)

        self.manual_window = None
        self.about_window = None

        self.manual_open = False
        self.about_open = False

    def _show_manual(self):

        if not self.manual_open:
            self.manual_window = tx.Tk()
            self.manual_window.protocol('WM_DELETE_WINDOW', self._safe_close_manual)
            self.manual_window.title('vClient Manual')
            self.manual_window.geometry('1070x300+50+50')
            try:
                self.manual_window.iconbitmap('logo.ico')
            except:
                pass

            self.manual = manual.Manual(self.manual_window, scrollbar=tx.BOTH)
            self.manual.pack(fill=tx.BOTH, expand=1)
            self.manual_open = True
            self.manual_window.mainloop()

    def _show_about(self):

        if not self.about_open:
            self.about_window = tk.Tk()
            self.about_window.protocol('WM_DELETE_WINDOW', self._safe_close_about)
            self.about_window.title('About vClient')
            self.about_window.geometry('370x120+50+50')
            self.about_window.resizable(False, False)
            try:
                self.about_window.iconbitmap('logo.ico')
            except:
                pass

            self.about = about.About(self.about_window)
            self.about.pack(fill=tk.BOTH, expand=1)
            self.about_open = True
            self.about_window.mainloop()

    def _safe_close_manual(self):

        self.manual_window.destroy()
        self.manual_open = False

    def _safe_close_about(self):

        self.about_window.destroy()
        self.about_open = False
