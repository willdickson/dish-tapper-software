import collections
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import sounddevice as sd


def pulse_sequence(pulses, pulse_dt=0.01, length=1.0, cutoff_freq=800.0, rate=44100):
    """
    Creates a (multichannel) pulse sequence

    Parameters
    ----------
    pulses : int or array_like 
        number of pulses in sequence (single channel) or an array of integers specifying 
        the number of for each channel in the sequence.  

    pulse_dt : float or int 
        the duration of the pulses in seconds.

    length : float or int
        the duration of the sequence in seconds.

    cutoff_freq : float or int or None 
        the cutoff freqeuncy for lowpass filtering the pulses. If None then no lowpass 
        filtering is performed. 

    rate : int
        the sampling frequency of the sequence waveform (samples/second), e.g. 44100.

    """
    if not isinstance(pulses, (collections.abc.Sequence, np.ndarray)):
        pulses = np.array([pulses])
    else:
        pulses = np.array(pulses)
    t = np.arange(int(length*rate))/rate
    num_pts = len(t)
    num_chan = len(pulses)
    waveform = np.zeros((num_pts, num_chan),dtype=np.float64)
    for chan, num_pulse in enumerate(pulses):
        for i in range(num_pulse):
            t0 =  (i/num_pulse)*length + 1*pulse_dt
            t1 =  (i/num_pulse)*length + 2*pulse_dt
            mask = np.logical_and(t >= t0, t<=t1)
            waveform[mask,chan] = 1.0
    if cutoff_freq is not None: 
        b, a = signal.butter(4, cutoff_freq, fs=rate)
        for chan in range(num_chan):
            waveform[:,chan] = signal.filtfilt(b, a, waveform[:,chan])
    return t, waveform


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import time
    import sounddevice as sd

    pulses = [5,5]
    rate = 44100

    t, seq = pulse_sequence(pulses, pulse_dt=0.005, cutoff_freq=8000.0, rate=rate)

    num_chan = len(pulses)

    if 1:
        fig, ax = plt.subplots(num_chan, 1, sharex=True)
        for chan in range(num_chan):
            ax[chan].plot(t, seq[:,chan])
            ax[chan].grid(True)
            ax[chan].set_ylabel(f'chan {chan}')
        ax[chan].set_xlabel('t (sec)')
        plt.show()
    duration = 5.0

    if 0:
        sd.play(seq, rate, loop=True)
        time.sleep(duration)
        sd.stop()






