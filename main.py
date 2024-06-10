from ui.world import mainUI
from PyQt6.QtWidgets import QApplication


if __name__ == "__main__":
    import sys

    # standard application
    app = QApplication(sys.argv)
    window = mainUI()
    window.show()
    sys.exit(app.exec())
