# Signal mean algorithm from scratch
import mysignals as sig

_mean = 0.0

def calculate_signal_mean(signal_arr):
    global _mean
    for i in range(len(signal_arr)):
        _mean += signal_arr[i]
    _mean = _mean /len(signal_arr)
    return _mean


mean_sig = calculate_signal_mean(sig.)