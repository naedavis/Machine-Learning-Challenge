#Naeeemah Davis
#Challenge 1
#Write a NumPy program to compute the mean, standard deviation,
# and variance of a given array along the second axis.
# Use np.arange function to generate 20 numbers starting from 0.
import numpy as np
num = np.arange(1,21)
my_mean = np.mean(num)
my_std = np.std(num)
my_variance= np.var(num)
print("numbers:" + str(num) + "\n" +
      "Mean: " + str(my_mean) + "\n" +
      "Standard Deviation: " + str(my_std) + "\n" +
      "variance: " + str(my_variance))


#Challenge 2
#Write a NumPy program to compute the histogram of nums against the bins.
#  Label your x-axis with nums and y-axis with bins.
# Add a title to the histogram: Histogram of nums against bins.
import matplotlib.pyplot as plt

nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]
# x_pos = [i for i, _ in enumerate(nums)]
plt.xlabel(' NUMS ')
plt.ylabel('BINS')
plt.title('Histogram of nums against bins')
# plt.hist2d(x_pos, bins, color="green")
plt.hist(nums, bins, color='green')
plt.show()