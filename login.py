import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class LoginView():    
    def __init__(self, mainController):
        self.mc = mainController
        self.builder = Gtk.Builder()
        self.builder.add_from_file("login.glade")
        
        self.window = self.builder.get_object("mainWindow")
        self.window.connect("destroy", Gtk.main_quit)
        login_button = self.builder.get_object("loginButton")
        login_button.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(20000, 10000, 10000))
        login_button.connect("clicked", self.on_btn_submit)
        self.window.show_all()
        
    def on_btn_submit(self, button):
        username = self.builder.get_object("usernameInput").get_text()
        password = self.builder.get_object("passwordInput").get_text()
        # check againts the password from the database
        self.mc.check_account(username, password)

    def setInfo(self, message):
        self.builder.get_object("infoLabel")
        info_label = self.builder.get_object("InfoLabel")
        markup_text = "<span foreground=\"#ff0044\">"+ message + "</span>"
        info_label.set_markup(markup_text)
        
    def close_window(self):
        self.window.close()
        
    def hide_window(self):
        self.window.hide()
