""" Main body """
# pyinstaller 	--noconfirm 
#				--hidden-import six 
#				--hidden-import packaging 
#				--hidden-import packaging.version 
#				--hidden-import packaging.specifiers 
#				--hidden-import packaging.requirements 
#               -i "icon.ICO"
#               -F
#               -w
#				main.py
import sys
import time
import visa
from PyQt5 import QtCore, QtWidgets
from interface import UI_Window

RM = visa.ResourceManager("C:/Windows/System32/visa64.dll") # "C:/Windows/System32/visa32.dll"
KEYSIGHT = RM.open_resource('TCPIP0::10.11.0.200::inst0::INSTR')

class Thread(QtCore.QThread):
    """ Class Threading """
    channel_one_v = QtCore.pyqtSignal(str)
    channel_two_v = QtCore.pyqtSignal(str)
    channel_three_v = QtCore.pyqtSignal(str)

    channel_one_i = QtCore.pyqtSignal(str)
    channel_two_i = QtCore.pyqtSignal(str)
    channel_three_i = QtCore.pyqtSignal(str)

    channel_one_w = QtCore.pyqtSignal(str)
    channel_two_w = QtCore.pyqtSignal(str)
    channel_three_w = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        """ Initialization """
        QtCore.QThread.__init__(self, parent=parent)
        self.isRunning = True

    def run(self):
        """ Run Thread """
        while self.isRunning:
            time.sleep(5)

            convert_one_power = round(float(KEYSIGHT.ask("MEASure:POWer? (@1)")), 3)
            convert_two_power = round(float(KEYSIGHT.ask("MEASure:POWer? (@2)")), 3)
            convert_three_power = round(float(KEYSIGHT.ask("MEASure:POWer? (@3)")), 3)

            convert_one_voltage = round(float(KEYSIGHT.ask("MEASure:VOLTage? (@1)")), 3)
            convert_two_voltage = round(float(KEYSIGHT.ask("MEASure:VOLTage? (@2)")), 3)
            convert_three_voltage = round(float(KEYSIGHT.ask("MEASure:VOLTage? (@3)")), 3)

            convert_one_current = round(float(KEYSIGHT.ask("MEASure:CURRent? (@1)")), 3)
            convert_two_current = round(float(KEYSIGHT.ask("MEASure:CURRent? (@1)")), 3)
            convert_three_current = round(float(KEYSIGHT.ask("MEASure:CURRent? (@1)")), 3)

            self.channel_one_v.emit(str(convert_one_voltage))
            self.channel_two_v.emit(str(convert_two_voltage))
            self.channel_three_v.emit(str(convert_three_voltage))

            self.channel_one_i.emit(str(convert_one_current))
            self.channel_two_i.emit(str(convert_two_current))
            self.channel_three_i.emit(str(convert_three_current))

            self.channel_one_w.emit(str(convert_one_power))
            self.channel_two_w.emit(str(convert_two_power))
            self.channel_three_w.emit(str(convert_three_power))


    def stop(self):
        """ Stop Thread """
        self.isRunning = False
        self.quit()
        self.wait()

