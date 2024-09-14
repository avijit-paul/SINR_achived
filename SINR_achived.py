import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


mean = 22.98       # in dB
std_dev = 17.53
min_val = -1.69
max_val = 51.43   # in dB





num_samples = 10000 # will be equal to number of events run in the SEAMCAT simulation approx.
sinr_values = np.random.normal(loc=mean, scale=std_dev, size=num_samples)


sinr_values = np.clip(sinr_values, min_val, max_val)

sinr_values_sorted = np.sort(sinr_values) # sort SINR
cdf = np.arange(1, len(sinr_values_sorted) + 1) / len(sinr_values_sorted) # find CDF and range





plt.plot(sinr_values_sorted, cdf, label="SINR achieved (all)", color="red")
plt.xlabel('SINR (dB)')
plt.ylabel('Cumulative distribution function (CDF)')
plt.title('SINR achieved (all)')
plt.grid(True)
plt.legend(loc='lower right')
plt.show()
