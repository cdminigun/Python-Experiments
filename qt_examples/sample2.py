import sys
from PyQt4 import QtGui
class GridLayout(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('grid layout')
        names = [ '7', '8', '9', '4', '5', '6']
        grid = QtGui.QGridLayout()
        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (1, 0), (1,1),(1,2)]
        for i in names:
            button = QtGui.QPushButton(i)
            grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1
            self.setLayout(grid)
app = QtGui.QApplication(sys.argv)
qb = GridLayout()
qb.show()
sys.exit(app.exec_())


