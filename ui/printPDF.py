# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printPDF.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_printWindow(object):
    def setupUi(self, printWindow):
        printWindow.setObjectName("printWindow")
        printWindow.setWindowModality(QtCore.Qt.WindowModal)
        printWindow.resize(690, 163)
        printWindow.setWindowOpacity(1.0)
        printWindow.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(printWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.group_page = QtWidgets.QGroupBox(printWindow)
        self.group_page.setObjectName("group_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.group_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.group_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cmbPageSize = QtWidgets.QComboBox(self.group_page)
        self.cmbPageSize.setObjectName("cmbPageSize")
        self.cmbPageSize.addItem("")
        self.cmbPageSize.addItem("")
        self.cmbPageSize.addItem("")
        self.horizontalLayout.addWidget(self.cmbPageSize)
        self.label_2 = QtWidgets.QLabel(self.group_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spbLeftPadding = QtWidgets.QSpinBox(self.group_page)
        self.spbLeftPadding.setProperty("value", 20)
        self.spbLeftPadding.setObjectName("spbLeftPadding")
        self.horizontalLayout.addWidget(self.spbLeftPadding)
        self.label_3 = QtWidgets.QLabel(self.group_page)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.group_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.spbTopPadding = QtWidgets.QSpinBox(self.group_page)
        self.spbTopPadding.setProperty("value", 20)
        self.spbTopPadding.setObjectName("spbTopPadding")
        self.horizontalLayout.addWidget(self.spbTopPadding)
        self.label_5 = QtWidgets.QLabel(self.group_page)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.group_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.spbRightPadding = QtWidgets.QSpinBox(self.group_page)
        self.spbRightPadding.setProperty("value", 20)
        self.spbRightPadding.setObjectName("spbRightPadding")
        self.horizontalLayout.addWidget(self.spbRightPadding)
        self.label_8 = QtWidgets.QLabel(self.group_page)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.group_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.spbBottomPadding = QtWidgets.QSpinBox(self.group_page)
        self.spbBottomPadding.setProperty("value", 20)
        self.spbBottomPadding.setObjectName("spbBottomPadding")
        self.horizontalLayout.addWidget(self.spbBottomPadding)
        self.label_6 = QtWidgets.QLabel(self.group_page)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.group_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.spbColumns = QtWidgets.QSpinBox(self.group_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spbColumns.sizePolicy().hasHeightForWidth())
        self.spbColumns.setSizePolicy(sizePolicy)
        self.spbColumns.setMinimum(1)
        self.spbColumns.setMaximum(5)
        self.spbColumns.setProperty("value", 2)
        self.spbColumns.setObjectName("spbColumns")
        self.horizontalLayout_2.addWidget(self.spbColumns)
        self.label_16 = QtWidgets.QLabel(self.group_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.spbColMargin = QtWidgets.QSpinBox(self.group_page)
        self.spbColMargin.setProperty("value", 5)
        self.spbColMargin.setObjectName("spbColMargin")
        self.horizontalLayout_2.addWidget(self.spbColMargin)
        self.label_18 = QtWidgets.QLabel(self.group_page)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.group_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.lineHeight = QtWidgets.QSpinBox(self.group_page)
        self.lineHeight.setMinimum(1)
        self.lineHeight.setProperty("value", 10)
        self.lineHeight.setObjectName("lineHeight")
        self.horizontalLayout_2.addWidget(self.lineHeight)
        self.label_15 = QtWidgets.QLabel(self.group_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.d_page = QtWidgets.QCheckBox(self.group_page)
        self.d_page.setObjectName("d_page")
        self.horizontalLayout_2.addWidget(self.d_page)
        self.printPageNumber = QtWidgets.QCheckBox(self.group_page)
        self.printPageNumber.setChecked(True)
        self.printPageNumber.setObjectName("printPageNumber")
        self.horizontalLayout_2.addWidget(self.printPageNumber)
        self.createAnswer = QtWidgets.QCheckBox(self.group_page)
        self.createAnswer.setChecked(True)
        self.createAnswer.setObjectName("createAnswer")
        self.horizontalLayout_2.addWidget(self.createAnswer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.group_page)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btnCreate = QtWidgets.QPushButton(printWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCreate.sizePolicy().hasHeightForWidth())
        self.btnCreate.setSizePolicy(sizePolicy)
        self.btnCreate.setObjectName("btnCreate")
        self.horizontalLayout_4.addWidget(self.btnCreate)
        spacerItem1 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btnOpenPDF = QtWidgets.QPushButton(printWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenPDF.sizePolicy().hasHeightForWidth())
        self.btnOpenPDF.setSizePolicy(sizePolicy)
        self.btnOpenPDF.setObjectName("btnOpenPDF")
        self.horizontalLayout_4.addWidget(self.btnOpenPDF)
        spacerItem2 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btnClose = QtWidgets.QPushButton(printWindow)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_4.addWidget(self.btnClose)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label.setBuddy(self.cmbPageSize)
        self.label_2.setBuddy(self.spbLeftPadding)
        self.label_3.setBuddy(self.spbLeftPadding)
        self.label_4.setBuddy(self.spbTopPadding)
        self.label_5.setBuddy(self.spbTopPadding)
        self.label_9.setBuddy(self.spbRightPadding)
        self.label_8.setBuddy(self.spbRightPadding)
        self.label_7.setBuddy(self.spbBottomPadding)
        self.label_6.setBuddy(self.spbBottomPadding)
        self.label_12.setBuddy(self.spbColumns)
        self.label_16.setBuddy(self.spbColMargin)
        self.label_18.setBuddy(self.lineHeight)
        self.label_19.setBuddy(self.lineHeight)
        self.label_15.setBuddy(self.d_page)

        self.retranslateUi(printWindow)
        self.btnClose.clicked.connect(printWindow.close)
        QtCore.QMetaObject.connectSlotsByName(printWindow)

    def retranslateUi(self, printWindow):
        _translate = QtCore.QCoreApplication.translate
        printWindow.setWindowTitle(_translate("printWindow", "重新生成PDF文件"))
        self.group_page.setTitle(_translate("printWindow", "生成设置"))
        self.label.setText(_translate("printWindow", "纸型："))
        self.cmbPageSize.setItemText(0, _translate("printWindow", "A4"))
        self.cmbPageSize.setItemText(1, _translate("printWindow", "B5"))
        self.cmbPageSize.setItemText(2, _translate("printWindow", "A3"))
        self.label_2.setText(_translate("printWindow", "左边距："))
        self.label_3.setText(_translate("printWindow", "毫米"))
        self.label_4.setText(_translate("printWindow", "顶边距："))
        self.label_5.setText(_translate("printWindow", "毫米"))
        self.label_9.setText(_translate("printWindow", "右边距："))
        self.label_8.setText(_translate("printWindow", "毫米"))
        self.label_7.setText(_translate("printWindow", "底边距："))
        self.label_6.setText(_translate("printWindow", "毫米"))
        self.label_12.setText(_translate("printWindow", "列数："))
        self.label_16.setText(_translate("printWindow", "列间距："))
        self.label_18.setText(_translate("printWindow", "毫米"))
        self.label_19.setText(_translate("printWindow", "行高："))
        self.label_15.setText(_translate("printWindow", "毫米"))
        self.d_page.setText(_translate("printWindow", "双面"))
        self.printPageNumber.setText(_translate("printWindow", "打印页码"))
        self.createAnswer.setText(_translate("printWindow", "生成答案"))
        self.btnCreate.setText(_translate("printWindow", "生成PDF"))
        self.btnOpenPDF.setText(_translate("printWindow", "打开PDF"))
        self.btnClose.setText(_translate("printWindow", "关闭"))

