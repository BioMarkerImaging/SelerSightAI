# ../celer_sight_ai/UiAssets/AutoImportInstractions.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(812, 518)
        Dialog.setMinimumSize(QtCore.QSize(812, 518))
        Dialog.setMaximumSize(QtCore.QSize(812, 518))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonSelectFolder = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButtonSelectFolder.sizePolicy().hasHeightForWidth()
        )
        self.pushButtonSelectFolder.setSizePolicy(sizePolicy)
        self.pushButtonSelectFolder.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonSelectFolder.setFont(font)
        self.pushButtonSelectFolder.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.pushButtonSelectFolder.setObjectName("pushButtonSelectFolder")
        self.gridLayout.addWidget(self.pushButtonSelectFolder, 2, 2, 1, 1)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 100))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelRemoveDuplicates = QtWidgets.QLabel(parent=self.frame)
        self.labelRemoveDuplicates.setObjectName("labelRemoveDuplicates")
        self.gridLayout_2.addWidget(self.labelRemoveDuplicates, 1, 0, 1, 1)
        self.checkBoxRemoveDuplicates = QtWidgets.QCheckBox(parent=self.frame)
        self.checkBoxRemoveDuplicates.setMinimumSize(QtCore.QSize(20, 0))
        self.checkBoxRemoveDuplicates.setMaximumSize(QtCore.QSize(20, 16777215))
        self.checkBoxRemoveDuplicates.setText("")
        self.checkBoxRemoveDuplicates.setChecked(True)
        self.checkBoxRemoveDuplicates.setObjectName("checkBoxRemoveDuplicates")
        self.gridLayout_2.addWidget(self.checkBoxRemoveDuplicates, 1, 1, 1, 1)
        self.OptionsLabel = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OptionsLabel.setFont(font)
        self.OptionsLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.OptionsLabel.setObjectName("OptionsLabel")
        self.gridLayout_2.addWidget(self.OptionsLabel, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 2)
        self.labelInstractions = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelInstractions.sizePolicy().hasHeightForWidth()
        )
        self.labelInstractions.setSizePolicy(sizePolicy)
        self.labelInstractions.setText("")
        self.labelInstractions.setObjectName("labelInstractions")
        self.gridLayout.addWidget(self.labelInstractions, 1, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonSelectFolder.setText(_translate("Dialog", "Select Folder"))
        self.labelRemoveDuplicates.setText(_translate("Dialog", "Remove duplicates"))
        self.OptionsLabel.setText(_translate("Dialog", "Options"))
