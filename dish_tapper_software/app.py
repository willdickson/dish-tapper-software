import sys
import time
import collections
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import importlib.resources as pkg_resourses

from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets


from .ui_main_window import Ui_MainWindow
from . import config
from . import pulse_utils

class AppMainWindow(QtWidgets.QMainWindow):

    START_STOP_BUTTON_TEXT = {
            True  : 'Stop',
            False : 'Start',
            }

    TIMER_DT_MS = 100
    PULSE_SEQ_MAX_VALUE = 1.0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_timer)
        self.channel_to_widget = collections.OrderedDict((
            ('Channel A', self.ui.channelAWidget), 
            ('Channel B', self.ui.channelBWidget),
            ))
        self.running = False
        self.start_time = 0.0
        self.set_default_values()
        self.connect_actions()

    def check_config(self):
        if not config.sequence['length'] is int:
            raise ValueError('sequence length must be an integer')
        if not config.sequence['length'] > 0:
            raise ValueError('sequence length must be > 0')

    def set_default_values(self):
        for name, widget in self.channel_to_widget.items():
            widget.set_label_text(name)
            widget.set_frequency_minimum(config.frequency['min'])
            widget.set_amplitude_minimum(config.amplitude['min'])
            widget.set_lowpass_minimum(config.lowpass['min'])
            widget.set_frequency_maximum(config.frequency['max'])
            widget.set_amplitude_maximum(config.amplitude['max'])
            widget.set_lowpass_maximum(config.lowpass['max'])
            widget.set_frequency(config.frequency['default'])
            widget.set_amplitude(config.amplitude['default'])
            widget.set_lowpass(config.lowpass['default'])
            widget.set_lowpass_checked(config.lowpass['enabled'])

        self.ui.hrSpinBox.setMinimum(0)
        self.ui.minSpinBox.setMinimum(0)
        self.ui.secSpinBox.setMinimum(0)
        self.ui.hrSpinBox.setValue(config.duration_default['hour'])
        self.ui.minSpinBox.setValue(config.duration_default['minute'])
        self.ui.secSpinBox.setValue(config.duration_default['second'])
        self.set_start_stop_button_text()
        self.ui.progressBar.setValue(0)

    def connect_actions(self):
        self.ui.startStopPushButton.clicked.connect(self.on_start_stop_button)
        self.ui.plotPushButton.clicked.connect(self.on_plot_button)

    def on_timer(self):
        now = time.time()
        elapsed_time = now - self.start_time
        progress = 100*elapsed_time/self.duration
        self.ui.progressBar.setValue(progress)
        if elapsed_time >= self.duration:
            self.stop_audio()
            self.timer.stop()
            self.running = False
            self.set_start_stop_button_text()

    def on_start_stop_button(self):
        self.running = not self.running
        self.set_start_stop_button_text()
        if self.running:
            self.start_time = time.time()
            self.timer.start(self.TIMER_DT_MS)
            self.set_widgets_enabled(False)
            self.start_audio()
        else:
            self.timer.stop()
            self.set_widgets_enabled(True)
            self.stop_audio()

    def on_plot_button(self):
        self.fig, self.ax = plt.subplots(2,1,num=1)
        t, seq = self.get_audio_seq()
        self.ax[0].set_title('Audio Signal')
        self.ax[0].plot(t, seq[:,0])
        self.ax[0].grid(True)
        self.ax[0].set_ylabel('chan 1')

        self.ax[1].plot(t, seq[:,1])
        self.ax[1].grid(True)
        self.ax[1].set_ylabel('Channel 1')
        self.ax[1].set_ylabel('t (sec)')
        plt.show()


    def set_start_stop_button_text(self):
        self.ui.startStopPushButton.setText(self.START_STOP_BUTTON_TEXT[self.running])

    def set_widgets_enabled(self, value):
        self.ui.durationWidget.setEnabled(value)
        self.ui.channelAWidget.setEnabled(value)
        self.ui.channelBWidget.setEnabled(value)

    def start_audio(self):
        sd.stop()
        sample_rate = config.sequence['sample_rate']
        t, seq_array = self.get_audio_seq()
        sd.play(seq_array, sample_rate, loop=True)

    def stop_audio(self):
        sd.stop()

    def get_audio_seq(self):
        pulse_dt = config.sequence['pulse_dt']
        seq_length = config.sequence['length']
        sample_rate = config.sequence['sample_rate']
        seq_list = []
        for name, widget in self.channel_to_widget.items():
            frequency = widget.frequency()
            amplitude = widget.amplitude()
            if widget.lowpass_checked():
                lowpass = widget.lowpass()
            else:
                lowpass = None
            max_amplitude = widget.amplitude_maximum()
            t, seq = pulse_utils.pulse_sequence( 
                    [frequency], 
                    pulse_dt=pulse_dt, 
                    length=seq_length, 
                    cutoff_freq=lowpass, 
                    rate=sample_rate)
            relative_amplitude = (amplitude/max_amplitude)
            seq = seq*self.PULSE_SEQ_MAX_VALUE*relative_amplitude
            seq_list.append(seq)
        seq_array = np.hstack(seq_list)
        return t, seq_array 

    @property
    def duration(self):
        hours   = self.ui.hrSpinBox.value()
        minutes = self.ui.minSpinBox.value()
        seconds = self.ui.secSpinBox.value()
        duration = 360*hours + 60*minutes + seconds
        return duration

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = AppMainWindow()
    win.show()
    sys.exit(app.exec())