class Window(QtWidgets.QMainWindow):
    """ Main Window """
    def __init__(self, parent=None):
        """ Initialization """
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = UI_Window()
        self.ui.UI_Setup(self)

        self.ui.pushButton_start.clicked.connect(self.start_connection)
        self.ui.pushButton_stop.clicked.connect(self.stop_connection)

        self.ui.pushButton_emergency.clicked.connect(self.emergency_stop)
        self.ui.pushButton_allon.clicked.connect(self.turn_all_channels_on)

        self.ui.pushButton_Ch1.clicked.connect(self.turn_on_channel_one)
        self.ui.pushButton_Ch2.clicked.connect(self.turn_on_channel_two)
        self.ui.pushButton_Ch3.clicked.connect(self.turn_on_channel_three)

        self.ui.lineEdit_V_Ch1.returnPressed.connect(self.set_voltage_to_channel_one)
        self.ui.lineEdit_V_Ch2.returnPressed.connect(self.set_voltage_to_channel_two)
        self.ui.lineEdit_V_Ch3.returnPressed.connect(self.set_voltage_to_channel_three)

        self.ui.lineEdit_I_Ch1.returnPressed.connect(self.set_current_to_channel_one)
        self.ui.lineEdit_I_Ch2.returnPressed.connect(self.set_current_to_channel_two)
        self.ui.lineEdit_I_Ch3.returnPressed.connect(self.set_current_to_channel_three)

        self.th = Thread(self)

        self.th.channel_one_v.connect(self.ui.lcdNumber_V_Ch1.display)
        self.th.channel_two_v.connect(self.ui.lcdNumber_V_Ch2.display)
        self.th.channel_three_v.connect(self.ui.lcdNumber_V_Ch3.display)

        self.th.channel_one_i.connect(self.ui.lcdNumber_I_Ch1.display)
        self.th.channel_two_i.connect(self.ui.lcdNumber_I_Ch2.display)
        self.th.channel_three_i.connect(self.ui.lcdNumber_I_Ch3.display)

        self.th.channel_one_w.connect(self.ui.lcdNumber_W_Ch1.display)
        self.th.channel_two_w.connect(self.ui.lcdNumber_W_Ch2.display)
        self.th.channel_three_w.connect(self.ui.lcdNumber_W_Ch3.display)

        self.th.start()

    def start_connection(self):
        """ Соединение """
        try:
            if KEYSIGHT.resource_name.startswith('ASRL') or KEYSIGHT.resource_name.endswith('SOCKET'):
                KEYSIGHT.read_termination = '\n'
            self.ui.textEdit.append('IP-адрес: %s\nИмя: %s\nПорт: %d' % (KEYSIGHT.get_visa_attribute(visa.constants.VI_ATTR_TCPIP_ADDR),
                                                                         KEYSIGHT.get_visa_attribute(visa.constants.VI_ATTR_TCPIP_HOSTNAME),
                                                                         KEYSIGHT.get_visa_attribute(visa.constants.VI_ATTR_TCPIP_PORT)))
            KEYSIGHT.write('*IDN?')
            IDN = KEYSIGHT.read()
            self.ui.textEdit.append('Идентификатор прибора: %s' % IDN.rstrip(' '))
        except visa.Error as ex:
            self.ui.textEdit.append('Ошибка: %s' % ex)

    def stop_connection(self):
        """ Закрыть соединение (не работает) """
        try:
            KEYSIGHT.close()
            RM.close()
            self.ui.textEdit.append('Соединение завершено')
        except visa.Error as ex:
            self.ui.textEdit.append('Ошибка: %s' % ex)

    def turn_all_channels_on(self):
        """ Включить все каналы """
        KEYSIGHT.write("OUTPut:STATe ON, (@1)")
        time.sleep(0.1)
        KEYSIGHT.write("OUTPut:STATe ON, (@2)")
        time.sleep(0.1)
        KEYSIGHT.write("OUTPut:STATe ON, (@3)")
        time.sleep(0.1)
        self.ui.textEdit.append('ВНИМАНИЕ! Все каналы работают')

    def emergency_stop(self):
        """ Аварийное отключение всех каналов """
        KEYSIGHT.write("OUTPut:STATe OFF, (@1)")
        time.sleep(0.1)
        KEYSIGHT.write("OUTPut:STATe OFF, (@2)")
        time.sleep(0.1)
        KEYSIGHT.write("OUTPut:STATe OFF, (@3)")
        time.sleep(0.1)
        self.ui.textEdit.append('ВНИМАНИЕ! Выполнено аварийное отключение')

    def set_current_to_channel_one(self):
        """ Установка тока """
        current_variable = self.ui.lineEdit_I_Ch1.text()

        if self.ui.lineEdit_I_Ch1.text().replace('.', '', 1).isdigit():
            KEYSIGHT.write("CURRent " + current_variable + ", (@1)")
            self.ui.textEdit.append('Ограничение по току на перовом канале: ' + current_variable + ' A')
        else:
            self.ui.textEdit.append("Ошибка: неверный формат ввода данных")

    def set_current_to_channel_two(self):
        """ Установка тока """
        current_variable = self.ui.lineEdit_I_Ch2.text()

        if self.ui.lineEdit_I_Ch2.text().replace('.', '', 1).isdigit():
            KEYSIGHT.write("CURRent " + current_variable + ", (@2)")
            self.ui.textEdit.append('Ограничение по току на втором канале: ' + current_variable + ' A')
        else:
            self.ui.textEdit.append("Ошибка: неверный формат ввода данных")

    def set_current_to_channel_three(self):
        """ Установка тока """
        current_variable = self.ui.lineEdit_I_Ch3.text()

        if self.ui.lineEdit_I_Ch3.text().replace('.', '', 1).isdigit():
            KEYSIGHT.write("CURRent " + current_variable + ", (@3)")
            self.ui.textEdit.append('Ограничение по току на третьем канале: ' + current_variable + ' A')
        else:
            self.ui.textEdit.append("Ошибка: неверный формат ввода данных")

    def set_voltage_to_channel_one(self):
        """ Установка напряжения """
        voltage_variable = self.ui.lineEdit_V_Ch1.text()

        if self.ui.lineEdit_V_Ch1.text().replace('.', '', 1).isdigit():
            KEYSIGHT.write("VOLTage " + voltage_variable + ", (@1)")
            self.ui.textEdit.append('Напряжение на перовом канале: ' + voltage_variable + ' В')
        else:
            self.ui.textEdit.append("Ошибка: неверный формат ввода данных")

    def set_voltage_to_channel_two(self):
        """ Установка напряжения """
        voltage_variable = self.ui.lineEdit_V_Ch2.text()
        if self.ui.lineEdit_V_Ch2.text().replace('.', '', 1).isdigit():
            KEYSIGHT.write("VOLTage " + voltage_variable + ", (@2)")
            self.ui.textEdit.append('Напряжение на втором канале: ' + voltage_variable + ' В')
        else:
            self.ui.textEdit.append("Ошибка: неверный формат ввода данных")

    def set_voltage_to_channel_three(self):
        """ Установка напряжения """
        voltage_variable = self.ui.lineEdit_V_Ch3.text()

        if self.ui.lineEdit_V_Ch3.text().replace('.', '', 1).isdigit():
            KEYSIGHT.write("VOLTage " + voltage_variable + ", (@3)")
            self.ui.textEdit.append('Напряжение на третьем канале: ' + voltage_variable + ' В')
        else:
            self.ui.textEdit.append("Ошибка: неверный формат ввода данных")

    def turn_on_channel_one(self):
        """ Включить канал """
        if self.ui.pushButton_Ch1.isChecked():
            KEYSIGHT.write("OUTPut:STATe ON, (@1)")
            self.ui.textEdit.append('Первый канал работает')
            self.ui.pushButton_Ch1.setText('Выключить')
        else:
            KEYSIGHT.write("OUTPut:STATe OFF, (@1)")
            self.ui.textEdit.append('Первый канал отключен')
            self.ui.pushButton_Ch1.setText('Включить')

    def turn_on_channel_two(self):
        """ Включить канал """
        if self.ui.pushButton_Ch2.isChecked():
            KEYSIGHT.write("OUTPut:STATe ON, (@2)")
            self.ui.textEdit.append('Второй канал работает')
            self.ui.pushButton_Ch2.setText('Выключить')
        else:
            KEYSIGHT.write("OUTPut:STATe OFF, (@2)")
            self.ui.textEdit.append('Второй канал отключен')
            self.ui.pushButton_Ch2.setText('Включить')

    def turn_on_channel_three(self):
        """ Включить канал """
        if self.ui.pushButton_Ch3.isChecked():
            KEYSIGHT.write("OUTPut:STATe ON, (@3)")
            self.ui.textEdit.append('Третий канал работает')
            self.ui.pushButton_Ch3.setText('Выключить')
        else:
            KEYSIGHT.write("OUTPut:STATe OFF, (@3)")
            self.ui.textEdit.append('Третий канал отключен')
            self.ui.pushButton_Ch3.setText('Включить')

if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    MY_APP = Window()
    MY_APP.show()
    sys.exit(APP.exec_())
    