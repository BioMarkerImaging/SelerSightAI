# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\backup_work_old - Copy\stripplot_settings_wdiget.ui'
#
# Created by: PyQt6 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets


class strip_plot_settings_form(object):
    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(328, 471)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pg_2_stripplot_plot_settings_1 = QtWidgets.QFrame(Form)
        self.pg_2_stripplot_plot_settings_1.setObjectName(
            "pg_2_stripplot_plot_settings_1"
        )
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(
            self.pg_2_stripplot_plot_settings_1
        )
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pg_2_stripplot_plot_settings_1_left = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1
        )
        self.pg_2_stripplot_plot_settings_1_left.setObjectName(
            "pg_2_stripplot_plot_settings_1_left"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.pg_2_stripplot_plot_settings_1_left
        )
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pg_2_color_graph_frame_stripplot_plot = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1_left
        )
        self.pg_2_color_graph_frame_stripplot_plot.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel
        )
        self.pg_2_color_graph_frame_stripplot_plot.setFrameShadow(
            QtWidgets.QFrame.Shadow.Raised
        )
        self.pg_2_color_graph_frame_stripplot_plot.setObjectName(
            "pg_2_color_graph_frame_stripplot_plot"
        )
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.pg_2_color_graph_frame_stripplot_plot
        )
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pg2_graph_color_stripplot_plot = QtWidgets.QLabel(
            self.pg_2_color_graph_frame_stripplot_plot
        )
        self.pg2_graph_color_stripplot_plot.setMinimumSize(QtCore.QSize(0, 20))
        self.pg2_graph_color_stripplot_plot.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pg2_graph_color_stripplot_plot.setFont(font)
        self.pg2_graph_color_stripplot_plot.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.pg2_graph_color_stripplot_plot.setObjectName(
            "pg2_graph_color_stripplot_plot"
        )
        self.horizontalLayout_2.addWidget(self.pg2_graph_color_stripplot_plot)
        self.pg_2_graph_colors_pallete_2_stripplot_plot = QtWidgets.QPushButton(
            self.pg_2_color_graph_frame_stripplot_plot
        )
        self.pg_2_graph_colors_pallete_2_stripplot_plot.setMaximumSize(
            QtCore.QSize(60, 16777215)
        )
        self.pg_2_graph_colors_pallete_2_stripplot_plot.setObjectName(
            "pg_2_graph_colors_pallete_2_stripplot_plot"
        )
        self.horizontalLayout_2.addWidget(
            self.pg_2_graph_colors_pallete_2_stripplot_plot
        )
        self.verticalLayout.addWidget(self.pg_2_color_graph_frame_stripplot_plot)
        self.pg_2_graph_border_color_frame_stripplot_plot = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1_left
        )
        self.pg_2_graph_border_color_frame_stripplot_plot.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel
        )
        self.pg_2_graph_border_color_frame_stripplot_plot.setFrameShadow(
            QtWidgets.QFrame.Shadow.Raised
        )
        self.pg_2_graph_border_color_frame_stripplot_plot.setObjectName(
            "pg_2_graph_border_color_frame_stripplot_plot"
        )
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.pg_2_graph_border_color_frame_stripplot_plot
        )
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pg2_graph_border_color_stripplot_plot = QtWidgets.QLabel(
            self.pg_2_graph_border_color_frame_stripplot_plot
        )
        self.pg2_graph_border_color_stripplot_plot.setMinimumSize(QtCore.QSize(0, 20))
        self.pg2_graph_border_color_stripplot_plot.setMaximumSize(
            QtCore.QSize(16777215, 10)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pg2_graph_border_color_stripplot_plot.setFont(font)
        self.pg2_graph_border_color_stripplot_plot.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignTop
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.pg2_graph_border_color_stripplot_plot.setObjectName(
            "pg2_graph_border_color_stripplot_plot"
        )
        self.horizontalLayout.addWidget(self.pg2_graph_border_color_stripplot_plot)
        self.pg_2_graph_border_colors_pallete_1_stripplot_plot = QtWidgets.QPushButton(
            self.pg_2_graph_border_color_frame_stripplot_plot
        )
        self.pg_2_graph_border_colors_pallete_1_stripplot_plot.setMinimumSize(
            QtCore.QSize(60, 0)
        )
        self.pg_2_graph_border_colors_pallete_1_stripplot_plot.setMaximumSize(
            QtCore.QSize(60, 16777215)
        )
        self.pg_2_graph_border_colors_pallete_1_stripplot_plot.setObjectName(
            "pg_2_graph_border_colors_pallete_1_stripplot_plot"
        )
        self.horizontalLayout.addWidget(
            self.pg_2_graph_border_colors_pallete_1_stripplot_plot
        )
        self.verticalLayout.addWidget(self.pg_2_graph_border_color_frame_stripplot_plot)
        self.pg2_graph_border_width_frame_stripplot_plot = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1_left
        )
        self.pg2_graph_border_width_frame_stripplot_plot.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel
        )
        self.pg2_graph_border_width_frame_stripplot_plot.setFrameShadow(
            QtWidgets.QFrame.Shadow.Raised
        )
        self.pg2_graph_border_width_frame_stripplot_plot.setObjectName(
            "pg2_graph_border_width_frame_stripplot_plot"
        )
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
            self.pg2_graph_border_width_frame_stripplot_plot
        )
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pg2_graph_border_width_label_stripplot_plot = QtWidgets.QLabel(
            self.pg2_graph_border_width_frame_stripplot_plot
        )
        self.pg2_graph_border_width_label_stripplot_plot.setMinimumSize(
            QtCore.QSize(0, 20)
        )
        self.pg2_graph_border_width_label_stripplot_plot.setMaximumSize(
            QtCore.QSize(16777215, 10)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pg2_graph_border_width_label_stripplot_plot.setFont(font)
        self.pg2_graph_border_width_label_stripplot_plot.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignTop
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.pg2_graph_border_width_label_stripplot_plot.setObjectName(
            "pg2_graph_border_width_label_stripplot_plot"
        )
        self.horizontalLayout_4.addWidget(
            self.pg2_graph_border_width_label_stripplot_plot
        )
        self.pg2_graph_border_width_spinBox_stripplot_plot = QtWidgets.QSpinBox(
            self.pg2_graph_border_width_frame_stripplot_plot
        )
        self.pg2_graph_border_width_spinBox_stripplot_plot.setMaximumSize(
            QtCore.QSize(65, 16777215)
        )
        self.pg2_graph_border_width_spinBox_stripplot_plot.setMinimum(0)
        self.pg2_graph_border_width_spinBox_stripplot_plot.setMaximum(100)
        self.pg2_graph_border_width_spinBox_stripplot_plot.setProperty("value", 100)
        self.pg2_graph_border_width_spinBox_stripplot_plot.setObjectName(
            "pg2_graph_border_width_spinBox_stripplot_plot"
        )
        self.horizontalLayout_4.addWidget(
            self.pg2_graph_border_width_spinBox_stripplot_plot
        )
        self.verticalLayout.addWidget(self.pg2_graph_border_width_frame_stripplot_plot)
        self.pg2_graph_pallete_colors_frame_stripplot = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1_left
        )
        self.pg2_graph_pallete_colors_frame_stripplot.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel
        )
        self.pg2_graph_pallete_colors_frame_stripplot.setFrameShadow(
            QtWidgets.QFrame.Shadow.Raised
        )
        self.pg2_graph_pallete_colors_frame_stripplot.setObjectName(
            "pg2_graph_pallete_colors_frame_stripplot"
        )
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(
            self.pg2_graph_pallete_colors_frame_stripplot
        )
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pg2_graph_Pallete_colors_label_stripplot = QtWidgets.QLabel(
            self.pg2_graph_pallete_colors_frame_stripplot
        )
        self.pg2_graph_Pallete_colors_label_stripplot.setMinimumSize(
            QtCore.QSize(0, 20)
        )
        self.pg2_graph_Pallete_colors_label_stripplot.setMaximumSize(
            QtCore.QSize(16777215, 10)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pg2_graph_Pallete_colors_label_stripplot.setFont(font)
        self.pg2_graph_Pallete_colors_label_stripplot.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignTop
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.pg2_graph_Pallete_colors_label_stripplot.setObjectName(
            "pg2_graph_Pallete_colors_label_stripplot"
        )
        self.horizontalLayout_12.addWidget(
            self.pg2_graph_Pallete_colors_label_stripplot
        )
        self.pg2_graph_Pallete_colors_spinbox_stripplot = QtWidgets.QSpinBox(
            self.pg2_graph_pallete_colors_frame_stripplot
        )
        self.pg2_graph_Pallete_colors_spinbox_stripplot.setMaximumSize(
            QtCore.QSize(65, 16777215)
        )
        self.pg2_graph_Pallete_colors_spinbox_stripplot.setMinimum(0)
        self.pg2_graph_Pallete_colors_spinbox_stripplot.setMaximum(100)
        self.pg2_graph_Pallete_colors_spinbox_stripplot.setProperty("value", 100)
        self.pg2_graph_Pallete_colors_spinbox_stripplot.setObjectName(
            "pg2_graph_Pallete_colors_spinbox_stripplot"
        )
        self.horizontalLayout_12.addWidget(
            self.pg2_graph_Pallete_colors_spinbox_stripplot
        )
        self.verticalLayout.addWidget(self.pg2_graph_pallete_colors_frame_stripplot)
        self.pg2_graph_stripplot_pallete_style_frame = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1_left
        )
        self.pg2_graph_stripplot_pallete_style_frame.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel
        )
        self.pg2_graph_stripplot_pallete_style_frame.setFrameShadow(
            QtWidgets.QFrame.Shadow.Raised
        )
        self.pg2_graph_stripplot_pallete_style_frame.setObjectName(
            "pg2_graph_stripplot_pallete_style_frame"
        )
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(
            self.pg2_graph_stripplot_pallete_style_frame
        )
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pg2_graph_pallete_style_label_stripplot = QtWidgets.QLabel(
            self.pg2_graph_stripplot_pallete_style_frame
        )
        self.pg2_graph_pallete_style_label_stripplot.setMinimumSize(QtCore.QSize(0, 20))
        self.pg2_graph_pallete_style_label_stripplot.setMaximumSize(
            QtCore.QSize(16777215, 10)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pg2_graph_pallete_style_label_stripplot.setFont(font)
        self.pg2_graph_pallete_style_label_stripplot.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignTop
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.pg2_graph_pallete_style_label_stripplot.setObjectName(
            "pg2_graph_pallete_style_label_stripplot"
        )
        self.horizontalLayout_11.addWidget(self.pg2_graph_pallete_style_label_stripplot)
        self.pg_2_graph_stripplot_pallete_style_combobox = QtWidgets.QComboBox(
            self.pg2_graph_stripplot_pallete_style_frame
        )
        self.pg_2_graph_stripplot_pallete_style_combobox.setObjectName(
            "pg_2_graph_stripplot_pallete_style_combobox"
        )
        self.pg_2_graph_stripplot_pallete_style_combobox.addItem("")
        self.pg_2_graph_stripplot_pallete_style_combobox.addItem("")
        self.pg_2_graph_stripplot_pallete_style_combobox.addItem("")
        self.pg_2_graph_stripplot_pallete_style_combobox.addItem("")
        self.pg_2_graph_stripplot_pallete_style_combobox.addItem("")
        self.pg_2_graph_stripplot_pallete_style_combobox.addItem("")
        self.pg_2_graph_stripplot_pallete_style_combobox.addItem("")
        self.horizontalLayout_11.addWidget(
            self.pg_2_graph_stripplot_pallete_style_combobox
        )
        self.verticalLayout.addWidget(self.pg2_graph_stripplot_pallete_style_frame)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_7.addWidget(self.pg_2_stripplot_plot_settings_1_left)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_7.addItem(spacerItem1)
        self.pg_2_stripplot_plot_settings_1_right_stripplot_plot = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1
        )
        self.pg_2_stripplot_plot_settings_1_right_stripplot_plot.setObjectName(
            "pg_2_stripplot_plot_settings_1_right_stripplot_plot"
        )
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.pg_2_stripplot_plot_settings_1_right_stripplot_plot
        )
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pg2_graph_size_frame_stripplot_plot = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1_right_stripplot_plot
        )
        self.pg2_graph_size_frame_stripplot_plot.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel
        )
        self.pg2_graph_size_frame_stripplot_plot.setFrameShadow(
            QtWidgets.QFrame.Shadow.Raised
        )
        self.pg2_graph_size_frame_stripplot_plot.setObjectName(
            "pg2_graph_size_frame_stripplot_plot"
        )
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(
            self.pg2_graph_size_frame_stripplot_plot
        )
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pg2_graph_size_label_stripplot_plot = QtWidgets.QLabel(
            self.pg2_graph_size_frame_stripplot_plot
        )
        self.pg2_graph_size_label_stripplot_plot.setMinimumSize(QtCore.QSize(0, 20))
        self.pg2_graph_size_label_stripplot_plot.setMaximumSize(
            QtCore.QSize(16777215, 10)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pg2_graph_size_label_stripplot_plot.setFont(font)
        self.pg2_graph_size_label_stripplot_plot.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignTop
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.pg2_graph_size_label_stripplot_plot.setObjectName(
            "pg2_graph_size_label_stripplot_plot"
        )
        self.horizontalLayout_6.addWidget(self.pg2_graph_size_label_stripplot_plot)
        self.pg2_graph_size_spinBox_stripplot_plot = QtWidgets.QSpinBox(
            self.pg2_graph_size_frame_stripplot_plot
        )
        self.pg2_graph_size_spinBox_stripplot_plot.setMaximumSize(
            QtCore.QSize(65, 16777215)
        )
        self.pg2_graph_size_spinBox_stripplot_plot.setMinimum(0)
        self.pg2_graph_size_spinBox_stripplot_plot.setMaximum(100)
        self.pg2_graph_size_spinBox_stripplot_plot.setProperty("value", 100)
        self.pg2_graph_size_spinBox_stripplot_plot.setObjectName(
            "pg2_graph_size_spinBox_stripplot_plot"
        )
        self.horizontalLayout_6.addWidget(self.pg2_graph_size_spinBox_stripplot_plot)
        self.verticalLayout_2.addWidget(self.pg2_graph_size_frame_stripplot_plot)
        self.pg2_graph_saturation_frame_stripplot_plot = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1_right_stripplot_plot
        )
        self.pg2_graph_saturation_frame_stripplot_plot.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel
        )
        self.pg2_graph_saturation_frame_stripplot_plot.setFrameShadow(
            QtWidgets.QFrame.Shadow.Raised
        )
        self.pg2_graph_saturation_frame_stripplot_plot.setObjectName(
            "pg2_graph_saturation_frame_stripplot_plot"
        )
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(
            self.pg2_graph_saturation_frame_stripplot_plot
        )
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pg2_graph_saturation_label_stripplot_plot = QtWidgets.QLabel(
            self.pg2_graph_saturation_frame_stripplot_plot
        )
        self.pg2_graph_saturation_label_stripplot_plot.setMinimumSize(
            QtCore.QSize(0, 20)
        )
        self.pg2_graph_saturation_label_stripplot_plot.setMaximumSize(
            QtCore.QSize(16777215, 10)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pg2_graph_saturation_label_stripplot_plot.setFont(font)
        self.pg2_graph_saturation_label_stripplot_plot.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignTop
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.pg2_graph_saturation_label_stripplot_plot.setObjectName(
            "pg2_graph_saturation_label_stripplot_plot"
        )
        self.horizontalLayout_5.addWidget(
            self.pg2_graph_saturation_label_stripplot_plot
        )
        self.pg2_graph_saturation_spinBox_stripplot_plot = QtWidgets.QSpinBox(
            self.pg2_graph_saturation_frame_stripplot_plot
        )
        self.pg2_graph_saturation_spinBox_stripplot_plot.setMaximumSize(
            QtCore.QSize(65, 16777215)
        )
        self.pg2_graph_saturation_spinBox_stripplot_plot.setMinimum(0)
        self.pg2_graph_saturation_spinBox_stripplot_plot.setMaximum(100)
        self.pg2_graph_saturation_spinBox_stripplot_plot.setProperty("value", 100)
        self.pg2_graph_saturation_spinBox_stripplot_plot.setObjectName(
            "pg2_graph_saturation_spinBox_stripplot_plot"
        )
        self.horizontalLayout_5.addWidget(
            self.pg2_graph_saturation_spinBox_stripplot_plot
        )
        self.verticalLayout_2.addWidget(self.pg2_graph_saturation_frame_stripplot_plot)
        self.pg2_graph_stripplot_jitter_frame = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1_right_stripplot_plot
        )
        self.pg2_graph_stripplot_jitter_frame.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel
        )
        self.pg2_graph_stripplot_jitter_frame.setFrameShadow(
            QtWidgets.QFrame.Shadow.Raised
        )
        self.pg2_graph_stripplot_jitter_frame.setObjectName(
            "pg2_graph_stripplot_jitter_frame"
        )
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
            self.pg2_graph_stripplot_jitter_frame
        )
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pg2_graph_jitter_label_stripplot_plot = QtWidgets.QLabel(
            self.pg2_graph_stripplot_jitter_frame
        )
        self.pg2_graph_jitter_label_stripplot_plot.setMinimumSize(QtCore.QSize(0, 20))
        self.pg2_graph_jitter_label_stripplot_plot.setMaximumSize(
            QtCore.QSize(16777215, 10)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pg2_graph_jitter_label_stripplot_plot.setFont(font)
        self.pg2_graph_jitter_label_stripplot_plot.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignTop
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.pg2_graph_jitter_label_stripplot_plot.setObjectName(
            "pg2_graph_jitter_label_stripplot_plot"
        )
        self.horizontalLayout_3.addWidget(self.pg2_graph_jitter_label_stripplot_plot)
        self.pg2_graph_stripplot_jitter_checkBox_stripplot = QtWidgets.QCheckBox(
            self.pg2_graph_stripplot_jitter_frame
        )
        self.pg2_graph_stripplot_jitter_checkBox_stripplot.setText("")
        self.pg2_graph_stripplot_jitter_checkBox_stripplot.setObjectName(
            "pg2_graph_stripplot_jitter_checkBox_stripplot"
        )
        self.horizontalLayout_3.addWidget(
            self.pg2_graph_stripplot_jitter_checkBox_stripplot
        )
        self.verticalLayout_2.addWidget(self.pg2_graph_stripplot_jitter_frame)
        self.pg_2_custom_color_graph_frame_stripplot = QtWidgets.QFrame(
            self.pg_2_stripplot_plot_settings_1_right_stripplot_plot
        )
        self.pg_2_custom_color_graph_frame_stripplot.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel
        )
        self.pg_2_custom_color_graph_frame_stripplot.setFrameShadow(
            QtWidgets.QFrame.Shadow.Raised
        )
        self.pg_2_custom_color_graph_frame_stripplot.setObjectName(
            "pg_2_custom_color_graph_frame_stripplot"
        )
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(
            self.pg_2_custom_color_graph_frame_stripplot
        )
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pg2_graph_color_stripplot = QtWidgets.QLabel(
            self.pg_2_custom_color_graph_frame_stripplot
        )
        self.pg2_graph_color_stripplot.setMinimumSize(QtCore.QSize(0, 20))
        self.pg2_graph_color_stripplot.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pg2_graph_color_stripplot.setFont(font)
        self.pg2_graph_color_stripplot.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignTop
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.pg2_graph_color_stripplot.setObjectName("pg2_graph_color_stripplot")
        self.horizontalLayout_9.addWidget(self.pg2_graph_color_stripplot)
        self.pg_2_graph_colors_pallete_2_stripplot = QtWidgets.QPushButton(
            self.pg_2_custom_color_graph_frame_stripplot
        )
        self.pg_2_graph_colors_pallete_2_stripplot.setMaximumSize(
            QtCore.QSize(60, 16777215)
        )
        self.pg_2_graph_colors_pallete_2_stripplot.setObjectName(
            "pg_2_graph_colors_pallete_2_stripplot"
        )
        self.horizontalLayout_9.addWidget(self.pg_2_graph_colors_pallete_2_stripplot)
        self.verticalLayout_2.addWidget(self.pg_2_custom_color_graph_frame_stripplot)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_7.addWidget(
            self.pg_2_stripplot_plot_settings_1_right_stripplot_plot
        )
        self.horizontalLayout_8.addWidget(self.pg_2_stripplot_plot_settings_1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pg2_graph_color_stripplot_plot.setText(_translate("Form", "Color"))
        self.pg_2_graph_colors_pallete_2_stripplot_plot.setText(
            _translate("Form", "Pallet")
        )
        self.pg2_graph_border_color_stripplot_plot.setText(
            _translate("Form", "Border Color")
        )
        self.pg_2_graph_border_colors_pallete_1_stripplot_plot.setText(
            _translate("Form", "Pallet")
        )
        self.pg2_graph_border_width_label_stripplot_plot.setText(
            _translate("Form", "Border width")
        )
        self.pg2_graph_Pallete_colors_label_stripplot.setText(
            _translate("Form", "Pallete Colors")
        )
        self.pg2_graph_pallete_style_label_stripplot.setText(
            _translate("Form", "Palette Style")
        )
        self.pg_2_graph_stripplot_pallete_style_combobox.setItemText(
            0, _translate("Form", "Custom")
        )
        self.pg_2_graph_stripplot_pallete_style_combobox.setItemText(
            1, _translate("Form", "muted")
        )
        self.pg_2_graph_stripplot_pallete_style_combobox.setItemText(
            2, _translate("Form", "New Item")
        )
        self.pg_2_graph_stripplot_pallete_style_combobox.setItemText(
            3, _translate("Form", "RdBu")
        )
        self.pg_2_graph_stripplot_pallete_style_combobox.setItemText(
            4, _translate("Form", "Set1")
        )
        self.pg_2_graph_stripplot_pallete_style_combobox.setItemText(
            5, _translate("Form", "Blues_d")
        )
        self.pg_2_graph_stripplot_pallete_style_combobox.setItemText(
            6, _translate("Form", "husl")
        )
        self.pg2_graph_size_label_stripplot_plot.setText(_translate("Form", "Size"))
        self.pg2_graph_saturation_label_stripplot_plot.setText(
            _translate("Form", "Saturation")
        )
        self.pg2_graph_jitter_label_stripplot_plot.setText(_translate("Form", "Jitter"))
        self.pg2_graph_color_stripplot.setText(_translate("Form", "Color"))
        self.pg_2_graph_colors_pallete_2_stripplot.setText(_translate("Form", "Pallet"))


if __name__ == "__main__":
    pass
