# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinalProject2.ui'
#
# Created: Sat Mar 23 16:21:09 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import re

class Ui_MainWindow(object):
    Max_Pin_Number=37
    ConfigurationPinList = {}
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 451)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ucPinList = QtGui.QListWidget(self.centralwidget)
        self.ucPinList.setMaximumSize(QtCore.QSize(160, 16777215))
        self.ucPinList.setObjectName("ucPinList")
        for Num_counter in range(self.Max_Pin_Number):
            QtGui.QListWidgetItem(self.ucPinList)
        self.gridLayout.addWidget(self.ucPinList, 1, 0, 1, 1)
        self.MicrocontrollerType = QtGui.QComboBox(self.centralwidget)
        self.MicrocontrollerType.setObjectName("MicrocontrollerType")
        self.MicrocontrollerType.addItem("")
        self.MicrocontrollerType.addItem("")
        self.gridLayout.addWidget(self.MicrocontrollerType, 0, 0, 1, 2)
        self.Pin_ConfigBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.Pin_ConfigBox.setFont(font)
        self.Pin_ConfigBox.setObjectName("Pin_ConfigBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.Pin_ConfigBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Default_Check = QtGui.QCheckBox(self.Pin_ConfigBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Default_Check.setFont(font)
        self.Default_Check.setObjectName("Default_Check")
        self.gridLayout_2.addWidget(self.Default_Check, 2, 0, 1, 1)
        self.Pin_NameEdit = QtGui.QLineEdit(self.Pin_ConfigBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Pin_NameEdit.setFont(font)
        self.Pin_NameEdit.setObjectName("Pin_NameEdit")
        self.gridLayout_2.addWidget(self.Pin_NameEdit, 1, 0, 1, 1)
        self.Pin_ModeBox = QtGui.QGroupBox(self.Pin_ConfigBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Pin_ModeBox.setFont(font)
        self.Pin_ModeBox.setObjectName("Pin_ModeBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.Pin_ModeBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.InputButton = QtGui.QRadioButton(self.Pin_ModeBox)
        self.InputButton.setObjectName("InputButton")
        self.verticalLayout.addWidget(self.InputButton)
        self.OutputButton = QtGui.QRadioButton(self.Pin_ModeBox)
        self.OutputButton.setObjectName("OutputButton")
        self.verticalLayout.addWidget(self.OutputButton)
        self.gridLayout_2.addWidget(self.Pin_ModeBox, 0, 0, 1, 1)
        self.Input_ConfigBox = QtGui.QGroupBox(self.Pin_ConfigBox)
        self.Input_ConfigBox.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Input_ConfigBox.setFont(font)
        self.Input_ConfigBox.setObjectName("Input_ConfigBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.Input_ConfigBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AnalogButton = QtGui.QRadioButton(self.Input_ConfigBox)
        self.AnalogButton.setObjectName("AnalogButton")
        self.verticalLayout_2.addWidget(self.AnalogButton)
        self.FloatButton = QtGui.QRadioButton(self.Input_ConfigBox)
        self.FloatButton.setObjectName("FloatButton")
        self.verticalLayout_2.addWidget(self.FloatButton)
        self.PullupButton = QtGui.QRadioButton(self.Input_ConfigBox)
        self.PullupButton.setObjectName("PullupButton")
        self.verticalLayout_2.addWidget(self.PullupButton)
        self.PullDownButton = QtGui.QRadioButton(self.Input_ConfigBox)
        self.PullDownButton.setObjectName("PullDownButton")
        self.verticalLayout_2.addWidget(self.PullDownButton)
        self.gridLayout_2.addWidget(self.Input_ConfigBox, 0, 1, 1, 2)
        self.Output_ConfigBox = QtGui.QGroupBox(self.Pin_ConfigBox)
        self.Output_ConfigBox.setMinimumSize(QtCore.QSize(0, 120))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Output_ConfigBox.setFont(font)
        self.Output_ConfigBox.setObjectName("Output_ConfigBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Output_ConfigBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.PushPullButton = QtGui.QRadioButton(self.Output_ConfigBox)
        self.PushPullButton.setObjectName("PushPullButton")
        self.verticalLayout_3.addWidget(self.PushPullButton)
        self.OpenDrainButton = QtGui.QRadioButton(self.Output_ConfigBox)
        self.OpenDrainButton.setObjectName("OpenDrainButton")
        self.verticalLayout_3.addWidget(self.OpenDrainButton)
        self.AFPushPullButton = QtGui.QRadioButton(self.Output_ConfigBox)
        self.AFPushPullButton.setObjectName("AFPushPullButton")
        self.verticalLayout_3.addWidget(self.AFPushPullButton)
        self.AFOpenDrainButton = QtGui.QRadioButton(self.Output_ConfigBox)
        self.AFOpenDrainButton.setObjectName("AFOpenDrainButton")
        self.verticalLayout_3.addWidget(self.AFOpenDrainButton)
        self.gridLayout_2.addWidget(self.Output_ConfigBox, 1, 1, 4, 2)
        self.PinValueBox = QtGui.QGroupBox(self.Pin_ConfigBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PinValueBox.setFont(font)
        self.PinValueBox.setObjectName("PinValueBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.PinValueBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.HighButton = QtGui.QRadioButton(self.PinValueBox)
        self.HighButton.setObjectName("HighButton")
        self.horizontalLayout.addWidget(self.HighButton)
        self.LowButton = QtGui.QRadioButton(self.PinValueBox)
        self.LowButton.setObjectName("LowButton")
        self.horizontalLayout.addWidget(self.LowButton)
        self.gridLayout_2.addWidget(self.PinValueBox, 3, 0, 2, 1)
        self.gridLayout.addWidget(self.Pin_ConfigBox, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.SetDefaultConfig()
        self.ShowPinConfiguration('PIN0')
        

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.MicrocontrollerType, QtCore.SIGNAL("currentIndexChanged(int)"), self.ComboIndexChange)
        QtCore.QObject.connect(self.MicrocontrollerType, QtCore.SIGNAL("currentIndexChanged(int)"), self.SetDefaultConfig)
        QtCore.QObject.connect(self.MicrocontrollerType, QtCore.SIGNAL("currentIndexChanged(int)"), self.ucPinList.setCurrentRow (0))
        QtCore.QObject.connect(self.MicrocontrollerType, QtCore.SIGNAL("currentIndexChanged(int)"), self.ShowPinItem)
        QtCore.QObject.connect(self.Default_Check, QtCore.SIGNAL("clicked(bool)"), self.Pin_NameEdit.setDisabled)
        QtCore.QObject.connect(self.ucPinList, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.ShowPinItem)
        QtCore.QObject.connect(self.InputButton, QtCore.SIGNAL("clicked(bool)"), self.SetPinMode)
        QtCore.QObject.connect(self.InputButton, QtCore.SIGNAL("clicked(bool)"), self.Input_ConfigBox.setEnabled)
        QtCore.QObject.connect(self.InputButton, QtCore.SIGNAL("clicked(bool)"), self.Output_ConfigBox.setDisabled)
        QtCore.QObject.connect(self.InputButton, QtCore.SIGNAL("clicked(bool)"), self.PinValueBox.setDisabled)
        QtCore.QObject.connect(self.OutputButton, QtCore.SIGNAL("clicked(bool)"), self.SetPinMode)
        QtCore.QObject.connect(self.OutputButton, QtCore.SIGNAL("clicked(bool)"), self.Output_ConfigBox.setEnabled)
        QtCore.QObject.connect(self.OutputButton, QtCore.SIGNAL("clicked(bool)"), self.PinValueBox.setEnabled)
        QtCore.QObject.connect(self.OutputButton, QtCore.SIGNAL("clicked(bool)"), self.Input_ConfigBox.setDisabled)
        QtCore.QObject.connect(self.AnalogButton, QtCore.SIGNAL("clicked(bool)"), self.SetPinConfig)
        QtCore.QObject.connect(self.FloatButton, QtCore.SIGNAL("clicked(bool)"), self.SetPinConfig)
        QtCore.QObject.connect(self.PullupButton, QtCore.SIGNAL("clicked(bool)"), self.SetPinConfig)
        QtCore.QObject.connect(self.PullDownButton, QtCore.SIGNAL("clicked(bool)"), self.SetPinConfig)
        QtCore.QObject.connect(self.PushPullButton, QtCore.SIGNAL("clicked(bool)"), self.SetPinConfig)
        QtCore.QObject.connect(self.OpenDrainButton, QtCore.SIGNAL("clicked(bool)"), self.SetPinConfig)
        QtCore.QObject.connect(self.AFPushPullButton, QtCore.SIGNAL("clicked(bool)"), self.SetPinConfig)
        QtCore.QObject.connect(self.AFOpenDrainButton, QtCore.SIGNAL("clicked(bool)"), self.SetPinConfig)
        QtCore.QObject.connect(self.Pin_NameEdit, QtCore.SIGNAL("textChanged(QString)"), self.SetPinName)

        QtCore.QObject.connect(self.Default_Check, QtCore.SIGNAL("clicked()"), self.Pin_NameEdit.clear)
        QtCore.QObject.connect(self.actionNew, QtCore.SIGNAL("activated()"), self.FloatButton.hide)
        QtCore.QObject.connect(self.actionLoad, QtCore.SIGNAL("activated()"), self.LoadConfigurationFile)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL("activated()"), self.SaveConfigurationFile)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QObject.connect(self.actionHelp, QtCore.SIGNAL("activated()"), self.FloatButton.hide)
        QtCore.QObject.connect(self.ucPinList, QtCore.SIGNAL("currentRowChanged(int)"), self.ShowPinItem)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.ucPinList.isSortingEnabled()
        self.ucPinList.setSortingEnabled(False)
        Num_counter = 0
        for Num_counter in range(self.Max_Pin_Number):
            self.ucPinList.item(Num_counter).setText(QtGui.QApplication.translate("MainWindow", "DIO Pin" + str(Num_counter), None, QtGui.QApplication.UnicodeUTF8))
        self.ucPinList.setSortingEnabled(__sortingEnabled)
        self.MicrocontrollerType.setItemText(0, QtGui.QApplication.translate("MainWindow", "ARM Microcontroller Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.MicrocontrollerType.setItemText(1, QtGui.QApplication.translate("MainWindow", "AVR Microcontroller Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.Pin_ConfigBox.setTitle(QtGui.QApplication.translate("MainWindow", "Pin0 Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.Default_Check.setText(QtGui.QApplication.translate("MainWindow", "Set Default Name", None, QtGui.QApplication.UnicodeUTF8))
        self.Pin_NameEdit.setText(QtGui.QApplication.translate("MainWindow", "Enter the pin name", None, QtGui.QApplication.UnicodeUTF8))
        self.Pin_ModeBox.setTitle(QtGui.QApplication.translate("MainWindow", "Pin Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.InputButton.setText(QtGui.QApplication.translate("MainWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.OutputButton.setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.Input_ConfigBox.setTitle(QtGui.QApplication.translate("MainWindow", "Input Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.AnalogButton.setText(QtGui.QApplication.translate("MainWindow", "Analog", None, QtGui.QApplication.UnicodeUTF8))
        self.FloatButton.setText(QtGui.QApplication.translate("MainWindow", "Float", None, QtGui.QApplication.UnicodeUTF8))
        self.PullupButton.setText(QtGui.QApplication.translate("MainWindow", "Pull Up", None, QtGui.QApplication.UnicodeUTF8))
        self.PullDownButton.setText(QtGui.QApplication.translate("MainWindow", "Pull Down", None, QtGui.QApplication.UnicodeUTF8))
        self.Output_ConfigBox.setTitle(QtGui.QApplication.translate("MainWindow", "Output Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.PushPullButton.setText(QtGui.QApplication.translate("MainWindow", "Push Pull", None, QtGui.QApplication.UnicodeUTF8))
        self.OpenDrainButton.setText(QtGui.QApplication.translate("MainWindow", "Open Drain", None, QtGui.QApplication.UnicodeUTF8))
        self.AFPushPullButton.setText(QtGui.QApplication.translate("MainWindow", "Alternative Push Pull", None, QtGui.QApplication.UnicodeUTF8))
        self.AFOpenDrainButton.setText(QtGui.QApplication.translate("MainWindow", "Alternative Open drain", None, QtGui.QApplication.UnicodeUTF8))
        self.PinValueBox.setTitle(QtGui.QApplication.translate("MainWindow", "Pin Value", None, QtGui.QApplication.UnicodeUTF8))
        self.HighButton.setText(QtGui.QApplication.translate("MainWindow", "High", None, QtGui.QApplication.UnicodeUTF8))
        self.LowButton.setText(QtGui.QApplication.translate("MainWindow", "Low", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))

        
    def SetPinMode(self):
        print "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
        cuIndex = self.MicrocontrollerType.currentIndex()
        cuItem = self.ucPinList.currentRow()
        
        if  cuIndex == 0:
            self.OutputButton.setChecked(False)
            self.AFPushPullButton.setChecked(False)
            self.AFOpenDrainButton.setChecked(False)
            self.PushPullButton.setChecked(False)
            self.OpenDrainButton.setChecked(False)
            self.InputButton.setChecked(False)
            self.AnalogButton.setChecked(False)
            self.FloatButton.setChecked(False)
            self.PullupButton.setChecked(False)
            self.PullDownButton.setChecked(False)
            if self.InputButton.isChecked() == True:
                self.ConfigurationPinList['PIN'+str(cuItem)]['Mode'] = 'GPIO_u8_INPUT_'
                self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'ANALOG'
                self.AnalogButton.setChecked(True)
            elif self.OutputButton.isChecked() == True:
                self.ConfigurationPinList['PIN'+str(cuItem)]['Mode'] = 'GPIO_u8_OUTPUT_'
                self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'AF_PUSH_PULL'
                self.AFPushPullButton.setChecked(True)
        elif cuIndex == 1:
            self.OutputButton.setChecked(False)
            self.PushPullButton.setChecked(False)
            self.OpenDrainButton.setChecked(False)
            self.InputButton.setChecked(False)
            self.PullupButton.setChecked(False)
            self.PullDownButton.setChecked(False)
            if self.InputButton.isChecked() == True:
                self.ConfigurationPinList['PIN'+str(cuItem)]['Mode'] = 'DIO_u8_INPUT_'
                self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'PULL_UP'
                self.PullupButton.setChecked(True)

            elif self.OutputButton.isChecked() == True:
                self.ConfigurationPinList['PIN'+str(cuItem)]['Mode'] = 'DIO_u8_OUTPUT_'
                self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'PUSH_PULL'
                self.PushPullButton.setChecked(True)



    def SetPinConfig(self):
        cuIndex = self.MicrocontrollerType.currentIndex()
        cuItem = self.ucPinList.currentRow()
        
        if  cuIndex == 0:
            if self.OutputButton.isChecked() == True:
                if  self.AFPushPullButton.isChecked() == True:
                   self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'AF_PUSH_PULL'
                elif self.AFOpenDrainButton.isChecked() == True:
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'AF_OPEN_DRAIN'
                elif self.PushPullButton.isChecked() == True :
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'GP_PUSH_PULL'
                elif self.OpenDrainButton.isChecked() == True :
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'GP_OPEN_DRAIN'
            elif self.InputButton.isChecked() == True:
                if self.AnalogButton.isChecked() == True:
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'ANALOG'
                elif self.FloatButton.isChecked() == True :
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'FLOATING'
                elif self.PullupButton.isChecked() == True:
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'PULL_UP'
                elif self.PullDownButton.isChecked() == True:
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'PULL_DOWN'

        elif cuIndex == 1:
            if self.OutputButton.isChecked() == True:
                if self.PushPullButton.isChecked() == True:
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'PUSH_PULL'
                elif self.OpenDrainButton.isChecked() == True:
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'OPEN_DRAIN'
            elif self.InputButton.isChecked() == True:
                if self.PullupButton.isChecked() == True :
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'PULL_UP'
                elif self.PullDownButton.isChecked() == True :
                    self.ConfigurationPinList['PIN'+str(cuItem)]['Config'] = 'PULL_DOWN'



    def ComboIndexChange(self):
        cuIndex = self.MicrocontrollerType.currentIndex()
        if  cuIndex == 1:
            self.Max_Pin_Number=32
            self.ucPinList.clear()
            for Num_counter in range(self.Max_Pin_Number):
                QtGui.QListWidgetItem(self.ucPinList)
                self.ucPinList.item(Num_counter).setText(QtGui.QApplication.translate("MainWindow", "DIO Pin" + str(Num_counter), None, QtGui.QApplication.UnicodeUTF8))
            self.AnalogButton.hide()
            self.FloatButton.hide()
            self.AFOpenDrainButton.hide()
            self.AFPushPullButton.hide()
        else:
            self.Max_Pin_Number=37
            self.ucPinList.clear()
            for Num_counter in range(self.Max_Pin_Number):
                QtGui.QListWidgetItem(self.ucPinList)
                self.ucPinList.item(Num_counter).setText(QtGui.QApplication.translate("MainWindow", "DIO Pin" + str(Num_counter), None, QtGui.QApplication.UnicodeUTF8))
            self.AnalogButton.show()
            self.FloatButton.show()
            self.AFOpenDrainButton.show()
            self.AFPushPullButton.show()

    def SetDefaultConfig(self):
        Num_counter = 0
        cuIndex = self.MicrocontrollerType.currentIndex()
        print(cuIndex)
        if  cuIndex == 0:
            for Num_counter in range(self.Max_Pin_Number):
                self.ConfigurationPinList.setdefault('PIN'+str(Num_counter),{})['Mode'] = 'GPIO_u8_INPUT_'
                self.ConfigurationPinList.setdefault('PIN'+str(Num_counter),{})['Config'] = 'ANALOG'
                self.ConfigurationPinList.setdefault('PIN'+str(Num_counter),{})['Value'] = 'GPIO_u8_HIGH'
                self.ConfigurationPinList.setdefault('PIN'+str(Num_counter),{})['Name'] = 'GPIO_PIN'+str(Num_counter)
            self.Pin_ConfigBox.setTitle(QtGui.QApplication.translate("MainWindow", "Pin0 Configuration", None, QtGui.QApplication.UnicodeUTF8))
        elif cuIndex == 1:
            for Num_counter in range(self.Max_Pin_Number):
                self.ConfigurationPinList.setdefault('PIN'+str(Num_counter),{})['Mode'] = 'DIO_u8_OUTPUT_'
                self.ConfigurationPinList.setdefault('PIN'+str(Num_counter),{})['Config'] = 'PUSH_PULL'
                self.ConfigurationPinList.setdefault('PIN'+str(Num_counter),{})['Value'] = 'DIO_u8_HIGH'
                self.ConfigurationPinList.setdefault('PIN'+str(Num_counter),{})['Name'] = 'DIO_PIN'+str(Num_counter)
            self.Pin_ConfigBox.setTitle(QtGui.QApplication.translate("MainWindow", "Pin0 Configuration", None, QtGui.QApplication.UnicodeUTF8))
        
    
    def ShowPinConfiguration(self,Pinname):
        print Pinname
        cuIndex = self.MicrocontrollerType.currentIndex()
        if  cuIndex == 0:
            self.OutputButton.setChecked(False)
            self.AFPushPullButton.setChecked(False)
            self.AFOpenDrainButton.setChecked(False)
            self.PushPullButton.setChecked(False)
            self.OpenDrainButton.setChecked(False)
            self.InputButton.setChecked(False)
            self.AnalogButton.setChecked(False)
            self.FloatButton.setChecked(False)
            self.PullupButton.setChecked(False)
            self.PullDownButton.setChecked(False)
            if self.ConfigurationPinList[Pinname]['Mode'] == 'GPIO_u8_OUTPUT_':
                self.Input_ConfigBox.setDisabled(True)
                self.Output_ConfigBox.setEnabled(True)
                self.PinValueBox.setEnabled(True)
                self.OutputButton.setChecked(True)
                if self.ConfigurationPinList[Pinname]['Config'] == 'AF_PUSH_PULL':
                    self.AFPushPullButton.setChecked(True)
                elif self.ConfigurationPinList[Pinname]['Config'] == 'AF_OPEN_DRAIN':
                    self.AFOpenDrainButton.setChecked(True)
                elif self.ConfigurationPinList[Pinname]['Config'] == 'GP_PUSH_PULL':
                    self.PushPullButton.setChecked(True)
                elif self.ConfigurationPinList[Pinname]['Config'] == 'GP_OPEN_DRAIN':
                    self.OpenDrainButton.setChecked(True)
            elif self.ConfigurationPinList[Pinname]['Mode'] == 'GPIO_u8_INPUT_':
                self.Output_ConfigBox.setDisabled(True)
                self.Input_ConfigBox.setEnabled(True)
                self.PinValueBox.setDisabled(True)
                self.InputButton.setChecked(True)
                if self.ConfigurationPinList[Pinname]['Config'] == 'ANALOG':
                    self.AnalogButton.setChecked(True)
                elif self.ConfigurationPinList[Pinname]['Config'] == 'FLOATING':
                    self.FloatButton.setChecked(True)
                elif self.ConfigurationPinList[Pinname]['Config'] == 'PULL_UP':
                    self.PullupButton.setChecked(True)
                elif self.ConfigurationPinList[Pinname]['Config'] == 'PULL_DOWN':
                    self.PullDownButton.setChecked(True)
        elif cuIndex == 1:
            self.OutputButton.setChecked(False)
            self.PushPullButton.setChecked(False)
            self.OpenDrainButton.setChecked(False)
            self.InputButton.setChecked(False)
            self.PullupButton.setChecked(False)
            self.PullDownButton.setChecked(False)
            if self.ConfigurationPinList[Pinname]['Mode'] == 'DIO_u8_OUTPUT_':
                self.Input_ConfigBox.setDisabled(True)
                self.Output_ConfigBox.setEnabled(True)
                self.PinValueBox.setEnabled(True)
                self.OutputButton.setChecked(True)
                if self.ConfigurationPinList[Pinname]['Config'] == 'PUSH_PULL':
                    self.PushPullButton.setChecked(True)
                elif self.ConfigurationPinList[Pinname]['Config'] == 'OPEN_DRAIN':
                    self.OpenDrainButton.setChecked(True)
            elif self.ConfigurationPinList[Pinname]['Mode'] == 'DIO_u8_INPUT_':
                self.Output_ConfigBox.setDisabled(True)
                self.Input_ConfigBox.setEnabled(True)
                self.PinValueBox.setDisabled(True)
                self.InputButton.setChecked(True)
                if self.ConfigurationPinList[Pinname]['Config'] == 'PULL_UP':
                    self.PullupButton.setChecked(True)
                elif self.ConfigurationPinList[Pinname]['Config'] == 'PULL_DOWN':
                    self.PullDownButton.setChecked(True)

    def ShowPinItem(self):
        cuItem = self.ucPinList.currentRow ()
        print cuItem
        if cuItem == -1:
            cuItem = 0
        self.Pin_ConfigBox.setTitle(QtGui.QApplication.translate("MainWindow", "Pin"+str(cuItem)+" Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.ShowPinConfiguration('PIN'+str(cuItem))


    def SaveConfigurationFile(self):
        self.filedialog = QtGui.QFileDialog()
        name = self.filedialog.getSaveFileName()
        try:
            file = open(name[0],'w')
            Num_counter = 0
            file.write('Microcontroller Type =' + str(self.MicrocontrollerType.currentIndex())+'\n')
            for Num_counter in range(self.Max_Pin_Number):
                file.write('#define '+self.ConfigurationPinList['PIN'+str(Num_counter)]['Name']+'Direction'+'                                     '+
                self.ConfigurationPinList['PIN'+str(Num_counter)]['Mode']+self.ConfigurationPinList['PIN'+str(Num_counter)]['Config']+'\n')
            for Num_counter in range(self.Max_Pin_Number):
                file.write('#define '+self.ConfigurationPinList['PIN'+str(Num_counter)]['Name']+'Value'+'                                     '+
                self.ConfigurationPinList['PIN'+str(Num_counter)]['Value']+'\n')
            file.close()
        except IOError :
          print 'You did not enter a file name'
        

    def LoadConfigurationFile(self):
        self.filedialog = QtGui.QFileDialog()
        self.filedialog.setFileMode(QtGui.QFileDialog.AnyFile)
        #self.filedialog.setFilter("Text files (*.txt)")
        self.filedialog.setFilter("Text files (*.h)")
        filenames = self.filedialog.getOpenFileName()
        try:
            file = open(filenames[0], 'r')
            regexUCtype = r'\w+\sType =(\d)'
            ARMregexPinDir = r'.+_(PIN\d+)(\w+)+\s+(G\w+u+\w+T_)(\w+)'
            ARMregexPinValue = r'.+_(PIN\d+)(V\w+)+\s+(G\w+u+\w+)'
            AVRregexPinDir=r'.+_(PIN\d+)(\w+)+\s+(\w+u+\w+T_)(\w+)'
            AVRregexPinValue=r'.+_(PIN\d+)(V\w+)+\s+(\w+u+\w+)'
            if re.match(regexUCtype, file.readline()):
                file.seek(0)
                str1=re.search(regexUCtype,file.readline())
                print(str1)
                resint=int(str1.group(1))
                self.MicrocontrollerType.setCurrentIndex(resint)
            else:
                print 'This file is not suitable for pin configuration'
            ListLines=file.readlines()
            cuIndex = self.MicrocontrollerType.currentIndex()
            if cuIndex ==0:
                for line in ListLines:
                    if re.match(ARMregexPinDir, line):
                        str2=re.search(ARMregexPinDir,line)
                        self.ConfigurationPinList[str2.group(1)]['Mode']=str2.group(3)
                        self.ConfigurationPinList[str2.group(1)]['Config']=str2.group(4)
                file.seek(0)
                for line in ListLines:
                    if re.match(ARMregexPinValue, line):
                        str3=re.search(ARMregexPinValue,line)
                        self.ConfigurationPinList[str3.group(1)][str3.group(2)]=str3.group(3)
            else:
                for line in ListLines:
                    if re.match(AVRregexPinDir, line):
                        str2=re.search(AVRregexPinDir,line)
                        self.ConfigurationPinList[str2.group(1)]['Mode']=str2.group(3)
                        self.ConfigurationPinList[str2.group(1)]['Config']=str2.group(4)
                file.seek(0)
                for line in ListLines:
                    if re.match(AVRregexPinValue, line):
                        str3=re.search(AVRregexPinValue,line)
                        self.ConfigurationPinList[str3.group(1)][str3.group(2)]=str3.group(3)
        except IOError :
          print 'You did not enter a file name'
        self.ShowPinConfiguration('PIN0')

    def SetPinName(self):
        cuItem = self.ucPinList.currentRow ()
        print cuItem
        if cuItem == -1:
            cuItem = 0
        self.ConfigurationPinList['PIN'+str(cuItem)]['Name'] = self.Pin_NameEdit.text()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())