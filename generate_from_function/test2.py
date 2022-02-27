import timesynth as ts
# Initializing TimeSampler
time_sampler = ts.TimeSampler(start_time=1642989836, stop_time=1645668236)
# Sampling irregular time samples
irregular_time_samples = time_sampler.sample_irregular_time(num_points=500, keep_percentage=50)
# Initializing Sinusoidal signal
# 这里选择了时间序列的波形
sinusoid = ts.signals.Sinusoidal(frequency=0.25)
# Initializing Gaussian noise
white_noise = ts.noise.GaussianNoise(std=250)
# Initializing TimeSeries class with the signal and noise objects
timeseries = ts.TimeSeries(sinusoid, noise_generator=white_noise)
# Sampling using the irregular time samples
samples, signals, errors = timeseries.sample(irregular_time_samples)
print(samples)