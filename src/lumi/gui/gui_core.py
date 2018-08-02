# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        # initializing Dialog window
        Dialog.setObjectName("Dialog")
        Dialog.resize(721, 424)

        # create the 'gridLayout' layout
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        # create an horizontal layout with index 5
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        # create a vertical layout with index 2
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # create and set a tab widget
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        # create a tab named 'tab'
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        # create a vertical layout with index 3 in tab
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # create a frame wrapping lists and distro description with name 'lists_and_distro_description_frame'
        self.lists_and_distro_description_frame = QtWidgets.QFrame(self.tab)
        self.lists_and_distro_description_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lists_and_distro_description_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lists_and_distro_description_frame.setObjectName("lists_and_distro_description_frame")
        
        # create an horizontal layout in the 'lists_and_distro_description_frame' frame with index 2
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.lists_and_distro_description_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        # set a frame wrapping the installed distro list with name 'installed_distro_list_frame'
        self.installed_distro_list_frame = QtWidgets.QFrame(self.lists_and_distro_description_frame)
        self.installed_distro_list_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.installed_distro_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.installed_distro_list_frame.setObjectName("installed_distro_list_frame")

        # create and set a vertical with index 7 layout to the 'installed_distro_list_frame' frame
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.installed_distro_list_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # create and set a label for in 'installed_distro_list_frame' 
        self.installed_distro_list_label = QtWidgets.QLabel(self.installed_distro_list_frame)
        self.installed_distro_list_label.setObjectName("installed_distro_list_label")
        self.verticalLayout_7.addWidget(self.installed_distro_list_label)

        # create and set a listWidget (for installed distros) in installed_distro_list_frame
        self.installed_distros_listWidget = QtWidgets.QListWidget(self.installed_distro_list_frame)
        self.installed_distros_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.installed_distros_listWidget.setObjectName("installed_distros_listWidget")

        # create and set an item fon the installed distros listWidget
        item = QtWidgets.QListWidgetItem()
        self.installed_distros_listWidget.addItem(item)
        
        # add to vertical layout 7 the installed distros listWidget widget
        self.verticalLayout_7.addWidget(self.installed_distros_listWidget)
        
        # create and set push button to uninstall the installed distros to vertical layout 7
        self.uninstall_installed_distros_pushButton = QtWidgets.QPushButton(self.installed_distro_list_frame)
        self.uninstall_installed_distros_pushButton.setEnabled(False)
        self.uninstall_installed_distros_pushButton.setObjectName("uninstall_installed_distros_pushButton")
        self.verticalLayout_7.addWidget(self.uninstall_installed_distros_pushButton)
        
        # create and set installed stage3 files label to vertical layout 7
        self.installed_stage3_files_label = QtWidgets.QLabel(self.installed_distro_list_frame)
        self.installed_stage3_files_label.setObjectName("installed_stage3_files_label")
        self.verticalLayout_7.addWidget(self.installed_stage3_files_label)

        # create an installed stage3 files listWidget widget
        self.installed_stage3_listWidget = QtWidgets.QListWidget(self.installed_distro_list_frame)
        self.installed_stage3_listWidget.setObjectName("installed_stage3_listWidget")

        # create and set an item to installed stage3 files listWidget widget
        item = QtWidgets.QListWidgetItem()
        self.installed_stage3_listWidget.addItem(item)

        # set installed stage3 files listWidget widget to vertical layout 7
        self.verticalLayout_7.addWidget(self.installed_stage3_listWidget)
        
        # create and set an uninstall installed stage3 pushButtom widget to vertiacal layout 7
        self.uninstall_installed_stage3_pushButton = QtWidgets.QPushButton(self.installed_distro_list_frame)
        self.uninstall_installed_stage3_pushButton.setObjectName("uninstall_installed_stage3_pushButton")
        self.verticalLayout_7.addWidget(self.uninstall_installed_stage3_pushButton)
        
        # set 'installed_distro_list_frame' frame to horizontal layout with index 2
        self.horizontalLayout_2.addWidget(self.installed_distro_list_frame)

        # create a 'available_distro_list_frame' frame 
        self.available_distro_list_frame = QtWidgets.QFrame(self.lists_and_distro_description_frame)
        self.available_distro_list_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.available_distro_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.available_distro_list_frame.setObjectName("available_distro_list_frame")

        # set a vertical layout with index 5 to 'available_distro_list_frame' frame
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.available_distro_list_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # create and set a 'available_distro_list_label' label to vertical layout with index 5
        self.available_distro_list_label = QtWidgets.QLabel(self.available_distro_list_frame)
        self.available_distro_list_label.setObjectName("available_distro_list_label")
        self.verticalLayout_5.addWidget(self.available_distro_list_label)

        # create a 'available_distros_listWidget' listWidget 
        self.available_distros_listWidget = QtWidgets.QListWidget(self.available_distro_list_frame)
        self.available_distros_listWidget.setObjectName("available_distros_listWidget")

        # create and set an Item for 'available_distros_listWidget' istWidget
        item = QtWidgets.QListWidgetItem()
        self.available_distros_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.available_distros_listWidget.addItem(item)

        # add 'available_distros_listWidget' listWidget to vertical layout with index 5
        self.verticalLayout_5.addWidget(self.available_distros_listWidget)

        #create and set a 'install_available_distros_pushButton' pushButton to vertical layout with index 5
        self.install_available_distros_pushButton = QtWidgets.QPushButton(self.available_distro_list_frame)
        self.install_available_distros_pushButton.setEnabled(False)
        self.install_available_distros_pushButton.setObjectName("install_available_distros_pushButton")
        self.verticalLayout_5.addWidget(self.install_available_distros_pushButton)

        # create and set a 'available_stage3_files_label' label to vertical layout with index 5
        self.available_stage3_files_label = QtWidgets.QLabel(self.available_distro_list_frame)
        self.available_stage3_files_label.setObjectName("available_stage3_files_label")
        self.verticalLayout_5.addWidget(self.available_stage3_files_label)

        # create a 'available_stage3_listWidget' listWidget
        self.available_stage3_listWidget = QtWidgets.QListWidget(self.available_distro_list_frame)
        self.available_stage3_listWidget.setObjectName("available_stage3_listWidget")

        # create and set a 'available_stage3_listWidget' listWidget's item to vertical layout with index 5
        item = QtWidgets.QListWidgetItem()
        self.available_stage3_listWidget.addItem(item)
        self.verticalLayout_5.addWidget(self.available_stage3_listWidget)

        # create and set a 'install_available_stage3_pushButton' pushButton to vertical layout with index 5
        self.install_available_stage3_pushButton = QtWidgets.QPushButton(self.available_distro_list_frame)
        self.install_available_stage3_pushButton.setEnabled(False)
        self.install_available_stage3_pushButton.setObjectName("install_available_stage3_pushButton")
        self.verticalLayout_5.addWidget(self.install_available_stage3_pushButton)

        # add 'available_distro_list_frame' frame to horizontal layout with index 2
        self.horizontalLayout_2.addWidget(self.available_distro_list_frame)

        # create a 'distro_description_frame' frame
        self.distro_description_frame = QtWidgets.QFrame(self.lists_and_distro_description_frame)
        self.distro_description_frame.setEnabled(True)
        self.distro_description_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.distro_description_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.distro_description_frame.setObjectName("distro_description_frame")

        # create a vertical layout with index 6
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.distro_description_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # create and set a 'distro_description_label' label to vertical layout with index 6
        self.distro_description_label = QtWidgets.QLabel(self.distro_description_frame)
        self.distro_description_label.setObjectName("distro_description_label")
        self.verticalLayout_6.addWidget(self.distro_description_label)

        # create and set a 'distro_description_textBrowser' textBrowser to vertical layout with index 6
        self.distro_description_textBrowser = QtWidgets.QTextBrowser(self.distro_description_frame)
        self.distro_description_textBrowser.setMinimumSize(QtCore.QSize(200, 0))
        self.distro_description_textBrowser.setObjectName("distro_description_textBrowser")
        self.verticalLayout_6.addWidget(self.distro_description_textBrowser)

        # add 'distro_description_frame' frame to horizontal layout with index 2
        self.horizontalLayout_2.addWidget(self.distro_description_frame)

        # add 'lists_and_distro_description_frame' frame to vertical layout with index 3
        self.verticalLayout_3.addWidget(self.lists_and_distro_description_frame)

        # create an horizontal layout with index 0
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # create a 'progressBar' progressBar
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 55)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")

        # add 'progressBar' progressBar widget to horizontl layout with index 0
        self.horizontalLayout.addWidget(self.progressBar)

        #add horizontal layout with index 0 to vertical layout with index 3
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        
        # add 'tab' tab to tabWidget
        self.tabWidget.addTab(self.tab, "")
        """
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        """

        # add tabWidget to vertical layout with index 2
        self.verticalLayout_2.addWidget(self.tabWidget)

        # add vertical layout with index 2 to horizontal layout with index 5
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        # add horizontal layout with index 5 to the 'gridLayout' gridLayout
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        # set buddies
        self.installed_distro_list_label.setBuddy(self.installed_distros_listWidget)
        self.installed_stage3_files_label.setBuddy(self.installed_stage3_listWidget)
        self.available_distro_list_label.setBuddy(self.available_distros_listWidget)
        self.available_stage3_files_label.setBuddy(self.available_stage3_listWidget)
        self.distro_description_label.setBuddy(self.distro_description_textBrowser)
        
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        self.available_distros_listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.installed_distro_list_label.setText(_translate("Dialog", "I&nstalled distros"))
        __sortingEnabled = self.installed_distros_listWidget.isSortingEnabled()
        self.installed_distros_listWidget.setSortingEnabled(False)
        item = self.installed_distros_listWidget.item(0)
        item.setText(_translate("Dialog", "ubuntu"))
        self.installed_distros_listWidget.setSortingEnabled(__sortingEnabled)
        self.uninstall_installed_distros_pushButton.setText(_translate("Dialog", "Uninstall"))
        self.installed_stage3_files_label.setText(_translate("Dialog", "Installed sta&ge3"))
        __sortingEnabled = self.installed_stage3_listWidget.isSortingEnabled()
        self.installed_stage3_listWidget.setSortingEnabled(False)
        item = self.installed_stage3_listWidget.item(0)
        item.setText(_translate("Dialog", "gentoo"))
        self.installed_stage3_listWidget.setSortingEnabled(__sortingEnabled)
        self.uninstall_installed_stage3_pushButton.setText(_translate("Dialog", "Uninstall"))
        self.available_distro_list_label.setText(_translate("Dialog", "Avai&lable distros"))
        __sortingEnabled = self.available_distros_listWidget.isSortingEnabled()
        self.available_distros_listWidget.setSortingEnabled(False)
        item = self.available_distros_listWidget.item(0)
        item.setText(_translate("Dialog", "ubuntu"))
        item = self.available_distros_listWidget.item(1)
        item.setText(_translate("Dialog", "arch"))
        self.available_distros_listWidget.setSortingEnabled(__sortingEnabled)
        self.install_available_distros_pushButton.setText(_translate("Dialog", "Install"))
        self.available_stage3_files_label.setText(_translate("Dialog", "Available stage&3"))
        __sortingEnabled = self.available_stage3_listWidget.isSortingEnabled()
        self.available_stage3_listWidget.setSortingEnabled(False)
        item = self.available_stage3_listWidget.item(0)
        item.setText(_translate("Dialog", "gentoo"))
        self.available_stage3_listWidget.setSortingEnabled(__sortingEnabled)
        self.install_available_stage3_pushButton.setText(_translate("Dialog", "Install"))
        self.distro_description_label.setText(_translate("Dialog", "Distro descri&ption"))
        self.distro_description_textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Something Dom will write too lazy for lorem ipsum so bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla  bla </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "/dev/sdb"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
