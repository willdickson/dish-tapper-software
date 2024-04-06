
channel_names = ['A', 'B']

sequence = {
        'length'      : 1,     # pulse sequence length (s), for looping output (integer > 0)
        'sample_rate' : 44100, # pulse sequence sample rate (samples/s)
        'pulse_dt'    : 0.005, # pulse duration (s)
        }

frequency = {
        'min'     : 1,         # miminum allowed frequency (Hz)
        'max'     : 200,       # maximum allowed frequency (Hz)
        'default' : 2,         # default frequency setting (Hz)
        }

amplitude = {
        'min'     : 0,         # minimum allowed amplitude (unitless?)
        'max'     : 100,       # maximum allowed amplitude (unitless?)
        'default' : 50,        # default amplitude setting (unitless?)
        }

lowpass = {
        'min'     : 100.0,     # minimum lowpass filter cutoff frequency (Hz)
        'max'     : 20000.0,   # maximum lowpass filter cutoff frequency (Hz)
        'default' : 400.0,     # default lowpass filter cutoff frequency (Hz)
        'enabled' : True,      # lowpass filter enabled flag
        }

duration_default = {   
        'hour'   : 0,          # default hours setting for duration
        'minute' : 0,          # default minute setting for duration
        'second' : 10,         # default second setting for duration
        }
        

