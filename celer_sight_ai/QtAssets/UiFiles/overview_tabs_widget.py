# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\manos\Documents\topfluov2\UiAssets\overview_tabs_widget.ui'
#
# Created by: PyQt6 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(276, 519)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.overview_tabs = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.overview_tabs.sizePolicy().hasHeightForWidth()
        )
        self.overview_tabs.setSizePolicy(sizePolicy)
        self.overview_tabs.setMinimumSize(QtCore.QSize(220, 108))
        self.overview_tabs.setMaximumSize(QtCore.QSize(16777215, 5000))
        self.overview_tabs.setObjectName("overview_tabs")
        self.overview_tabs_image = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.overview_tabs_image.sizePolicy().hasHeightForWidth()
        )
        self.overview_tabs_image.setSizePolicy(sizePolicy)
        self.overview_tabs_image.setObjectName("overview_tabs_image")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.overview_tabs_image)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.image_preview_scrollArea = QtWidgets.QScrollArea(self.overview_tabs_image)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.image_preview_scrollArea.sizePolicy().hasHeightForWidth()
        )
        self.image_preview_scrollArea.setSizePolicy(sizePolicy)
        self.image_preview_scrollArea.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.image_preview_scrollArea.setStyleSheet(
            "\n" "    border-color: rgb(255, 255, 255);\n" ""
        )
        self.image_preview_scrollArea.setWidgetResizable(True)
        self.image_preview_scrollArea.setObjectName("image_preview_scrollArea")
        self.image_preview_scrollArea_Contents = QtWidgets.QWidget()
        self.image_preview_scrollArea_Contents.setGeometry(QtCore.QRect(0, 0, 268, 491))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.image_preview_scrollArea_Contents.sizePolicy().hasHeightForWidth()
        )
        self.image_preview_scrollArea_Contents.setSizePolicy(sizePolicy)
        self.image_preview_scrollArea_Contents.setObjectName(
            "image_preview_scrollArea_Contents"
        )
        self.image_preview_scrollArea.setWidget(self.image_preview_scrollArea_Contents)
        self.verticalLayout_4.addWidget(self.image_preview_scrollArea)
        self.overview_tabs.addTab(self.overview_tabs_image, "")
        self.overview_tabs_mask = QtWidgets.QWidget()
        self.overview_tabs_mask.setObjectName("overview_tabs_mask")
        self.gridLayout = QtWidgets.QGridLayout(self.overview_tabs_mask)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.mask_preview_scrollArea = QtWidgets.QScrollArea(self.overview_tabs_mask)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mask_preview_scrollArea.sizePolicy().hasHeightForWidth()
        )
        self.mask_preview_scrollArea.setSizePolicy(sizePolicy)
        self.mask_preview_scrollArea.setWidgetResizable(True)
        self.mask_preview_scrollArea.setObjectName("mask_preview_scrollArea")
        self.MaskScrollAreaWidgetContents = QtWidgets.QWidget()
        self.MaskScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 268, 435))
        self.MaskScrollAreaWidgetContents.setObjectName("MaskScrollAreaWidgetContents")
        self.mask_preview_scrollArea.setWidget(self.MaskScrollAreaWidgetContents)
        self.gridLayout.addWidget(self.mask_preview_scrollArea, 1, 0, 1, 1)
        self.MaskLabelAreaAddRemove = QtWidgets.QFrame(self.overview_tabs_mask)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MaskLabelAreaAddRemove.sizePolicy().hasHeightForWidth()
        )
        self.MaskLabelAreaAddRemove.setSizePolicy(sizePolicy)
        self.MaskLabelAreaAddRemove.setMaximumSize(QtCore.QSize(16777215, 50))
        self.MaskLabelAreaAddRemove.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.MaskLabelAreaAddRemove.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.MaskLabelAreaAddRemove.setObjectName("MaskLabelAreaAddRemove")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.MaskLabelAreaAddRemove)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MaskLabelAddToCombobox = QtWidgets.QPushButton(self.MaskLabelAreaAddRemove)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MaskLabelAddToCombobox.sizePolicy().hasHeightForWidth()
        )
        self.MaskLabelAddToCombobox.setSizePolicy(sizePolicy)
        self.MaskLabelAddToCombobox.setMaximumSize(QtCore.QSize(25, 25))
        self.MaskLabelAddToCombobox.setObjectName("MaskLabelAddToCombobox")
        self.horizontalLayout_2.addWidget(self.MaskLabelAddToCombobox)
        self.MaskLabelRemoveFromCombobox = QtWidgets.QPushButton(
            self.MaskLabelAreaAddRemove
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MaskLabelRemoveFromCombobox.sizePolicy().hasHeightForWidth()
        )
        self.MaskLabelRemoveFromCombobox.setSizePolicy(sizePolicy)
        self.MaskLabelRemoveFromCombobox.setMaximumSize(QtCore.QSize(25, 25))
        self.MaskLabelRemoveFromCombobox.setObjectName("MaskLabelRemoveFromCombobox")
        self.horizontalLayout_2.addWidget(self.MaskLabelRemoveFromCombobox)
        self.MasterMaskLabelcomboBox = QtWidgets.QComboBox(self.MaskLabelAreaAddRemove)
        self.MasterMaskLabelcomboBox.setEditable(True)
        self.MasterMaskLabelcomboBox.setInsertPolicy(
            QtWidgets.QComboBox.InsertPolicy.InsertAtTop
        )
        self.MasterMaskLabelcomboBox.setObjectName("MasterMaskLabelcomboBox")
        self.horizontalLayout_2.addWidget(self.MasterMaskLabelcomboBox)
        self.PerAnnotationTypeColorButton = QtWidgets.QPushButton(
            self.MaskLabelAreaAddRemove
        )
        self.PerAnnotationTypeColorButton.setMaximumSize(QtCore.QSize(50, 50))
        self.PerAnnotationTypeColorButton.setText("")
        self.PerAnnotationTypeColorButton.setObjectName("PerAnnotationTypeColorButton")
        self.horizontalLayout_2.addWidget(self.PerAnnotationTypeColorButton)
        self.gridLayout.addWidget(self.MaskLabelAreaAddRemove, 0, 0, 1, 1)
        self.overview_tabs.addTab(self.overview_tabs_mask, "")
        self.horizontalLayout.addWidget(self.overview_tabs)

        self.retranslateUi(Form)
        self.overview_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.overview_tabs.setTabText(
            self.overview_tabs.indexOf(self.overview_tabs_image),
            _translate("Form", "Images"),
        )
        self.MaskLabelAddToCombobox.setText(_translate("Form", "+"))
        self.MaskLabelRemoveFromCombobox.setText(_translate("Form", "-"))
        self.overview_tabs.setTabText(
            self.overview_tabs.indexOf(self.overview_tabs_mask),
            _translate("Form", "Masks"),
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
