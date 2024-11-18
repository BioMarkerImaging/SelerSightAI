# ../UiAssets/aboutSection.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(325, 335)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pg_2_PlotParameteres_label = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pg_2_PlotParameteres_label.sizePolicy().hasHeightForWidth()
        )
        self.pg_2_PlotParameteres_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.pg_2_PlotParameteres_label.setFont(font)
        self.pg_2_PlotParameteres_label.setStyleSheet(
            "color: rgb(200,200,200);\n"
            "background-color: rgb(80, 80, 80);\n"
            "border-radius:10px;"
        )
        self.pg_2_PlotParameteres_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter
        )
        self.pg_2_PlotParameteres_label.setObjectName("pg_2_PlotParameteres_label")
        self.verticalLayout.addWidget(self.pg_2_PlotParameteres_label)
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setStyleSheet(
            "background-color:rgb(80, 80, 80);\n" "border-radius:10px;"
        )
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(160, 73))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setStyleSheet("color:rgb(215,215,215);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setStyleSheet("color:rgb(215,215,215);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setStyleSheet("color:rgb(215,215,215);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pg_2_PlotParameteres_label.setText(
            _translate("Form", "About Celer SIght AI")
        )
        self.label.setText(_translate("Form", "version"))
        self.label_2.setText(_translate("Form", "0.0.6"))
        self.label_3.setText(
            _translate("Form", "© 2021 Manos Chaniotakis All rights reserved")
        )
