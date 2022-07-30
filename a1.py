
from PyQt5 import QtCore, QtGui, QtWidgets
import b1
import c1
import pandas
# ostatnie zmiany 30 07 2022

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 700)

        self.model = QtGui.QStandardItemModel() ################

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 400, 31))
        self.label.setStyleSheet("QLabel{\n"
"    background-color: rgb(202, 202, 202);\n"
"    border: 2px solid;\n"
"    border-color: rgb(0, 255, 0);\n"
"    border-radius: 10px;\n"
"    font-size: 20px;     \n"
"}\n"
"QLabel:hover{\n"
"    background-color:rgb(142, 253, 255);\n"
"    border: 3px solid;\n"
"    border-color: rgb(0, 0, 255);\n"
"\n"
"}")
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 90, 211, 51))
        self.comboBox.setStyleSheet("QComboBox{\n"
"    background-color: rgb(202, 202, 202);\n"
"    border: 2px solid;\n"
"    border-color: rgb(0, 255, 0);\n"
"    font-size: 22px;\n"
"}\n"
"QComboBox:hover{\n"
"    background-color:rgb(142, 253, 255);\n"
"    border: 3px solid;\n"
"    border-color: rgb(0, 0, 255);\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems( c1.daty( self.plik_html( ) ) )
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                clicked =lambda :
                                                self.guzik1( self.comboBox.currentText()) )
        self.pushButton.setGeometry(QtCore.QRect(240, 90, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(248, 25, 5);\n"
"    border: 2px solid;\n"
"    border-color: rgb(255, 255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    border: 3px solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size:26px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 90, 211, 51))
        self.comboBox_2.setStyleSheet("QComboBox{\n"
"    background-color: rgb(202, 202, 202);\n"
"    border: 2px solid;\n"
"    border-color: rgb(0, 255, 0);\n"
"    font-size: 22px;\n"
"}\n"
"QComboBox:hover{\n"
"    background-color:rgb(142, 253, 255);\n"
"    border: 3px solid;\n"
"    border-color: rgb(0, 0, 255);\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        # self.comboBox_2.addItems(b1.pokemony_naglowki('pokemon.csv'))
        self.comboBox_2.addItems(c1.waluty_naglowki(self.plik_html()))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,
                                                clicked =lambda :
                                                self.guzik2( self.comboBox_2.currentText() ) )
        self.pushButton_2.setGeometry(QtCore.QRect(540, 90, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(248, 25, 5);\n"
"    border: 2px solid;\n"
"    border-color: rgb(255, 255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    border: 3px solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size:26px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 170, 281, 211))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"    background-color: rgb(202, 202, 202);\n"
"    border: 2px solid;\n"
"    border-color: rgb(0, 255, 0);\n"
# "    font-size: 22px;\n"
"}\n"
"QTextBrowser:hover{\n"
"    background-color:rgb(142, 253, 255);\n"
"    border: 3px solid;\n"
"    border-color: rgb(0, 0, 255);\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setPlaceholderText('Tu się pojawię wszystkie\nnotowania z wybranego dnia')
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(320, 170, 281, 211))
        self.textBrowser_2.setStyleSheet("QTextBrowser{\n"
"    background-color: rgb(202, 202, 202);\n"
"    border: 2px solid;\n"
"    border-color: rgb(0, 255, 0);\n"
"    font-size: 22px;\n"
"}\n"
"QTextBrowser:hover{\n"
"    background-color:rgb(142, 253, 255);\n"
"    border: 3px solid;\n"
"    border-color: rgb(0, 0, 255);\n"
"}")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setPlaceholderText('Wybierz walutę powyżej i kliknij OK\n'
                                              'zobaczysz kurs waluty z wybranego dnia ')

        # wybor daty
        self.comboBox_pocz_daty = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pocz_daty.setGeometry(QtCore.QRect(20, 390, 130, 40))
        self.comboBox_pocz_daty.setStyleSheet("QComboBox{\n"
                                    "    background-color: rgb(202, 202, 202);\n"
                                    "    border: 2px solid;\n"
                                    "    border-color: rgb(0, 255, 0);\n"
                                    "    font-size: 20px;\n"
                                    "}\n"
                                    "QComboBox:hover{\n"
                                    "    background-color:rgb(142, 253, 255);\n"
                                    "    border: 3px solid;\n"
                                    "    border-color: rgb(0, 0, 255);\n"
                                    "}")
        self.comboBox_pocz_daty.setObjectName("comboBox_pocz_daty")

        self.comboBox_pocz_daty.setModel(self.model) #################################


        self.comboBox_koniec_daty = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_koniec_daty.setGeometry(QtCore.QRect(170, 390, 130, 40))
        self.comboBox_koniec_daty.setStyleSheet("QComboBox{\n"
                                              "    background-color: rgb(202, 202, 202);\n"
                                              "    border: 2px solid;\n"
                                              "    border-color: rgb(0, 255, 0);\n"
                                              "    font-size: 20px;\n"
                                              "}\n"
                                              "QComboBox:hover{\n"
                                              "    background-color:rgb(142, 253, 255);\n"
                                              "    border: 3px solid;\n"
                                              "    border-color: rgb(0, 0, 255);\n"
                                              "}")
        self.comboBox_koniec_daty.setObjectName("comboBox_koniec_daty")

        self.comboBox_koniec_daty.setModel(self.model) ###########################

        slownik_ = c1.daty(self.plik_html())
        slownik = {  el: c1.daty_zalezne( self.plik_html(),el)  for el in slownik_ }
        for k , v in slownik.items():
            poczatek_ = QtGui.QStandardItem(k) ################
            self.model.appendRow( poczatek_)
            for value in v:
                koniec_ = QtGui.QStandardItem(value) ################
                poczatek_.appendRow( koniec_ )

        self.pushButton_wykres = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.guzik_wykres())
        self.pushButton_wykres.setGeometry(QtCore.QRect(320, 390, 130, 40))
        self.pushButton_wykres.setStyleSheet("QPushButton{\n"
                                                "    background-color: rgb(202, 202, 202);\n"
                                                "    border: 2px solid;\n"
                                                "    border-color: rgb(0, 255, 0);\n"
                                                "    font-size: 20px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(142, 253, 255);\n"
                                                "    border: 3px solid;\n"
                                                "    border-color: rgb(0, 0, 255);\n"
                                                "}")
        self.pushButton_wykres.setObjectName("pushButton_wykres")


        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 440, 583, 211))
        self.textBrowser_3.setStyleSheet("QTextBrowser{\n"
                                       "    background-color: rgb(202, 202, 202);\n"
                                       "    border: 2px solid;\n"
                                       "    border-color: rgb(0, 255, 0);\n"
                                       "}\n"
                                       "QTextBrowser:hover{\n"
                                       "    background-color:rgb(142, 253, 255);\n"
                                       "    border: 3px solid;\n"
                                       "    border-color: rgb(0, 0, 255);\n"
                                       "}")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_3.setPlaceholderText('cos tu tam bedzie ')

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox_pocz_daty.currentIndexChanged.connect( self.update_combo_koniec)
        self.update_combo_koniec( 0 )

    def update_combo_koniec(self, index ): ###########
        indx = self.model.index( index, 0 , self.comboBox_pocz_daty.rootModelIndex())
        self.comboBox_koniec_daty.setRootModelIndex( indx )
        self.comboBox_koniec_daty.setCurrentIndex( 0 )

    def guzik1(self,pressed):
        self.label.setText( f'wybrałeś kursy z dnia {self.comboBox.currentText()}r.')
        data = pressed[-4:]+ pressed[3:5]+pressed[:2]
        self.textBrowser.setText( c1.waluty_wybierz_wiersz(self.plik_html(),data))

    def zmiana_data(self):
        data_pocz = self.comboBox_pocz_daty.currentText()
        data_kon = self.comboBox_koniec_daty.currentText()
        data_pocz = data_pocz[-4:] + data_pocz[3:5] + data_pocz[:2]
        data_kon = data_kon[-4:] + data_kon[3:5] + data_kon[:2]
        return data_pocz, data_kon


    def guzik2(self, pressed ):
        self.label.setText( f'wybrałeś kurs {self.comboBox_2.currentText()} z dnia {self.comboBox.currentText()}r. ')
        data = self.comboBox.currentText()
        data = data[-4:] + data[3:5] + data[:2]
        self.textBrowser_2.setText( c1.waluta_wartosc( self.plik_html(),data, pressed ))


    def zakres_dat(self):
        return c1.daty( self.plik_html() )


    def co_ma_poczatek_dat(self):
        self.comboBox_pocz_daty.addItems( self.zakres_dat() )
        return self.comboBox_pocz_daty.currentText()

    def zakres_konca_dat(self):
        self.comboBox_koniec_daty.addItems([self.co_ma_poczatek_dat(),'v'])


    def plik_html(self):
        plik = 'https://www.nbp.pl/kursy/Archiwum/archiwum_tab_a_2022.csv'
        return plik

    def guzik_wykres(self):
        a = self.zmiana_data()
        self.textBrowser_3.setText(
            f'wybrales wykres daty od \n{self.comboBox_pocz_daty.currentText()} do {self.comboBox_koniec_daty.currentText(),} \n{str(a[0])} {str(a[1])}')

        b1.wykres()
        # print( a )
        print('poczatek dat ', self.co_ma_poczatek_dat() )


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ceny walut w NBP"))
        self.pushButton.setText(_translate("MainWindow", "ok"))
        self.pushButton_2.setText(_translate("MainWindow", "ok"))
        self.pushButton_wykres.setText(_translate("MainWindow", "pokaż wykres"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

