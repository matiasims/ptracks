# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './wnd_main_piloto.ui'
#
# Created: Mon Apr 18 14:33:04 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_wndMainPiloto(object):
    def setupUi(self, wndMainPiloto):
        wndMainPiloto.setObjectName(_fromUtf8("wndMainPiloto"))
        wndMainPiloto.resize(1056, 680)
        wndMainPiloto.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget = QtGui.QWidget(wndMainPiloto)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frmStrips = QtGui.QFrame(self.centralwidget)
        self.frmStrips.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmStrips.setFrameShadow(QtGui.QFrame.Raised)
        self.frmStrips.setObjectName(_fromUtf8("frmStrips"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.frmStrips)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.widLV = QtGui.QWidget(self.frmStrips)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widLV.sizePolicy().hasHeightForWidth())
        self.widLV.setSizePolicy(sizePolicy)
        self.widLV.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: #729fcf;"))
        self.widLV.setObjectName(_fromUtf8("widLV"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widLV)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setMargin(3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_icon = QtGui.QLabel(self.widLV)
        self.lbl_icon.setText(_fromUtf8(""))
        self.lbl_icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/tracks/compile16.png")))
        self.lbl_icon.setObjectName(_fromUtf8("lbl_icon"))
        self.horizontalLayout.addWidget(self.lbl_icon)
        self.lbl_title = QtGui.QLabel(self.widLV)
        self.lbl_title.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 14pt \"Arial\";"))
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.horizontalLayout.addWidget(self.lbl_title)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_7.addWidget(self.widLV)
        self.qtv_stp = QtGui.QTableView(self.frmStrips)
        self.qtv_stp.setObjectName(_fromUtf8("qtv_stp"))
        self.verticalLayout_7.addWidget(self.qtv_stp)
        self.qlw_strips = QtGui.QListWidget(self.frmStrips)
        self.qlw_strips.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
