import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def plot_random():
    x = [1, 2, 4, 6, 7]
    y = [4, 3, 6, 2, 8]
    x1 = [5, 3, 8, 1, 9]
    y1 = [2, 1, 1, 2, 4.5]
    if len(x) == len(y) and len(x1)==len(y1):
        style.use("dark_background")
        plt.figure(figsize=(12,6))
        # plt.plot(np.sin(x), np.sin(y), color='r', label='First Signal')
        plt.plot(x1, y1, color='g', label='Second Signal')
        plt.title("Random Signal Plotting")
        plt.show()
# plot_random()

def multiplot_random_signal():
    signal = np.random.randn(300)
    style.use("ggplot")
    style.use("dark_background")
    f, plt_arr =  plt.subplots(3, sharex=True, sharey=True)
    f.suptitle("Multiplot of Signals")
    plt_arr[0].plot(signal[0:100], color='magenta')
    plt_arr[1].plot(signal[100:200], color='red')
    plt_arr[2].plot(signal[200:300], color='blue')
    plt.savefig("Multiplot Signal Plotting")
    plt.show()
# multiplot_random_signal()


def plot_signal(fr1,fr2):
    time = np.linspace(0,1.0,num=2000)
    _fr1 = fr1 
    _fr2 = fr2
    signal_1hz = np.sin(2*np.pi*_fr1*time)
    signal_2hz = np.sin(2*np.pi*_fr2*time)
    combined_signal = signal_1hz + signal_2hz
    # style.use("ggplot")
    style.use("dark_background")
    # plt.figure(figsize=(20,12))
    f, plt_arr = plt.subplots(3, sharex=True)
    f.suptitle("Multiplot of signals of {} and {} hz".format(_fr1,_fr2))
    plt_arr[0].plot(signal_1hz,color='yellow')
    plt_arr[0].set_title("{} Hz Sine Wave".format(_fr1), color='red')
    plt_arr[1].plot(signal_2hz,color='blue')
    plt_arr[1].set_title("{} Hz Sine Wave".format(_fr2), color='red')
    plt_arr[2].plot(combined_signal,color='magenta')
    plt_arr[2].set_title("Combined Sine Wave", color='red')
    plt.savefig("TwoSignals")
    plt.show()
plot_signal(5,30)