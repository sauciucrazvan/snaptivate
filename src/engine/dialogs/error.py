import sys

from PyQt5.QtWidgets import QApplication, QMessageBox

def show_error_dialog(message):
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle("Snaptivate: Error")
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()
    app.quit()