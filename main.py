import math
import sys
import random
from random import randint
from time import localtime, strftime

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtCore import QFile
from PySide6.QtGui import QPainter
from PySide6.QtCharts import QChart, QChartView
from ui_main import Ui_MainWindow
from scipy.interpolate import make_interp_spline
import numpy as np
from chart import Chart
import pyqtgraph as pg
from usb_connections import communication


QtGui.QImageReader.setAllocationLimit(0)

shadow_elements = {
    "frame",
    "frame_2",
}


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        # self.graphWidget = pg.GraphicsLayoutWidget()

        self.graphWidget = pg.PlotWidget()
        self.x_plot = list(range(1000))
        self.y_plot = list(range(1000))
        self.graphWidget.setBackground('w')
        #self.label = pg.LabelItem(text='test', justify='right')

        self.pen = pg.mkPen(color=(255, 0, 0), width=2)
        # self.data_line = self.graphWidget.addPlot(self.x_plot, self.y_plot, pen=self.pen)
        self.data_line = self.graphWidget.plot(self.x_plot, self.y_plot, pen=self.pen)
        #self.graphWidget.addItem(self.label)
        self.graphWidget.showGrid(x=True, y=True, alpha=1.0)
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.graphWidget.addItem(self.vLine, ignoreBounds=True)
        self.graphWidget.addItem(self.hLine, ignoreBounds=True)
        # self.graphWidget.setAutoPan(y=True, x=True)
        self.vb = self.graphWidget.plotItem.vb
        self.graphWidget.scene().sigMouseMoved.connect(self.mouseMoved)
        self.ui.gridLayout.addWidget(self.graphWidget)
        self.clock_timer = QTimer()
        self.clock_timer.setInterval(500)
        self.clock_timer.timeout.connect(self.clock)
        self.clock_timer.start()

        # self.usb = communication.UsbCommunication()

        self.dl = communication.DlmmUSB(0x5750, 0x0483)
        self.connection_timer = QTimer()
        self.connection_timer.setInterval(500)
        self.connection_timer.timeout.connect(self.check_device_connection)
        self.connection_timer.start()
        self.sensor_btns = [self.ui.btn_conn_1, self.ui.btn_conn_2, self.ui.btn_conn_3, self.ui.btn_conn_4,
                            self.ui.btn_conn_5, self.ui.btn_conn_6, self.ui.btn_conn_7, self.ui.btn_conn_8]
        self.sensor_names = [self.ui.label_name_1, self.ui.label_name_2, self.ui.label_name_3, self.ui.label_name_4,
                             self.ui.label_name_5, self.ui.label_name_6, self.ui.label_name_7, self.ui.label_name_8]
        self.sensor_values = [self.ui.label_value_1, self.ui.label_value_2, self.ui.label_value_3, self.ui.label_value_4,
                              self.ui.label_value_5, self.ui.label_value_6, self.ui.label_value_7, self.ui.label_value_8]
        self.sensor_btns_start = [self.ui.btn_start_1, self.ui.btn_start_2, self.ui.btn_start_3,
                                  self.ui.btn_start_4, self.ui.btn_start_5, self.ui.btn_start_6,
                                  self.ui.btn_start_7, self.ui.btn_start_8]
        self.sensor_btns_stop = [self.ui.btn_stop_1, self.ui.btn_stop_2, self.ui.btn_stop_3,
                                 self.ui.btn_stop_4, self.ui.btn_stop_5, self.ui.btn_stop_6,
                                 self.ui.btn_stop_7, self.ui.btn_stop_8]

        self.sensor_edits_hz = [self.ui.lineEdit_hz_1, self.ui.lineEdit_hz_2, self.ui.lineEdit_hz_3,
                                self.ui.lineEdit_hz_4, self.ui.lineEdit_hz_5, self.ui.lineEdit_hz_6,
                                self.ui.lineEdit_hz_7, self.ui.lineEdit_hz_8]

        self.last_btn_clicked = 0
        self.ui.btn_start.clicked.connect(self.btn_start_action)
        self.ui.btn_stop.clicked.connect(self.btn_stop_action)
        self.ui.lineEdit.textChanged.connect(self.edit_hz_one_action)
        for i in self.sensor_edits_hz:
            i.textChanged.connect(self.edit_hz_action)
        for i in self.sensor_btns_start:
            i.clicked.connect(self.btn_start_one_sensor)
        for i in self.sensor_btns_stop:
            i.clicked.connect(self.btn_stop_one_sensor)

        self.timers = [QTimer() for _ in range(8)]
        for i in self.timers:
            i.timeout.connect(self.handle_timeout)

        self.sensors = [communication.Sensor(index=i) for i in range(8)]
        for i in self.timers:
            i.setInterval(1000)
        self.device_connected = 1
        self.check_device_connection()
        # self.sensors_id = self.usb.check_connections()
        self.set_shadow()
        self.check_connections()
        self.ui.btn_all_sensors.clicked.connect(self.btn_all_sensors_action)
        for i in self.sensor_btns:
            i.clicked.connect(self.btn_sensor_action)
        now = strftime("%Y", localtime())
        self.ui.label_5.setText(f'© DCIE {now}')

    def clock(self):
        #print(localtime())
        curr_time = strftime("%H:%M:%S %Y-%m-%d", localtime())
        self.ui.label_16.setText(curr_time)

    def mouseMoved(self, evt):

        pos = evt
        #print(pos)
        #if self.data_line.sceneBoundingRect().contains(pos):
        #print("mouse")
        mousePoint = self.vb.mapSceneToView(pos)
        #print(mousePoint.x())
        index = mousePoint.x()
        y_ind = round((index-self.x_plot[0])*10)+10
        if y_ind >= 1000:
            y_ind = 999
        elif y_ind <= 0:
            y_ind = 0
        y_val = round(self.y_plot[y_ind], 2)
        #print(self.x_plot)
        # print(self.x_plot[0], index, int((index-self.x_plot[0]-1)*10),  y_val, self.y_plot[int((index-self.x_plot[0])-1)*10])
        self.graphWidget.setTitle(f"<span style='font-size: 12pt'>x={round(index, 2)}, "
            f"<span style='color: red'>y={y_val}</span>")
        '''if index > 0 and index < 100:
            self.label.setText(
            f"<span style='font-size: 4pt'>x={round(mousePoint.x(), 2)},   "
            f"<span style='color: red'>y1={self.sensors[self.last_btn_clicked].y[index]}</span>,   "
            f"<span style='color: green'>y2={self.sensors[self.last_btn_clicked].y[index]}</span>")'''
        self.vLine.setPos(mousePoint.x())
        self.hLine.setPos(mousePoint.y())

    @staticmethod
    def example_func(x):
        return math.sin(x*3) + 4*math.sin(x)

    def update_data(self, i: int):
        self.sensors[i].x = self.sensors[i].x[1:]
        self.sensors[i].x.append(self.sensors[i].x[-1] + 1)
        self.sensors[i].y = self.sensors[i].y[1:]
        data = self.dl.get_data_from_sensor(self.sensors[i])
        #print(data)
        # self.sensors[i].y.append(self.example_func(self.sensors[i].x[-1]))
        self.sensors[i].y.append(data)
        # print(sum(self.sensors[i].y[-50:])/len(self.sensors[i].y[-50:]))
        # print(self.sensors[i].x)
        self.x_plot = np.linspace(min(self.sensors[i].x), max(self.sensors[i].x), 1000)
        spl = make_interp_spline(self.sensors[i].x, self.sensors[i].y, 3)
        self.y_plot = spl(self.x_plot)
        # print(self.x_plot[999], self.y_plot[999])
        #self.sensor_values[i].setText(str(self.sensors[i].y[-1]))
        #print(self.sensors[i].y)
        #self.data_line.setData(self.sensors[i].x, self.sensors[i].y)

    def edit_hz_one_action(self):
        sender = self.sender()
        try:
            #print(f"new hz: {sender.text()}")
            new_hz = int(sender.text())

        except ValueError:
            new_hz = 1
        if new_hz > 10:
            new_hz = 10
            sender.setText(str(new_hz))
        self.sensors[self.last_btn_clicked].frequency = new_hz
        self.timers[self.last_btn_clicked].setInterval(int(1 / new_hz * 1000))

    def edit_hz_action(self):
        sender = self.sender()
        idx = 0
        for i, j in enumerate(self.sensor_edits_hz):
            if sender is j:
                idx = i
        try:
            new_hz = int(sender.text())
        except ValueError:
            new_hz = 1
        if new_hz > 10:
            new_hz = 10
            sender.setText(str(new_hz))
        self.sensors[idx].frequency = new_hz
        # print(int(1/new_hz*1000))
        self.timers[idx].setInterval(int(1/new_hz*1000))

    def btn_start_one_sensor(self):
        sender = self.sender()
        idx = 0
        for i, j in enumerate(self.sensor_btns_start):
            if sender is j:
                idx = i
                break
        if not self.timers[idx].isActive():
            self.timers[idx].start()
            self.sensors[idx].running = True

    def btn_stop_one_sensor(self):
        sender = self.sender()
        idx = 0
        for i, j in enumerate(self.sensor_btns_stop):
            if sender is j:
                idx = i
                break
        if self.timers[idx].isActive():
            self.timers[idx].stop()
            self.sensors[idx].running = False

    def handle_timeout(self):
        sender = self.sender()
        idx = 0
        for i, j in enumerate(self.timers):
            if j is sender:
                idx = i
                break

        if self.sensors[idx].running:
            self.update_data(idx)
        if self.last_btn_clicked == idx:
            #print(self.x_plot[0])
            self.ui.label_sensor_value.setText(f'{round(self.sensors[idx].y[-1], 2)}')
            #self.data_line.setData(self.sensors[idx].x, self.sensors[idx].y)
            self.data_line.setData(self.x_plot, self.y_plot)
            self.graphWidget.setXRange(int(self.x_plot[0]), int(self.x_plot[-1]), padding=None, update=True)
        self.sensor_values[idx].setText(f'{round(self.sensors[idx].y[-1], 2)}')
        #if self.ui.stackedWidget.currentWidget() is self.ui.one_sensor:

    def check_device_connection(self):
        # print('check_device_connection')
        self.dl.get_available_sensors(self.sensors)
        self.check_connections()
        # print(self.dl.device)
        if self.dl.device is not None:
            self.ui.label_15.setStyleSheet("""background-color: #00AE68""")
            self.ui.label_6.setText("Модуль подключен")

        else:
            self.ui.label_15.setStyleSheet("""background-color: #bf0600""")
            self.ui.label_6.setText("Модуль отключен")

    def btn_all_sensors_action(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.all_sensors)
        for i, j in enumerate(self.sensor_edits_hz):
            #print(self.sensors[i].frequency)
            j.setText(str(self.sensors[i].frequency))

    def btn_sensor_action(self):
        # print(self.sender().text())
        sender = int(self.sender().text().split()[0]) - 1
        # print(sender)
        self.last_btn_clicked = sender
        self.ui.stackedWidget.setCurrentWidget(self.ui.one_sensor)
        #print(self.last_btn_clicked, self.sensors[sender].y)
        self.ui.label_sensor_name.setText(self.sensors[sender].name)
        self.ui.lineEdit.setText(str(self.sensors[self.last_btn_clicked].frequency))
        self.data_line.setData(self.sensors[sender].x, self.sensors[sender].y)

        #self.data_line.setData(self.x_plot, self.y_plot)
        if self.timers[sender].isActive():

            self.ui.label_sensor_value.setText(f'{round(self.sensors[sender].y[-1], 2)}')

        else:
            self.ui.label_sensor_value.setText("------")
        #print(f"btn {self.sender().text()} checked")

    def btn_start_action(self):
        if not self.timers[self.last_btn_clicked].isActive():
            self.timers[self.last_btn_clicked].start()
            self.sensors[self.last_btn_clicked].running = True

    def btn_stop_action(self):
        if self.timers[self.last_btn_clicked].isActive():
            self.timers[self.last_btn_clicked].stop()
            self.ui.label_sensor_value.setText("------")
            self.sensor_values[self.last_btn_clicked].setText("------")
            self.sensors[self.last_btn_clicked].running = False

    def check_connections(self):
        for i in self.sensor_btns:
            i.setEnabled(False)
        for i, s in enumerate(self.sensors):
            # print(s.connected)
            if s.connected:
                self.sensor_btns[i].setEnabled(True)
                self.sensor_btns[i].setText(f'{i+1} {self.sensors[i].name}')
                self.sensors[i].id = i
                self.sensors[i].connected = True
                self.sensors[i].name = self.sensors[i].name
                self.sensor_names[i].setText(self.sensors[i].name)
            else:
                self.sensor_btns[i].setText(f'{i+1} разъём')
                self.sensor_names[i].setText("Не подключен")
                self.sensor_values[i].setText("------")
                self.sensor_btns_start[i].setEnabled(False)
                self.sensor_btns_stop[i].setEnabled(False)
                self.sensors[i].id = i
        if True not in [i.running for i in self.sensors]:
            if self.dl.start_condition:
                self.dl.set_start_condition(0x21)
        '''for i in self.sensors_id:
            self.sensor_btns[i].setEnabled(True)
        for i in range(len(self.sensor_names)):
            if i not in self.sensors_id:
                self.sensor_names[i].setText("Не подключен")
                self.sensor_values[i].setText("------")
                self.sensor_btns_start[i].setEnabled(False)
                self.sensor_btns_stop[i].setEnabled(False)
                self.sensors[i].id = i
            else:
                self.sensors[i].id = i
                self.sensors[i].connected = True
                self.sensors[i].name = f'Датчик {i+1}'
                self.sensor_names[i].setText(self.sensors[i].name)'''

    def set_shadow(self):
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(3)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 50))
            getattr(self.ui, x).setGraphicsEffect(effect)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
