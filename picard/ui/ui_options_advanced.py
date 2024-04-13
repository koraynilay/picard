# Form implementation generated from reading ui file 'ui/options_advanced.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdvancedOptionsPage(object):
    def setupUi(self, AdvancedOptionsPage):
        AdvancedOptionsPage.setObjectName("AdvancedOptionsPage")
        AdvancedOptionsPage.resize(570, 455)
        self.vboxlayout = QtWidgets.QVBoxLayout(AdvancedOptionsPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtWidgets.QGroupBox(parent=AdvancedOptionsPage)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout.setSpacing(2)
        self.gridlayout.setObjectName("gridlayout")
        self.label_ignore_regex = QtWidgets.QLabel(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ignore_regex.sizePolicy().hasHeightForWidth())
        self.label_ignore_regex.setSizePolicy(sizePolicy)
        self.label_ignore_regex.setWordWrap(True)
        self.label_ignore_regex.setObjectName("label_ignore_regex")
        self.gridlayout.addWidget(self.label_ignore_regex, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_query_limit = QtWidgets.QLabel(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_query_limit.sizePolicy().hasHeightForWidth())
        self.label_query_limit.setSizePolicy(sizePolicy)
        self.label_query_limit.setObjectName("label_query_limit")
        self.horizontalLayout_2.addWidget(self.label_query_limit)
        self.query_limit = QtWidgets.QComboBox(parent=self.groupBox)
        self.query_limit.setCurrentText("50")
        self.query_limit.setObjectName("query_limit")
        self.query_limit.addItem("")
        self.query_limit.setItemText(0, "25")
        self.query_limit.addItem("")
        self.query_limit.setItemText(1, "50")
        self.query_limit.addItem("")
        self.query_limit.setItemText(2, "75")
        self.query_limit.addItem("")
        self.query_limit.setItemText(3, "100")
        self.horizontalLayout_2.addWidget(self.query_limit)
        self.gridlayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)
        self.regex_error = QtWidgets.QLabel(parent=self.groupBox)
        self.regex_error.setText("")
        self.regex_error.setObjectName("regex_error")
        self.gridlayout.addWidget(self.regex_error, 3, 0, 1, 1)
        self.ignore_regex = QtWidgets.QLineEdit(parent=self.groupBox)
        self.ignore_regex.setObjectName("ignore_regex")
        self.gridlayout.addWidget(self.ignore_regex, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_track_duration_diff = QtWidgets.QLabel(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_track_duration_diff.sizePolicy().hasHeightForWidth())
        self.label_track_duration_diff.setSizePolicy(sizePolicy)
        self.label_track_duration_diff.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_track_duration_diff.setObjectName("label_track_duration_diff")
        self.horizontalLayout.addWidget(self.label_track_duration_diff)
        self.ignore_track_duration_difference_under = QtWidgets.QSpinBox(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_track_duration_difference_under.sizePolicy().hasHeightForWidth())
        self.ignore_track_duration_difference_under.setSizePolicy(sizePolicy)
        self.ignore_track_duration_difference_under.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.ignore_track_duration_difference_under.setAccelerated(True)
        self.ignore_track_duration_difference_under.setSuffix("")
        self.ignore_track_duration_difference_under.setMinimum(1)
        self.ignore_track_duration_difference_under.setMaximum(7200)
        self.ignore_track_duration_difference_under.setProperty("value", 2)
        self.ignore_track_duration_difference_under.setObjectName("ignore_track_duration_difference_under")
        self.horizontalLayout.addWidget(self.ignore_track_duration_difference_under)
        self.gridlayout.addLayout(self.horizontalLayout, 6, 0, 2, 1)
        self.recursively_add_files = QtWidgets.QCheckBox(parent=self.groupBox)
        self.recursively_add_files.setObjectName("recursively_add_files")
        self.gridlayout.addWidget(self.recursively_add_files, 5, 0, 1, 1)
        self.ignore_hidden_files = QtWidgets.QCheckBox(parent=self.groupBox)
        self.ignore_hidden_files.setObjectName("ignore_hidden_files")
        self.gridlayout.addWidget(self.ignore_hidden_files, 4, 0, 1, 1)
        self.vboxlayout.addWidget(self.groupBox)
        self.groupBox_completeness = QtWidgets.QGroupBox(parent=AdvancedOptionsPage)
        self.groupBox_completeness.setObjectName("groupBox_completeness")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_completeness)
        self.gridLayout.setObjectName("gridLayout")
        self.completeness_ignore_videos = QtWidgets.QCheckBox(parent=self.groupBox_completeness)
        self.completeness_ignore_videos.setObjectName("completeness_ignore_videos")
        self.gridLayout.addWidget(self.completeness_ignore_videos, 0, 0, 1, 1)
        self.completeness_ignore_data = QtWidgets.QCheckBox(parent=self.groupBox_completeness)
        self.completeness_ignore_data.setCheckable(True)
        self.completeness_ignore_data.setObjectName("completeness_ignore_data")
        self.gridLayout.addWidget(self.completeness_ignore_data, 3, 0, 1, 1)
        self.completeness_ignore_pregap = QtWidgets.QCheckBox(parent=self.groupBox_completeness)
        self.completeness_ignore_pregap.setObjectName("completeness_ignore_pregap")
        self.gridLayout.addWidget(self.completeness_ignore_pregap, 0, 1, 1, 1)
        self.completeness_ignore_silence = QtWidgets.QCheckBox(parent=self.groupBox_completeness)
        self.completeness_ignore_silence.setObjectName("completeness_ignore_silence")
        self.gridLayout.addWidget(self.completeness_ignore_silence, 3, 1, 1, 1)
        self.vboxlayout.addWidget(self.groupBox_completeness)
        self.groupBox_ignore_tags = QtWidgets.QGroupBox(parent=AdvancedOptionsPage)
        self.groupBox_ignore_tags.setObjectName("groupBox_ignore_tags")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_ignore_tags)
        self.verticalLayout.setObjectName("verticalLayout")
        self.compare_ignore_tags = TagListEditor(parent=self.groupBox_ignore_tags)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compare_ignore_tags.sizePolicy().hasHeightForWidth())
        self.compare_ignore_tags.setSizePolicy(sizePolicy)
        self.compare_ignore_tags.setObjectName("compare_ignore_tags")
        self.verticalLayout.addWidget(self.compare_ignore_tags)
        self.vboxlayout.addWidget(self.groupBox_ignore_tags)

        self.retranslateUi(AdvancedOptionsPage)
        self.query_limit.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(AdvancedOptionsPage)
        AdvancedOptionsPage.setTabOrder(self.ignore_regex, self.ignore_hidden_files)
        AdvancedOptionsPage.setTabOrder(self.ignore_hidden_files, self.recursively_add_files)
        AdvancedOptionsPage.setTabOrder(self.recursively_add_files, self.ignore_track_duration_difference_under)
        AdvancedOptionsPage.setTabOrder(self.ignore_track_duration_difference_under, self.query_limit)
        AdvancedOptionsPage.setTabOrder(self.query_limit, self.completeness_ignore_videos)
        AdvancedOptionsPage.setTabOrder(self.completeness_ignore_videos, self.completeness_ignore_data)

    def retranslateUi(self, AdvancedOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_("Advanced options"))
        self.label_ignore_regex.setText(_("Ignore file paths matching the following regular expression:"))
        self.label_query_limit.setText(_("Maximum number of entities to return per MusicBrainz query"))
        self.label_track_duration_diff.setText(_("Ignore track duration difference under this number of seconds"))
        self.recursively_add_files.setText(_("Include sub-folders when adding files from folder"))
        self.ignore_hidden_files.setText(_("Ignore hidden files"))
        self.groupBox_completeness.setTitle(_("Ignore the following tracks when determining whether a release is complete"))
        self.completeness_ignore_videos.setText(_("Video tracks"))
        self.completeness_ignore_data.setText(_("Data tracks"))
        self.completeness_ignore_pregap.setText(_("Pregap tracks"))
        self.completeness_ignore_silence.setText(_("Silent tracks"))
        self.groupBox_ignore_tags.setTitle(_("Tags to ignore for comparison:"))
from picard.ui.widgets.taglisteditor import TagListEditor