""))
        self.qlw_strips.setObjectName(_fromUtf8("qlw_strips"))
        self.verticalLayout_7.addWidget(self.qlw_strips)
        self.horizontalLayout_3.addWidget(self.frmStrips)
        self.frmCmds = QtGui.QFrame(self.centralwidget)
        self.frmCmds.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmCmds.setFrameShadow(QtGui.QFrame.Raised)
        self.frmCmds.setObjectName(_fromUtf8("frmCmds"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.frmCmds)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.gbx_status = QtGui.QGroupBox(self.frmCmds)
        self.gbx_status.setObjectName(_fromUtf8("gbx_status"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gbx_status)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lbl_tit_prc = QtGui.QLabel(self.gbx_status)
        self.lbl_tit_prc.setObjectName(_fromUtf8("lbl_tit_prc"))
        self.gridLayout_2.addWidget(self.lbl_tit_prc, 0, 0, 1, 1)
        self.lbl_prc = QtGui.QLabel(self.gbx_status)
        self.lbl_prc.setObjectName(_fromUtf8("lbl_prc"))
        self.gridLayout_2.addWidget(self.lbl_prc, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_8.addWidget(self.gbx_status)
        self.gbx_comandos = QtGui.QGroupBox(self.frmCmds)
        self.gbx_comandos.setEnabled(False)
        self.gbx_comandos.setObjectName(_fromUtf8("gbx_comandos"))
        self.verticalLayout = QtGui.QVBoxLayout(self.gbx_comandos)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frm_btn = QtGui.QFrame(self.gbx_comandos)
        self.frm_btn.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frm_btn.setFrameShadow(QtGui.QFrame.Raised)
        self.frm_btn.setObjectName(_fromUtf8("frm_btn"))
        self.gridLayout = QtGui.QGridLayout(self.frm_btn)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btn_cmd_altitude = QtGui.QPushButton(self.frm_btn)
        self.btn_cmd_altitude.setEnabled(False)
        self.btn_cmd_altitude.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 255);\n"
"color:rgb(255, 255, 0);"))
        self.btn_cmd_altitude.setObjectName(_fromUtf8("btn_cmd_altitude"))
        self.gridLayout.addWidget(self.btn_cmd_altitude, 0, 3, 1, 1)
        self.btn_prc_pouso = QtGui.QPushButton(self.frm_btn)
        self.btn_prc_pouso.setEnabled(False)
        self.btn_prc_pouso.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0)"))
        self.btn_prc_pouso.setObjectName(_fromUtf8("btn_prc_pouso"))
        self.gridLayout.addWidget(self.btn_prc_pouso, 7, 3, 1, 1)
        self.btn_prc_sub = QtGui.QPushButton(self.frm_btn)
        self.btn_prc_sub.setEnabled(False)
        self.btn_prc_sub.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0)"))
        self.btn_prc_sub.setObjectName(_fromUtf8("btn_prc_sub"))
        self.gridLayout.addWidget(self.btn_prc_sub, 8, 0, 1, 1)
        self.btn_cancela = QtGui.QPushButton(self.frm_btn)
        self.btn_cancela.setEnabled(False)
        self.btn_cancela.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0)"))
        self.btn_cancela.setObjectName(_fromUtf8("btn_cancela"))
        self.gridLayout.addWidget(self.btn_cancela, 8, 3, 1, 1)
        self.btn_cod_spi = QtGui.QPushButton(self.frm_btn)
        self.btn_cod_spi.setEnabled(False)
        self.btn_cod_spi.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);"))
        self.btn_cod_spi.setObjectName(_fromUtf8("btn_cod_spi"))
        self.gridLayout.addWidget(self.btn_cod_spi, 11, 1, 1, 1)
        self.btn_prc_dep = QtGui.QPushButton(self.frm_btn)
        self.btn_prc_dep.setEnabled(False)
        self.btn_prc_dep.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0)"))
        self.btn_prc_dep.setObjectName(_fromUtf8("btn_prc_dep"))
        self.gridLayout.addWidget(self.btn_prc_dep, 5, 3, 1, 1)
        self.btn_cmd_velocidade = QtGui.QPushButton(self.frm_btn)
        self.btn_cmd_velocidade.setEnabled(False)
        self.btn_cmd_velocidade.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 255);\n"
"color:rgb(255, 255, 0);"))
        self.btn_cmd_velocidade.setObjectName(_fromUtf8("btn_cmd_velocidade"))
        self.gridLayout.addWidget(self.btn_cmd_velocidade, 0, 1, 1, 1)
        self.btn_cod_ssr = QtGui.QPushButton(self.frm_btn)
        self.btn_cod_ssr.setEnabled(False)
        self.btn_cod_ssr.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);"))
        self.btn_cod_ssr.setObjectName(_fromUtf8("btn_cod_ssr"))
        self.gridLayout.addWidget(self.btn_cod_ssr, 11, 0, 1, 1)
        self.btn_cod_emg = QtGui.QPushButton(self.frm_btn)
        self.btn_cod_emg.setEnabled(False)
        self.btn_cod_emg.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);"))
        self.btn_cod_emg.setObjectName(_fromUtf8("btn_cod_emg"))
        self.gridLayout.addWidget(self.btn_cod_emg, 11, 3, 1, 1)
        self.btn_prc_esp = QtGui.QPushButton(self.frm_btn)
        self.btn_prc_esp.setEnabled(False)
        self.btn_prc_esp.setStyleSheet(_fromUtf8("background-color: rgb(255, 255,  0);"))
        self.btn_prc_esp.setObjectName(_fromUtf8("btn_prc_esp"))
        self.gridLayout.addWidget(self.btn_prc_esp, 7, 0, 1, 1)
        self.btn_prc_dir_fix = QtGui.QPushButton(self.frm_btn)
        self.btn_prc_dir_fix.setEnabled(False)
        self.btn_prc_dir_fix.setStyleSheet(_fromUtf8("background-color: rgb(255, 255,  0);"))
        self.btn_prc_dir_fix.setObjectName(_fromUtf8("btn_prc_dir_fix"))
        self.gridLayout.addWidget(self.btn_prc_dir_fix, 7, 1, 1, 1)
        self.btn_prc_ape = QtGui.QPushButton(self.frm_btn)
        self.btn_prc_ape.setEnabled(False)
        self.btn_prc_ape.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0)"))
        self.btn_prc_ape.setObjectName(_fromUtf8("btn_prc_ape"))
        self.gridLayout.addWidget(self.btn_prc_ape, 5, 1, 1, 1)
        self.btn_prc_apch = QtGui.QPushButton(self.frm_btn)
        self.btn_prc_apch.setEnabled(False)
        self.btn_prc_apch.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0)"))
        self.btn_prc_apch.setObjectName(_fromUtf8("btn_prc_apch"))
        self.gridLayout.addWidget(self.btn_prc_apch, 5, 0, 1, 1)
        self.btn_prc_trj = QtGui.QPushButton(self.frm_btn)
        self.btn_prc_trj.setEnabled(False)
        self.btn_prc_trj.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0);"))
        self.btn_prc_trj.setObjectName(_fromUtf8("btn_prc_trj"))
        self.gridLayout.addWidget(self.btn_prc_trj, 8, 1, 1, 1)
        self.btn_cmd_direcao = QtGui.QPushButton(self.frm_btn)
        self.btn_cmd_direcao.setEnabled(False)
        self.btn_cmd_direcao.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 255);\n"
