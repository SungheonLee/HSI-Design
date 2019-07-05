# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SAMG.ui',
# licensing of 'SAMG.ui' applies.
#
# Created: Fri Jul  5 17:35:30 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(2120, 1320)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(60, 170, 261, 1061))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Expected_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Expected_pushButton_MIT01.setGeometry(QtCore.QRect(10, 100, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Expected_pushButton_MIT01.setFont(font)
        self.Expected_pushButton_MIT01.setObjectName("Expected_pushButton_MIT01")
        self.Purpose_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Purpose_pushButton_MIT01.setGeometry(QtCore.QRect(10, 20, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Purpose_pushButton_MIT01.setFont(font)
        self.Purpose_pushButton_MIT01.setObjectName("Purpose_pushButton_MIT01")
        self.Condition_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Condition_pushButton_MIT01.setGeometry(QtCore.QRect(10, 60, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Condition_pushButton_MIT01.setFont(font)
        self.Condition_pushButton_MIT01.setObjectName("Condition_pushButton_MIT01")
        self.Relation_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Relation_pushButton_MIT01.setGeometry(QtCore.QRect(10, 140, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Relation_pushButton_MIT01.setFont(font)
        self.Relation_pushButton_MIT01.setObjectName("Relation_pushButton_MIT01")
        self.Check_Means_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Check_Means_pushButton_MIT01.setGeometry(QtCore.QRect(10, 180, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Check_Means_pushButton_MIT01.setFont(font)
        self.Check_Means_pushButton_MIT01.setObjectName("Check_Means_pushButton_MIT01")
        self.Decide_Perform_or_not_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Decide_Perform_or_not_pushButton_MIT01.setGeometry(QtCore.QRect(10, 220, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Decide_Perform_or_not_pushButton_MIT01.setFont(font)
        self.Decide_Perform_or_not_pushButton_MIT01.setObjectName("Decide_Perform_or_not_pushButton_MIT01")
        self.Decide_Method_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Decide_Method_pushButton_MIT01.setGeometry(QtCore.QRect(10, 260, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Decide_Method_pushButton_MIT01.setFont(font)
        self.Decide_Method_pushButton_MIT01.setObjectName("Decide_Method_pushButton_MIT01")
        self.Perform_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.Perform_pushButton_MIT01.setGeometry(QtCore.QRect(10, 300, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Perform_pushButton_MIT01.setFont(font)
        self.Perform_pushButton_MIT01.setObjectName("Perform_pushButton_MIT01")
        self.End_pushButton_MIT01 = QtWidgets.QPushButton(self.frame)
        self.End_pushButton_MIT01.setGeometry(QtCore.QRect(10, 340, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.End_pushButton_MIT01.setFont(font)
        self.End_pushButton_MIT01.setObjectName("End_pushButton_MIT01")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(320, 170, 1011, 1061))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Out_textBrowser_MIT01 = QtWidgets.QTextBrowser(self.frame_2)
        self.Out_textBrowser_MIT01.setGeometry(QtCore.QRect(0, 40, 1001, 981))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Out_textBrowser_MIT01.setFont(font)
        self.Out_textBrowser_MIT01.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Out_textBrowser_MIT01.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Out_textBrowser_MIT01.setObjectName("Out_textBrowser_MIT01")
        self.Ok_pushButton_MIT01 = QtWidgets.QPushButton(self.frame_2)
        self.Ok_pushButton_MIT01.setGeometry(QtCore.QRect(0, 1020, 191, 41))
        self.Ok_pushButton_MIT01.setObjectName("Ok_pushButton_MIT01")
        self.Title_textBrowser_4 = QtWidgets.QTextBrowser(self.frame_2)
        self.Title_textBrowser_4.setGeometry(QtCore.QRect(0, 0, 1001, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Title_textBrowser_4.setFont(font)
        self.Title_textBrowser_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Title_textBrowser_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Title_textBrowser_4.setObjectName("Title_textBrowser_4")
        self.Ok_pushButton_MIT01_4 = QtWidgets.QPushButton(self.frame_2)
        self.Ok_pushButton_MIT01_4.setGeometry(QtCore.QRect(190, 1020, 191, 41))
        self.Ok_pushButton_MIT01_4.setObjectName("Ok_pushButton_MIT01_4")
        self.Ok_pushButton_MIT01_6 = QtWidgets.QPushButton(self.frame_2)
        self.Ok_pushButton_MIT01_6.setGeometry(QtCore.QRect(380, 1020, 191, 41))
        self.Ok_pushButton_MIT01_6.setObjectName("Ok_pushButton_MIT01_6")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(1329, 89, 731, 571))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.FBD_textBrowser_MIT01 = QtWidgets.QTextBrowser(self.frame_3)
        self.FBD_textBrowser_MIT01.setGeometry(QtCore.QRect(0, 0, 731, 571))
        self.FBD_textBrowser_MIT01.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.FBD_textBrowser_MIT01.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.FBD_textBrowser_MIT01.setObjectName("FBD_textBrowser_MIT01")
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setGeometry(QtCore.QRect(59, 90, 1271, 81))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame_5)
        self.dateTimeEdit.setGeometry(QtCore.QRect(20, 20, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_5)
        self.textBrowser.setGeometry(QtCore.QRect(250, 10, 161, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_5)
        self.textBrowser_2.setGeometry(QtCore.QRect(610, 10, 651, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_5)
        self.textBrowser_3.setGeometry(QtCore.QRect(430, 10, 161, 61))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(1330, 660, 731, 571))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.TBD_textBrowser_MIT01 = QtWidgets.QTextBrowser(self.frame_4)
        self.TBD_textBrowser_MIT01.setGeometry(QtCore.QRect(0, 0, 731, 571))
        self.TBD_textBrowser_MIT01.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.TBD_textBrowser_MIT01.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.TBD_textBrowser_MIT01.setObjectName("TBD_textBrowser_MIT01")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.Expected_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "예상 발전소 거동", None, -1))
        self.Purpose_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "목적", None, -1))
        self.Condition_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "수행 조건", None, -1))
        self.Relation_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "비상운전절차서와의 관계", None, -1))
        self.Check_Means_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "이용가능 수단 확인", None, -1))
        self.Decide_Perform_or_not_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "전략 수행 여부 결정", None, -1))
        self.Decide_Method_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "전략 수행 방법 결정", None, -1))
        self.Perform_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "전략 수행", None, -1))
        self.End_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "전략 종결", None, -1))
        self.Out_textBrowser_MIT01.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">안녕하세요</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>", None, -1))
        self.Ok_pushButton_MIT01.setText(QtWidgets.QApplication.translate("Dialog", "완료", None, -1))
        self.Title_textBrowser_4.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, -1))
        self.Ok_pushButton_MIT01_4.setText(QtWidgets.QApplication.translate("Dialog", "전략수행제어도로 이동", None, -1))
        self.Ok_pushButton_MIT01_6.setText(QtWidgets.QApplication.translate("Dialog", "이전수행중이던 지침서로 이동", None, -1))
        self.FBD_textBrowser_MIT01.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MFM 그림 입력.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">결과는 필요없고, 만족을 요구하는 경우에는 화살표 형태로 띄워줌</p></body></html>", None, -1))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">호기</p></body></html>", None, -1))
        self.textBrowser_2.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">완화-01 &quot;증기발생기 급수 주입&quot;</p></body></html>", None, -1))
        self.textBrowser_3.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">흐른 시간</p></body></html>", None, -1))
        self.TBD_textBrowser_MIT01.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TBD</p></body></html>", None, -1))

