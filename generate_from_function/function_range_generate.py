import math

import timesynth as ts
import numpy as np
import matplotlib.pyplot as plt


def self_defined_function(x_interval, time_interval, time_sampler, math_function):
    x = []
    for time_point in time_sampler:
        x_index = (x_interval[1]-x_interval[0])/(time_interval[1]-time_interval[0])*(time_point-time_interval[0])+x_interval[0]
        x.append(x_index)
    func = map(lambda x: math_function(x), [item for item in x])
    return time_sampler, list(func)



def generate_timeseries(math_exp, x_interval, time_interval, point_numbers, sample_percentage, measure_point_name, noise_std):
    # x_interval = [-10, 10]
    import datetime
    import time
    # time_interval = ["2022-01-24 00:00:00", "2022-02-24 00:00:00"]
    # measure_point_name = "concave"
    # 进行插值的时候需要转化成unix_time格式
    time_interval_unix_time = []
    for time_point in time_interval:
        time_interval_unix_time.append(time.mktime(time.strptime(time_point, "%Y-%m-%d %H:%M:%S")))

    datetime.datetime.strptime(time_interval[0], "%Y-%m-%d %H:%M:%S")
    # time_interval = [1642989836.123, 1645668236]

    time_sampler = ts.TimeSampler(start_time=time_interval_unix_time[0], stop_time=time_interval_unix_time[1])
    # Sampling irregular time samples
    irregular_time_samples = time_sampler.sample_irregular_time(num_points=point_numbers, keep_percentage=sample_percentage)
    x, y = self_defined_function(x_interval, time_interval_unix_time, irregular_time_samples, math_exp)
    white_noise = ts.noise.GaussianNoise(std=noise_std)

    irregular_time_samples_str = []
    output_file = open(measure_point_name + ".csv", "w")
    output_file.write("Time," + measure_point_name + '\n')
    for i in range(len(irregular_time_samples)):
        temp = datetime.datetime.fromtimestamp(irregular_time_samples[i])
        irregular_time_samples_str.append(temp.strftime("%Y-%m-%dT%H:%M:%S.000+08:00"))
        output_file.write(irregular_time_samples_str[i] + ',' + str(y[i]) + '\n')
    plt.plot(irregular_time_samples_str, y + white_noise.sample_vectorized(irregular_time_samples))
    plt.show()
    output_file.close()

# math_exp: 通过math.xxx调用或者写lambda表达式
generate_timeseries(math_exp=lambda x: -x*x,
                    x_interval=[-10, 10],
                    time_interval=["2022-01-24 00:00:00", "2022-02-24 00:00:00"],
                    point_numbers=500,
                    sample_percentage=60,
                    measure_point_name="convex",
                    noise_std=10)