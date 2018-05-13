#!/usr/bin/env python
import signal
import skywriter
from PyQt5 import Qt
#import autopy
import sys


application = Qt.QApplication(sys.argv)


class Display(Qt.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.foreground = Qt.QLabel()
        self.foreground.setScaledContents(True)

    def playMovie(self,filename):
        self.movie = Qt.QMovie(filename)
        self.foreground.setMovie(self.movie)
        self.movie.start()



class AspectRatioPadding(Qt.QWidget):
    def __init__(self,child,parent=None):
        super().__init__(parent)

        self.child = child
        self.child.setParent(self)

    def resizeEvent(self,event):
        new_size = event.size()
        child_size = self.child.sizeHint().scaled(
            new_size,
            Qt.Qt.KeepAspectRatio,
        )

        offset = (new_size - child_size) / 2

        self.child.setGeometry(
            offset.width(),
            offset.height(),
            child_size.width(),
            child_size.height(),
        )

    def sizeHint(self):
        return self.child.sizeHint()


display = Display()
padding = AspectRatioPadding(child=display)
padding.show()


# defines airwheel call
@skywriter.airwheel()
def airwheel(delta):
    display.playMovie(display,'paw 2.gif')


# defines doubletap call
@skywriter.double_tap()
def doubletap(position):
    display.playMovie(display,'lay down.gif')


# defines flick call
@skywriter.flick()
def flick(start,finish):
    display.playMovie(display,'jump.gif')


# defines touch call
@skywriter.touch()
def touch(position):
    display.playMovie(display,'sit.gif')


signal.pause()
sys.exit(application.exec())