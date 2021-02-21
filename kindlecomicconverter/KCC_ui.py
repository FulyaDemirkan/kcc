# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/KCC.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(450, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/icons/comic2ebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.optionWidget = QtWidgets.QWidget(self.centralWidget)
        self.optionWidget.setObjectName("optionWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.optionWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.upscaleBox = QtWidgets.QCheckBox(self.optionWidget)
        self.upscaleBox.setTristate(True)
        self.upscaleBox.setObjectName("upscaleBox")
        self.gridLayout_2.addWidget(self.upscaleBox, 1, 1, 1, 1)
        self.rotateBox = QtWidgets.QCheckBox(self.optionWidget)
        self.rotateBox.setTristate(True)
        self.rotateBox.setObjectName("rotateBox")
        self.gridLayout_2.addWidget(self.rotateBox, 0, 1, 1, 1)
        self.outputSplit = QtWidgets.QCheckBox(self.optionWidget)
        self.outputSplit.setObjectName("outputSplit")
        self.gridLayout_2.addWidget(self.outputSplit, 2, 1, 1, 1)
        self.webtoonBox = QtWidgets.QCheckBox(self.optionWidget)
        self.webtoonBox.setObjectName("webtoonBox")
        self.gridLayout_2.addWidget(self.webtoonBox, 1, 0, 1, 1)
        self.colorBox = QtWidgets.QCheckBox(self.optionWidget)
        self.colorBox.setObjectName("colorBox")
        self.gridLayout_2.addWidget(self.colorBox, 2, 2, 1, 1)
        self.gammaBox = QtWidgets.QCheckBox(self.optionWidget)
        self.gammaBox.setObjectName("gammaBox")
        self.gridLayout_2.addWidget(self.gammaBox, 1, 2, 1, 1)
        self.borderBox = QtWidgets.QCheckBox(self.optionWidget)
        self.borderBox.setTristate(True)
        self.borderBox.setObjectName("borderBox")
        self.gridLayout_2.addWidget(self.borderBox, 2, 0, 1, 1)
        self.mangaBox = QtWidgets.QCheckBox(self.optionWidget)
        self.mangaBox.setObjectName("mangaBox")
        self.gridLayout_2.addWidget(self.mangaBox, 0, 0, 1, 1)
        self.qualityBox = QtWidgets.QCheckBox(self.optionWidget)
        self.qualityBox.setTristate(True)
        self.qualityBox.setObjectName("qualityBox")
        self.gridLayout_2.addWidget(self.qualityBox, 0, 2, 1, 1)
        self.disableProcessingBox = QtWidgets.QCheckBox(self.optionWidget)
        self.disableProcessingBox.setObjectName("disableProcessingBox")
        self.gridLayout_2.addWidget(self.disableProcessingBox, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.optionWidget, 4, 0, 1, 2)
        self.gammaWidget = QtWidgets.QWidget(self.centralWidget)
        self.gammaWidget.setVisible(False)
        self.gammaWidget.setObjectName("gammaWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gammaWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gammaLabel = QtWidgets.QLabel(self.gammaWidget)
        self.gammaLabel.setObjectName("gammaLabel")
        self.horizontalLayout_2.addWidget(self.gammaLabel)
        self.gammaSlider = QtWidgets.QSlider(self.gammaWidget)
        self.gammaSlider.setMaximum(250)
        self.gammaSlider.setSingleStep(5)
        self.gammaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gammaSlider.setObjectName("gammaSlider")
        self.horizontalLayout_2.addWidget(self.gammaSlider)
        self.gridLayout.addWidget(self.gammaWidget, 6, 0, 1, 2)
        self.buttonWidget = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonWidget.sizePolicy().hasHeightForWidth())
        self.buttonWidget.setSizePolicy(sizePolicy)
        self.buttonWidget.setObjectName("buttonWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.buttonWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.directoryButton = QtWidgets.QPushButton(self.buttonWidget)
        self.directoryButton.setMinimumSize(QtCore.QSize(0, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Other/icons/folder_new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.directoryButton.setIcon(icon1)
        self.directoryButton.setObjectName("directoryButton")
        self.gridLayout_4.addWidget(self.directoryButton, 0, 0, 1, 1)
        self.fileButton = QtWidgets.QPushButton(self.buttonWidget)
        self.fileButton.setMinimumSize(QtCore.QSize(0, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Other/icons/document_new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileButton.setIcon(icon2)
        self.fileButton.setObjectName("fileButton")
        self.gridLayout_4.addWidget(self.fileButton, 0, 3, 1, 1)
        self.deviceBox = QtWidgets.QComboBox(self.buttonWidget)
        self.deviceBox.setMinimumSize(QtCore.QSize(0, 28))
        self.deviceBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.deviceBox.setObjectName("deviceBox")
        self.gridLayout_4.addWidget(self.deviceBox, 1, 0, 1, 1)
        self.formatBox = QtWidgets.QComboBox(self.buttonWidget)
        self.formatBox.setMinimumSize(QtCore.QSize(0, 28))
        self.formatBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.formatBox.setObjectName("formatBox")
        self.gridLayout_4.addWidget(self.formatBox, 1, 3, 1, 1)
        self.convertButton = QtWidgets.QPushButton(self.buttonWidget)
        self.convertButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.convertButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Other/icons/convert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.convertButton.setIcon(icon3)
        self.convertButton.setObjectName("convertButton")
        self.gridLayout_4.addWidget(self.convertButton, 1, 2, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.buttonWidget)
        self.clearButton.setMinimumSize(QtCore.QSize(0, 30))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Other/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon4)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout_4.addWidget(self.clearButton, 0, 2, 1, 1)
        self.directoryButton.raise_()
        self.clearButton.raise_()
        self.fileButton.raise_()
        self.deviceBox.raise_()
        self.convertButton.raise_()
        self.formatBox.raise_()
        self.gridLayout.addWidget(self.buttonWidget, 3, 0, 1, 2)
        self.toolWidget = QtWidgets.QWidget(self.centralWidget)
        self.toolWidget.setObjectName("toolWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editorButton = QtWidgets.QPushButton(self.toolWidget)
        self.editorButton.setMinimumSize(QtCore.QSize(0, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Other/icons/editor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editorButton.setIcon(icon5)
        self.editorButton.setObjectName("editorButton")
        self.horizontalLayout.addWidget(self.editorButton)
        self.wikiButton = QtWidgets.QPushButton(self.toolWidget)
        self.wikiButton.setMinimumSize(QtCore.QSize(0, 30))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Other/icons/wiki.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wikiButton.setIcon(icon6)
        self.wikiButton.setObjectName("wikiButton")
        self.horizontalLayout.addWidget(self.wikiButton)
        self.gridLayout.addWidget(self.toolWidget, 0, 0, 1, 2)
        self.jobList = QtWidgets.QListWidget(self.centralWidget)
        self.jobList.setStyleSheet("QListWidget#jobList {background:#ffffff;background-image:url(:/Other/icons/list_background.png);background-position:center center;background-repeat:no-repeat;color:rgb(0,0,0);}")
        self.jobList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.jobList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.jobList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.jobList.setObjectName("jobList")
        self.gridLayout.addWidget(self.jobList, 2, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setVisible(False)
        self.progressBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 2)
        self.customWidget = QtWidgets.QWidget(self.centralWidget)
        self.customWidget.setVisible(False)
        self.customWidget.setObjectName("customWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.customWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.hLabel = QtWidgets.QLabel(self.customWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hLabel.sizePolicy().hasHeightForWidth())
        self.hLabel.setSizePolicy(sizePolicy)
        self.hLabel.setObjectName("hLabel")
        self.gridLayout_3.addWidget(self.hLabel, 0, 2, 1, 1)
        self.widthBox = QtWidgets.QSpinBox(self.customWidget)
        self.widthBox.setMaximum(2160)
        self.widthBox.setObjectName("widthBox")
        self.gridLayout_3.addWidget(self.widthBox, 0, 1, 1, 1)
        self.wLabel = QtWidgets.QLabel(self.customWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wLabel.sizePolicy().hasHeightForWidth())
        self.wLabel.setSizePolicy(sizePolicy)
        self.wLabel.setObjectName("wLabel")
        self.gridLayout_3.addWidget(self.wLabel, 0, 0, 1, 1)
        self.heightBox = QtWidgets.QSpinBox(self.customWidget)
        self.heightBox.setMaximum(3840)
        self.heightBox.setObjectName("heightBox")
        self.gridLayout_3.addWidget(self.heightBox, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.customWidget, 7, 0, 1, 2)
        mainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.convertButton, self.clearButton)
        mainWindow.setTabOrder(self.clearButton, self.directoryButton)
        mainWindow.setTabOrder(self.directoryButton, self.fileButton)
        mainWindow.setTabOrder(self.fileButton, self.deviceBox)
        mainWindow.setTabOrder(self.deviceBox, self.formatBox)
        mainWindow.setTabOrder(self.formatBox, self.mangaBox)
        mainWindow.setTabOrder(self.mangaBox, self.rotateBox)
        mainWindow.setTabOrder(self.rotateBox, self.qualityBox)
        mainWindow.setTabOrder(self.qualityBox, self.webtoonBox)
        mainWindow.setTabOrder(self.webtoonBox, self.upscaleBox)
        mainWindow.setTabOrder(self.upscaleBox, self.gammaBox)
        mainWindow.setTabOrder(self.gammaBox, self.borderBox)
        mainWindow.setTabOrder(self.borderBox, self.outputSplit)
        mainWindow.setTabOrder(self.outputSplit, self.colorBox)
        mainWindow.setTabOrder(self.colorBox, self.editorButton)
        mainWindow.setTabOrder(self.editorButton, self.wikiButton)
        mainWindow.setTabOrder(self.wikiButton, self.jobList)
        mainWindow.setTabOrder(self.jobList, self.gammaSlider)
        mainWindow.setTabOrder(self.gammaSlider, self.widthBox)
        mainWindow.setTabOrder(self.widthBox, self.heightBox)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Kindle Comic Converter"))
        self.upscaleBox.setToolTip(_translate("mainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Nothing<br/></span>Images smaller than device resolution will not be resized.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - Stretching<br/></span>Images smaller than device resolution will be resized. Aspect ratio will be not preserved.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Upscaling<br/></span>Images smaller than device resolution will be resized. Aspect ratio will be preserved.</p></body></html>"))
        self.upscaleBox.setText(_translate("mainWindow", "Stretch/Upscale"))
        self.rotateBox.setToolTip(_translate("mainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Split<br/></span>Double page spreads will be cut into two separate pages.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - Rotate and split<br/></span>Double page spreads will be displayed twice. First rotated and then split. </p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Rotate<br/></span>Double page spreads will be rotated.</p></body></html>"))
        self.rotateBox.setText(_translate("mainWindow", "Spread splitter"))
        self.outputSplit.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Automatic mode<br/></span>The output will be split automatically.</p><p style=\'white-space:pre\'><span style=\" font-weight:600; text-decoration: underline;\">Checked - Volume mode<br/></span>Every subdirectory will be considered as a separate volume.</p></body></html>"))
        self.outputSplit.setText(_translate("mainWindow", "Output split"))
        self.webtoonBox.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Enable special parsing mode for Korean Webtoons.</p></body></html>"))
        self.webtoonBox.setText(_translate("mainWindow", "Webtoon mode"))
        self.colorBox.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Disable conversion to grayscale.</p></body></html>"))
        self.colorBox.setText(_translate("mainWindow", "Color mode"))
        self.gammaBox.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Disable automatic gamma correction.</p></body></html>"))
        self.gammaBox.setText(_translate("mainWindow", "Custom gamma"))
        self.borderBox.setToolTip(_translate("mainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Autodetection<br/></span>The color of margins fill will be detected automatically.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - White<br/></span>Margins will be filled with white color.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Black<br/></span>Margins will be filled with black color.</p></body></html>"))
        self.borderBox.setText(_translate("mainWindow", "W/B margins"))
        self.mangaBox.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Enable right-to-left reading.</p></body></html>"))
        self.mangaBox.setText(_translate("mainWindow", "Manga mode"))
        self.qualityBox.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - 4 panels<br/></span>Zoom each corner separately.</p><p style=\'white-space:pre\'><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - 2 panels<br/></span>Zoom only the top and bottom of the page.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - 4 high-quality panels<br/></span>Zoom each corner separately. Try to increase the quality of magnification. Check wiki for more details.</p></body></html>"))
        self.qualityBox.setText(_translate("mainWindow", "Panel View 4/2/HQ"))
        self.disableProcessingBox.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Do not process any image, ignore profil and processing options</p></body></html>"))
        self.disableProcessingBox.setText(_translate("mainWindow", "Disable processing"))
        self.gammaLabel.setText(_translate("mainWindow", "Gamma: Auto"))
        self.directoryButton.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Add directory containing JPG, PNG or GIF files to queue.<br/><span style=\" font-weight:600;\">CBR, CBZ and CB7 files inside will not be processed!</span></p></body></html>"))
        self.directoryButton.setText(_translate("mainWindow", "Add directory"))
        self.fileButton.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Add CBR, CBZ, CB7 or PDF file to queue.</p></body></html>"))
        self.fileButton.setText(_translate("mainWindow", "Add file"))
        self.deviceBox.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Target device.</p></body></html>"))
        self.formatBox.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Output format.</p></body></html>"))
        self.convertButton.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Shift+Click to select the output directory.</p></body></html>"))
        self.convertButton.setText(_translate("mainWindow", "Convert"))
        self.clearButton.setText(_translate("mainWindow", "Clear list"))
        self.editorButton.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Shift+Click to edit directory.</p></body></html>"))
        self.editorButton.setText(_translate("mainWindow", "Editor"))
        self.wikiButton.setText(_translate("mainWindow", "Wiki"))
        self.hLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Resolution of the target device.</p></body></html>"))
        self.hLabel.setText(_translate("mainWindow", "Custom height:"))
        self.widthBox.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Resolution of the target device.</p></body></html>"))
        self.wLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Resolution of the target device.</p></body></html>"))
        self.wLabel.setText(_translate("mainWindow", "Custom width:"))
        self.heightBox.setToolTip(_translate("mainWindow", "<html><head/><body><p style=\'white-space:pre\'>Resolution of the target device.</p></body></html>"))
from . import KCC_rc
