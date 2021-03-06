import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ConfirmationDialog(Gtk.Dialog):

    def __init__(self, parent, msg):
        Gtk.Dialog.__init__(self, "Confirmation Dialog", parent, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(150, 100)

        label = Gtk.Label("You sure want to order " + msg + "?")

        box = self.get_content_area()
        box.add(label)
        self.show_all()

class DialogWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Confirmation")
        self.set_border_width(6)
        self.connect("destroy", Gtk.main_quit)

    def open_dialog(self, msg):
        dialog = ConfirmationDialog(self, msg)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("Order confirmed")
        elif response == Gtk.ResponseType.CANCEL:
            print("You canceled the order")

        self.destroy()

