# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dlg_prf_edit_new.ui'
#
# Created: Tue Jan 26 11:33:06 2016
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

class Ui_dlgPrfEditNEW(object):
    def setupUi(self, dlgPrfEditNEW):
        dlgPrfEditNEW.setObjectName(_fromUtf8("dlgPrfEditNEW"))
        dlgPrfEditNEW.resize(753, 721)
        dlgPrfEditNEW.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        dlgPrfEditNEW.setSizeGripEnabled(True)
        dlgPrfEditNEW.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dlgPrfEditNEW)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frmGrpID = QtGui.QFrame(dlgPrfEditNEW)
        self.frmGrpID.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmGrpID.setFrameShadow(QtGui.QFrame.Raised)
        self.frmGrpID.setObjectName(_fromUtf8("frmGrpID"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frmGrpID)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblTipo = QtGui.QLabel(self.frmGrpID)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTipo.sizePolicy().hasHeightForWidth())
        self.lblTipo.setSizePolicy(sizePolicy)
        self.lblTipo.setObjectName(_fromUtf8("lblTipo"))
        self.horizontalLayout.addWidget(self.lblTipo)
        self.qleTipo = QtGui.QLineEdit(self.frmGrpID)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qleTipo.sizePolicy().hasHeightForWidth())
        self.qleTipo.setSizePolicy(sizePolicy)
        self.qleTipo.setObjectName(_fromUtf8("qleTipo"))
        self.horizontalLayout.addWidget(self.qleTipo)
        self.lblDesc = QtGui.QLabel(self.frmGrpID)
        self.lblDesc.setObjectName(_fromUtf8("lblDesc"))
        self.horizontalLayout.addWidget(self.lblDesc)
        self.qleDesc = QtGui.QLineEdit(self.frmGrpID)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qleDesc.sizePolicy().hasHeightForWidth())
        self.qleDesc.setSizePolicy(sizePolicy)
        self.qleDesc.setObjectName(_fromUtf8("qleDesc"))
        self.horizontalLayout.addWidget(self.qleDesc)
        self.verticalLayout.addWidget(self.frmGrpID)
        self.frmGrp1 = QtGui.QFrame(dlgPrfEditNEW)
        self.frmGrp1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmGrp1.setFrameShadow(QtGui.QFrame.Raised)
        self.frmGrp1.setObjectName(_fromUtf8("frmGrp1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frmGrp1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gbxMax = QtGui.QGroupBox(self.frmGrp1)
        self.gbxMax.setObjectName(_fromUtf8("gbxMax"))
        self.gridLayout = QtGui.QGridLayout(self.gbxMax)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.qsbMaxAlt = QtGui.QSpinBox(self.gbxMax)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbMaxAlt.sizePolicy().hasHeightForWidth())
        self.qsbMaxAlt.setSizePolicy(sizePolicy)
        self.qsbMaxAlt.setAlignment(QtCore.Qt.AlignRight)
        self.qsbMaxAlt.setMinimum(0)
        self.qsbMaxAlt.setMaximum(100000)
        self.qsbMaxAlt.setSingleStep(10)
        self.qsbMaxAlt.setProperty("value", 100)
        self.qsbMaxAlt.setObjectName(_fromUtf8("qsbMaxAlt"))
        self.gridLayout.addWidget(self.qsbMaxAlt, 1, 1, 1, 2)
        self.lblMaxAlt = QtGui.QLabel(self.gbxMax)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMaxAlt.sizePolicy().hasHeightForWidth())
        self.lblMaxAlt.setSizePolicy(sizePolicy)
        self.lblMaxAlt.setObjectName(_fromUtf8("lblMaxAlt"))
        self.gridLayout.addWidget(self.lblMaxAlt, 1, 0, 1, 1)
        self.lblMaxVel = QtGui.QLabel(self.gbxMax)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMaxVel.sizePolicy().hasHeightForWidth())
        self.lblMaxVel.setSizePolicy(sizePolicy)
        self.lblMaxVel.setObjectName(_fromUtf8("lblMaxVel"))
        self.gridLayout.addWidget(self.lblMaxVel, 2, 0, 1, 1)
        self.qsbMaxVel = QtGui.QSpinBox(self.gbxMax)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbMaxVel.sizePolicy().hasHeightForWidth())
        self.qsbMaxVel.setSizePolicy(sizePolicy)
        self.qsbMaxVel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbMaxVel.setMinimum(0)
        self.qsbMaxVel.setMaximum(1200)
        self.qsbMaxVel.setSingleStep(10)
        self.qsbMaxVel.setProperty("value", 100)
        self.qsbMaxVel.setObjectName(_fromUtf8("qsbMaxVel"))
        self.gridLayout.addWidget(self.qsbMaxVel, 2, 1, 1, 2)
        self.lblMaxVelTax = QtGui.QLabel(self.gbxMax)
        self.lblMaxVelTax.setObjectName(_fromUtf8("lblMaxVelTax"))
        self.gridLayout.addWidget(self.lblMaxVelTax, 5, 0, 1, 1)
        self.qsbMaxVelTax = QtGui.QSpinBox(self.gbxMax)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbMaxVelTax.sizePolicy().hasHeightForWidth())
        self.qsbMaxVelTax.setSizePolicy(sizePolicy)
        self.qsbMaxVelTax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbMaxVelTax.setObjectName(_fromUtf8("qsbMaxVelTax"))
        self.gridLayout.addWidget(self.qsbMaxVelTax, 5, 1, 1, 2)
        self.horizontalLayout_2.addWidget(self.gbxMax)
        self.gbxVoo = QtGui.QGroupBox(self.frmGrp1)
        self.gbxVoo.setObjectName(_fromUtf8("gbxVoo"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gbxVoo)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lblVooAcc = QtGui.QLabel(self.gbxVoo)
        self.lblVooAcc.setObjectName(_fromUtf8("lblVooAcc"))
        self.gridLayout_2.addWidget(self.lblVooAcc, 0, 0, 1, 1)
        self.qsbVooAcc = QtGui.QSpinBox(self.gbxVoo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbVooAcc.sizePolicy().hasHeightForWidth())
        self.qsbVooAcc.setSizePolicy(sizePolicy)
        self.qsbVooAcc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbVooAcc.setMaximum(1000)
        self.qsbVooAcc.setSingleStep(10)
        self.qsbVooAcc.setProperty("value", 100)
        self.qsbVooAcc.setObjectName(_fromUtf8("qsbVooAcc"))
        self.gridLayout_2.addWidget(self.qsbVooAcc, 0, 1, 1, 1)
        self.lblVooDac = QtGui.QLabel(self.gbxVoo)
        self.lblVooDac.setObjectName(_fromUtf8("lblVooDac"))
        self.gridLayout_2.addWidget(self.lblVooDac, 1, 0, 1, 1)
        self.qsbVooDac = QtGui.QSpinBox(self.gbxVoo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbVooDac.sizePolicy().hasHeightForWidth())
        self.qsbVooDac.setSizePolicy(sizePolicy)
        self.qsbVooDac.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbVooDac.setMaximum(500)
        self.qsbVooDac.setProperty("value", 1)
        self.qsbVooDac.setObjectName(_fromUtf8("qsbVooDac"))
        self.gridLayout_2.addWidget(self.qsbVooDac, 1, 1, 1, 1)
        self.lblVooDummy_1 = QtGui.QLabel(self.gbxVoo)
        self.lblVooDummy_1.setText(_fromUtf8(""))
        self.lblVooDummy_1.setObjectName(_fromUtf8("lblVooDummy_1"))
        self.gridLayout_2.addWidget(self.lblVooDummy_1, 2, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.gbxVoo)
        self.verticalLayout.addWidget(self.frmGrp1)
        self.frmGrp2 = QtGui.QFrame(dlgPrfEditNEW)
        self.frmGrp2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmGrp2.setFrameShadow(QtGui.QFrame.Raised)
        self.frmGrp2.setObjectName(_fromUtf8("frmGrp2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frmGrp2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.gbxDep = QtGui.QGroupBox(self.frmGrp2)
        self.gbxDep.setObjectName(_fromUtf8("gbxDep"))
        self.gridLayout_7 = QtGui.QGridLayout(self.gbxDep)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.lblDepAccMin = QtGui.QLabel(self.gbxDep)
        self.lblDepAccMin.setObjectName(_fromUtf8("lblDepAccMin"))
        self.gridLayout_7.addWidget(self.lblDepAccMin, 0, 0, 1, 1)
        self.qsbDepAccMin = QtGui.QSpinBox(self.gbxDep)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbDepAccMin.sizePolicy().hasHeightForWidth())
        self.qsbDepAccMin.setSizePolicy(sizePolicy)
        self.qsbDepAccMin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbDepAccMin.setMaximum(800)
        self.qsbDepAccMin.setProperty("value", 5)
        self.qsbDepAccMin.setObjectName(_fromUtf8("qsbDepAccMin"))
        self.gridLayout_7.addWidget(self.qsbDepAccMin, 0, 1, 1, 1)
        self.lblDepVelMin = QtGui.QLabel(self.gbxDep)
        self.lblDepVelMin.setObjectName(_fromUtf8("lblDepVelMin"))
        self.gridLayout_7.addWidget(self.lblDepVelMin, 1, 0, 1, 1)
        self.qsbDepVelMin = QtGui.QSpinBox(self.gbxDep)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbDepVelMin.sizePolicy().hasHeightForWidth())
        self.qsbDepVelMin.setSizePolicy(sizePolicy)
        self.qsbDepVelMin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbDepVelMin.setMinimum(0)
        self.qsbDepVelMin.setMaximum(1000)
        self.qsbDepVelMin.setSingleStep(10)
        self.qsbDepVelMin.setProperty("value", 100)
        self.qsbDepVelMin.setObjectName(_fromUtf8("qsbDepVelMin"))
        self.gridLayout_7.addWidget(self.qsbDepVelMin, 1, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.gbxDep)
        self.gbxArr = QtGui.QGroupBox(self.frmGrp2)
        self.gbxArr.setObjectName(_fromUtf8("gbxArr"))
        self.gridLayout_8 = QtGui.QGridLayout(self.gbxArr)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.lblArrDacMax = QtGui.QLabel(self.gbxArr)
        self.lblArrDacMax.setObjectName(_fromUtf8("lblArrDacMax"))
        self.gridLayout_8.addWidget(self.lblArrDacMax, 0, 0, 1, 1)
        self.qsbArrDacMax = QtGui.QSpinBox(self.gbxArr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbArrDacMax.sizePolicy().hasHeightForWidth())
        self.qsbArrDacMax.setSizePolicy(sizePolicy)
        self.qsbArrDacMax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbArrDacMax.setMaximum(1200)
        self.qsbArrDacMax.setObjectName(_fromUtf8("qsbArrDacMax"))
        self.gridLayout_8.addWidget(self.qsbArrDacMax, 0, 1, 1, 1)
        self.lblArrVelMax = QtGui.QLabel(self.gbxArr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblArrVelMax.sizePolicy().hasHeightForWidth())
        self.lblArrVelMax.setSizePolicy(sizePolicy)
        self.lblArrVelMax.setObjectName(_fromUtf8("lblArrVelMax"))
        self.gridLayout_8.addWidget(self.lblArrVelMax, 1, 0, 1, 1)
        self.qsbArrVelMax = QtGui.QSpinBox(self.gbxArr)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbArrVelMax.sizePolicy().hasHeightForWidth())
        self.qsbArrVelMax.setSizePolicy(sizePolicy)
        self.qsbArrVelMax.setAlignment(QtCore.Qt.AlignRight)
        self.qsbArrVelMax.setMinimum(1)
        self.qsbArrVelMax.setMaximum(500)
        self.qsbArrVelMax.setSingleStep(1)
        self.qsbArrVelMax.setProperty("value", 2)
        self.qsbArrVelMax.setObjectName(_fromUtf8("qsbArrVelMax"))
        self.gridLayout_8.addWidget(self.qsbArrVelMax, 1, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.gbxArr)
        self.verticalLayout.addWidget(self.frmGrp2)
        self.frmGrp3 = QtGui.QFrame(dlgPrfEditNEW)
        self.frmGrp3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmGrp3.setFrameShadow(QtGui.QFrame.Raised)
        self.frmGrp3.setObjectName(_fromUtf8("frmGrp3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frmGrp3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.gbxSub = QtGui.QGroupBox(self.frmGrp3)
        self.gbxSub.setObjectName(_fromUtf8("gbxSub"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gbxSub)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lblSubVel = QtGui.QLabel(self.gbxSub)
        self.lblSubVel.setObjectName(_fromUtf8("lblSubVel"))
        self.gridLayout_5.addWidget(self.lblSubVel, 2, 0, 1, 1)
        self.qsbSubVel = QtGui.QSpinBox(self.gbxSub)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbSubVel.sizePolicy().hasHeightForWidth())
        self.qsbSubVel.setSizePolicy(sizePolicy)
        self.qsbSubVel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbSubVel.setMinimum(0)
        self.qsbSubVel.setMaximum(1000)
        self.qsbSubVel.setSingleStep(10)
        self.qsbSubVel.setProperty("value", 100)
        self.qsbSubVel.setObjectName(_fromUtf8("qsbSubVel"))
        self.gridLayout_5.addWidget(self.qsbSubVel, 2, 1, 1, 1)
        self.lblSubRaz = QtGui.QLabel(self.gbxSub)
        self.lblSubRaz.setObjectName(_fromUtf8("lblSubRaz"))
        self.gridLayout_5.addWidget(self.lblSubRaz, 3, 0, 1, 1)
        self.qsbSubRaz = QtGui.QSpinBox(self.gbxSub)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbSubRaz.sizePolicy().hasHeightForWidth())
        self.qsbSubRaz.setSizePolicy(sizePolicy)
        self.qsbSubRaz.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbSubRaz.setMaximum(10000)
        self.qsbSubRaz.setObjectName(_fromUtf8("qsbSubRaz"))
        self.gridLayout_5.addWidget(self.qsbSubRaz, 3, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.gbxSub)
        self.gbxDsc = QtGui.QGroupBox(self.frmGrp3)
        self.gbxDsc.setObjectName(_fromUtf8("gbxDsc"))
        self.gridLayout_6 = QtGui.QGridLayout(self.gbxDsc)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.qsbDscRazMax = QtGui.QSpinBox(self.gbxDsc)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbDscRazMax.sizePolicy().hasHeightForWidth())
        self.qsbDscRazMax.setSizePolicy(sizePolicy)
        self.qsbDscRazMax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbDscRazMax.setMaximum(10000)
        self.qsbDscRazMax.setObjectName(_fromUtf8("qsbDscRazMax"))
        self.gridLayout_6.addWidget(self.qsbDscRazMax, 3, 1, 1, 1)
        self.qsbDscRaz = QtGui.QSpinBox(self.gbxDsc)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbDscRaz.sizePolicy().hasHeightForWidth())
        self.qsbDscRaz.setSizePolicy(sizePolicy)
        self.qsbDscRaz.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbDscRaz.setMaximum(10000)
        self.qsbDscRaz.setObjectName(_fromUtf8("qsbDscRaz"))
        self.gridLayout_6.addWidget(self.qsbDscRaz, 4, 1, 1, 1)
        self.lblDscRaz = QtGui.QLabel(self.gbxDsc)
        self.lblDscRaz.setObjectName(_fromUtf8("lblDscRaz"))
        self.gridLayout_6.addWidget(self.lblDscRaz, 4, 0, 1, 1)
        self.lblDscRazMax = QtGui.QLabel(self.gbxDsc)
        self.lblDscRazMax.setObjectName(_fromUtf8("lblDscRazMax"))
        self.gridLayout_6.addWidget(self.lblDscRazMax, 3, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.gbxDsc)
        self.verticalLayout.addWidget(self.frmGrp3)
        self.frmGrp4 = QtGui.QFrame(dlgPrfEditNEW)
        self.frmGrp4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmGrp4.setFrameShadow(QtGui.QFrame.Raised)
        self.frmGrp4.setObjectName(_fromUtf8("frmGrp4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frmGrp4)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gbxCrvRaz = QtGui.QGroupBox(self.frmGrp4)
        self.gbxCrvRaz.setObjectName(_fromUtf8("gbxCrvRaz"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gbxCrvRaz)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lblCrvRazRta = QtGui.QLabel(self.gbxCrvRaz)
        self.lblCrvRazRta.setObjectName(_fromUtf8("lblCrvRazRta"))
        self.gridLayout_4.addWidget(self.lblCrvRazRta, 0, 0, 1, 1)
        self.lblCrvRazSlo = QtGui.QLabel(self.gbxCrvRaz)
        self.lblCrvRazSlo.setObjectName(_fromUtf8("lblCrvRazSlo"))
        self.gridLayout_4.addWidget(self.lblCrvRazSlo, 1, 0, 1, 1)
        self.lblCrvRazTrf = QtGui.QLabel(self.gbxCrvRaz)
        self.lblCrvRazTrf.setObjectName(_fromUtf8("lblCrvRazTrf"))
        self.gridLayout_4.addWidget(self.lblCrvRazTrf, 2, 0, 1, 1)
        self.qsbCrvRazRta = QtGui.QDoubleSpinBox(self.gbxCrvRaz)
        self.qsbCrvRazRta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbCrvRazRta.setDecimals(1)
        self.qsbCrvRazRta.setMaximum(99.0)
        self.qsbCrvRazRta.setObjectName(_fromUtf8("qsbCrvRazRta"))
        self.gridLayout_4.addWidget(self.qsbCrvRazRta, 0, 1, 1, 1)
        self.qsbCrvRazSlo = QtGui.QDoubleSpinBox(self.gbxCrvRaz)
        self.qsbCrvRazSlo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbCrvRazSlo.setDecimals(1)
        self.qsbCrvRazSlo.setMaximum(99.0)
        self.qsbCrvRazSlo.setObjectName(_fromUtf8("qsbCrvRazSlo"))
        self.gridLayout_4.addWidget(self.qsbCrvRazSlo, 1, 1, 1, 1)
        self.qsbCrvRazTrf = QtGui.QDoubleSpinBox(self.gbxCrvRaz)
        self.qsbCrvRazTrf.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbCrvRazTrf.setDecimals(1)
        self.qsbCrvRazTrf.setMaximum(99.0)
        self.qsbCrvRazTrf.setObjectName(_fromUtf8("qsbCrvRazTrf"))
        self.gridLayout_4.addWidget(self.qsbCrvRazTrf, 2, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.gbxCrvRaz)
        self.gbxCkt = QtGui.QGroupBox(self.frmGrp4)
        self.gbxCkt.setObjectName(_fromUtf8("gbxCkt"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gbxCkt)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lblCkt = QtGui.QLabel(self.gbxCkt)
        self.lblCkt.setObjectName(_fromUtf8("lblCkt"))
        self.gridLayout_3.addWidget(self.lblCkt, 0, 0, 1, 1)
        self.qsbCkt = QtGui.QSpinBox(self.gbxCkt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbCkt.sizePolicy().hasHeightForWidth())
        self.qsbCkt.setSizePolicy(sizePolicy)
        self.qsbCkt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbCkt.setObjectName(_fromUtf8("qsbCkt"))
        self.gridLayout_3.addWidget(self.qsbCkt, 0, 1, 1, 1)
        self.lblCktVel = QtGui.QLabel(self.gbxCkt)
        self.lblCktVel.setObjectName(_fromUtf8("lblCktVel"))
        self.gridLayout_3.addWidget(self.lblCktVel, 2, 0, 1, 1)
        self.qsbCktVel = QtGui.QSpinBox(self.gbxCkt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbCktVel.sizePolicy().hasHeightForWidth())
        self.qsbCktVel.setSizePolicy(sizePolicy)
        self.qsbCktVel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbCktVel.setMaximum(1000)
        self.qsbCktVel.setObjectName(_fromUtf8("qsbCktVel"))
        self.gridLayout_3.addWidget(self.qsbCktVel, 2, 1, 1, 1)
        self.lblCktAlt = QtGui.QLabel(self.gbxCkt)
        self.lblCktAlt.setObjectName(_fromUtf8("lblCktAlt"))
        self.gridLayout_3.addWidget(self.lblCktAlt, 1, 0, 1, 1)
        self.qsbCktAlt = QtGui.QSpinBox(self.gbxCkt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbCktAlt.sizePolicy().hasHeightForWidth())
        self.qsbCktAlt.setSizePolicy(sizePolicy)
        self.qsbCktAlt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbCktAlt.setMaximum(20000)
        self.qsbCktAlt.setObjectName(_fromUtf8("qsbCktAlt"))
        self.gridLayout_3.addWidget(self.qsbCktAlt, 1, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.gbxCkt)
        self.verticalLayout.addWidget(self.frmGrp4)
        self.bbxPrfEdit = QtGui.QWidget(dlgPrfEditNEW)
        self.bbxPrfEdit.setObjectName(_fromUtf8("bbxPrfEdit"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.bbxPrfEdit)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.btnCancel = QtGui.QPushButton(self.bbxPrfEdit)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_6.addWidget(self.btnCancel)
        self.btnOk = QtGui.QPushButton(self.bbxPrfEdit)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOk.setIcon(icon1)
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.horizontalLayout_6.addWidget(self.btnOk)
        self.verticalLayout.addWidget(self.bbxPrfEdit)
        self.lblTipo.setBuddy(self.qleTipo)
        self.lblDesc.setBuddy(self.qleDesc)
        self.lblMaxAlt.setBuddy(self.qsbMaxAlt)
        self.lblMaxVel.setBuddy(self.qsbMaxVel)
        self.lblMaxVelTax.setBuddy(self.qsbMaxVelTax)
        self.lblVooAcc.setBuddy(self.qsbVooAcc)
        self.lblVooDac.setBuddy(self.qsbVooDac)
        self.lblDepAccMin.setBuddy(self.qsbDepAccMin)
        self.lblDepVelMin.setBuddy(self.qsbDepVelMin)
        self.lblArrDacMax.setBuddy(self.qsbArrDacMax)
        self.lblArrVelMax.setBuddy(self.qsbArrVelMax)
        self.lblSubVel.setBuddy(self.qsbSubVel)
        self.lblSubRaz.setBuddy(self.qsbSubRaz)
        self.lblDscRaz.setBuddy(self.qsbDscRaz)
        self.lblDscRazMax.setBuddy(self.qsbDscRazMax)
        self.lblCkt.setBuddy(self.qsbCkt)
        self.lblCktVel.setBuddy(self.qsbCktVel)
        self.lblCktAlt.setBuddy(self.qsbCktAlt)

        self.retranslateUi(dlgPrfEditNEW)
        QtCore.QMetaObject.connectSlotsByName(dlgPrfEditNEW)

    def retranslateUi(self, dlgPrfEditNEW):
        dlgPrfEditNEW.setWindowTitle(_translate("dlgPrfEditNEW", "TrackS - Edição de Performances", None))
        self.lblTipo.setText(_translate("dlgPrfEditNEW", "&Sigla:", None))
        self.lblDesc.setText(_translate("dlgPrfEditNEW", "Descrição:", None))
        self.gbxMax.setTitle(_translate("dlgPrfEditNEW", "Performance", None))
        self.qsbMaxAlt.setSpecialValueText(_translate("dlgPrfEditNEW", "Unknown", None))
        self.qsbMaxAlt.setSuffix(_translate("dlgPrfEditNEW", " ft", None))
        self.lblMaxAlt.setText(_translate("dlgPrfEditNEW", "Altitude máxima:", None))
        self.lblMaxVel.setText(_translate("dlgPrfEditNEW", "Velocidade máxima:", None))
        self.qsbMaxVel.setSuffix(_translate("dlgPrfEditNEW", " kt", None))
        self.lblMaxVelTax.setText(_translate("dlgPrfEditNEW", "Velocidade máxima de taxi:", None))
        self.qsbMaxVelTax.setSuffix(_translate("dlgPrfEditNEW", " kt", None))
        self.gbxVoo.setTitle(_translate("dlgPrfEditNEW", "Vôo", None))
        self.lblVooAcc.setText(_translate("dlgPrfEditNEW", "Aceleração de vôo:", None))
        self.qsbVooAcc.setSuffix(_translate("dlgPrfEditNEW", " m", None))
        self.lblVooDac.setText(_translate("dlgPrfEditNEW", "Desaceleração de vôo:", None))
        self.qsbVooDac.setSuffix(_translate("dlgPrfEditNEW", " gr", None))
        self.gbxDep.setTitle(_translate("dlgPrfEditNEW", "Decolagem", None))
        self.lblDepAccMin.setText(_translate("dlgPrfEditNEW", "Aceleração mínima de decolagem:", None))
        self.lblDepVelMin.setText(_translate("dlgPrfEditNEW", "Velocidade mínima de decolagem:", None))
        self.qsbDepVelMin.setSuffix(_translate("dlgPrfEditNEW", " kt", None))
        self.gbxArr.setTitle(_translate("dlgPrfEditNEW", "Pouso", None))
        self.lblArrDacMax.setText(_translate("dlgPrfEditNEW", "Desaceleração máx. de pouso:", None))
        self.lblArrVelMax.setText(_translate("dlgPrfEditNEW", "Velocidade máxima de pouso:", None))
        self.qsbArrVelMax.setSpecialValueText(_translate("dlgPrfEditNEW", "Unknown", None))
        self.qsbArrVelMax.setSuffix(_translate("dlgPrfEditNEW", " kt", None))
        self.gbxSub.setTitle(_translate("dlgPrfEditNEW", "Subida", None))
        self.lblSubVel.setText(_translate("dlgPrfEditNEW", "Velocidade de subida:", None))
        self.qsbSubVel.setSuffix(_translate("dlgPrfEditNEW", " m", None))
        self.lblSubRaz.setText(_translate("dlgPrfEditNEW", "Razão de subida:", None))
        self.gbxDsc.setTitle(_translate("dlgPrfEditNEW", "Descida", None))
        self.lblDscRaz.setText(_translate("dlgPrfEditNEW", "Razão de descida:", None))
        self.lblDscRazMax.setText(_translate("dlgPrfEditNEW", "Razão máxima de descida:", None))
        self.gbxCrvRaz.setTitle(_translate("dlgPrfEditNEW", "Razão de curva", None))
        self.lblCrvRazRta.setText(_translate("dlgPrfEditNEW", "Razão de curva em rota:", None))
        self.lblCrvRazSlo.setText(_translate("dlgPrfEditNEW", "Razão de curva no solo:", None))
        self.lblCrvRazTrf.setText(_translate("dlgPrfEditNEW", "Razão de curva em tráfego:", None))
        self.gbxCkt.setTitle(_translate("dlgPrfEditNEW", "Circuito", None))
        self.lblCkt.setText(_translate("dlgPrfEditNEW", "Circuito:", None))
        self.lblCktVel.setText(_translate("dlgPrfEditNEW", "Velocidade de circuito:", None))
        self.qsbCktVel.setSuffix(_translate("dlgPrfEditNEW", " kt", None))
        self.lblCktAlt.setText(_translate("dlgPrfEditNEW", "Altitude de circuito:", None))
        self.qsbCktAlt.setSuffix(_translate("dlgPrfEditNEW", " ft", None))
        self.btnCancel.setText(_translate("dlgPrfEditNEW", "Cancela", None))
        self.btnOk.setText(_translate("dlgPrfEditNEW", "Ok", None))

import qrc_resources_rc
