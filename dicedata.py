import random
import statistics
import plotly.figure_factory as ff

#Creating a list of sum of 2 dice, rolled 1000 times
dice_result =[]
for i in range(0, 1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)

#Calculating the mean, median, mode and the standard deviation
mean = sum(dice_result)/len(dice_result)
print("Mean of this data is {}".format(mean))

median = statistics.median(dice_result)
print("Median of this data is {}".format(median))

mode = statistics.mode(dice_result)
print("Mode of this data is {}".format(mode))

std_deviation = statistics.stdev(dice_result)
print("Standard deviation of this data is {}".format(std_deviation))

#Finding 1 standard deviation stard and end values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))


#Finding 2 standard deviation stard and end values
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2* std_deviation)
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))

#Finding 3 standard deviation stard and end values
third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean + (3* std_deviation)
list_of_data_within_3_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))

fig = ff.create_distplot([dice_result], ["Result"], show_hist=False)
fig.show() 