"color:rgb(255, 255, 0);"))
        self.btn_cmd_direcao.setObjectName(_fromUtf8("btn_cmd_direcao"))
        self.gridLayout.addWidget(self.btn_cmd_direcao, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frm_btn)
        self.widCmdLine = QtGui.QWidget(self.gbx_comandos)
        self.widCmdLine.setObjectName(_fromUtf8("widCmdLine"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widCmdLine)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lbl_comando = QtGui.QLabel(self.widCmdLine)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_comando.sizePolicy().hasHeightForWidth())
        self.lbl_comando.setSizePolicy(sizePolicy)
        self.lbl_comando.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(0, 190, 0)"))
        self.lbl_comando.setObjectName(_fromUtf8("lbl_comando"))
        self.horizontalLayout_4.addWidget(self.lbl_comando)
        self.btn_send = QtGui.QPushButton(self.widCmdLine)
        self.btn_send.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/tracks/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_send.setIcon(icon)
        self.btn_send.setObjectName(_fromUtf8("btn_send"))
        self.horizontalLayout_4.addWidget(self.btn_send)
        self.verticalLayout.addWidget(self.widCmdLine)
        self.qlw_history = QtGui.QListWidget(self.gbx_comandos)
        self.qlw_history.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(0, 190, 0)"))
        self.qlw_history.setObjectName(_fromUtf8("qlw_history"))
        self.verticalLayout.addWidget(self.qlw_history)
        self.verticalLayout_8.addWidget(self.gbx_comandos)
        self.widToolbox = QtGui.QWidget(self.frmCmds)
        self.widToolbox.setObjectName(_fromUtf8("widToolbox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widToolbox)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_a = QtGui.QToolButton(self.widToolbox)
        self.btn_a.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/tracks/fullscreen_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_a.setIcon(icon1)
        self.btn_a.setIconSize(QtCore.QSize(48, 48))
        self.btn_a.setObjectName(_fromUtf8("btn_a"))
        self.horizontalLayout_2.addWidget(self.btn_a)
        self.btn_b = QtGui.QToolButton(self.widToolbox)
        self.btn_b.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/pixmaps/gamenew.xpm")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_b.setIcon(icon2)
        self.btn_b.setIconSize(QtCore.QSize(48, 48))
        self.btn_b.setObjectName(_fromUtf8("btn_b"))
        self.horizontalLayout_2.addWidget(self.btn_b)
        self.btn_c = QtGui.QToolButton(self.widToolbox)
        self.btn_c.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/tracks/view-restore_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_c.setIcon(icon3)
        self.btn_c.setIconSize(QtCore.QSize(48, 48))
        self.btn_c.setObjectName(_fromUtf8("btn_c"))
        self.horizontalLayout_2.addWidget(self.btn_c)
        self.verticalLayout_8.addWidget(self.widToolbox)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.frmCmds)
        wndMainPiloto.setCentralWidget(self.centralwidget)
        self.menu_bar = QtGui.QMenuBar(wndMainPiloto)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1056, 27))
        self.menu_bar.setObjectName(_fromUtf8("menu_bar"))
        self.menu_file = QtGui.QMenu(self.menu_bar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        wndMainPiloto.setMenuBar(self.menu_bar)
        self.status_bar = QtGui.QStatusBar(wndMainPiloto)
        self.status_bar.setObjectName(_fromUtf8("status_bar"))
        wndMainPiloto.setStatusBar(self.status_bar)
        self.action_exit = QtGui.QAction(wndMainPiloto)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_bar.addAction(self.menu_file.menuAction())

        self.retranslateUi(wndMainPiloto)
        QtCore.QMetaObject.connectSlotsByName(wndMainPiloto)

    def retranslateUi(self, wndMainPiloto):
        wndMainPiloto.setWindowTitle(_translate("wndMainPiloto", "Pilot 0.1 [Pilotagem]", None))
        self.lbl_title.setText(_translate("wndMainPiloto", "Lista de Vôos", None))
        self.gbx_status.setTitle(_translate("wndMainPiloto", "Status", None))
        self.lbl_tit_prc.setText(_translate("wndMainPiloto", "Procedimento:", None))
        self.lbl_prc.setText(_translate("wndMainPiloto", "TRJ001", None))
        self.gbx_comandos.setTitle(_translate("wndMainPiloto", "Comandos", None))
        self.btn_cmd_altitude.setText(_translate("wndMainPiloto", "altitude", None))
        self.btn_prc_pouso.setText(_translate("wndMainPiloto", "pouso", None))
        self.btn_prc_sub.setText(_translate("wndMainPiloto", "subida", None))
        self.btn_cancela.setText(_translate("wndMainPiloto", "cancela", None))
        self.btn_cod_spi.setText(_translate("wndMainPiloto", "SPI", None))
        self.btn_prc_dep.setText(_translate("wndMainPiloto", "decolagem", None))
        self.btn_cmd_velocidade.setText(_translate("wndMainPiloto", "velocidade", None))
        self.btn_cod_ssr.setText(_translate("wndMainPiloto", "SSR", None))
        self.btn_cod_emg.setText(_translate("wndMainPiloto", "EMG", None))
        self.btn_prc_esp.setText(_translate("wndMainPiloto", "espera", None))
        self.btn_prc_dir_fix.setText(_translate("wndMainPiloto", "dir.fixo", None))
        self.btn_prc_ape.setText(_translate("wndMainPiloto", "apx.perdida", None))
        self.btn_prc_apch.setText(_translate("wndMainPiloto", "aproximação", None))
        self.btn_prc_trj.setText(_translate("wndMainPiloto", "trajetória", None))
        self.btn_cmd_direcao.setText(_translate("wndMainPiloto", "direção", None))
        self.lbl_comando.setText(_translate("wndMainPiloto", "SIL1970: CURVA DIR 212 GRAUS", None))
        self.btn_b.setText(_translate("wndMainPiloto", "...", None))
        self.btn_c.setText(_translate("wndMainPiloto", "...", None))
        self.menu_file.setTitle(_translate("wndMainPiloto", "Arquivo", None))
        self.action_exit.setText(_translate("wndMainPiloto", "Sair", None))
        self.action_exit.setShortcut(_translate("wndMainPiloto", "Ctrl+X", None))

import resources_visil_rc
