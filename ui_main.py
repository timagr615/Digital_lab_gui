# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1204, 1079)
        MainWindow.setStyleSheet(u"\n"
"font-family: OpenSans-Regular;\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"\n"
"font-family: OpenSans-Regular;\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"#comboBox{\n"
"border: 1px solid #ced4da;\n"
"border-radius: 4px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#comboBox::on {\n"
"border: 4px solid #c2dbfe;\n"
"}\n"
"\n"
"#comboBox QListView {\n"
"font-size: 12px;\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"padding: 5px;\n"
"background-color: #fff;\n"
"outline: 0px;\n"
"}\n"
"\n"
"#comboBox QListView::item {\n"
"padding-left: 10px;\n"
"background-color: #fff;\n"
"}\n"
"\n"
"#comboBox QListView::item::hover {\n"
"background-color: #1e90ff;\n"
"}\n"
"\n"
"#comboBox QListView::item::selected {\n"
"background-color: #1e90ff;\n"
"}\n"
"\n"
"#label_15{\n"
"border-radius: 3px;\n"
"background-color: rgba(236, 50, 50, 1);\n"
"}\n"
"\n"
"\n"
"#btn_save{\n"
"background-color: #3F92D2	;\n"
"}\n"
"#btn_save::pressed\n"
"{\n"
"	background-color: #0B61A4	;\n"
"\n"
"}\n"
"\n"
"#btn_save::hover,\n"
"#btn_save::focus {\n"
"  background-color: #0B61A4		;\n"
"  border: 3px solid #9ac3fe;\n"
""
                        "}\n"
"\n"
"\n"
"#btn_stop{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop::hover,\n"
"#btn_stop::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#btn_start::hover,\n"
"#btn_start::focus {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"#centralwidget {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(223, 228, 248, 0.5), stop:1 rgba(0, 56, 255, 0.5));\n"
"}\n"
"QLineEdit{\n"
"background-color: #e6eaef;\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"#label_sd_detect {\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#label_sd_size {\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#label_sd_date{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_sd_sensors{\n"
"border-top: 1px solid #586178	;\n"
""
                        "}\n"
"#frame_sd_plot{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame {\n"
"border: 1px solid #586178	;\n"
"border-radius: 8px;\n"
"}\n"
"#frame_2{\n"
"border: 1px solid #586178	;\n"
"border-radius: 8px;\n"
"}\n"
"#frame_14{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"#frame_7{\n"
"\n"
"border-top: 3px solid #586178	;\n"
"}\n"
"\n"
"#frame_5{\n"
"\n"
"border-bottom: 3px solid #586178	;\n"
"}\n"
"#frame_10{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_12{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_11{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_22{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_sens_2{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_sens_3{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_sens_4{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_sens_5{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_sens_6{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_sens_7{\n"
"border"
                        "-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_sens_8{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_sens_9{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_sens_10{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_sens_11{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_25{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"#frame_26{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"#frame_27{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"#frame_28{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"#frame_29{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"#frame_30{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_55{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_56{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_6{\n"
"border-top: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_16{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_17{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_18{\n"
"\n"
"border-right: 1px solid #586178	;"
                        "\n"
"}\n"
"#frame_20{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_21{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_23{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_31{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_32{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_33{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_35{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_36{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_37{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_39{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_40{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_41{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_47{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_48{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_49{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_43{\n"
"\n"
"border-right: 1px solid #586178	;\n"
""
                        "}\n"
"#frame_44{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_45{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_51{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_52{\n"
"\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"#frame_53{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_60{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_67{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_61{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_57{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_58{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_59{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_65{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_63{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"#frame_64{\n"
"border-right: 1px solid #586178	;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color: #3F92D2;\n"
"	color: #fff;\n"
"	font-size: 11px;\n"
"	font-weight: bold;\n"
"	bord"
                        "er: none;\n"
"	border-radius: 25px;\n"
"	\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #5c5c5c;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"QPushButton {\n"
"  background-color: #0d6efd;\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 5px 15px;\n"
"  \n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color: #0b5ed7;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"#btn_stop_1{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop_1::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_1::hover,\n"
"#btn_stop_1::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_1 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_1::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#btn_start_1::hover,\n"
"#btn_start_1::focus {\n"
"  background-color: #0"
                        "0bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"\n"
"#btn_stop_2{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop_2::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_2::hover,\n"
"#btn_stop_2::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_2 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_2::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#btn_start_2::hover,\n"
"#btn_start_2::focus {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"\n"
"#btn_stop_3{\n"
"background-color: #FF7373;\n"
"}\n"
"\n"
"#btn_stop_3::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_3::hover,\n"
"#btn_stop_3::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_3 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_3::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#btn_start_3::hover,\n"
"#btn_start_3::focu"
                        "s {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"\n"
"#btn_stop_4{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop_4::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_4::hover,\n"
"#btn_stop_4::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_4 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_4::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#btn_start_4::hover,\n"
"#btn_start_4::focus {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"\n"
"#btn_stop_5{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop_5::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_5::hover,\n"
"#btn_stop_5::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_5 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_5::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#btn_start_5::hove"
                        "r,\n"
"#btn_start_5::focus {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"#btn_stop_6{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop_6::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_6::hover,\n"
"#btn_stop_6::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_6 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_6::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#btn_start_6::hover,\n"
"#btn_start_6::focus {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"#btn_stop_7{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop_7::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_7::hover,\n"
"#btn_stop_7::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_7 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_7::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#bt"
                        "n_start_7::hover,\n"
"#btn_start_7::focus {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"\n"
"#btn_stop_8{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop_8::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_8::hover,\n"
"#btn_stop_8::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_8 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_8::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#btn_start_8::hover,\n"
"#btn_start_8::focus {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"#btn_stop_9{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop_9::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_9::hover,\n"
"#btn_stop_9::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_9 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_9::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
""
                        "\n"
"}\n"
"\n"
"#btn_start_9::hover,\n"
"#btn_start_9::focus {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"#btn_stop_10{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop_10::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_10::hover,\n"
"#btn_stop_10::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_10 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_10::pressed\n"
"{\n"
"	background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#btn_start_10::hover,\n"
"#btn_start_10::focus {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"#btn_stop_11{\n"
"background-color: #FF7373;\n"
"}\n"
"#btn_stop_11::pressed\n"
"{\n"
"	background-color: #bf0600;\n"
"\n"
"}\n"
"\n"
"#btn_stop_11::hover,\n"
"#btn_stop_11::focus {\n"
"  background-color: #bf0600	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"#btn_start_11 {\n"
"background-color: #00AE68;\n"
"}\n"
"#btn_start_11::pressed\n"
"{\n"
"	ba"
                        "ckground-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"#btn_start_11::hover,\n"
"#btn_start_11::focus {\n"
"  background-color: #00bf06	;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(260, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 115))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(220, 0))
        self.label.setMaximumSize(QSize(220, 95))
        self.label.setPixmap(QPixmap(u":/images/images/logo.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_conn_1 = QPushButton(self.frame_4)
        self.btn_conn_1.setObjectName(u"btn_conn_1")
        self.btn_conn_1.setEnabled(True)
        self.btn_conn_1.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.btn_conn_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_conn_2 = QPushButton(self.frame_4)
        self.btn_conn_2.setObjectName(u"btn_conn_2")
        self.btn_conn_2.setEnabled(True)

        self.horizontalLayout_9.addWidget(self.btn_conn_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_conn_3 = QPushButton(self.frame_4)
        self.btn_conn_3.setObjectName(u"btn_conn_3")
        self.btn_conn_3.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.btn_conn_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_conn_4 = QPushButton(self.frame_4)
        self.btn_conn_4.setObjectName(u"btn_conn_4")
        self.btn_conn_4.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.btn_conn_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_conn_5 = QPushButton(self.frame_4)
        self.btn_conn_5.setObjectName(u"btn_conn_5")
        self.btn_conn_5.setEnabled(False)

        self.horizontalLayout_12.addWidget(self.btn_conn_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_conn_6 = QPushButton(self.frame_4)
        self.btn_conn_6.setObjectName(u"btn_conn_6")
        self.btn_conn_6.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.btn_conn_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_conn_7 = QPushButton(self.frame_4)
        self.btn_conn_7.setObjectName(u"btn_conn_7")
        self.btn_conn_7.setEnabled(False)

        self.horizontalLayout_14.addWidget(self.btn_conn_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_conn_8 = QPushButton(self.frame_4)
        self.btn_conn_8.setObjectName(u"btn_conn_8")
        self.btn_conn_8.setEnabled(False)

        self.horizontalLayout_15.addWidget(self.btn_conn_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.btn_conn_9 = QPushButton(self.frame_4)
        self.btn_conn_9.setObjectName(u"btn_conn_9")

        self.horizontalLayout_35.addWidget(self.btn_conn_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_35)

        self.btn_conn_10 = QPushButton(self.frame_4)
        self.btn_conn_10.setObjectName(u"btn_conn_10")

        self.verticalLayout_2.addWidget(self.btn_conn_10)

        self.btn_conn_11 = QPushButton(self.frame_4)
        self.btn_conn_11.setObjectName(u"btn_conn_11")

        self.verticalLayout_2.addWidget(self.btn_conn_11)


        self.verticalLayout.addWidget(self.frame_4)

        self.btn_all_sensors = QPushButton(self.frame)
        self.btn_all_sensors.setObjectName(u"btn_all_sensors")

        self.verticalLayout.addWidget(self.btn_all_sensors)

        self.btn_sd_data = QPushButton(self.frame)
        self.btn_sd_data.setObjectName(u"btn_sd_data")

        self.verticalLayout.addWidget(self.btn_sd_data)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(40, 40))
        self.label_15.setPixmap(QPixmap(u":/icons/icons/usb_FILL0_wght400_GRAD0_opsz48.svg"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_15)

        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)


        self.verticalLayout.addWidget(self.frame_14)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.one_sensor = QWidget()
        self.one_sensor.setObjectName(u"one_sensor")
        self.verticalLayout_4 = QVBoxLayout(self.one_sensor)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.one_sensor)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 100))
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        font = QFont()
        font.setFamilies([u"OpenSans-Regular"])
        font.setPointSize(16)
        self.frame_10.setFont(font)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_sensor_name = QLabel(self.frame_10)
        self.label_sensor_name.setObjectName(u"label_sensor_name")
        self.label_sensor_name.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_sensor_name)


        self.horizontalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(150, 200))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.frame_11)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_3.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(100, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_sensor_value = QLabel(self.frame_12)
        self.label_sensor_value.setObjectName(u"label_sensor_value")
        self.label_sensor_value.setFont(font)

        self.verticalLayout_6.addWidget(self.label_sensor_value)


        self.horizontalLayout_3.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_save = QPushButton(self.frame_13)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon)
        self.btn_save.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.btn_save)

        self.btn_start = QPushButton(self.frame_13)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/play_circle_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start.setIcon(icon1)
        self.btn_start.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.btn_start)

        self.btn_stop = QPushButton(self.frame_13)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMaximumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/stop_circle_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stop.setIcon(icon2)
        self.btn_stop.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.btn_stop)


        self.horizontalLayout_3.addWidget(self.frame_13)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_chart = QFrame(self.one_sensor)
        self.frame_chart.setObjectName(u"frame_chart")
        self.frame_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_chart.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_chart)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.horizontalLayout_34.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.frame_chart)

        self.frame_7 = QFrame(self.one_sensor)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 60))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_16.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_17.addWidget(self.label_16)


        self.horizontalLayout_6.addWidget(self.frame_9)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.one_sensor)
        self.all_sensors = QWidget()
        self.all_sensors.setObjectName(u"all_sensors")
        self.verticalLayout_40 = QVBoxLayout(self.all_sensors)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_sens_1 = QFrame(self.all_sensors)
        self.frame_sens_1.setObjectName(u"frame_sens_1")
        self.frame_sens_1.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_1.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_sens_1)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_16 = QFrame(self.frame_sens_1)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_name_1 = QLabel(self.frame_16)
        self.label_name_1.setObjectName(u"label_name_1")
        self.label_name_1.setFont(font)

        self.verticalLayout_8.addWidget(self.label_name_1)


        self.horizontalLayout_18.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_sens_1)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(150, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_17)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_33 = QLabel(self.frame_17)
        self.label_33.setObjectName(u"label_33")
        font1 = QFont()
        font1.setFamilies([u"OpenSans-Regular"])
        font1.setPointSize(11)
        self.label_33.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_33)

        self.lineEdit_hz_1 = QLineEdit(self.frame_17)
        self.lineEdit_hz_1.setObjectName(u"lineEdit_hz_1")

        self.verticalLayout_16.addWidget(self.lineEdit_hz_1)


        self.horizontalLayout_18.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_sens_1)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_18)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_value_1 = QLabel(self.frame_18)
        self.label_value_1.setObjectName(u"label_value_1")
        self.label_value_1.setFont(font)

        self.verticalLayout_24.addWidget(self.label_value_1)


        self.horizontalLayout_18.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_sens_1)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.btn_start_1 = QPushButton(self.frame_19)
        self.btn_start_1.setObjectName(u"btn_start_1")
        self.btn_start_1.setMinimumSize(QSize(0, 0))
        self.btn_start_1.setMaximumSize(QSize(50, 50))
        self.btn_start_1.setIcon(icon1)
        self.btn_start_1.setIconSize(QSize(35, 35))

        self.horizontalLayout_26.addWidget(self.btn_start_1)

        self.btn_stop_1 = QPushButton(self.frame_19)
        self.btn_stop_1.setObjectName(u"btn_stop_1")
        self.btn_stop_1.setMaximumSize(QSize(50, 50))
        self.btn_stop_1.setIcon(icon2)
        self.btn_stop_1.setIconSize(QSize(35, 35))

        self.horizontalLayout_26.addWidget(self.btn_stop_1)


        self.horizontalLayout_18.addWidget(self.frame_19)


        self.verticalLayout_40.addWidget(self.frame_sens_1)

        self.frame_sens_2 = QFrame(self.all_sensors)
        self.frame_sens_2.setObjectName(u"frame_sens_2")
        self.frame_sens_2.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_2.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_sens_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_20 = QFrame(self.frame_sens_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_name_2 = QLabel(self.frame_20)
        self.label_name_2.setObjectName(u"label_name_2")
        self.label_name_2.setFont(font)

        self.verticalLayout_9.addWidget(self.label_name_2)


        self.horizontalLayout_19.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_sens_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(150, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_21)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_34 = QLabel(self.frame_21)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_17.addWidget(self.label_34)

        self.lineEdit_hz_2 = QLineEdit(self.frame_21)
        self.lineEdit_hz_2.setObjectName(u"lineEdit_hz_2")

        self.verticalLayout_17.addWidget(self.lineEdit_hz_2)


        self.horizontalLayout_19.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.frame_sens_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_23)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_value_2 = QLabel(self.frame_23)
        self.label_value_2.setObjectName(u"label_value_2")
        self.label_value_2.setFont(font)

        self.verticalLayout_25.addWidget(self.label_value_2)


        self.horizontalLayout_19.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_sens_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.btn_start_2 = QPushButton(self.frame_24)
        self.btn_start_2.setObjectName(u"btn_start_2")
        self.btn_start_2.setMaximumSize(QSize(50, 50))
        self.btn_start_2.setIcon(icon1)
        self.btn_start_2.setIconSize(QSize(35, 35))

        self.horizontalLayout_27.addWidget(self.btn_start_2)

        self.btn_stop_2 = QPushButton(self.frame_24)
        self.btn_stop_2.setObjectName(u"btn_stop_2")
        self.btn_stop_2.setMaximumSize(QSize(50, 50))
        self.btn_stop_2.setIcon(icon2)
        self.btn_stop_2.setIconSize(QSize(35, 35))

        self.horizontalLayout_27.addWidget(self.btn_stop_2)


        self.horizontalLayout_19.addWidget(self.frame_24)


        self.verticalLayout_40.addWidget(self.frame_sens_2)

        self.frame_sens_3 = QFrame(self.all_sensors)
        self.frame_sens_3.setObjectName(u"frame_sens_3")
        self.frame_sens_3.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_3.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_sens_3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_31 = QFrame(self.frame_sens_3)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_31)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_name_3 = QLabel(self.frame_31)
        self.label_name_3.setObjectName(u"label_name_3")
        self.label_name_3.setFont(font)

        self.verticalLayout_10.addWidget(self.label_name_3)


        self.horizontalLayout_20.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_sens_3)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(150, 16777215))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_32)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_35 = QLabel(self.frame_32)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_18.addWidget(self.label_35)

        self.lineEdit_hz_3 = QLineEdit(self.frame_32)
        self.lineEdit_hz_3.setObjectName(u"lineEdit_hz_3")

        self.verticalLayout_18.addWidget(self.lineEdit_hz_3)


        self.horizontalLayout_20.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_sens_3)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_33)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_value_3 = QLabel(self.frame_33)
        self.label_value_3.setObjectName(u"label_value_3")
        self.label_value_3.setFont(font)

        self.verticalLayout_26.addWidget(self.label_value_3)


        self.horizontalLayout_20.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_sens_3)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.btn_start_3 = QPushButton(self.frame_34)
        self.btn_start_3.setObjectName(u"btn_start_3")
        self.btn_start_3.setMaximumSize(QSize(50, 50))
        self.btn_start_3.setIcon(icon1)
        self.btn_start_3.setIconSize(QSize(35, 35))

        self.horizontalLayout_28.addWidget(self.btn_start_3)

        self.btn_stop_3 = QPushButton(self.frame_34)
        self.btn_stop_3.setObjectName(u"btn_stop_3")
        self.btn_stop_3.setMaximumSize(QSize(50, 50))
        self.btn_stop_3.setIcon(icon2)
        self.btn_stop_3.setIconSize(QSize(35, 35))

        self.horizontalLayout_28.addWidget(self.btn_stop_3)


        self.horizontalLayout_20.addWidget(self.frame_34)


        self.verticalLayout_40.addWidget(self.frame_sens_3)

        self.frame_sens_4 = QFrame(self.all_sensors)
        self.frame_sens_4.setObjectName(u"frame_sens_4")
        self.frame_sens_4.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_4.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_sens_4)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_35 = QFrame(self.frame_sens_4)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_35)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_name_4 = QLabel(self.frame_35)
        self.label_name_4.setObjectName(u"label_name_4")
        self.label_name_4.setFont(font)

        self.verticalLayout_11.addWidget(self.label_name_4)


        self.horizontalLayout_25.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_sens_4)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(150, 16777215))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_36)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_36 = QLabel(self.frame_36)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_19.addWidget(self.label_36)

        self.lineEdit_hz_4 = QLineEdit(self.frame_36)
        self.lineEdit_hz_4.setObjectName(u"lineEdit_hz_4")

        self.verticalLayout_19.addWidget(self.lineEdit_hz_4)


        self.horizontalLayout_25.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_sens_4)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_value_4 = QLabel(self.frame_37)
        self.label_value_4.setObjectName(u"label_value_4")
        self.label_value_4.setFont(font)

        self.verticalLayout_27.addWidget(self.label_value_4)


        self.horizontalLayout_25.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_sens_4)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.btn_start_4 = QPushButton(self.frame_38)
        self.btn_start_4.setObjectName(u"btn_start_4")
        self.btn_start_4.setMaximumSize(QSize(50, 50))
        self.btn_start_4.setIcon(icon1)
        self.btn_start_4.setIconSize(QSize(35, 35))

        self.horizontalLayout_29.addWidget(self.btn_start_4)

        self.btn_stop_4 = QPushButton(self.frame_38)
        self.btn_stop_4.setObjectName(u"btn_stop_4")
        self.btn_stop_4.setMaximumSize(QSize(50, 50))
        self.btn_stop_4.setIcon(icon2)
        self.btn_stop_4.setIconSize(QSize(35, 35))

        self.horizontalLayout_29.addWidget(self.btn_stop_4)


        self.horizontalLayout_25.addWidget(self.frame_38)


        self.verticalLayout_40.addWidget(self.frame_sens_4)

        self.frame_sens_5 = QFrame(self.all_sensors)
        self.frame_sens_5.setObjectName(u"frame_sens_5")
        self.frame_sens_5.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_5.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_sens_5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_39 = QFrame(self.frame_sens_5)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_39)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_name_5 = QLabel(self.frame_39)
        self.label_name_5.setObjectName(u"label_name_5")
        self.label_name_5.setFont(font)

        self.verticalLayout_12.addWidget(self.label_name_5)


        self.horizontalLayout_24.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_sens_5)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(150, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_40)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_37 = QLabel(self.frame_40)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_20.addWidget(self.label_37)

        self.lineEdit_hz_5 = QLineEdit(self.frame_40)
        self.lineEdit_hz_5.setObjectName(u"lineEdit_hz_5")

        self.verticalLayout_20.addWidget(self.lineEdit_hz_5)


        self.horizontalLayout_24.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_sens_5)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_41)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_value_5 = QLabel(self.frame_41)
        self.label_value_5.setObjectName(u"label_value_5")
        self.label_value_5.setFont(font)

        self.verticalLayout_28.addWidget(self.label_value_5)


        self.horizontalLayout_24.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_sens_5)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.btn_start_5 = QPushButton(self.frame_42)
        self.btn_start_5.setObjectName(u"btn_start_5")
        self.btn_start_5.setMaximumSize(QSize(50, 50))
        self.btn_start_5.setIcon(icon1)
        self.btn_start_5.setIconSize(QSize(35, 35))

        self.horizontalLayout_30.addWidget(self.btn_start_5)

        self.btn_stop_5 = QPushButton(self.frame_42)
        self.btn_stop_5.setObjectName(u"btn_stop_5")
        self.btn_stop_5.setMaximumSize(QSize(50, 50))
        self.btn_stop_5.setIcon(icon2)
        self.btn_stop_5.setIconSize(QSize(35, 35))

        self.horizontalLayout_30.addWidget(self.btn_stop_5)


        self.horizontalLayout_24.addWidget(self.frame_42)


        self.verticalLayout_40.addWidget(self.frame_sens_5)

        self.frame_sens_6 = QFrame(self.all_sensors)
        self.frame_sens_6.setObjectName(u"frame_sens_6")
        self.frame_sens_6.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_6.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_sens_6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_43 = QFrame(self.frame_sens_6)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_43)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_name_6 = QLabel(self.frame_43)
        self.label_name_6.setObjectName(u"label_name_6")
        self.label_name_6.setFont(font)

        self.verticalLayout_13.addWidget(self.label_name_6)


        self.horizontalLayout_23.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_sens_6)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMaximumSize(QSize(150, 16777215))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_44)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_38 = QLabel(self.frame_44)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_21.addWidget(self.label_38)

        self.lineEdit_hz_6 = QLineEdit(self.frame_44)
        self.lineEdit_hz_6.setObjectName(u"lineEdit_hz_6")

        self.verticalLayout_21.addWidget(self.lineEdit_hz_6)


        self.horizontalLayout_23.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_sens_6)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_45)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_value_6 = QLabel(self.frame_45)
        self.label_value_6.setObjectName(u"label_value_6")
        self.label_value_6.setFont(font)

        self.verticalLayout_29.addWidget(self.label_value_6)


        self.horizontalLayout_23.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_sens_6)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.btn_start_6 = QPushButton(self.frame_46)
        self.btn_start_6.setObjectName(u"btn_start_6")
        self.btn_start_6.setMaximumSize(QSize(50, 50))
        self.btn_start_6.setIcon(icon1)
        self.btn_start_6.setIconSize(QSize(35, 35))

        self.horizontalLayout_31.addWidget(self.btn_start_6)

        self.btn_stop_6 = QPushButton(self.frame_46)
        self.btn_stop_6.setObjectName(u"btn_stop_6")
        self.btn_stop_6.setMaximumSize(QSize(50, 50))
        self.btn_stop_6.setIcon(icon2)
        self.btn_stop_6.setIconSize(QSize(35, 35))

        self.horizontalLayout_31.addWidget(self.btn_stop_6)


        self.horizontalLayout_23.addWidget(self.frame_46)


        self.verticalLayout_40.addWidget(self.frame_sens_6)

        self.frame_sens_7 = QFrame(self.all_sensors)
        self.frame_sens_7.setObjectName(u"frame_sens_7")
        self.frame_sens_7.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_7.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_sens_7)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_47 = QFrame(self.frame_sens_7)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_47)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_name_7 = QLabel(self.frame_47)
        self.label_name_7.setObjectName(u"label_name_7")
        self.label_name_7.setFont(font)

        self.verticalLayout_14.addWidget(self.label_name_7)


        self.horizontalLayout_22.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_sens_7)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMaximumSize(QSize(150, 16777215))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_48)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_39 = QLabel(self.frame_48)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_22.addWidget(self.label_39)

        self.lineEdit_hz_7 = QLineEdit(self.frame_48)
        self.lineEdit_hz_7.setObjectName(u"lineEdit_hz_7")

        self.verticalLayout_22.addWidget(self.lineEdit_hz_7)


        self.horizontalLayout_22.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.frame_sens_7)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_49)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_value_7 = QLabel(self.frame_49)
        self.label_value_7.setObjectName(u"label_value_7")
        self.label_value_7.setFont(font)

        self.verticalLayout_30.addWidget(self.label_value_7)


        self.horizontalLayout_22.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_sens_7)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.btn_start_7 = QPushButton(self.frame_50)
        self.btn_start_7.setObjectName(u"btn_start_7")
        self.btn_start_7.setMaximumSize(QSize(50, 50))
        self.btn_start_7.setIcon(icon1)
        self.btn_start_7.setIconSize(QSize(35, 35))

        self.horizontalLayout_32.addWidget(self.btn_start_7)

        self.btn_stop_7 = QPushButton(self.frame_50)
        self.btn_stop_7.setObjectName(u"btn_stop_7")
        self.btn_stop_7.setMaximumSize(QSize(50, 50))
        self.btn_stop_7.setIcon(icon2)
        self.btn_stop_7.setIconSize(QSize(35, 35))

        self.horizontalLayout_32.addWidget(self.btn_stop_7)


        self.horizontalLayout_22.addWidget(self.frame_50)


        self.verticalLayout_40.addWidget(self.frame_sens_7)

        self.frame_sens_8 = QFrame(self.all_sensors)
        self.frame_sens_8.setObjectName(u"frame_sens_8")
        self.frame_sens_8.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_8.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_sens_8)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_51 = QFrame(self.frame_sens_8)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_51)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_name_8 = QLabel(self.frame_51)
        self.label_name_8.setObjectName(u"label_name_8")
        self.label_name_8.setFont(font)

        self.verticalLayout_15.addWidget(self.label_name_8)


        self.horizontalLayout_21.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_sens_8)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(150, 16777215))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_52)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_40 = QLabel(self.frame_52)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_23.addWidget(self.label_40)

        self.lineEdit_hz_8 = QLineEdit(self.frame_52)
        self.lineEdit_hz_8.setObjectName(u"lineEdit_hz_8")

        self.verticalLayout_23.addWidget(self.lineEdit_hz_8)


        self.horizontalLayout_21.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_sens_8)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_53)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_value_8 = QLabel(self.frame_53)
        self.label_value_8.setObjectName(u"label_value_8")
        self.label_value_8.setFont(font)

        self.verticalLayout_31.addWidget(self.label_value_8)


        self.horizontalLayout_21.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_sens_8)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.btn_start_8 = QPushButton(self.frame_54)
        self.btn_start_8.setObjectName(u"btn_start_8")
        self.btn_start_8.setMaximumSize(QSize(50, 50))
        self.btn_start_8.setIcon(icon1)
        self.btn_start_8.setIconSize(QSize(35, 35))

        self.horizontalLayout_33.addWidget(self.btn_start_8)

        self.btn_stop_8 = QPushButton(self.frame_54)
        self.btn_stop_8.setObjectName(u"btn_stop_8")
        self.btn_stop_8.setMaximumSize(QSize(50, 50))
        self.btn_stop_8.setIcon(icon2)
        self.btn_stop_8.setIconSize(QSize(35, 35))

        self.horizontalLayout_33.addWidget(self.btn_stop_8)


        self.horizontalLayout_21.addWidget(self.frame_54)


        self.verticalLayout_40.addWidget(self.frame_sens_8)

        self.frame_sens_9 = QFrame(self.all_sensors)
        self.frame_sens_9.setObjectName(u"frame_sens_9")
        self.frame_sens_9.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_9.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_sens_9)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.frame_60 = QFrame(self.frame_sens_9)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_60)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_name_9 = QLabel(self.frame_60)
        self.label_name_9.setObjectName(u"label_name_9")
        self.label_name_9.setFont(font)

        self.verticalLayout_7.addWidget(self.label_name_9)


        self.horizontalLayout_37.addWidget(self.frame_60)

        self.frame_67 = QFrame(self.frame_sens_9)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMaximumSize(QSize(150, 16777215))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_67)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_9 = QLabel(self.frame_67)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_33.addWidget(self.label_9)

        self.lineEdit_hz_9 = QLineEdit(self.frame_67)
        self.lineEdit_hz_9.setObjectName(u"lineEdit_hz_9")

        self.verticalLayout_33.addWidget(self.lineEdit_hz_9)


        self.horizontalLayout_37.addWidget(self.frame_67)

        self.frame_61 = QFrame(self.frame_sens_9)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_61)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_value_9 = QLabel(self.frame_61)
        self.label_value_9.setObjectName(u"label_value_9")
        self.label_value_9.setFont(font)

        self.verticalLayout_32.addWidget(self.label_value_9)


        self.horizontalLayout_37.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_sens_9)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(30, 0))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.btn_start_9 = QPushButton(self.frame_62)
        self.btn_start_9.setObjectName(u"btn_start_9")
        self.btn_start_9.setMaximumSize(QSize(50, 50))
        self.btn_start_9.setIcon(icon1)
        self.btn_start_9.setIconSize(QSize(35, 35))

        self.horizontalLayout_39.addWidget(self.btn_start_9)

        self.btn_stop_9 = QPushButton(self.frame_62)
        self.btn_stop_9.setObjectName(u"btn_stop_9")
        self.btn_stop_9.setMaximumSize(QSize(50, 50))
        self.btn_stop_9.setIcon(icon2)
        self.btn_stop_9.setIconSize(QSize(35, 35))

        self.horizontalLayout_39.addWidget(self.btn_stop_9)


        self.horizontalLayout_37.addWidget(self.frame_62)


        self.verticalLayout_40.addWidget(self.frame_sens_9)

        self.frame_sens_10 = QFrame(self.all_sensors)
        self.frame_sens_10.setObjectName(u"frame_sens_10")
        self.frame_sens_10.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_10.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_sens_10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.frame_57 = QFrame(self.frame_sens_10)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_57)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_name_10 = QLabel(self.frame_57)
        self.label_name_10.setObjectName(u"label_name_10")
        self.label_name_10.setFont(font)

        self.verticalLayout_37.addWidget(self.label_name_10)


        self.horizontalLayout_36.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_sens_10)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(150, 16777215))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_58)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_13 = QLabel(self.frame_58)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_38.addWidget(self.label_13)

        self.lineEdit_hz_10 = QLineEdit(self.frame_58)
        self.lineEdit_hz_10.setObjectName(u"lineEdit_hz_10")

        self.verticalLayout_38.addWidget(self.lineEdit_hz_10)


        self.horizontalLayout_36.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.frame_sens_10)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_59)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_value_10 = QLabel(self.frame_59)
        self.label_value_10.setObjectName(u"label_value_10")
        self.label_value_10.setFont(font)

        self.verticalLayout_39.addWidget(self.label_value_10)


        self.horizontalLayout_36.addWidget(self.frame_59)

        self.frame_68 = QFrame(self.frame_sens_10)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.btn_start_10 = QPushButton(self.frame_68)
        self.btn_start_10.setObjectName(u"btn_start_10")
        self.btn_start_10.setMaximumSize(QSize(50, 50))
        self.btn_start_10.setIcon(icon1)
        self.btn_start_10.setIconSize(QSize(35, 35))

        self.horizontalLayout_41.addWidget(self.btn_start_10)

        self.btn_stop_10 = QPushButton(self.frame_68)
        self.btn_stop_10.setObjectName(u"btn_stop_10")
        self.btn_stop_10.setMaximumSize(QSize(50, 50))
        self.btn_stop_10.setIcon(icon2)
        self.btn_stop_10.setIconSize(QSize(35, 35))

        self.horizontalLayout_41.addWidget(self.btn_stop_10)


        self.horizontalLayout_36.addWidget(self.frame_68)


        self.verticalLayout_40.addWidget(self.frame_sens_10)

        self.frame_sens_11 = QFrame(self.all_sensors)
        self.frame_sens_11.setObjectName(u"frame_sens_11")
        self.frame_sens_11.setMaximumSize(QSize(16777215, 80))
        self.frame_sens_11.setFrameShape(QFrame.StyledPanel)
        self.frame_sens_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_sens_11)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_65 = QFrame(self.frame_sens_11)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_65)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_name_11 = QLabel(self.frame_65)
        self.label_name_11.setObjectName(u"label_name_11")
        self.label_name_11.setFont(font)

        self.verticalLayout_36.addWidget(self.label_name_11)


        self.horizontalLayout_38.addWidget(self.frame_65)

        self.frame_63 = QFrame(self.frame_sens_11)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMaximumSize(QSize(150, 16777215))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_63)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_7 = QLabel(self.frame_63)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_34.addWidget(self.label_7)

        self.lineEdit_hz_11 = QLineEdit(self.frame_63)
        self.lineEdit_hz_11.setObjectName(u"lineEdit_hz_11")

        self.verticalLayout_34.addWidget(self.lineEdit_hz_11)


        self.horizontalLayout_38.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_sens_11)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_64)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_value_11 = QLabel(self.frame_64)
        self.label_value_11.setObjectName(u"label_value_11")
        self.label_value_11.setFont(font)

        self.verticalLayout_35.addWidget(self.label_value_11)


        self.horizontalLayout_38.addWidget(self.frame_64)

        self.frame_66 = QFrame(self.frame_sens_11)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.btn_start_11 = QPushButton(self.frame_66)
        self.btn_start_11.setObjectName(u"btn_start_11")
        self.btn_start_11.setMaximumSize(QSize(50, 50))
        self.btn_start_11.setIcon(icon1)
        self.btn_start_11.setIconSize(QSize(35, 35))

        self.horizontalLayout_40.addWidget(self.btn_start_11)

        self.btn_stop_11 = QPushButton(self.frame_66)
        self.btn_stop_11.setObjectName(u"btn_stop_11")
        self.btn_stop_11.setMaximumSize(QSize(50, 50))
        self.btn_stop_11.setIcon(icon2)
        self.btn_stop_11.setIconSize(QSize(35, 35))

        self.horizontalLayout_40.addWidget(self.btn_stop_11)


        self.horizontalLayout_38.addWidget(self.frame_66)


        self.verticalLayout_40.addWidget(self.frame_sens_11)

        self.stackedWidget.addWidget(self.all_sensors)
        self.sd_page = QWidget()
        self.sd_page.setObjectName(u"sd_page")
        self.verticalLayout_41 = QVBoxLayout(self.sd_page)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_sd_info = QFrame(self.sd_page)
        self.frame_sd_info.setObjectName(u"frame_sd_info")
        self.frame_sd_info.setMaximumSize(QSize(16777215, 100))
        self.frame_sd_info.setFrameShape(QFrame.StyledPanel)
        self.frame_sd_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_sd_info)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_sd_detect = QLabel(self.frame_sd_info)
        self.label_sd_detect.setObjectName(u"label_sd_detect")

        self.horizontalLayout_42.addWidget(self.label_sd_detect)

        self.label_sd_date = QLabel(self.frame_sd_info)
        self.label_sd_date.setObjectName(u"label_sd_date")

        self.horizontalLayout_42.addWidget(self.label_sd_date)

        self.label_sd_size = QLabel(self.frame_sd_info)
        self.label_sd_size.setObjectName(u"label_sd_size")

        self.horizontalLayout_42.addWidget(self.label_sd_size)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_2)

        self.comboBox = QComboBox(self.frame_sd_info)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(200, 0))
        self.comboBox.setMaximumSize(QSize(1500, 16777215))

        self.horizontalLayout_42.addWidget(self.comboBox)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.btn_sd_download = QPushButton(self.frame_sd_info)
        self.btn_sd_download.setObjectName(u"btn_sd_download")

        self.verticalLayout_42.addWidget(self.btn_sd_download)

        self.btn_sd_save = QPushButton(self.frame_sd_info)
        self.btn_sd_save.setObjectName(u"btn_sd_save")

        self.verticalLayout_42.addWidget(self.btn_sd_save)


        self.horizontalLayout_42.addLayout(self.verticalLayout_42)

        self.btn_sd_clear = QPushButton(self.frame_sd_info)
        self.btn_sd_clear.setObjectName(u"btn_sd_clear")

        self.horizontalLayout_42.addWidget(self.btn_sd_clear)


        self.verticalLayout_41.addWidget(self.frame_sd_info)

        self.frame_sd_sensors = QFrame(self.sd_page)
        self.frame_sd_sensors.setObjectName(u"frame_sd_sensors")
        self.frame_sd_sensors.setMaximumSize(QSize(16777215, 100))
        self.frame_sd_sensors.setFrameShape(QFrame.StyledPanel)
        self.frame_sd_sensors.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_sd_sensors)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_sd_1 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_1.setObjectName(u"btn_sd_1")

        self.gridLayout_2.addWidget(self.btn_sd_1, 0, 0, 1, 1)

        self.btn_sd_2 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_2.setObjectName(u"btn_sd_2")

        self.gridLayout_2.addWidget(self.btn_sd_2, 0, 1, 1, 1)

        self.btn_sd_3 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_3.setObjectName(u"btn_sd_3")

        self.gridLayout_2.addWidget(self.btn_sd_3, 0, 2, 1, 1)

        self.btn_sd_4 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_4.setObjectName(u"btn_sd_4")

        self.gridLayout_2.addWidget(self.btn_sd_4, 0, 3, 1, 1)

        self.btn_sd_5 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_5.setObjectName(u"btn_sd_5")

        self.gridLayout_2.addWidget(self.btn_sd_5, 0, 4, 1, 1)

        self.btn_sd_6 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_6.setObjectName(u"btn_sd_6")

        self.gridLayout_2.addWidget(self.btn_sd_6, 0, 5, 1, 1)

        self.btn_sd_7 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_7.setObjectName(u"btn_sd_7")

        self.gridLayout_2.addWidget(self.btn_sd_7, 1, 0, 1, 1)

        self.btn_sd_8 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_8.setObjectName(u"btn_sd_8")

        self.gridLayout_2.addWidget(self.btn_sd_8, 1, 1, 1, 1)

        self.btn_sd_9 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_9.setObjectName(u"btn_sd_9")

        self.gridLayout_2.addWidget(self.btn_sd_9, 1, 2, 1, 1)

        self.btn_sd_10 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_10.setObjectName(u"btn_sd_10")

        self.gridLayout_2.addWidget(self.btn_sd_10, 1, 3, 1, 1)

        self.btn_sd_11 = QPushButton(self.frame_sd_sensors)
        self.btn_sd_11.setObjectName(u"btn_sd_11")

        self.gridLayout_2.addWidget(self.btn_sd_11, 1, 4, 1, 1)


        self.verticalLayout_41.addWidget(self.frame_sd_sensors)

        self.frame_sd_plot = QFrame(self.sd_page)
        self.frame_sd_plot.setObjectName(u"frame_sd_plot")
        self.frame_sd_plot.setFrameShape(QFrame.StyledPanel)
        self.frame_sd_plot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_sd_plot)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.horizontalLayout_43.addLayout(self.gridLayout_3)


        self.verticalLayout_41.addWidget(self.frame_sd_plot)

        self.stackedWidget.addWidget(self.sd_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Exell Tech", None))
        self.label.setText("")
        self.btn_conn_1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 1", None))
        self.btn_conn_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 2", None))
        self.btn_conn_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 3", None))
        self.btn_conn_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 4", None))
        self.btn_conn_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 5", None))
        self.btn_conn_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 6", None))
        self.btn_conn_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 7", None))
        self.btn_conn_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 8", None))
        self.btn_conn_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 9", None))
        self.btn_conn_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 10", None))
        self.btn_conn_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 11", None))
        self.btn_all_sensors.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0434\u0430\u0442\u0447\u0438\u043a\u0438", None))
        self.btn_sd_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0441 \u043a\u0430\u0440\u0442\u044b \u043f\u0430\u043c\u044f\u0442\u0438", None))
        self.label_15.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043c\u043e\u0434\u0443\u043b\u044c", None))
        self.label_sensor_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_sensor_value.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_save.setText("")
        self.btn_start.setText("")
        self.btn_stop.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Copyright DCIE", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.label_name_1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 1", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_1.setText("")
        self.btn_stop_1.setText("")
        self.label_name_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 2", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_2.setText("")
        self.btn_stop_2.setText("")
        self.label_name_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 3", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_3.setText("")
        self.btn_stop_3.setText("")
        self.label_name_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 4", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_4.setText("")
        self.btn_stop_4.setText("")
        self.label_name_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 5", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_5.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_5.setText("")
        self.btn_stop_5.setText("")
        self.label_name_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 6", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_6.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_6.setText("")
        self.btn_stop_6.setText("")
        self.label_name_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 7", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_7.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_7.setText("")
        self.btn_stop_7.setText("")
        self.label_name_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 8", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_8.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_8.setText("")
        self.btn_stop_8.setText("")
        self.label_name_9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 9", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_9.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_9.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_9.setText("")
        self.btn_stop_9.setText("")
        self.label_name_10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 10", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_10.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_10.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_10.setText("")
        self.btn_stop_10.setText("")
        self.label_name_11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 11", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.lineEdit_hz_11.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_value_11.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_start_11.setText("")
        self.btn_stop_11.setText("")
        self.label_sd_detect.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u0430 \u043f\u0430\u043c\u044f\u0442\u0438 \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u0430 ", None))
        self.label_sd_date.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u0430 \u043f\u0443\u0441\u0442\u0430", None))
        self.label_sd_size.setText(QCoreApplication.translate("MainWindow", u"0 \u0431\u0430\u0439\u0442", None))
        self.btn_sd_download.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.btn_sd_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_sd_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u0443", None))
        self.btn_sd_1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 1", None))
        self.btn_sd_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 2", None))
        self.btn_sd_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 3", None))
        self.btn_sd_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 4", None))
        self.btn_sd_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 5", None))
        self.btn_sd_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 6", None))
        self.btn_sd_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 7", None))
        self.btn_sd_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 8", None))
        self.btn_sd_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 9", None))
        self.btn_sd_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 10", None))
        self.btn_sd_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a 11", None))
    # retranslateUi

