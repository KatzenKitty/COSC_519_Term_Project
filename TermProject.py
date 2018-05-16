import skywriter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import signal
import sys

class MoviePlayer(QWidget):
    def __init__(self,parent=None):
        
        QWidget.__init__(self,parent)
        
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("test gif")
        
        self.movie_screen = QLabel()
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.movie_screen.setAlignment(Qt.AlignCenter)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)
        self.setLayout(main_layout)
        
    def playMovie(self, fileName):
        self.movie = QMovie(fileName, QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        
        
        # defines airwheel call
    @skywriter.airwheel()
    def airwheel(delta):
        signals.input_a.emit('8bad_fetch.gif')


    # defines doubletap call
    @skywriter.double_tap(repeat_rate=1)
    def doubletap(position):
        signals.input_a.emit('3lay_down.gif')


    # defines flick call
    @skywriter.flick()
    def flick(start,finish):
        signals.input_a.emit('2sad_paw.gif')


    # defines touch call
    @skywriter.touch(repeat_rate=1)
    def touch(position):
        signals.input_a.emit('4get_up.gif')
        

class Signals(QObject):
    input_a = pyqtSignal(str)
    
    def __init__(self, player, parent=None):
        super().__init__(parent)
        
        self.player = player
        
        self.input_a.connect(self.a)
        
        
        
    def a(self, fileName):
        self.player.playMovie(fileName)

        
app = QApplication(sys.argv)
player = MoviePlayer()
signals = Signals(player=player)

player.playMovie('1sit.gif')
player.showFullScreen()
sys.exit(app.exec_())


signal.pause(5)

