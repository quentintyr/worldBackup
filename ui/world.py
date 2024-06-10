from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon

class mainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainUI, self).__init__()   # call the inherited classes __init__ method
        uic.loadUi('ui/world.ui', self)   # load the ui file

        # main window settings
        self.setWindowTitle("World Backups")
        self.setWindowIcon(QIcon("icons/logo_rect.png"))
        
        # set file icons
        self.actionNew.setIcon(QIcon("icons/file/new.ico"))
        self.actionExisting.setIcon(QIcon("icons/file/search.png"))
        self.actionClone.setIcon(QIcon("icons/file/clone.png"))
        self.actionOptions.setIcon(QIcon("icons/file/options.png"))
        self.actionExit.setIcon(QIcon("icons/file/exit.png"))

        # set edit icons
        self.actionUndo.setIcon(QIcon("icons/edit/undo.png"))
        self.actionRedo.setIcon(QIcon("icons/edit/redo.png"))
        self.actionCut.setIcon(QIcon("icons/edit/cut.png"))
        self.actionCopy.setIcon(QIcon("icons/edit/copy.png"))
        self.actionPaste.setIcon(QIcon("icons/edit/paste.png"))
        self.actionselectAll.setIcon(QIcon("icons/edit/selectAll.png"))
        self.actionFind.setIcon(QIcon("icons/edit/find.png"))

        # set view icons
        self.actionChanges.setIcon(QIcon("icons/view/changes.png"))
        self.actionHistory.setIcon(QIcon("icons/view/history.png"))
        self.actionBackup_List.setIcon(QIcon("icons/view/list.png"))
        self.actiondevTools.setIcon(QIcon("icons/view/dev.png"))

        #set bakups iconss
        self.actionPush.setIcon(QIcon("icons/backups/push.png"))
        self.actionPull.setIcon(QIcon("icons/backups/pull.png"))
        self.actionFetch.setIcon(QIcon("icons/backups/fetch.png"))
        self.actionRemove.setIcon(QIcon("icons/backups/remove.png"))
        self.actionView_on_Browser.setIcon(QIcon("icons/backups/browser.png"))
        self.actionShow_in_Explorer.setIcon(QIcon("icons/backups/explorer.png"))
        self.actionSettings.setIcon(QIcon("icons/backups/settings.png"))

        # set help icons
        self.actionReport_Issue.setIcon(QIcon("icons/help/issue.png"))
        self.actionContact_Support.setIcon(QIcon("icons/help/support.png"))
        self.actionShow_Keyboard_Shortcuts.setIcon(QIcon("icons/help/keyboard.png"))
        self.actionShow_Logs.setIcon(QIcon("icons/help/logs.png"))
        self.actionAbout.setIcon(QIcon("icons/help/about.png"))

        # 