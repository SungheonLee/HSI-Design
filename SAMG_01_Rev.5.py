from ui_SAMG_2 import *

import sys
from PySide2 import (QtCore, QtWidgets, QtGui)
from PySide2.QtWidgets import QPushButton
# import random

class MainDialog(QtWidgets.QDialog):
    # def openWindow(self):
    #     self.window = QtWidgets.QDialog()
    #     self.ui = Ui_Guideline()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    #     super().__init__()
    #     self.ui = Ui_Dialog()
    #     self.ui.setupUi(self)

        # self.pushbutton = QPushButton('A', self) #Pushbutton 생성

        # self.ui.Purpose_pushButton_MIT01.clicked.connect(self.make_msg_box)
        self.ui.Purpose_pushButton_MIT01.clicked.connect(self.textclicked)
        self.ui.Condition_pushButton_MIT01.clicked.connect(self.textclicked2)
        self.ui.Expected_pushButton_MIT01.clicked.connect(self.textclicked3)

        self.out_data = ''
        self.out_data2 = ''
        self.out_data3 = ''

#PushBUtton을 원하는 위치에 생성되게 하는 기능들, 이 기능은 Guideline Display에서 각 전략이 선택 될 떄, 같이 나타남.

    # def make_msg_box(self):
    #     self.b = QtWidgets.QMessageBox()
    #     #self.b.show()
    #     self.ans = QPushButton
    #     print(self.ans)
    #     self.collected_QpushButton = []
    #     init_pos_x, init_pos_y, nub = 1200, 50, 0
    #     for _ in range(0, 1):
    #         for __ in range(0, 1):
    #             self.collected_QpushButton.append(QtWidgets.QPushButton(self.ui.Out_textBrowser_MIT01))
    #             self.collected_QpushButton[-1].setGeometry(QtCore.QRect(init_pos_x, init_pos_y, 100, 30))
    #             self.collected_QpushButton[-1].show()

# ----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#Guideline Display에서 Push버튼을 클릭할시, 각 화면들(Guideline Support, TBD, FBD)에서 결과값을 출력 하도록 하는 기능들
#----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def textclicked(self): #목적 버튼을 누르면, Information, TBD, FBD에 자동으로 표시되게 하는 로직
        print(self.ui.Purpose_pushButton_MIT01.text())
        self.ui.Out_textBrowser_MIT01.clear()
        self.ui.Out_textBrowser_MIT01.setText('\n' + '증기발생기 급수 주입의 목적은 다음과 같다.\n'
                                                    '● RCS 열 제거\n'
                                                    '● RCS를 감압하여 RCS 내로 냉각재 공급을 가능하게 함\n'
                                                    '● 증기발생기 튜브의 크립 파손 방지\n'
                                                    '● 증기발생기로 방출된 핵분열생성물의 세정(Scrubbing)\n'
                                                    '● 증기발생기 튜브 파손시 파손부를 통하여 RCS 내에 냉각재 공급')
        self.ui.FBD_textBrowser_MIT01.clear()
        self.ui.FBD_textBrowser_MIT01.setText('\n' + 'a')
        self.ui.TBD_textBrowser_MIT01.clear()
        self.ui.TBD_textBrowser_MIT01.setText('\n' + 'a')
        self.ui.Current_Strategy_textBrowser_MIT01.clear()
        self.ui.Current_Strategy_textBrowser_MIT01.setText('안녕')

    def textclicked2(self): #수행조건확인 버튼을 누르면, Information, TBD, FBD에 자동으로 표시되게 하는 로직
        print(self.ui.Condition_pushButton_MIT01.text())
        self.ui.Out_textBrowser_MIT01.clear()
        self.ui.Out_textBrowser_MIT01.setText('\n' + '● 발전소 상태가 A 또는 B이고 어느 하나라도 증기발생기 수위가 협역수위 지시기로 68% 이하일 때\n'
                                                     '● 발전소 상태가 C이고 핵분열생성물의 방출이 있는 증기발생기 수위가 협역수위 지시기로 68% 이하일 때')
        self.ui.FBD_textBrowser_MIT01.clear()
        self.ui.FBD_textBrowser_MIT01.setText('\n' + 'b')
        self.ui.TBD_textBrowser_MIT01.clear()
        self.ui.TBD_textBrowser_MIT01.setText('\n' + 'b')
        self.ui.Current_Strategy_textBrowser_MIT01.clear()
        self.ui.Current_Strategy_textBrowser_MIT01.setText('안녕')

    def textclicked3(self): #예상발전소거동 버튼을 누르면, Information, TBD, FBD에 자동으로 표시되게 하는 로직
        print(self.ui.Expected_pushButton_MIT01.text())
        self.ui.Out_textBrowser_MIT01.clear()
        self.ui.Out_textBrowser_MIT01.setText('\n' + '● 증기발생기 수위 상승\n'
                                                     '● 증기발생기 증기 유량 증가\n'
                                                     '● 노심 출구와 고온관의 온도 감소\n'
                                                     '● 증기발생기 튜브 상부에 수소 축적')
        self.ui.FBD_textBrowser_MIT01.clear()
        self.ui.FBD_textBrowser_MIT01.setText('\n' + 'c')
        self.ui.TBD_textBrowser_MIT01.clear()
        self.ui.TBD_textBrowser_MIT01.setText('\n' + 'c')
        self.ui.Current_Strategy_textBrowser_MIT01.clear()
        self.ui.Current_Strategy_textBrowser_MIT01.setText('안녕')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    app.exec_()