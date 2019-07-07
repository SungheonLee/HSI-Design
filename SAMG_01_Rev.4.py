from ui_SAMG_2 import *
#
import sys
from PySide2 import (QtCore, QtWidgets, QtGui)
from PySide2.QtWidgets import QPushButton
import random

class MainDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # self.pushbutton = QPushButton('A', self) #Pushbutton 생성

        self.ui.Purpose_pushButton_MIT01.clicked.connect(self.make_msg_box)
        self.ui.Condition_pushButton_MIT01.clicked.connect(self.textclicked2)
        self.ui.Expected_pushButton_MIT01.clicked.connect(self.textclicked3)

        self.out_data = ''
        self.out_data2 = ''
        self.out_data3 = ''

    def make_msg_box(self):
        self.b = QtWidgets.QMessageBox().critical(self, "주의!", "승헌이 컴을 포맷시킵니다.\n 해체를 위해서 오른쪽 버튼을 누르세요!!!")
        #self.b.show()
        self.ans = random.randrange(0,100)
        print(self.ans)
        self.collected_botton = []
        init_pos_x, init_pos_y, nub = 10, 25, 0
        for _ in range(0, 10):
            for __ in range(0, 10):
                self.collected_botton.append(QtWidgets.QPushButton(self.ui.FBD_textBrowser_MIT01))
                self.collected_botton[-1].setGeometry(QtCore.QRect(init_pos_x, init_pos_y, 20, 20))
                self.collected_botton[-1].show()
                nub += 1
                init_pos_x += 20
            init_pos_x = 10
            init_pos_y += 20

        for _ in range(0, 100):
            self.test(_)

    def test(self, nub):
        self.collected_botton[nub].clicked.connect(lambda: self.boom(self.collected_botton[nub], nub))

    def boom(self, bottom, nub):
        if nub == self.ans:
            self.b = QtWidgets.QMessageBox().critical(self, "주의!", "성공~~~")
            for _ in self.collected_botton:
                _.close()
        else:
            self.b = QtWidgets.QMessageBox().critical(self, "주의!", "꽝")
        bottom.close()

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
        self.ui.Title_textBrowser_4.clear()
        self.ui.Title_textBrowser_4.setText('안녕')

    def textclicked2(self): #수행조건확인 버튼을 누르면, Information, TBD, FBD에 자동으로 표시되게 하는 로직
        print(self.ui.Condition_pushButton_MIT01.text())
        self.ui.Out_textBrowser_MIT01.clear()
        self.ui.Out_textBrowser_MIT01.setText('\n' + '● 발전소 상태가 A 또는 B이고 어느 하나라도 증기발생기 수위가 협역수위 지시기로 68% 이하일 때\n'
                                                     '● 발전소 상태가 C이고 핵분열생성물의 방출이 있는 증기발생기 수위가 협역수위 지시기로 68% 이하일 때')
        self.ui.FBD_textBrowser_MIT01.clear()
        self.ui.FBD_textBrowser_MIT01.setText('\n' + 'b')
        self.ui.TBD_textBrowser_MIT01.clear()
        self.ui.TBD_textBrowser_MIT01.setText('\n' + 'b')
        self.ui.Title_textBrowser_4.clear()
        self.ui.Title_textBrowser_4.setText('안녕')

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
        self.ui.Title_textBrowser_4.clear()
        self.ui.Title_textBrowser_4.setText('안녕')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    app.exec_()