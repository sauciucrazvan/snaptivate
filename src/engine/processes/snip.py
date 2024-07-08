import os, sys

from processes import upload

from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QWidget, QRubberBand, QApplication
from PyQt5.QtGui import QMouseEvent, QKeyEvent

class Capture(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main = main_window
        
        self.setMouseTracking(True)
        desk_size = QApplication.desktop()
        self.setGeometry(0, 0, desk_size.width(), desk_size.height())
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.10) # TODO: Should remove the opacity when the screenshot is taken

        self.rubber_band = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()

        QApplication.setOverrideCursor(Qt.CrossCursor)

    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        if event.button() == Qt.LeftButton:
            self.origin = event.pos()
            self.rubber_band.setGeometry(QRect(self.origin, event.pos()).normalized())
            self.rubber_band.show() 

            screen = QApplication.primaryScreen()
            rect = QApplication.desktop().rect()
            self.imgmap = screen.grabWindow(QApplication.desktop().winId(), rect.x(), rect.y(), rect.width(), rect.height())

    def mouseMoveEvent(self, event: QMouseEvent | None) -> None:
        if not self.origin.isNull():
            self.rubber_band.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event: QMouseEvent | None) -> None:
        if event.button() == Qt.LeftButton:
            self.rubber_band.hide()
            
            rect = self.rubber_band.geometry()
            self.imgmap = self.imgmap.copy(rect)
            QApplication.restoreOverrideCursor()

            image_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'Snaptivate')
            if not os.path.exists(image_dir):
                os.makedirs(image_dir)

            image_path = os.path.join(image_dir, 'latest.jpg')
            self.imgmap.save(image_path)

            self.hide()
            upload.start()
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            sys.exit()