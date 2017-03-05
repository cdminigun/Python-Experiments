import sys #System import
from PyQt4 import QtGui #Imports QtGui from QT4

#The Basic GUI widget are located
#in QtGui module


app = QtGui.QApplication(sys.argv)

#Every PyQt4 application must define
#An application object located in QtGui

widget = QtGui.QWidget() 

#The QWidget widget is the base
#class of all user interface objects
#in PyQt4


widget.resize(250, 150)
widget.setWindowTitle('Hello World')
widget.show()
sys.exit(app.exec_())
#Finally, we enter the mainloop of the application. The event handling starts
#from this point. The mainloop receives events from the window system and
#dispatches them to the application widgets.
#The mainloop ends, if we call the exit()
#method or the main widget is destroyed
