import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class InventoryView():    
    def __init__(self, mainController):
        self.builder = Gtk.Builder()
        self.mc = mainController
        self.builder.add_from_file("inventory.glade")
        
        self.window = self.builder.get_object("inventoryWindow")
        self.window.connect("destroy", Gtk.main_quit)
        self.stylize_order_buttons()
        self.window.activate_focus()
        self.window.show_all()
        
    def stylize_order_buttons(self):
        """
        Red colorize order button here, since we couldn't do that on Glade
        """
        button_ids = ["paketA_btn","paketB_btn", "paketC_btn", "paketD_btn"]
        i = 0
        for btn_id in button_ids:
            button = self.builder.get_object(btn_id)
            bg_rgba = Gdk.RGBA()
            bg_rgba.parse("#DC143C")
            button.override_background_color(Gtk.StateType.NORMAL, bg_rgba)
            fg_rgba = Gdk.RGBA()
            fg_rgba.parse("#FFFFF0")
            button.override_color(Gtk.StateType.NORMAL, fg_rgba)
            button.connect("clicked", self.on_btn_submit, str(i))
            i += 1
        
    def on_btn_submit(self, button, id):
        """
        Should open final confirmation dialog, but view is not allowed to open another view. 
        Do that through mainController.
        """
        switcher = {
            0: "Paket A",
            1: "Paket B",
            2: "Paket C",
            3: "Paket D"
        }
        msg = switcher.get(int(id), "")
        self.mc.show_confirmation(msg)
        



