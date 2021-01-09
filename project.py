from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import sqlite3

ALPHABET = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
UPPER_ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


class Cezar:
    def __init__(self, word, count):
        self.new_word = ''
        self.word = word
        self.count = count

    def coding(self):
        try:
            for i in self.word:
                if i in ALPHABET:
                    self.new_word += ALPHABET[ALPHABET.index(i) + self.count % 33]
                elif i in UPPER_ALPHABET:
                    self.new_word += UPPER_ALPHABET[UPPER_ALPHABET.index(i) + self.count % 33]
                elif i == ' ':
                    self.new_word += ' '
            return self.new_word
        except Exception:
            ui.label_10.setText('Неверный формат ввода')


class Vigener:
    def __init__(self, word, key_word):
        self.word = word
        self.key_word = key_word
        self.letters_to_numbers = list()
        self.new_word = ''

    def coding(self):
        try:
            for i in self.key_word:
                if i in ALPHABET:
                    self.letters_to_numbers.append(ALPHABET.index(i))
                elif i in UPPER_ALPHABET:
                    self.letters_to_numbers.append(UPPER_ALPHABET.index(i))
            for i, j in enumerate(self.word):
                if j in ALPHABET:
                    if i >= len(self.key_word):
                        self.new_word += ALPHABET[
                            ALPHABET.index(j) + self.letters_to_numbers[i % len(self.key_word)]]
                    else:
                        self.new_word += ALPHABET[ALPHABET.index(j) + self.letters_to_numbers[i]]
                elif j in UPPER_ALPHABET:
                    if i >= len(self.key_word):
                        self.new_word += UPPER_ALPHABET[
                            UPPER_ALPHABET.index(j) + self.letters_to_numbers[
                                i % len(self.key_word)]]
                    else:
                        self.new_word += UPPER_ALPHABET[
                            UPPER_ALPHABET.index(j) + self.letters_to_numbers[i]]
                elif j == ' ':
                    self.new_word += ' '
            return self.new_word
        except Exception:
            ui.label_9.setText('Неверный формат ввода')


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

    def initUI(self):
        ui.pushButton.clicked.connect(self.vigener_shifr)
        ui.pushButton_2.clicked.connect(self.cezar_shifr)

    def vigener_shifr(self):
        try:
            ui.label_9.setText('')
            self.con = sqlite3.connect('Ciphers.sqlite')
            self.cur = self.con.cursor()
            shifr = Vigener(ui.lineEdit.text(), ui.lineEdit_2.text())
            new_word = shifr.coding()
            ui.lineEdit_3.setText(new_word)
            if not new_word:
                raise Exception
            self.cur.execute('''INSERT INTO [Vingener] (old_text, key_word, new_text)
            VALUES (?, ?, ?)''', (ui.lineEdit.text(), ui.lineEdit_2.text(), new_word))
            self.con.commit()
        except Exception:
            ui.label_9.setText('Неверный формат ввода')
        finally:
            self.con.close()

    def cezar_shifr(self):
        try:
            ui.label_10.setText('')
            self.con = sqlite3.connect('Ciphers.sqlite')
            self.cur = self.con.cursor()
            shifr_2 = Cezar(ui.lineEdit_4.text(), ui.spinBox.value())
            new_word_2 = shifr_2.coding()
            ui.lineEdit_5.setText(new_word_2)
            if not new_word_2:
                raise Exception
            self.cur.execute('''INSERT INTO [Cezar] (old_text, Shift, new_text)
            VALUES (?, ?, ?)''', (ui.lineEdit_4.text(), ui.spinBox.value(), new_word_2))
            self.con.commit()
        except Exception:
            ui.label_10.setText('Неверный формат ввода')
        finally:
            self.con.close()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(593, 174)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 171))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(200, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 70, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(400, 40, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(324, 70, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(220, 0, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(350, 125, 231, 21))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(230, 0, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(70, 30, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(380, 30, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(410, 60, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 90, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setGeometry(QtCore.QRect(270, 60, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(270, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(260, 115, 321, 31))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Шифровка"))
        self.label.setText(_translate("Form", "Исходное сообщение"))
        self.label_2.setText(_translate("Form", "Ключевое слово"))
        self.label_3.setText(_translate("Form", "Зашифрованное сообщение"))
        self.pushButton.setText(_translate("Form", "Кодирование"))
        self.label_4.setText(_translate("Form", "Шифр Виженера"))
        self.label_9.setText(_translate("Form", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("Form", "Шифр Виженера"))
        self.label_5.setText(_translate("Form", "Шифр Цезаря"))
        self.label_6.setText(_translate("Form", "Исходное сообщение"))
        self.label_7.setText(_translate("Form", "Зашифрованное сообщение"))
        self.pushButton_2.setText(_translate("Form", "Кодирование"))
        self.label_8.setText(_translate("Form", "Сдвиг"))
        self.label_10.setText(_translate("Form", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("Form", "Шифр Цезаря"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    ui = Ui_Form()
    ui.setupUi(win)
    win.initUI()
    win.show()
    sys.exit(app.exec_())
