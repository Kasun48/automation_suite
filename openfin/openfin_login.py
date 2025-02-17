import time
from pywinauto import Application
import pygetwindow as gw
from utils.config import USERNAME, PASSWORD, LOGIN_URL

def automate_login():
    time.sleep(20)
    login_window = gw.getWindowsWithTitle("Mizuho Front Office")[0]

    app = Application(backend = 'uia').connect(handle=login_window._hWind)

    dlg = app.window(title="Mizuho Front Office")

    username_field = dlg.child_window(control_type)