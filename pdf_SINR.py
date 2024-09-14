import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


mean = 30
std_dev = 10
min_val = 5
max_val = 50    # in dB


num_samples = 10000 # same as number of events in SEAMCAT
sinr_values = np.random.normal(loc=mean, scale=std_dev, size=num_samples)


sinr_values = np.clip(sinr_values, min_val, max_val)


plt.hist(sinr_values, bins=50, density=True, alpha=0.6, color='g', label="Histogram")


x = np.linspace(min_val, max_val, 1000)
pdf = norm.pdf(x, mean, std_dev)
plt.plot(x, pdf, 'r', label="Normal PDF")

plt.xlabel('SINR (dB)')
plt.ylabel('Probability Density')
plt.title('SINR Probability Density Function (PDF)')
plt.grid(True)
plt.legend(loc='upper right')
plt.show()
