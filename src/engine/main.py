import sys

from handlers import snip, upload
from PyQt5.QtWidgets import QApplication, QMainWindow

class Snaptivate(QMainWindow):

    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.setWindowTitle("Snaptivate")

        # Snipping action
        self.capturer = snip.Capture(self)
        self.capturer.show()

    def close(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("Debug: Starting the application...")
    Snaptivate()
    sys.exit(app.exec_())