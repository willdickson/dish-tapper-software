# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

from .channel_form import ChannelForm

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 250))
        MainWindow.setMaximumSize(QSize(800, 250))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.durationWidget = QWidget(self.centralwidget)
        self.durationWidget.setObjectName(u"durationWidget")
        self.horizontalLayout = QHBoxLayout(self.durationWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.durationLabel = QLabel(self.durationWidget)
        self.durationLabel.setObjectName(u"durationLabel")
        font = QFont()
        font.setBold(True)
        self.durationLabel.setFont(font)

        self.horizontalLayout.addWidget(self.durationLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.hrSpinBox = QSpinBox(self.durationWidget)
        self.hrSpinBox.setObjectName(u"hrSpinBox")
        self.hrSpinBox.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.hrSpinBox)

        self.hourUnitLabel = QLabel(self.durationWidget)
        self.hourUnitLabel.setObjectName(u"hourUnitLabel")

        self.horizontalLayout.addWidget(self.hourUnitLabel)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.minSpinBox = QSpinBox(self.durationWidget)
        self.minSpinBox.setObjectName(u"minSpinBox")
        self.minSpinBox.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.minSpinBox)

        self.minUnitLabel = QLabel(self.durationWidget)
        self.minUnitLabel.setObjectName(u"minUnitLabel")

        self.horizontalLayout.addWidget(self.minUnitLabel)

        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.secSpinBox = QSpinBox(self.durationWidget)
        self.secSpinBox.setObjectName(u"secSpinBox")
        self.secSpinBox.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.secSpinBox)

        self.secUnitLabel = QLabel(self.durationWidget)
        self.secUnitLabel.setObjectName(u"secUnitLabel")

        self.horizontalLayout.addWidget(self.secUnitLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.plotPushButton = QPushButton(self.durationWidget)
        self.plotPushButton.setObjectName(u"plotPushButton")

        self.horizontalLayout.addWidget(self.plotPushButton)

        self.horizontalSpacer_7 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addWidget(self.durationWidget)

        self.channelAWidget = ChannelForm(self.centralwidget)
        self.channelAWidget.setObjectName(u"channelAWidget")
        self.channelAWidget.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.channelAWidget)

        self.channelBWidget = ChannelForm(self.centralwidget)
        self.channelBWidget.setObjectName(u"channelBWidget")
        self.channelBWidget.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.channelBWidget)

        self.startStopWidget = QWidget(self.centralwidget)
        self.startStopWidget.setObjectName(u"startStopWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.startStopWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startStopPushButton = QPushButton(self.startStopWidget)
        self.startStopPushButton.setObjectName(u"startStopPushButton")
        self.startStopPushButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.startStopPushButton)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(self.startStopWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 0))
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.startStopWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dish Tapper", None))
        self.durationLabel.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.hourUnitLabel.setText(QCoreApplication.translate("MainWindow", u"(hr) ", None))
        self.minUnitLabel.setText(QCoreApplication.translate("MainWindow", u"(min)", None))
        self.secUnitLabel.setText(QCoreApplication.translate("MainWindow", u"(sec)", None))
        self.plotPushButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.startStopPushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

