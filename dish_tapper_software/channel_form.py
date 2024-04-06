from PySide6 import QtWidgets
from .ui_channel_form import Ui_channelFormWidget
from . import config

class ChannelForm(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_channelFormWidget()
        self.ui.setupUi(self)

    def label_text(self):
        return self.ui.channelLabel.text()

    def frequency(self):
        return self.ui.frequencySpinBox.value()

    def amplitude(self):
        return self.ui.amplitudeSpinBox.value()

    def lowpass(self):
        return self.ui.lowpassSpinBox.value()

    def lowpass_checked(self):
        return self.ui.lowpassCheckBox.isChecked()

    def frequency_maximum(self):
        return self.ui.frequencySpinBox.maximum()

    def frequency_minimum(self):
        return self.ui.frequencySpinBox.minimum()

    def amplitude_maximum(self):
        return self.ui.amplitudeSpinBox.maximum()

    def amplitude_minimum(self):
        return self.ui.amplitudeSpinBox.minimum()

    def lowpass_maximum(self):
        return self.ui.lowpassSpinBox.maximum()

    def lowpass_minimum(self):
        return self.ui.lowpassSpinBox.minimum()

    def set_label_text(self, value):
        self.ui.channelLabel.setText(value)

    def set_frequency(self, value):
        self.ui.frequencySpinBox.setValue(value)

    def set_amplitude(self, value):
        self.ui.amplitudeSpinBox.setValue(value)

    def set_lowpass(self, value):
        self.ui.lowpassSpinBox.setValue(value)

    def set_frequency_maximum(self, value):
        self.ui.frequencySpinBox.setMaximum(value)

    def set_frequency_minimum(self, value):
        self.ui.frequencySpinBox.setMinimum(value)

    def set_amplitude_maximum(self, value):
        self.ui.amplitudeSpinBox.setMaximum(value)

    def set_amplitude_minimum(self, value):
        self.ui.amplitudeSpinBox.setMinimum(value)

    def set_lowpass_maximum(self, value):
        self.ui.lowpassSpinBox.setMaximum(value)

    def set_lowpass_minimum(self, value):
        self.ui.lowpassSpinBox.setMinimum(value)

    def set_lowpass_checked(self, value):
        self.ui.lowpassCheckBox.setChecked(value)








