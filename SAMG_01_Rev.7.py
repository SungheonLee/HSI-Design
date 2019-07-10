from ui_SAMG_2 import *
from ui_1 import *
#
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class MainDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.Purpose_pushButton_MIT01.clicked.connect(self.window(ui_1)

        print(self.ui.Purpose_pushButton_MIT01.text())
        self.ui.Purpose_Out_textBrowser_MIT01.clear()
        self.ui.Purpose_Out_textBrowser_MIT01.setText('\n' + 'aaaaaaaaaaaaaa')

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