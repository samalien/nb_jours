# les import
from PyQt5 import QtCore, QtGui, QtWidgets
from fenetre import Ui_MainWindow
import sys
from fonctions import *
# l'interface grapghique
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
global nombre
# les fonctions
#----------------------------------------------------------------#
#                afficher le resultat final                      #
#----------------------------------------------------------------#




def start():
    day1 = ui.date1.selectedDate().day()
    month1 = ui.date1.selectedDate().month()
    year1 = ui.date1.selectedDate().year()
    day2 = ui.date2.selectedDate().day()
    month2 = ui.date2.selectedDate().month()
    year2 = ui.date2.selectedDate().year()

    if dateIsBefore(day1, month1, year1, day2, month2, year2):
        nb = count(day1, month1, year1, day2, month2, year2)
    else:
        nb = count(day2, month2, year2, day1, month1, year1)
    return nb

# les connexions*******************************************
def afficher():
    ui.nb.setText(str(start()))

ui.pushButton.clicked.connect(afficher)
#**********************************************************



sys.exit(app.exec_())