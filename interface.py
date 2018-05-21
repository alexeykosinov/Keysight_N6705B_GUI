""" User Interface """
from PyQt5 import QtCore, QtWidgets, QtGui

class UI_Window(object):
    """ User Interface Define """
    def UI_Setup(self, dialog):
        """ Settings """
        dialog.setObjectName("dialog")
        dialog.resize(469, 652)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        self.tabWidget = QtWidgets.QTabWidget(dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 451, 491))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_Ch3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_Ch3.setGeometry(QtCore.QRect(330, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.pushButton_Ch3.setFont(font)
        self.pushButton_Ch3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_Ch3.setCheckable(True)
        self.pushButton_Ch3.setChecked(False)
        self.pushButton_Ch3.setDefault(False)
        self.pushButton_Ch3.setFlat(False)
        self.pushButton_Ch3.setObjectName("pushButton_Ch3")
        self.lcdNumber_W_Ch2 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_W_Ch2.setGeometry(QtCore.QRect(170, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lcdNumber_W_Ch2.setFont(font)
        self.lcdNumber_W_Ch2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_W_Ch2.setObjectName("lcdNumber_W_Ch2")
        self.lineEdit_I_Ch3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_I_Ch3.setGeometry(QtCore.QRect(330, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lineEdit_I_Ch3.setFont(font)
        self.lineEdit_I_Ch3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_I_Ch3.setReadOnly(False)
        self.lineEdit_I_Ch3.setObjectName("lineEdit_I_Ch3")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(280, 20, 51, 421))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lcdNumber_I_Ch2 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_I_Ch2.setGeometry(QtCore.QRect(170, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lcdNumber_I_Ch2.setFont(font)
        self.lcdNumber_I_Ch2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_I_Ch2.setObjectName("lcdNumber_I_Ch2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(140, 300, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lcdNumber_I_Ch1 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_I_Ch1.setGeometry(QtCore.QRect(10, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lcdNumber_I_Ch1.setFont(font)
        self.lcdNumber_I_Ch1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_I_Ch1.setObjectName("lcdNumber_I_Ch1")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(330, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_I_Ch1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_I_Ch1.setGeometry(QtCore.QRect(10, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lineEdit_I_Ch1.setFont(font)
        self.lineEdit_I_Ch1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_I_Ch1.setReadOnly(False)
        self.lineEdit_I_Ch1.setObjectName("lineEdit_I_Ch1")
        self.pushButton_Ch2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_Ch2.setGeometry(QtCore.QRect(170, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.pushButton_Ch2.setFont(font)
        self.pushButton_Ch2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_Ch2.setCheckable(True)
        self.pushButton_Ch2.setChecked(False)
        self.pushButton_Ch2.setDefault(False)
        self.pushButton_Ch2.setFlat(False)
        self.pushButton_Ch2.setObjectName("pushButton_Ch2")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(112, 20, 51, 421))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(170, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lcdNumber_V_Ch2 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_V_Ch2.setGeometry(QtCore.QRect(170, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lcdNumber_V_Ch2.setFont(font)
        self.lcdNumber_V_Ch2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_V_Ch2.setObjectName("lcdNumber_V_Ch2")
        self.lineEdit_V_Ch2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_V_Ch2.setGeometry(QtCore.QRect(170, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lineEdit_V_Ch2.setFont(font)
        self.lineEdit_V_Ch2.setInputMask("")
        self.lineEdit_V_Ch2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_V_Ch2.setReadOnly(False)
        self.lineEdit_V_Ch2.setObjectName("lineEdit_V_Ch2")
        self.lineEdit_V_Ch1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_V_Ch1.setGeometry(QtCore.QRect(10, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lineEdit_V_Ch1.setFont(font)
        self.lineEdit_V_Ch1.setInputMask("")
        self.lineEdit_V_Ch1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_V_Ch1.setReadOnly(False)
        self.lineEdit_V_Ch1.setObjectName("lineEdit_V_Ch1")
        self.lcdNumber_I_Ch3 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_I_Ch3.setGeometry(QtCore.QRect(330, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lcdNumber_I_Ch3.setFont(font)
        self.lcdNumber_I_Ch3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_I_Ch3.setObjectName("lcdNumber_I_Ch3")
        self.lcdNumber_W_Ch3 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_W_Ch3.setGeometry(QtCore.QRect(330, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lcdNumber_W_Ch3.setFont(font)
        self.lcdNumber_W_Ch3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_W_Ch3.setObjectName("lcdNumber_W_Ch3")
        self.pushButton_Ch1 = QtWidgets.QPushButton(self.tab)
        self.pushButton_Ch1.setEnabled(True)
        self.pushButton_Ch1.setGeometry(QtCore.QRect(10, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.pushButton_Ch1.setFont(font)
        self.pushButton_Ch1.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_Ch1.setCheckable(True)
        self.pushButton_Ch1.setChecked(False)
        self.pushButton_Ch1.setDefault(False)
        self.pushButton_Ch1.setFlat(False)
        self.pushButton_Ch1.setObjectName("pushButton_Ch1")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_I_Ch2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_I_Ch2.setGeometry(QtCore.QRect(170, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lineEdit_I_Ch2.setFont(font)
        self.lineEdit_I_Ch2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_I_Ch2.setReadOnly(False)
        self.lineEdit_I_Ch2.setObjectName("lineEdit_I_Ch2")
        self.lineEdit_V_Ch3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_V_Ch3.setGeometry(QtCore.QRect(330, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lineEdit_V_Ch3.setFont(font)
        self.lineEdit_V_Ch3.setInputMask("")
        self.lineEdit_V_Ch3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_V_Ch3.setReadOnly(False)
        self.lineEdit_V_Ch3.setObjectName("lineEdit_V_Ch3")
        self.lcdNumber_W_Ch1 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_W_Ch1.setGeometry(QtCore.QRect(10, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lcdNumber_W_Ch1.setFont(font)
        self.lcdNumber_W_Ch1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_W_Ch1.setObjectName("lcdNumber_W_Ch1")

        self.lcdNumber_V_Ch1 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_V_Ch1.setGeometry(QtCore.QRect(10, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lcdNumber_V_Ch1.setFont(font)
        self.lcdNumber_V_Ch1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_V_Ch1.setObjectName("lcdNumber_V_Ch1")
        
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(140, 380, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 220, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lcdNumber_V_Ch3 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_V_Ch3.setGeometry(QtCore.QRect(330, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lcdNumber_V_Ch3.setFont(font)
        self.lcdNumber_V_Ch3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_V_Ch3.setObjectName("lcdNumber_V_Ch3")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(310, 300, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(310, 380, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(310, 220, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(0, 300, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(0, 380, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(0, 220, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_start = QtWidgets.QPushButton(dialog)
        self.pushButton_start.setGeometry(QtCore.QRect(246, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(dialog)
        self.pushButton_stop.setGeometry(QtCore.QRect(360, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_allon = QtWidgets.QPushButton(dialog)
        self.pushButton_allon.setGeometry(QtCore.QRect(10, 550, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.pushButton_allon.setFont(font)
        self.pushButton_allon.setDefault(False)
        self.pushButton_allon.setFlat(False)
        self.pushButton_allon.setObjectName("pushButton_allon")
        self.pushButton_emergency = QtWidgets.QPushButton(dialog)
        self.pushButton_emergency.setGeometry(QtCore.QRect(240, 550, 200, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_emergency.setFont(font)
        self.pushButton_emergency.setStyleSheet("background-color:#ca0000; color: white;\n""")
        self.pushButton_emergency.setDefault(False)
        self.pushButton_emergency.setFlat(False)
        self.pushButton_emergency.setObjectName("pushButton_emergency")

        self.textEdit = QtWidgets.QTextEdit(dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 610, 431, 101))
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dialog)

        # Мои
        dialog.setFixedSize(450, 721) # Размер нельзя изменять пользователю

        self.lineEdit_I_Ch1.setPlaceholderText("Ток")
        self.lineEdit_I_Ch2.setPlaceholderText("Ток")
        self.lineEdit_I_Ch3.setPlaceholderText("Ток")

        self.lineEdit_V_Ch1.setPlaceholderText("Напряжение")
        self.lineEdit_V_Ch2.setPlaceholderText("Напряжение")
        self.lineEdit_V_Ch3.setPlaceholderText("Напряжение")

        self.pushButton_allon.setEnabled(True)
        self.pushButton_emergency.setEnabled(True)
        self.pushButton_start.setEnabled(True)
        #self.pushButton_start.setCheckable(True)
        self.pushButton_stop.setEnabled(True)


    def retranslateUi(self, dialog):
        """ ещё одна херня """
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Панель управление N6705B"))
        self.pushButton_Ch1.setText(_translate("dialog", "Включить"))
        self.pushButton_Ch2.setText(_translate("dialog", "Включить"))   
        self.pushButton_Ch3.setText(_translate("dialog", "Включить"))   

        self.pushButton_start.setText(_translate("dialog", "Соединение"))
        self.pushButton_stop.setText(_translate("dialog", "Отмена"))
        self.pushButton_allon.setText(_translate("dialog", "Включить все модули"))
        self.pushButton_emergency.setText(_translate("dialog", "Аварийное отключение"))

        self.lineEdit_I_Ch1.setText(_translate("dialog", ""))
        self.lineEdit_I_Ch2.setText(_translate("dialog", ""))
        self.lineEdit_I_Ch3.setText(_translate("dialog", ""))

        self.lineEdit_V_Ch1.setText(_translate("dialog", ""))
        self.lineEdit_V_Ch2.setText(_translate("dialog", ""))
        self.lineEdit_V_Ch3.setText(_translate("dialog", ""))

        self.label.setText(_translate("dialog", "Канал 1"))
        self.label_5.setText(_translate("dialog", "Канал 2"))
        self.label_6.setText(_translate("dialog", "Канал 3"))

        self.label_3.setText(_translate("dialog", "Ток, А"))
        self.label_7.setText(_translate("dialog", "Ток, А"))
        self.label_10.setText(_translate("dialog", "Ток, А"))

        self.label_11.setText(_translate("dialog", "Мощность, Вт"))
        self.label_8.setText(_translate("dialog", "Мощность, Вт"))
        self.label_4.setText(_translate("dialog", "Мощность, Вт"))

        self.label_2.setText(_translate("dialog", "Напряжение, В"))
        self.label_9.setText(_translate("dialog", "Напряжение, В"))
        self.label_12.setText(_translate("dialog", "Напряжение, В"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("dialog", "Ручной режим"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("dialog", "Автоматический режим"))