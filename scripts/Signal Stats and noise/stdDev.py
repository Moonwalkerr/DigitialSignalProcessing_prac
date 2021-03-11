import mysignals as sig

_mean = 0.0
_variance = 0.0

def calculate_std_Deviation(signal_arr):
    # referencing the deinfed global variables inside the function
    global _mean, _variance
    
    # calculating mean of the signal
    for i in range(len(signal_arr)):
        _mean += signal_arr[i]
    _mean = _mean / len(signal_arr)

    # calculating variance of the signal from calcuated mean
    for v in range(len(signal_arr)):
        _variance += (signal_arr[v] - _mean)**2
    _variance = _variance / len(signal_arr)

    # Now calculating the square root of the variance
    # to find out the standard deviation
    std = _variance ** (0.5)
    
    return std

std_signal = calculate_std_Deviation(sig.InputSignal_1kHz_15kHz)

print("The standard deviation of the signal is :", std_signal)