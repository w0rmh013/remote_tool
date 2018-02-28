import Tix as tx


class Manual(tx.ScrolledWindow):

    def __init__(self, parent, *args, **kwargs):

        tx.ScrolledWindow.__init__(self, parent, *args, **kwargs)

        self.parent = parent

        with open('docs\\manual.txt', 'rb') as f:
            self.raw_manual = f.read()

        self.manual_content = tx.Text(self)
        self.manual_content.insert(tx.END, self.raw_manual)
        self.manual_content.config(state=tx.DISABLED)
        self.manual_content.pack(fill=tx.BOTH, expand=1)
