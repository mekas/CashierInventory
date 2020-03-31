import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from login import LoginView
from inventory import InventoryView
from user import User
from sqlalchemy.ext.declarative import declarative_base
from dialog import DialogWindow

class MainController:
    def __init__(self):
        self.loginView = LoginView(self)
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.set_admin_account()
        
        Gtk.main()
        
    def set_admin_account(self):
        user = User(username="admin", password="test")
        user.init_user_table(self.engine)
        
        self.session.add(user)
        self.session.commit()
        
    def check_account(self, username, password):
        """ check with user db """
        print(len(username), len(password))
        if username == "" and password == "":
            self.loginView.setInfo("Please fill username and password")
        elif username == "":
            self.loginView.setInfo("Username must not be empty")
        elif password == "":
            self.loginView.setInfo("Password must not be empty")    
        user = User()
        t_username, t_password = user.get_account(self.session)
        
        if username == t_username and password == t_password:
            # open inventory window
            self.loginView.setInfo("Right")
            self.loginView.hide_window()
            self.inventoryView = InventoryView(self)
        else:
            self.loginView.setInfo("Username or password incorrect")
            
    def show_confirmation(self, msg):
        dialog = DialogWindow()
        dialog.open_dialog(msg)
        dialog.show_all()
        
# main session must persist through application lifetime
main = MainController()

