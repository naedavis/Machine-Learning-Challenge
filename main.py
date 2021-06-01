#Naeeemah Davis
#Challenge 1
#Write a NumPy program to compute the mean, standard deviation,
# and variance of a given array along the second axis.
# Use np.arange function to generate 20 numbers starting from 0.
#import numpy in order to use built in functions
import numpy as np
#arange() used to save time instead of manually creating an array of numbers eg nums = [1,2,3,4,5...]
num = np.arange(1,21)
#creating a variable to store the mean of given list
my_mean = np.mean(num)
#creating a variable to store standard deviation value
my_std = np.std(num)
#creating a variable to store variance value
my_variance= np.var(num)
#printing all variable declared with their values 
print("numbers:" + str(num) + "\n" +
      "Mean: " + str(my_mean) + "\n" +
      "Standard Deviation: " + str(my_std) + "\n" +
      "variance: " + str(my_variance))


#Challenge 2
#Write a NumPy program to compute the histogram of nums against the bins.
#  Label your x-axis with nums and y-axis with bins.
# Add a title to the histogram: Histogram of nums against bins.
#import matplotlib in order to have a graph so we can plot values
import matplotlib.pyplot as plt

#given values nums and bins to be plotted on histogram
nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]
#x-axis name
plt.xlabel(' NUMS ')
#y-axis name
plt.ylabel('BINS')
#histogram title
plt.title('Histogram of nums against bins')
# using the "hist" for histogram
#syaing which values should be plotted on the histograms(nums and bins) 
#also making the colour of the graph green bc green is cool
plt.hist(nums, bins, color='green')
#executing the histogram
plt.show()
