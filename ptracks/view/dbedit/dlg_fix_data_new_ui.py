# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dlg_fix_data_new.ui'
#
# Created: Wed Dec  7 13:03:45 2016
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

class Ui_CDlgFixDataNEW(object):
    def setupUi(self, CDlgFixDataNEW):
        CDlgFixDataNEW.setObjectName(_fromUtf8("CDlgFixDataNEW"))
        CDlgFixDataNEW.setWindowModality(QtCore.Qt.WindowModal)
        CDlgFixDataNEW.resize(760, 484)
        CDlgFixDataNEW.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        CDlgFixDataNEW.setSizeGripEnabled(True)
        CDlgFixDataNEW.setModal(True)
        self.horizontalLayout_6 = QtGui.QHBoxLayout(CDlgFixDataNEW)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.splitter = QtGui.QSplitter(CDlgFixDataNEW)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.wid_list = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wid_list.sizePolicy().hasHeightForWidth())
        self.wid_list.setSizePolicy(sizePolicy)
        self.wid_list.setObjectName(_fromUtf8("wid_list"))
        self.verticalLayout = QtGui.QVBoxLayout(self.wid_list)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.qtw_fixos = QtGui.QTableWidget(self.wid_list)
        self.qtw_fixos.setObjectName(_fromUtf8("qtw_fixos"))
        self.qtw_fixos.setColumnCount(0)
        self.qtw_fixos.setRowCount(0)
        self.verticalLayout.addWidget(self.qtw_fixos)
        self.wid_data = QtGui.QWidget(self.splitter)
        self.wid_data.setObjectName(_fromUtf8("wid_data"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wid_data)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frm_id = QtGui.QFrame(self.wid_data)
        self.frm_id.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frm_id.setFrameShadow(QtGui.QFrame.Raised)
        self.frm_id.setObjectName(_fromUtf8("frm_id"))
        self.gridLayout = QtGui.QGridLayout(self.frm_id)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.txt_indc = QtGui.QLabel(self.frm_id)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txt_indc.setFont(font)
        self.txt_indc.setObjectName(_fromUtf8("txt_indc"))
        self.gridLayout.addWidget(self.txt_indc, 0, 3, 1, 1)
        self.lbl_desc = QtGui.QLabel(self.frm_id)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_desc.sizePolicy().hasHeightForWidth())
        self.lbl_desc.setSizePolicy(sizePolicy)
        self.lbl_desc.setObjectName(_fromUtf8("lbl_desc"))
        self.gridLayout.addWidget(self.lbl_desc, 2, 1, 1, 1)
        self.lbl_indc = QtGui.QLabel(self.frm_id)
        self.lbl_indc.setObjectName(_fromUtf8("lbl_indc"))
        self.gridLayout.addWidget(self.lbl_indc, 0, 1, 1, 1)
        self.qle_desc = QtGui.QLineEdit(self.frm_id)
        self.qle_desc.setObjectName(_fromUtf8("qle_desc"))
        self.gridLayout.addWidget(self.qle_desc, 2, 3, 1, 2)
        self.verticalLayout_2.addWidget(self.frm_id)
        self.wid_fields = QtGui.QWidget(self.wid_data)
        self.wid_fields.setObjectName(_fromUtf8("wid_fields"))
        self.gridLayout_4 = QtGui.QGridLayout(self.wid_fields)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gbx_pos = QtGui.QGroupBox(self.wid_fields)
        self.gbx_pos.setObjectName(_fromUtf8("gbx_pos"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gbx_pos)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.qle_lat = QtGui.QLineEdit(self.gbx_pos)
        self.qle_lat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qle_lat.setObjectName(_fromUtf8("qle_lat"))
        self.gridLayout_2.addWidget(self.qle_lat, 0, 1, 1, 1)
        self.qle_lng = QtGui.QLineEdit(self.gbx_pos)
        self.qle_lng.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qle_lng.setObjectName(_fromUtf8("qle_lng"))
        self.gridLayout_2.addWidget(self.qle_lng, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gbx_pos)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gbx_pos)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.gbx_pos, 0, 1, 1, 1)
        self.gbx_tipo = QtGui.QGroupBox(self.wid_fields)
        self.gbx_tipo.setObjectName(_fromUtf8("gbx_tipo"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gbx_tipo)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.ckx_dme = QtGui.QCheckBox(self.gbx_tipo)
        self.ckx_dme.setObjectName(_fromUtf8("ckx_dme"))
        self.gridLayout_3.addWidget(self.ckx_dme, 0, 0, 1, 1)
        self.ckx_ndb = QtGui.QCheckBox(self.gbx_tipo)
        self.ckx_ndb.setObjectName(_fromUtf8("ckx_ndb"))
        self.gridLayout_3.addWidget(self.ckx_ndb, 1, 0, 1, 1)
        self.ckx_vor = QtGui.QCheckBox(self.gbx_tipo)
        self.ckx_vor.setObjectName(_fromUtf8("ckx_vor"))
        self.gridLayout_3.addWidget(self.ckx_vor, 0, 1, 1, 1)
        self.ckx_branco = QtGui.QCheckBox(self.gbx_tipo)
        self.ckx_branco.setObjectName(_fromUtf8("ckx_branco"))
        self.gridLayout_3.addWidget(self.ckx_branco, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.gbx_tipo, 0, 0, 1, 1)
        self.gbx_freq = QtGui.QGroupBox(self.wid_fields)
        self.gbx_freq.setObjectName(_fromUtf8("gbx_freq"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.gbx_freq)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lbl_freq = QtGui.QLabel(self.gbx_freq)
        self.lbl_freq.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_freq.setObjectName(_fromUtf8("lbl_freq"))
        self.horizontalLayout_4.addWidget(self.lbl_freq)
        self.dsb_freq = QtGui.QDoubleSpinBox(self.gbx_freq)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_freq.sizePolicy().hasHeightForWidth())
        self.dsb_freq.setSizePolicy(sizePolicy)
        self.dsb_freq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsb_freq.setDecimals(1)
        self.dsb_freq.setMaximum(100000.0)
        self.dsb_freq.setSingleStep(1000.0)
        self.dsb_freq.setObjectName(_fromUtf8("dsb_freq"))
        self.horizontalLayout_4.addWidget(self.dsb_freq)
        self.gridLayout_4.addWidget(self.gbx_freq, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.wid_fields)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.frm_bbx = QtGui.QFrame(self.wid_data)
        self.frm_bbx.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frm_bbx.setFrameShadow(QtGui.QFrame.Raised)
        self.frm_bbx.setObjectName(_fromUtf8("frm_bbx"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frm_bbx)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_new = QtGui.QPushButton(self.frm_bbx)
        self.btn_new.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/dbedit/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_new.setIcon(icon)
        self.btn_new.setObjectName(_fromUtf8("btn_new"))
        self.horizontalLayout_2.addWidget(self.btn_new)
        self.btn_del = QtGui.QPushButton(self.frm_bbx)
        self.btn_del.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/dbedit/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_del.setIcon(icon1)
        self.btn_del.setObjectName(_fromUtf8("btn_del"))
        self.horizontalLayout_2.addWidget(self.btn_del)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.dbb_fixos = QtGui.QDialogButtonBox(self.frm_bbx)
        self.dbb_fixos.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.dbb_fixos.setObjectName(_fromUtf8("dbb_fixos"))
        self.horizontalLayout_2.addWidget(self.dbb_fixos)
        self.verticalLayout_2.addWidget(self.frm_bbx)
        self.horizontalLayout_6.addWidget(self.splitter)

        self.retranslateUi(CDlgFixDataNEW)
        QtCore.QMetaObject.connectSlotsByName(CDlgFixDataNEW)
        CDlgFixDataNEW.setTabOrder(self.ckx_ndb, self.ckx_dme)

    def retranslateUi(self, CDlgFixDataNEW):
        CDlgFixDataNEW.setWindowTitle(_translate("CDlgFixDataNEW", "Edição de Fixos", None))
        self.txt_indc.setText(_translate("CDlgFixDataNEW", "Nonono", None))
        self.lbl_desc.setText(_translate("CDlgFixDataNEW", "Descrição:", None))
        self.lbl_indc.setText(_translate("CDlgFixDataNEW", "Indicativo:", None))
        self.gbx_pos.setTitle(_translate("CDlgFixDataNEW", "Posicão", None))
        self.label.setText(_translate("CDlgFixDataNEW", "Latitude:", None))
        self.label_2.setText(_translate("CDlgFixDataNEW", "Longitude:", None))
        self.gbx_tipo.setTitle(_translate("CDlgFixDataNEW", "Tipo", None))
        self.ckx_dme.setText(_translate("CDlgFixDataNEW", "DME", None))
        self.ckx_ndb.setText(_translate("CDlgFixDataNEW", "NDB", None))
        self.ckx_vor.setText(_translate("CDlgFixDataNEW", "VOR", None))
        self.ckx_branco.setText(_translate("CDlgFixDataNEW", "W/P", None))
        self.gbx_freq.setTitle(_translate("CDlgFixDataNEW", "Freqüência", None))
        self.lbl_freq.setText(_translate("CDlgFixDataNEW", "Freqüência:", None))
        self.dsb_freq.setSuffix(_translate("CDlgFixDataNEW", " Hz", None))
        self.btn_new.setText(_translate("CDlgFixDataNEW", "Novo", None))
        self.btn_del.setText(_translate("CDlgFixDataNEW", "Remove", None))

import resources_rc
