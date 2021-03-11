# calculating the signal variance from scratch
# importing sample signals file
import mysignals as sig

_mean = 0.0
_variance = 0.0

def calc_variance(signal_arr):
    global _mean, _variance
    for i in range(len(signal_arr)):
        _mean += signal_arr[i]
    _mean = _mean / len(signal_arr)

    # calculating variance
    # we need to substract each data points of the signal with the calcualted mean
    # and then take square of each data points 
    # in order to calculate the variance

    for v in range(len(signal_arr)):
        _variance += (signal_arr[v]- _mean)**2
    _variance = _variance / len(signal_arr)
    return _variance


sig_var = calc_variance(sig.InputSignal_1kHz_15kHz)

print("The variance of the given signal is : ", sig_var)
