import sys

from processes import snip
from PyQt5.QtWidgets import QApplication, QMainWindow

class Snaptivate(QMainWindow):

    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.setWindowTitle("Snaptivate")

        # Snipping process
        self.capturer = snip.Capture(self)
        self.capturer.show()

    def close(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Snaptivate()
    sys.exit(app.exec_())