import matplotlib.pyplot as plt
import numpy as np

def get_func(x):
    return np.exp(-2*x)*np.cos(x)

def get_dif_func(x):
    return -2*np.exp(-2*x) * np.cos(x) - np.exp(-2*x) * np.sin(x)

def get_dif2_func(x):
    return 4 * np.exp(-2*x) * np.cos(x) + 4 * np.exp(-2*x) * np.sin(x) - np.exp(-2*x) * np.cos(x)

def diff_middle(y_right, y_left, step):
    return (y_right - y_left) / (2 * step)

def diff_right(y_right, y_current, step):
    return (y_right - y_current) / step

def diff2_precision2(y_left, y_current, y_right, step):
    return (y_right - 2*y_current + y_left)/step**2

def diff2_precision4(y_left_left, y_left, y_current, y_right, y_right_right, step):
    return (-y_right_right + 16*y_right - 30*y_current +16*y_left - y_left_left)/(12*step**2)

def get_errors(arr_default, arr_calculated):
    errors = []
    for i, f in enumerate(arr_default):
        errors.append(np.abs(f - arr_calculated[i]))
    return errors




left = -0.8
right = 0.8
#step = 0.01

for step in np.arange(0.01,0.21,0.01):

    arr_x = np.arange(left,right,step)
    arr_x_dif1_mid = arr_x[1:-1]
    arr_x_dif1_right = arr_x[:-1]
    arr_x_dif2_precision2 = arr_x[1:-1]
    arr_x_dif2_precision4 = arr_x[2:-2]

    func = [get_func(x) for x in arr_x]
    dif_func = [get_dif_func(x) for x in arr_x]
    dif2_func = [get_dif2_func(x) for x in arr_x]

    my_dif_func_mid = [diff_middle(func[i+1],func[i-1], step) for i in range(1,len(arr_x)-1)]
    my_dif_func_right = [diff_right(func[i+1], func[i], step) for i in range(len(arr_x)-1)]
    my_dif2_func_precision2 = [diff2_precision2(func[i-1], func[i], func[i+1], step) for i in range(1,len(arr_x)-1)]
    my_dif2_func_precision4 = [diff2_precision4(func[i-2], func[i-1], func[i], func[i+1], func[i+2], step) for i in range (2,len(arr_x)-2)]

    error_dif1_mid = get_errors(dif_func[1:-1], my_dif_func_mid)
    error_dif1_right = get_errors(dif_func[:-1], my_dif_func_right)
    error_dif2_precision2 = get_errors(dif2_func[1:-1], my_dif2_func_precision2)
    error_dif2_precision4 = get_errors(dif2_func[2:-2], my_dif2_func_precision4)

    plt.subplot(2,2,1)
    plt.title('dif1')
    plt.plot(arr_x, dif_func, color='b', label='default')
    plt.plot(arr_x_dif1_mid, my_dif_func_mid, color='r', label='middle')
    plt.plot(arr_x_dif1_right, my_dif_func_right, color='g', label='right')
    plt.legend()

    plt.subplot(2,2,2)
    plt.title('dif2')
    plt.plot(arr_x, dif2_func, color='b', label='default')
    plt.plot(arr_x_dif2_precision2, my_dif2_func_precision2, color='r', label='precision2')
    plt.plot(arr_x_dif2_precision4, my_dif2_func_precision4, color='g', label='precision4')
    plt.legend()

    plt.subplot(2,2,3)
    plt.title('dif1 errors')
    plt.plot(arr_x_dif1_mid, error_dif1_mid, color='r', label='middle error')
    plt.plot(arr_x_dif1_right, error_dif1_right, color='g', label='right error')
    plt.legend()

    plt.subplot(2,2,4)
    plt.title('dif2 errors')
    plt.plot(arr_x_dif2_precision2, error_dif2_precision2, color='r', label='precision2 error')
    plt.plot(arr_x_dif2_precision4, error_dif2_precision4, color='g', label='precision4 error')
    plt.legend()

    plt.figtext(0.05, 0.95, f"step: {round(step, 2)}", color='g')
    plt.show()

