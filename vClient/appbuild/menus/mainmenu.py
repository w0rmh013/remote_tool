import Tkinter as tk

import helpmenu
import optionmenu


class MainMenu(tk.Menu):

    def __init__(self, parent, *args, **kwargs):

        tk.Menu.__init__(self, parent, *args, **kwargs)

        self.parent = parent

        self.help_menu = helpmenu.HelpMenu(self)
        self.option_menu = optionmenu.OptionMenu(self)

        self.add_cascade(label='Options', menu=self.option_menu)
        self.add_cascade(label='Help', menu=self.help_menu)
