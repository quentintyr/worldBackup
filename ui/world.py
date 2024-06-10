from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon

class mainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainUI, self).__init__()   # call the inherited classes __init__ method
        uic.loadUi('ui/world.ui', self)   # load the ui file

        # main window settings
        self.setWindowTitle("Event Manager")
        self.setWindowIcon(QIcon("icons/event.png"))
        
        