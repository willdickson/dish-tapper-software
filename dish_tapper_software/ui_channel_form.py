# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'channel_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_channelFormWidget(object):
    def setupUi(self, channelFormWidget):
        if not channelFormWidget.objectName():
            channelFormWidget.setObjectName(u"channelFormWidget")
        channelFormWidget.resize(786, 68)
        self.horizontalLayout = QHBoxLayout(channelFormWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.channelLabel = QLabel(channelFormWidget)
        self.channelLabel.setObjectName(u"channelLabel")
        font = QFont()
        font.setBold(True)
        self.channelLabel.setFont(font)

        self.horizontalLayout.addWidget(self.channelLabel)

        self.horizontalSpacer_1 = QSpacerItem(35, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_1)

        self.frequencyLabel = QLabel(channelFormWidget)
        self.frequencyLabel.setObjectName(u"frequencyLabel")

        self.horizontalLayout.addWidget(self.frequencyLabel)

        self.frequencySpinBox = QSpinBox(channelFormWidget)
        self.frequencySpinBox.setObjectName(u"frequencySpinBox")
        self.frequencySpinBox.setMinimumSize(QSize(60, 0))

        self.horizontalLayout.addWidget(self.frequencySpinBox)

        self.frequencyUnitLabel = QLabel(channelFormWidget)
        self.frequencyUnitLabel.setObjectName(u"frequencyUnitLabel")

        self.horizontalLayout.addWidget(self.frequencyUnitLabel)

        self.horizontalSpacer_2 = QSpacerItem(35, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.amplitudeLabel = QLabel(channelFormWidget)
        self.amplitudeLabel.setObjectName(u"amplitudeLabel")

        self.horizontalLayout.addWidget(self.amplitudeLabel)

        self.amplitudeSpinBox = QSpinBox(channelFormWidget)
        self.amplitudeSpinBox.setObjectName(u"amplitudeSpinBox")
        self.amplitudeSpinBox.setMinimumSize(QSize(60, 0))

        self.horizontalLayout.addWidget(self.amplitudeSpinBox)

        self.amplitudeUnitLabel = QLabel(channelFormWidget)
        self.amplitudeUnitLabel.setObjectName(u"amplitudeUnitLabel")

        self.horizontalLayout.addWidget(self.amplitudeUnitLabel)

        self.horizontalSpacer = QSpacerItem(35, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lowpassCheckBox = QCheckBox(channelFormWidget)
        self.lowpassCheckBox.setObjectName(u"lowpassCheckBox")

        self.horizontalLayout.addWidget(self.lowpassCheckBox)

        self.label_2 = QLabel(channelFormWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lowpassSpinBox = QSpinBox(channelFormWidget)
        self.lowpassSpinBox.setObjectName(u"lowpassSpinBox")
        self.lowpassSpinBox.setMinimumSize(QSize(90, 0))

        self.horizontalLayout.addWidget(self.lowpassSpinBox)

        self.horizontalSpacer_3 = QSpacerItem(404, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.retranslateUi(channelFormWidget)

        QMetaObject.connectSlotsByName(channelFormWidget)
    # setupUi

    def retranslateUi(self, channelFormWidget):
        channelFormWidget.setWindowTitle(QCoreApplication.translate("channelFormWidget", u"Form", None))
        self.channelLabel.setText(QCoreApplication.translate("channelFormWidget", u"Channel 1:", None))
        self.frequencyLabel.setText(QCoreApplication.translate("channelFormWidget", u"Frequency", None))
        self.frequencyUnitLabel.setText(QCoreApplication.translate("channelFormWidget", u"(Hz)", None))
        self.amplitudeLabel.setText(QCoreApplication.translate("channelFormWidget", u"Amplitude", None))
        self.amplitudeUnitLabel.setText(QCoreApplication.translate("channelFormWidget", u"(0 - 100)", None))
        self.lowpassCheckBox.setText(QCoreApplication.translate("channelFormWidget", u"Lowpass", None))
        self.label_2.setText(QCoreApplication.translate("channelFormWidget", u"(Hz)", None))
    # retranslateUi

