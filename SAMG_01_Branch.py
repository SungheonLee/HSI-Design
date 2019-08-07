from DE import *
import SAMG_01_Branch_DB as Pro_DB

import sys
from PySide2.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PySide2.QtCore import QTimer, QRect, QLine, Qt
from PySide2.QtGui import QPainter, QPen, QColor
from datetime import datetime

class main_body(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_ui = Ui_MainForm()
        self.main_ui.setupUi(self)
        if True:
            # 초기 정보 입력
            self.ST = St()                          # 색상 사전 정의
            self.accident = False
            self.accident_time = datetime.now()
            self.load_frame(0, '')                  # 프레임 초기화
            self.step = Pro_DB.DB                   # 절차서 각 스텝 DB 가져옴
            self.map_mem = Pro_DB.Pro_map           # map DB

        if True:
            # 좌측 메뉴에서 화면 변환용 버튼 명령
            self.main_ui.B_1.clicked.connect(lambda: self.load_frame(1, '목적'))
            self.main_ui.B_2.clicked.connect(lambda: self.load_frame(2, '수행조건'))
            self.main_ui.B_3.clicked.connect(lambda: self.load_frame(3, '예상 발전소 거동'))
            self.main_ui.B_4.clicked.connect(lambda: self.load_frame(4, '비상운전절차서와 관계'))
            self.main_ui.B_5.clicked.connect(lambda: self.load_frame(5, '이용가능 수단 확인'))
            self.main_ui.B_6.clicked.connect(lambda: self.load_frame(6, '전략 수행 여부 결정'))
            self.main_ui.B_7.clicked.connect(lambda: self.load_frame(7, '전략 수행 방법 결정'))
            self.main_ui.B_8.clicked.connect(lambda: self.load_frame(8, '전략 수행'))
            self.main_ui.B_9.clicked.connect(lambda: self.load_frame(9, '전략 종결'))

            # stack 프레임에 내용 생성
            self.load_each_frame()

            # scroll map
            self.load_map()

        if True:
            # interface up-date -------------------------------------------
            self.updater = QTimer(self)
            for _ in [self.load_current_tiem, self.up_draw_info, self.up_draw_map_info]:
                self.updater.timeout.connect(_)
            self.updater.start(120)
            # -------------------------------------------------------------

    # 시간 업데이트 용 로직 시작 -----------------------------------------------------------------
    def load_current_tiem(self):
        # 현재 시간 업데이트
        now = datetime.now()
        # 사고 발생 시 발생 시간 표시
        if self.accident:
            self.main_ui.label_2.setText('Accident Time:')
            # 프레임 색 변경
            self.main_ui.frame.setStyleSheet(self.ST.f_1_red)
            # 저장된 사고 발생시간 표시
            h, m, s = self.accident_time.hour, self.accident_time.minute, self.accident_time.second
            self.main_ui.T_time_g.setText(f'{h%12:02}:{m:02}:{s:02}')
            # 경과 시간 계산
            ela_time = now - self.accident_time
            self.main_ui.T_time_g_2.setText(f'+ {ela_time.seconds//3600:02}:'
                                            f'{ela_time.seconds//60:02}:{ela_time.seconds%60:02}')
            self.main_ui.T_time.setText(f'{now.hour % 12:02}:{now.minute:02}:{now.second:02}')
        else:
            for _ in [self.main_ui.T_time_g, self.main_ui.T_time_g_2, self.main_ui.label_2]:
                _.setText('')
            self.main_ui.T_time.setText(f'{now.hour % 12:02}:{now.minute:02}:{now.second:02}')

    def keyPressEvent(self, event):
        # print(event.key())
        if event.key() == 65: # 'a' 클릭 시 사고 주입
            self.accident = True
            # 사고 발생 시간 저장
            self.accident_time = datetime.now()
        elif event.key() == 66: # 'b' 클릭 시 사고 제거
            self.accident = False
            # 프레임 색 변경
            self.main_ui.frame.setStyleSheet(self.ST.f_1_blue)
        elif event.key() == 49: # '1' 선
            print('선그리기 모드')
            self.map_mem['C']['L'] = True
            self.map_mem['C']['R'] = False
        elif event.key() == 50: # '2' 박스
            print('박스그리기 모드')
            self.map_mem['C']['L'] = False
            self.map_mem['C']['R'] = True
        else:
            pass

    # 프레임 변경용 로직 시작 --------------------------------------------------------------------
    def load_frame(self, load_nub, title):
        if True:
            # 클릭 시 해당 버튼 색 변경 및 이전 버튼 초기화 기능
            botton_list = [self.main_ui.B_1, self.main_ui.B_2, self.main_ui.B_3, self.main_ui.B_4,
                           self.main_ui.B_5, self.main_ui.B_6, self.main_ui.B_7, self.main_ui.B_8,
                           self.main_ui.B_9]
            for _ in botton_list:
                if botton_list.index(_) + 1 == load_nub:
                    _.setStyleSheet(self.ST.B_C_select)
                else:
                    _.setStyleSheet(self.ST.B_C_unsele)

        self.main_ui.stackedWidget.setCurrentIndex(load_nub)
        self.main_ui.stack_title.setText(title)

    # 사전에 프레임내에 화면 구성
    def load_each_frame(self):
        # 접근 경로 : 선택된 프레임 -> 내부 위젯 -> 스트롤 에어리어 -> 하위 위젯
        for load_nub in range(0, 10):
            cur_scoll_w = self.main_ui.stackedWidget.widget(load_nub).children()[0].widget()
            if load_nub == 1:
                # 1번 프레임에서 그려 질 내용들 ----------------
                self.line_1 = p_line(self.step, load_nub, cur_scoll_w)
                self.step_1_1 = S_Label(self.step[f'{load_nub}'][1], 20, 20, cur_scoll_w)
                self.step_1_2 = S_Label(self.step[f'{load_nub}'][2], 20, self.step_1_1.max_y + 20, cur_scoll_w)
                self.step_1_3 = S_Label(self.step[f'{load_nub}'][3], 20, self.step_1_2.max_y + 20, cur_scoll_w)
                self.step_1_4 = S_Label(self.step[f'{load_nub}'][4], 20, self.step_1_3.max_y + 20, cur_scoll_w)
                self.step_1_5 = S_Label(self.step[f'{load_nub}'][5], 20, self.step_1_4.max_y + 20, cur_scoll_w)
                cur_scoll_w.setMinimumSize(0, self.step_1_5.max_y + 30)

            elif load_nub == 2:
                # 2번 프레임에서 그려 질 내용들 ----------------
                self.line_2 = p_line(self.step, load_nub, cur_scoll_w)
                self.step_2_1 = S_Label(self.step[f'{load_nub}'][1], 20, 20, cur_scoll_w)
                self.step_2_2 = S_Label(self.step[f'{load_nub}'][2], 20, self.step_1_1.max_y + 20, cur_scoll_w)
                self.step_2_3 = S_Label(self.step[f'{load_nub}'][3], 20, self.step_1_2.max_y + 300, cur_scoll_w)
                cur_scoll_w.setMinimumSize(0, self.step_2_3.max_y + 30)

    # 프레임내의 정보에 따른 그림 변화
    def up_draw_info(self):
        # 버튼 클릭시 선색 변화
        step_list = [self.step_1_1, self.step_1_2, self.step_1_3, self.step_1_4, self.step_1_5]
        for _ in step_list:
            self.line_1.up_gp(step_list.index(_) + 1, _.T_boll)

        step_list = [self.step_2_1, self.step_2_2]
        for _ in step_list:
            self.line_2.up_gp(step_list.index(_) + 1, _.T_boll)

        # 2. 2.5의 실시간 테이블 변화
        self.line_2.step_info['2'][2.5][5] = str(int(self.line_2.step_info['2'][2.5][5])%200 + 1)
        self.line_2.step_info['2'][2.5][8] = str(int(self.line_2.step_info['2'][2.5][8])%100 + 2)
        self.line_2.step_info['2'][2.5][11] = str(int(self.line_2.step_info['2'][2.5][11])%100 + 3)
        self.line_2.step_info['2'][2.5][14] = str(int(self.line_2.step_info['2'][2.5][14])%100 + 1)

    # 절차서 로직 프레임 ------------------------------------------------------------------------
    def load_map(self):
        self.p_map = p_map(self.map_mem, self.main_ui.sa_map_0)
        self.main_ui.sa_map_0.setMinimumSize(600, 600) # 오른쪽 스크롤 바의 크기

    def up_draw_map_info(self):
        # 타 프레임 -> self.map_mem -> self.p_map.mem 로 데이터 전달
        # -------------------------------------------------------------------------------------
        # 타 프레임 -> self.map_mem

        # -------------------------------------------------------------------------------------
        # self.map_mem -> self.p_map.mem
        self.p_map.mem = self.map_mem
    # -----------------------------------------------------------------------------------------
    # Class 종료


class S_Label(QWidget):
    def __init__(self, step_info, x, y, parent=None):
        QWidget.__init__(self)
        self.ST = St()
        self.par = parent       # 부모 레이어의 정보
        self.x = x              # 레이블이 그려지는 x
        self.y = y              # 레이블이 그려지는 y
        self.max_y = 0          # 레이블의 최대 길이를 계산용
        # print(self.y)

        self.step_info = step_info
        self.content = self.step_info[0]
        self.T_boll = self.step_info[1]
        self.detail_contents = self.step_info[2]

        self.dis_boll()
        self.dis_cotnet()
        self.dis_bottom()
        self.dis_detail()
        self.dis_check_time()

        self.bottom.clicked.connect(self.click_bottom)

    def dis_boll(self):
        # 수행 여부 확인
        if self.T_boll:
            self.boll = QLabel('●', self.par)
        else:
            self.boll = QLabel('○', self.par)

        self.boll.setGeometry(self.x, self.y, 35, 35)
        self.boll.setStyleSheet(self.ST.L_bord)
        self.boll.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        self.boll.show()

    def dis_cotnet(self):
        # Top 타이틀
        self.cont = QLabel(self.content, self.par)
        self.cont.setGeometry(self.x + 35, self.y, 410, 35)
        self.cont.setStyleSheet(self.ST.L_r_bord)
        self.cont.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.cont.show()

    def dis_bottom(self):
        self.bottom = QPushButton('확인', self.par)
        self.bottom.setGeometry(self.x + 520, self.y, 35, 35)
        self.bottom.setStyleSheet(self.ST.B_bord)
        self.bottom.show()

    def dis_detail(self):
        line_nub = len(self.detail_contents.split('\n'))
        if not self.detail_contents == '':
            self.detail_out = QLabel('', self.par)
            self.detail_out.setGeometry(self.x + 35, self.y + 35, 480, line_nub * 16 + 15)
            self.detail_out.setStyleSheet(self.ST.L_d_bord)

            self.detail = QLabel(self.detail_contents, self.par)
            self.detail.setGeometry(self.x + 40, self.y + 40, 460, line_nub * 16 + 5)
            self.detail.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.detail.setStyleSheet(self.ST.L_dd_bord)

            self.detail_out.show()
            self.max_y = self.y + 35 + line_nub * 16 + 15
        else:
            self.max_y = self.y + 35

    def dis_check_time(self):
        self.ch_time = QLabel('00:00:00', self.par)
        self.ch_time.setGeometry(self.x + 445, self.y, 70, 35)
        self.ch_time.setStyleSheet(self.ST.L_t_bord)
        self.ch_time.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        self.ch_time.show()

    def click_bottom(self):
        if self.T_boll:
            self.T_boll = False
            self.boll.setText('○')
            self.boll.setStyleSheet(self.ST.L_bord)
            self.cont.setStyleSheet(self.ST.L_r_bord)
            self.ch_time.setStyleSheet(self.ST.L_t_bord)
            self.ch_time.setText('00:00:00')
            # self.detail_out.setStyleSheet(self.ST.L_d_bord)
        else:
            self.T_boll = True
            self.boll.setText('●')
            self.boll.setStyleSheet(self.ST.L_s_bord)
            self.cont.setStyleSheet(self.ST.L_rs_bord)
            self.ch_time.setStyleSheet(self.ST.L_ts_bord)
            now = datetime.now()
            self.ch_time.setText(f'{now.hour % 12:02}:{now.minute:02}:{now.second:02}')
            # self.detail_out.setStyleSheet(self.ST.L_ds_bord)


class p_line(QWidget):
    def __init__(self, step_info, nub, par=None):
        self.par = par
        super().__init__(self.par)
        self.setGeometry(self.par.geometry())  # 부모의 geometry 따라감.

        self.frame_nub = nub
        self.line_color = {
            '1': Qt.black, '2': Qt.black, '3': Qt.black, '4': Qt.black,
            #'t_1': QColor(250, 142, 145), rgb(188, 188, 188)
        }
        self.step_info = step_info                   # 절차서 각 스텝 DB 가져옴

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.frame_nub == 1:
            painter.setPen(QPen(self.line_color['1'], 3))
            painter.drawLine(QLine(37, 30, 37, 106))
            painter.setPen(QPen(self.line_color['2'], 3))
            painter.drawLine(QLine(37, 106, 37, 161))
            painter.setPen(QPen(self.line_color['3'], 3))
            painter.drawLine(QLine(37, 161, 37, 295))
            painter.setPen(QPen(self.line_color['4'], 3))
            painter.drawLine(QLine(37, 295, 37, 493))
        elif self.frame_nub == 2:
            painter.setPen(QPen(self.line_color['1'], 3))
            painter.drawLine(QLine(37, 30, 37, 106))
            painter.setPen(QPen(self.line_color['2'], 3))
            painter.drawLine(QLine(37, 106, 37, 161 + 280))

            # 표가 그려지는 부분 -------------------------------------------------
            painter.setPen(QPen(self.line_color['3'], 2))
            table_counter = 0
            for i in range(0, 200, 40):
                for j in range(0, 450, 150):
                    rect = QRect(70 + j, 200 + i, 150, 40)

                    # 특정 제한치 이상부터 경고 색으로 바뀜 -----------------------
                    if table_counter in [5, 8, 11, 14]:
                        if table_counter == 5:
                            if int(self.step_info['2'][2.5][table_counter]) >= 160:
                                painter.fillRect(rect, QColor(250, 142, 145))
                            else:
                                painter.fillRect(rect, QColor(234, 234, 234))
                        else:
                            if int(self.step_info['2'][2.5][table_counter]) >= 50:
                                painter.fillRect(rect, QColor(250, 142, 145))
                            else:
                                painter.fillRect(rect, QColor(234, 234, 234))
                    else:
                        painter.fillRect(rect, QColor(234, 234, 234))
                    # ---------------------------------------------------------
                    painter.drawRect(rect)
                    painter.drawText(rect, Qt.AlignCenter,
                                     self.step_info['2'][2.5][table_counter])
                    table_counter += 1
            # ------------------------------------------------------------------
        self.update()

    def up_gp(self, nub, trig):
        # 버튼 명령에 따라서 라인 색 변경
        if trig:
            self.line_color[f'{nub}'] = Qt.red
        else:
            self.line_color[f'{nub}'] = Qt.black

    def mousePressEvent(self, event):
        print(event.pos())


class p_map(QWidget):
    def __init__(self, mother_mem, par=None):
        super().__init__(par)
        self.map_mem = mother_mem
        self.setGeometry(par.geometry())

        # 좌표 추출
        self.cont = 0
        self.line_xy = []

    def paintEvent(self, event):
        p = QPainter(self)
        # 선 모두 그리기
        for _ in self.map_mem['L'].keys():
            self.draw_line(p, self.map_mem['L'][_])
        for _ in self.map_mem['R'].keys():
            self.draw_box(p, self.map_mem['R'][_])

        self.update()

    # 드로잉 툴 ==================================================================================================
    def draw_info(self, painter, info):
        painter.setPen(QPen(info['C'], info['W']))
        painter.setRenderHint(QPainter.Antialiasing, True)

    def draw_line(self, painter, info):
        self.draw_info(painter, info)
        painter.drawLine(info['P'])

    def draw_box(self, painter, info):
        self.draw_info(painter, info)
        painter.drawRect(info['P'])

    def mousePressEvent(self, event):
        if self.map_mem['C']['L']:      # 라인 그리는 툴
            self.get_two_point(event, 'L')
        if self.map_mem['C']['R']:      # 박스 그리는 툴
            self.get_two_point(event, 'R')

    def get_two_point(self, event, type):
        if self.cont == 1:
            self.line_xy.append(event.pos())
            print(f'draw {self.line_xy}')
            if type == 'L':
                self.map_mem[type][len(self.map_mem[type].keys()) + 1] = {'C': Qt.black, 'W': 2,
                                                                          'P': QLine(self.line_xy[0],self.line_xy[1])}
            elif type == 'R':
                self.map_mem[type][len(self.map_mem[type].keys()) + 1] = {'C': Qt.black, 'W': 2,
                                                                          'P': QRect(self.line_xy[0], self.line_xy[1])}

            self.cont = 0
            self.line_xy = []
        else:
            self.line_xy.append(event.pos())
            self.cont += 1
    # ===========================================================================================================


class St:
    # 스타일 및 색에 대한 정보
    def __init__(self):
        self.f_1_red = 'border-top-left-radius: 20px; border-top-right-radius: 20px; ' \
                        'border: 1px solid black; background: qlineargradient(x1: 0, y1: ' \
                        '0, x2: 0, y2: 1, stop: 0 #56a, stop: 0.5 #c03546);'
        self.f_1_blue = 'border-top-left-radius: 20px; border-top-right-radius: 20px; ' \
                        'border: 1px solid black; background: qlineargradient(x1: 0, y1: ' \
                        '0, x2: 0, y2: 1, stop: 0 #56a, stop: 0.5 #2b90d9);'
        self.B_C_unsele = 'QPushButton{border-top-left-radius: 5px; border-top-right-radius: 5px;' \
                         'border-bottom-right-radius: 5px; 	border-bottom-left-radius: 5px; ' \
                         'background-color: rgb(234, 234, 234);}' \
                         'QPushButton:pressed {	background-color: rgb(188, 188, 188);}'
        self.B_C_select = 'QPushButton{border-top-left-radius: 5px; border-top-right-radius: 5px;' \
                         'border-bottom-right-radius: 5px; 	border-bottom-left-radius: 5px; ' \
                         'background-color: rgb(255, 255, 0);}' \
                         'QPushButton:pressed {	background-color: rgb(188, 188, 188);}'
        # 탑 볼
        self.L_bord = 'border-top: 1px solid black; border-bottom: 1px solid black; ' \
                      'border-left: 1px solid black; font: 13pt \"HY견고딕\"; background-color: rgb(234, 234, 234);'
        self.L_s_bord = 'border-top: 1px solid black; border-bottom: 1px solid black; ' \
                        'border-left: 1px solid black; font: 13pt \"HY견고딕\"; background-color: #2b90d9;'
        # 탑 시계
        self.L_t_bord = 'border-top: 1px solid black; border-bottom: 1px solid black; ' \
                        'border-right: 1px solid black; font: 8pt \"HY견고딕\"; background-color: rgb(234, 234, 234);'
        self.L_ts_bord = 'border-top: 1px solid black; border-bottom: 1px solid black; ' \
                         'border-right: 1px solid black; font: 8pt \"HY견고딕\"; background-color: #2b90d9;'
        # 세부 내용 껍데기
        self.L_d_bord = 'border-right: 1px solid black; border-bottom: 1px solid black; ' \
                        'border-left: 1px solid black; font: 10pt \"HY견고딕\"; background-color: rgb(234, 234, 234);'
        self.L_ds_bord = 'border-right: 1px solid black; border-bottom: 1px solid black; ' \
                         'border-left: 1px solid black; font: 10pt \"HY견고딕\"; background-color: #2b90d9;'
        # 세부 내용
        self.L_dd_bord = 'font: none; background-color: rgb(234, 234, 234);'
        self.L_dds_bord = 'font: none; background-color: #2b90d9;'
        #
        self.L_r_bord = 'border-top: 1px solid black; border-bottom: 1px solid black; ' \
                        'font: 10pt \"HY견고딕\"; background-color: rgb(234, 234, 234);'
        self.L_rs_bord = 'border-top: 1px solid black; border-bottom: 1px solid black; ' \
                         'font: 10pt \"HY견고딕\"; background-color: #2b90d9;'
        self.B_bord = 'font: 9pt \"HY견고딕\"; background-color: rgb(234, 234, 234);'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    body = main_body()
    body.show()
    app.exec_()