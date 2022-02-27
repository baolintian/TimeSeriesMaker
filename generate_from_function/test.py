from timeseries_generator import LinearTrend, Generator, WhiteNoise, RandomFeatureFactor
import pandas as pd

# setting up a linear tren
lt = LinearTrend(coef=2.0, offset=0.01, col_name="my_linear_trend")
g = Generator(factors={lt}, features=None, date_range=pd.date_range(start="01-01-2020 00:00:00", end="02-01-2022 00:00:00"))
g.generate()

g.plot()

# update by adding some white noise to the generator
wn = WhiteNoise(stdev_factor=0.05)
g.update_factor(wn)
g.generate()
g.plot()