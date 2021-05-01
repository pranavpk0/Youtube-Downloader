from PyQt5 import QtCore, QtGui, QtWidgets
import resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        def Browse(): 
            resource.Browse(self.entry_path)

        def Default():
            resource.Default(self.entry_path)

    
        def Download():
            resource.Download(entry_path = self.entry_path , entry_link = self.entry_link , mainwindow = MainWindow)


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.heading = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setObjectName("heading")
        self.gridLayout.addWidget(self.heading, 0, 0, 1, 4)

        self.label_download = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_download.setFont(font)
        self.label_download.setObjectName("label_download")
        self.gridLayout.addWidget(self.label_download, 4, 0, 1, 1)

        self.Default_button = QtWidgets.QPushButton(self.centralwidget)
        self.Default_button.setObjectName("Default_button")
        self.Default_button.clicked.connect(Default)

        self.gridLayout.addWidget(self.Default_button, 4, 3, 1, 1)

        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setObjectName("Browse")
        self.Browse.clicked.connect(Browse)

        self.gridLayout.addWidget(self.Browse, 5, 3, 1, 1)

        self.entry_path = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.entry_path.setFont(font)
        self.entry_path.setObjectName("entry_path")
        self.gridLayout.addWidget(self.entry_path, 4, 2, 1, 1)

        self.Download_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Download_button.setFont(font)
        self.Download_button.setObjectName("Download_button")
        self.Download_button.clicked.connect(Download)

        self.gridLayout.addWidget(self.Download_button, 6, 0, 1, 4)
        self.entry_link = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.entry_link.setFont(font)
        self.entry_link.setObjectName("entry_link")
        
        self.gridLayout.addWidget(self.entry_link, 3, 2, 1, 1)

        self.label_link = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_link.setFont(font)
        self.label_link.setObjectName("label_link")

        self.gridLayout.addWidget(self.label_link, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_download.setBuddy(self.entry_link)
        self.label_link.setBuddy(self.entry_path)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.heading.setText(_translate("MainWindow", "       Youtube Downloader"))
        self.label_download.setText(_translate("MainWindow", "Download Path"))
        self.Default_button.setText(_translate("MainWindow", "Default"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.Download_button.setText(_translate("MainWindow", "Download"))
        self.label_link.setText(_translate("MainWindow", "Youtube Link"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
