# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SAMG_2.ui',
# licensing of 'SAMG_2.ui' applies.
#
# Created: Sun Jul 14 14:23:11 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(2570, 5000)
        Dialog.setMinimumSize(QtCore.QSize(2570, 5000))
        Dialog.setMaximumSize(QtCore.QSize(2570, 1566))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 20, 411, 1341))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.Expected_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Expected_pushButton_MIT01.setGeometry(QtCore.QRect(10, 310, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Expected_pushButton_MIT01.setFont(font)
        self.Expected_pushButton_MIT01.setObjectName("Expected_pushButton_MIT01")
        self.Purpose_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Purpose_pushButton_MIT01.setGeometry(QtCore.QRect(10, 190, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Purpose_pushButton_MIT01.setFont(font)
        self.Purpose_pushButton_MIT01.setAutoFillBackground(True)
        self.Purpose_pushButton_MIT01.setObjectName("Purpose_pushButton_MIT01")
        self.Condition_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Condition_pushButton_MIT01.setGeometry(QtCore.QRect(10, 250, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Condition_pushButton_MIT01.setFont(font)
        self.Condition_pushButton_MIT01.setObjectName("Condition_pushButton_MIT01")
        self.Relation_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Relation_pushButton_MIT01.setGeometry(QtCore.QRect(10, 370, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Relation_pushButton_MIT01.setFont(font)
        self.Relation_pushButton_MIT01.setObjectName("Relation_pushButton_MIT01")
        self.Check_Means_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Check_Means_pushButton_MIT01.setGeometry(QtCore.QRect(10, 430, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Check_Means_pushButton_MIT01.setFont(font)
        self.Check_Means_pushButton_MIT01.setObjectName("Check_Means_pushButton_MIT01")
        self.Decide_Perform_or_not_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Decide_Perform_or_not_pushButton_MIT01.setGeometry(QtCore.QRect(10, 490, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Decide_Perform_or_not_pushButton_MIT01.setFont(font)
        self.Decide_Perform_or_not_pushButton_MIT01.setObjectName("Decide_Perform_or_not_pushButton_MIT01")
        self.Decide_Method_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Decide_Method_pushButton_MIT01.setGeometry(QtCore.QRect(10, 550, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Decide_Method_pushButton_MIT01.setFont(font)
        self.Decide_Method_pushButton_MIT01.setObjectName("Decide_Method_pushButton_MIT01")
        self.Perform_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Perform_pushButton_MIT01.setGeometry(QtCore.QRect(10, 610, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Perform_pushButton_MIT01.setFont(font)
        self.Perform_pushButton_MIT01.setObjectName("Perform_pushButton_MIT01")
        self.End_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.End_pushButton_MIT01.setGeometry(QtCore.QRect(10, 670, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.End_pushButton_MIT01.setFont(font)
        self.End_pushButton_MIT01.setObjectName("End_pushButton_MIT01")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 411, 171))
        self.frame_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_5)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 90, 181, 61))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(200, 20, 161, 16))
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame_5)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 10, 161, 71))
        self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(1780, 20, 771, 671))
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(1780, 690, 771, 671))
        self.frame_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(420, 20, 1361, 1341))
        self.stackedWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Main_page = QtWidgets.QWidget()
        self.Main_page.setObjectName("Main_page")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.Main_page)
        self.textBrowser_5.setGeometry(QtCore.QRect(10, 10, 1341, 61))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.stackedWidget.addWidget(self.Main_page)
        self.Purpose_page = QtWidgets.QWidget()
        self.Purpose_page.setObjectName("Purpose_page")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.Purpose_page)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 1341, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.Purpose_page)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 80, 1341, 61))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.stackedWidget.addWidget(self.Purpose_page)
        self.Condition_page = QtWidgets.QWidget()
        self.Condition_page.setObjectName("Condition_page")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.Condition_page)
        self.textBrowser_6.setGeometry(QtCore.QRect(10, 10, 1341, 61))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.Condition_page)
        self.textBrowser_7.setGeometry(QtCore.QRect(10, 80, 1341, 61))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.stackedWidget.addWidget(self.Condition_page)
        self.Expected_page = QtWidgets.QWidget()
        self.Expected_page.setObjectName("Expected_page")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.Expected_page)
        self.textBrowser_8.setGeometry(QtCore.QRect(10, 10, 1341, 61))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.Expected_page)
        self.textBrowser_9.setGeometry(QtCore.QRect(10, 80, 1341, 61))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.stackedWidget.addWidget(self.Expected_page)
        self.Related_page = QtWidgets.QWidget()
        self.Related_page.setObjectName("Related_page")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.Related_page)
        self.textBrowser_10.setGeometry(QtCore.QRect(10, 10, 1341, 61))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.Related_page)
        self.textBrowser_11.setGeometry(QtCore.QRect(10, 80, 1341, 61))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.stackedWidget.addWidget(self.Related_page)
        self.Available_page = QtWidgets.QWidget()
        self.Available_page.setObjectName("Available_page")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.Available_page)
        self.textBrowser_12.setGeometry(QtCore.QRect(10, 10, 1341, 61))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.Available_page)
        self.textBrowser_13.setGeometry(QtCore.QRect(10, 80, 1341, 61))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.stackedWidget.addWidget(self.Available_page)
        self.Wether_page = QtWidgets.QWidget()
        self.Wether_page.setObjectName("Wether_page")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.Wether_page)
        self.textBrowser_14.setGeometry(QtCore.QRect(10, 10, 1341, 61))
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.Wether_page)
        self.textBrowser_15.setGeometry(QtCore.QRect(10, 80, 1341, 61))
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.stackedWidget.addWidget(self.Wether_page)
        self.Mean_page = QtWidgets.QWidget()
        self.Mean_page.setObjectName("Mean_page")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.Mean_page)
        self.textBrowser_16.setGeometry(QtCore.QRect(10, 10, 1341, 61))
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.Mean_page)
        self.textBrowser_17.setGeometry(QtCore.QRect(10, 80, 1341, 61))
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.stackedWidget.addWidget(self.Mean_page)
        self.Perform_page = QtWidgets.QWidget()
        self.Perform_page.setObjectName("Perform_page")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.Perform_page)
        self.textBrowser_18.setGeometry(QtCore.QRect(10, 10, 1341, 61))
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.textBrowser_19 = QtWidgets.QTextBrowser(self.Perform_page)
        self.textBrowser_19.setGeometry(QtCore.QRect(10, 80, 1341, 61))
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.stackedWidget.addWidget(self.Perform_page)
        self.End_page = QtWidgets.QWidget()
        self.End_page.setObjectName("End_page")
        self.textBrowser_20 = QtWidgets.QTextBrowser(self.End_page)
        self.textBrowser_20.setGeometry(QtCore.QRect(10, 10, 1341, 61))
        self.textBrowser_20.setObjectName("textBrowser_20")
        self.textBrowser_21 = QtWidgets.QTextBrowser(self.End_page)
        self.textBrowser_21.setGeometry(QtCore.QRect(10, 80, 1341, 61))
        self.textBrowser_21.setObjectName("textBrowser_21")
        self.stackedWidget.addWidget(self.End_page)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Mitigation-01", None, -1))
        self.Expected_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "예상 발전소 거동", None, -1))
        self.Purpose_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "목적", None, -1))
        self.Condition_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "수행 조건", None, -1))
        self.Relation_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "비상운전절차서와의 관계", None, -1))
        self.Check_Means_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "이용가능 수단 확인", None, -1))
        self.Decide_Perform_or_not_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "전략 수행 여부 결정", None, -1))
        self.Decide_Method_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "전략 수행 방법 결정", None, -1))
        self.Perform_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "전략 수행", None, -1))
        self.End_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "전략 종결", None, -1))
        self.textBrowser_3.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">흐른 시간</p></body></html>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "진행중인 호기", None, -1))
        self.dateTimeEdit.setDisplayFormat(QtWidgets.QApplication.translate("Dialog", "yyyy-MM-dd AP hh:mm:ss", None, -1))
        self.textBrowser_5.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_2.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_4.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">목적</p></body></html>", None, -1))
        self.textBrowser_6.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_7.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">수행 조건</p></body></html>", None, -1))
        self.textBrowser_8.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_9.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">예상 발전소 거동</p></body></html>", None, -1))
        self.textBrowser_10.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_11.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">비상운전절차서와의 관계</p></body></html>", None, -1))
        self.textBrowser_12.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_13.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">이용가능 수단 확인</p></body></html>", None, -1))
        self.textBrowser_14.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_15.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">전략 수행 여부 결정</p></body></html>", None, -1))
        self.textBrowser_16.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_17.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">전략 수행 방법 결정</p></body></html>", None, -1))
        self.textBrowser_18.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_19.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">전략 수행</p></body></html>", None, -1))
        self.textBrowser_20.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_21.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">전략 종결</p></body></html>", None, -1))

