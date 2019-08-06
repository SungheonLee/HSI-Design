# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DE.ui',
# licensing of 'DE.ui' applies.
#
# Created: Wed Jul 31 22:24:21 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1110, 600)
        MainForm.setStyleSheet("background-color: rgb(217, 225, 232);")
        self.Bar_1 = QtWidgets.QFrame(MainForm)
        self.Bar_1.setGeometry(QtCore.QRect(0, 0, 225, 600))
        self.Bar_1.setStyleSheet("background-color: #d9e1e8;\n"
"border: none;\n"
"border-right: 2px solid black;")
        self.Bar_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Bar_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Bar_1.setObjectName("Bar_1")
        self.frame = QtWidgets.QFrame(self.Bar_1)
        self.frame.setGeometry(QtCore.QRect(10, 10, 205, 111))
        self.frame.setStyleSheet("border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"border: 1px solid black;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #56a, stop: 0.5 #2b90d9);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(5, 30, 110, 20))
        self.label.setStyleSheet("border-top-left-radius: none;\n"
"font: 10pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.T_time = QtWidgets.QLabel(self.frame)
        self.T_time.setGeometry(QtCore.QRect(115, 30, 90, 20))
        self.T_time.setStyleSheet("border-top-left-radius: none;\n"
"font: 10pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.T_time.setAlignment(QtCore.Qt.AlignCenter)
        self.T_time.setObjectName("T_time")
        self.T_time_g = QtWidgets.QLabel(self.frame)
        self.T_time_g.setGeometry(QtCore.QRect(115, 55, 90, 20))
        self.T_time_g.setStyleSheet("border-top-left-radius: none;\n"
"font: 10pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.T_time_g.setAlignment(QtCore.Qt.AlignCenter)
        self.T_time_g.setObjectName("T_time_g")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(5, 55, 110, 20))
        self.label_2.setStyleSheet("border-top-left-radius: none;\n"
"font: 10pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.T_time_g_2 = QtWidgets.QLabel(self.frame)
        self.T_time_g_2.setGeometry(QtCore.QRect(104, 80, 101, 20))
        self.T_time_g_2.setStyleSheet("border-top-left-radius: none;\n"
"font: 10pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.T_time_g_2.setAlignment(QtCore.Qt.AlignCenter)
        self.T_time_g_2.setObjectName("T_time_g_2")
        self.frame_2 = QtWidgets.QFrame(self.Bar_1)
        self.frame_2.setGeometry(QtCore.QRect(10, 129, 205, 461))
        self.frame_2.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background: none;")
        self.frame_2.setObjectName("frame_2")
        self.B_1 = QtWidgets.QPushButton(self.frame_2)
        self.B_1.setGeometry(QtCore.QRect(6, 50, 190, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.B_1.setFont(font)
        self.B_1.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_1.setObjectName("B_1")
        self.B_2 = QtWidgets.QPushButton(self.frame_2)
        self.B_2.setGeometry(QtCore.QRect(6, 90, 190, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.B_2.setFont(font)
        self.B_2.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_2.setObjectName("B_2")
        self.B_3 = QtWidgets.QPushButton(self.frame_2)
        self.B_3.setGeometry(QtCore.QRect(6, 130, 190, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.B_3.setFont(font)
        self.B_3.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_3.setObjectName("B_3")
        self.B_4 = QtWidgets.QPushButton(self.frame_2)
        self.B_4.setGeometry(QtCore.QRect(6, 170, 190, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.B_4.setFont(font)
        self.B_4.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_4.setObjectName("B_4")
        self.B_5 = QtWidgets.QPushButton(self.frame_2)
        self.B_5.setGeometry(QtCore.QRect(6, 210, 190, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.B_5.setFont(font)
        self.B_5.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_5.setObjectName("B_5")
        self.B_6 = QtWidgets.QPushButton(self.frame_2)
        self.B_6.setGeometry(QtCore.QRect(6, 250, 190, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.B_6.setFont(font)
        self.B_6.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_6.setObjectName("B_6")
        self.B_7 = QtWidgets.QPushButton(self.frame_2)
        self.B_7.setGeometry(QtCore.QRect(6, 290, 190, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.B_7.setFont(font)
        self.B_7.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_7.setObjectName("B_7")
        self.B_8 = QtWidgets.QPushButton(self.frame_2)
        self.B_8.setGeometry(QtCore.QRect(6, 330, 190, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.B_8.setFont(font)
        self.B_8.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_8.setObjectName("B_8")
        self.B_9 = QtWidgets.QPushButton(self.frame_2)
        self.B_9.setGeometry(QtCore.QRect(6, 370, 190, 30))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.B_9.setFont(font)
        self.B_9.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_9.setObjectName("B_9")
        self.stackedWidget = QtWidgets.QStackedWidget(MainForm)
        self.stackedWidget.setGeometry(QtCore.QRect(225, 59, 600, 541))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.bp_0 = QtWidgets.QWidget()
        self.bp_0.setObjectName("bp_0")
        self.sa_0 = QtWidgets.QScrollArea(self.bp_0)
        self.sa_0.setGeometry(QtCore.QRect(0, 0, 600, 541))
        self.sa_0.setWidgetResizable(True)
        self.sa_0.setObjectName("sa_0")
        self.sa_0_w = QtWidgets.QWidget()
        self.sa_0_w.setGeometry(QtCore.QRect(0, 0, 598, 539))
        self.sa_0_w.setMinimumSize(QtCore.QSize(0, 0))
        self.sa_0_w.setObjectName("sa_0_w")
        self.sa_0.setWidget(self.sa_0_w)
        self.stackedWidget.addWidget(self.bp_0)
        self.bp_1 = QtWidgets.QWidget()
        self.bp_1.setObjectName("bp_1")
        self.sa_1 = QtWidgets.QScrollArea(self.bp_1)
        self.sa_1.setGeometry(QtCore.QRect(0, 0, 600, 541))
        self.sa_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_1.setWidgetResizable(True)
        self.sa_1.setObjectName("sa_1")
        self.sa_1_w = QtWidgets.QWidget()
        self.sa_1_w.setGeometry(QtCore.QRect(0, 0, 584, 539))
        self.sa_1_w.setObjectName("sa_1_w")
        self.sa_1.setWidget(self.sa_1_w)
        self.stackedWidget.addWidget(self.bp_1)
        self.bp_2 = QtWidgets.QWidget()
        self.bp_2.setObjectName("bp_2")
        self.sa_2 = QtWidgets.QScrollArea(self.bp_2)
        self.sa_2.setGeometry(QtCore.QRect(0, 0, 600, 541))
        self.sa_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_2.setWidgetResizable(True)
        self.sa_2.setObjectName("sa_2")
        self.sa_2_w = QtWidgets.QWidget()
        self.sa_2_w.setGeometry(QtCore.QRect(0, 0, 584, 539))
        self.sa_2_w.setObjectName("sa_2_w")
        self.sa_2.setWidget(self.sa_2_w)
        self.stackedWidget.addWidget(self.bp_2)
        self.bp_3 = QtWidgets.QWidget()
        self.bp_3.setObjectName("bp_3")
        self.sa_3 = QtWidgets.QScrollArea(self.bp_3)
        self.sa_3.setGeometry(QtCore.QRect(0, 0, 600, 541))
        self.sa_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_3.setWidgetResizable(True)
        self.sa_3.setObjectName("sa_3")
        self.sa_3_w = QtWidgets.QWidget()
        self.sa_3_w.setGeometry(QtCore.QRect(0, 0, 584, 539))
        self.sa_3_w.setObjectName("sa_3_w")
        self.sa_3.setWidget(self.sa_3_w)
        self.stackedWidget.addWidget(self.bp_3)
        self.bq_4 = QtWidgets.QWidget()
        self.bq_4.setObjectName("bq_4")
        self.sa_4 = QtWidgets.QScrollArea(self.bq_4)
        self.sa_4.setGeometry(QtCore.QRect(0, 0, 600, 541))
        self.sa_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_4.setWidgetResizable(True)
        self.sa_4.setObjectName("sa_4")
        self.sa_4_w = QtWidgets.QWidget()
        self.sa_4_w.setGeometry(QtCore.QRect(0, 0, 584, 539))
        self.sa_4_w.setObjectName("sa_4_w")
        self.sa_4.setWidget(self.sa_4_w)
        self.stackedWidget.addWidget(self.bq_4)
        self.bp_5 = QtWidgets.QWidget()
        self.bp_5.setObjectName("bp_5")
        self.sa_5 = QtWidgets.QScrollArea(self.bp_5)
        self.sa_5.setGeometry(QtCore.QRect(0, 0, 600, 541))
        self.sa_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_5.setWidgetResizable(True)
        self.sa_5.setObjectName("sa_5")
        self.sa_5_w = QtWidgets.QWidget()
        self.sa_5_w.setGeometry(QtCore.QRect(0, 0, 584, 539))
        self.sa_5_w.setObjectName("sa_5_w")
        self.sa_5.setWidget(self.sa_5_w)
        self.stackedWidget.addWidget(self.bp_5)
        self.bp_6 = QtWidgets.QWidget()
        self.bp_6.setObjectName("bp_6")
        self.sa_6 = QtWidgets.QScrollArea(self.bp_6)
        self.sa_6.setGeometry(QtCore.QRect(0, 0, 600, 541))
        self.sa_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_6.setWidgetResizable(True)
        self.sa_6.setObjectName("sa_6")
        self.sa_6_w = QtWidgets.QWidget()
        self.sa_6_w.setGeometry(QtCore.QRect(0, 0, 584, 539))
        self.sa_6_w.setObjectName("sa_6_w")
        self.sa_6.setWidget(self.sa_6_w)
        self.stackedWidget.addWidget(self.bp_6)
        self.bp_7 = QtWidgets.QWidget()
        self.bp_7.setObjectName("bp_7")
        self.sa_7 = QtWidgets.QScrollArea(self.bp_7)
        self.sa_7.setGeometry(QtCore.QRect(0, 0, 600, 541))
        self.sa_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_7.setWidgetResizable(True)
        self.sa_7.setObjectName("sa_7")
        self.sa_7_w = QtWidgets.QWidget()
        self.sa_7_w.setGeometry(QtCore.QRect(0, 0, 584, 539))
        self.sa_7_w.setObjectName("sa_7_w")
        self.sa_7.setWidget(self.sa_7_w)
        self.stackedWidget.addWidget(self.bp_7)
        self.bp_8 = QtWidgets.QWidget()
        self.bp_8.setObjectName("bp_8")
        self.sa_8 = QtWidgets.QScrollArea(self.bp_8)
        self.sa_8.setGeometry(QtCore.QRect(0, 0, 600, 541))
        self.sa_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_8.setWidgetResizable(True)
        self.sa_8.setObjectName("sa_8")
        self.sa_8_w = QtWidgets.QWidget()
        self.sa_8_w.setGeometry(QtCore.QRect(0, 0, 584, 539))
        self.sa_8_w.setObjectName("sa_8_w")
        self.sa_8.setWidget(self.sa_8_w)
        self.stackedWidget.addWidget(self.bp_8)
        self.bp_9 = QtWidgets.QWidget()
        self.bp_9.setObjectName("bp_9")
        self.sa_9 = QtWidgets.QScrollArea(self.bp_9)
        self.sa_9.setGeometry(QtCore.QRect(0, 0, 600, 541))
        self.sa_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_9.setWidgetResizable(True)
        self.sa_9.setObjectName("sa_9")
        self.sa_9_w = QtWidgets.QWidget()
        self.sa_9_w.setGeometry(QtCore.QRect(0, 0, 584, 539))
        self.sa_9_w.setObjectName("sa_9_w")
        self.sa_9.setWidget(self.sa_9_w)
        self.stackedWidget.addWidget(self.bp_9)
        self.stack_title = QtWidgets.QLabel(MainForm)
        self.stack_title.setGeometry(QtCore.QRect(235, 15, 580, 35))
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        font.setPointSize(12)
        self.stack_title.setFont(font)
        self.stack_title.setStyleSheet("border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.stack_title.setText("")
        self.stack_title.setAlignment(QtCore.Qt.AlignCenter)
        self.stack_title.setObjectName("stack_title")
        self.sa_map = QtWidgets.QScrollArea(MainForm)
        self.sa_map.setGeometry(QtCore.QRect(830, 60, 271, 291))
        self.sa_map.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_map.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_map.setWidgetResizable(True)
        self.sa_map.setObjectName("sa_map")
        self.sa_map_0 = QtWidgets.QWidget()
        self.sa_map_0.setGeometry(QtCore.QRect(0, 0, 255, 275))
        self.sa_map_0.setObjectName("sa_map_0")
        self.sa_map.setWidget(self.sa_map_0)

        self.retranslateUi(MainForm)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtWidgets.QApplication.translate("MainForm", "SAMG", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainForm", "Current Time  :", None, -1))
        self.T_time.setText(QtWidgets.QApplication.translate("MainForm", "00:00:00", None, -1))
        self.T_time_g.setText(QtWidgets.QApplication.translate("MainForm", "00:00:00", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainForm", "Accident Time:", None, -1))
        self.T_time_g_2.setText(QtWidgets.QApplication.translate("MainForm", "+ 00:00:00", None, -1))
        self.B_1.setText(QtWidgets.QApplication.translate("MainForm", "목적", None, -1))
        self.B_2.setText(QtWidgets.QApplication.translate("MainForm", "수행조건", None, -1))
        self.B_3.setText(QtWidgets.QApplication.translate("MainForm", "예상 발전소 거동", None, -1))
        self.B_4.setText(QtWidgets.QApplication.translate("MainForm", "비상운전절차서와 관계", None, -1))
        self.B_5.setText(QtWidgets.QApplication.translate("MainForm", "이용가능 수단 확인", None, -1))
        self.B_6.setText(QtWidgets.QApplication.translate("MainForm", "전략 수행 여부 결정", None, -1))
        self.B_7.setText(QtWidgets.QApplication.translate("MainForm", "전략 수행 방법 결정", None, -1))
        self.B_8.setText(QtWidgets.QApplication.translate("MainForm", "전략 수행", None, -1))
        self.B_9.setText(QtWidgets.QApplication.translate("MainForm", "전략 종결", None, -1))

