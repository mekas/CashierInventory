import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("login.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.connect("destroy", Gtk.main_quit)
login_button = builder.get_object("loginButton")
login_button.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(20000, 10000, 10000))
window.show_all()

Gtk.main()
