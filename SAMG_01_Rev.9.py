from ui_SAMG_2 import *

import sys
from PySide2 import (QtCore, QtWidgets, QtGui)
from PySide2.QtCore import *
from PyQt5 import uic


class MainDialog(QtWidgets.QDialog):
    def __init__(self):
        # super().__init__()
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

# ---------------------------------------------------------------------------------------------------------------------- (현재 Date Time 생성 로직)

        self.currentDateTime = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(self.currentDateTime)
# ---------------------------------------------------------------------------------------------------------------------- (현재 Date Time 생성 로직 여기까지)


# ---------------------------------------------------------------------------------------------------------------------- (Frame Change 로직)
        self.ui.Purpose_pushButton_MIT01.clicked.connect(self.show_clicked_1)
        self.ui.Condition_pushButton_MIT01.clicked.connect(self.show_clicked_2)
        self.ui.Expected_pushButton_MIT01.clicked.connect(self.show_clicked_3)
        self.ui.Relation_pushButton_MIT01.clicked.connect(self.show_clicked_4)
        self.ui.Check_Means_pushButton_MIT01.clicked.connect(self.show_clicked_5)
        self.ui.Decide_Perform_or_not_pushButton_MIT01.clicked.connect(self.show_clicked_6)
        self.ui.Decide_Method_pushButton_MIT01.clicked.connect(self.show_clicked_7)
        self.ui.Perform_pushButton_MIT01.clicked.connect(self.show_clicked_8)
        self.ui.End_pushButton_MIT01.clicked.connect(self.show_clicked_9)


    def show_clicked_1(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def show_clicked_2(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def show_clicked_3(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def show_clicked_4(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    def show_clicked_5(self):
        self.ui.stackedWidget.setCurrentIndex(5)
    def show_clicked_6(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    def show_clicked_7(self):
        self.ui.stackedWidget.setCurrentIndex(7)
    def show_clicked_8(self):
        self.ui.stackedWidget.setCurrentIndex(8)
    def show_clicked_9(self):
        self.ui.stackedWidget.setCurrentIndex(9)

# ---------------------------------------------------------------------------------------------------------------------- (Frame Change 로직 여기까지)

        # self.ui.Purpose_pushButton_MIT01.clicked.connect(self.textclicked)
        # self.outdata = ""

    # def textclicked(self):

        # print(self.ui.Purpose_pushButton_MIT01.show())
        # self.ui.textBrowser_4.clear()
        # self.ui.textBrowser_4.setText("\n" + 'aaa')



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # self.ui.Purpose_pushButton_MIT01.clicked.connect(self.textclicked)
        # self.out_data = ''
    # def textclicked(self): #목적 버튼을 누르면, Information, TBD, FBD에 자동으로 표시되게 하는 로직
    #     print(self.ui.Purpose_pushButton_MIT01.text())
    #     self.ui.Out_textBrowser_MIT01.clear()
    #     self.ui.Out_textBrowser_MIT01.setText('\n' + '증기발생기 급수 주입의 목적은 다음과 같다.\n'
    #                                                 '● RCS 열 제거\n'
    #                                                 '● RCS를 감압하여 RCS 내로 냉각재 공급을 가능하게 함\n'
    #                                                 '● 증기발생기 튜브의 크립 파손 방지\n'
    #                                                 '● 증기발생기로 방출된 핵분열생성물의 세정(Scrubbing)\n'
    #                                                 '● 증기발생기 튜브 파손시 파손부를 통하여 RCS 내에 냉각재 공급')
    #     self.ui.FBD_textBrowser_MIT01.clear()
    #     self.ui.FBD_textBrowser_MIT01.setText('\n' + 'a')
    #     self.ui.TBD_textBrowser_MIT01.clear()
    #     self.ui.TBD_textBrowser_MIT01.setText('\n' + 'a')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    app.exec_()