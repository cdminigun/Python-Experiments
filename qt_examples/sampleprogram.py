import sys
from PyQt4 import QtGui, QtCore #Necessary imports
app = QtGui.QApplication(sys.argv) 
widget=QtGui.QWidget()
widget.setWindowTitle('Simple')
widget.setGeometry(300, 300, 250, 150)
button=QtGui.QPushButton('Close',widget) #Creates the "close" button
button.setGeometry(10, 10, 60, 35) #Defines the regions for the "close" button
app.connect(button, QtCore.SIGNAL('clicked()'),QtGui.qApp, QtCore.SLOT('quit()')) 
#Adds functionality to the "close" button
widget.show()
sys.exit(app.exec_())




