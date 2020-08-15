# Importing header files
import numpy as np
import warnings


warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((data , new_record), axis = 0)

age = census[:,[0]]

max_age = age.max()
min_age = age.min()
age_mean = np.mean(age)
age_std = np.std(age)

print(max_age, min_age, age_mean, age_std)

race = census[:,[2]]

race_0 = race[race == 0]
len_0 = len(race_0)

race_1 = race[race == 1]
len_1 = len(race_1)

race_2 = race[race == 2]
len_2 = len(race_2)

race_3 = race[race == 3]
len_3 = len(race_3)

race_4 = race[race == 4]
len_4 = len(race_4)

minority_race = 3
print(minority_race)

senior_citizens = age[age>60]
senior_citizens_len = len(senior_citizens)

workinghours = census[:,[6]]

working_hours = []
for i in range(len(age)):
    if age[i] > 60:
        working_hours.append(workinghours[i])

working_hours_sum = np.sum(working_hours)

avg_working_hours = working_hours_sum/senior_citizens_len
print(round(avg_working_hours,2))

education_num = census[:,[1]]

high = education_num[education_num > 10]
low = education_num[education_num <= 10]

income = census[:,[7]]

income_high = []
for i in range(len(education_num)):
    if education_num[i] > 10:
       income_high.append(income[i])

income_low = []
for i in range(len(education_num)):
    if education_num[i] <= 10:
       income_low.append(income[i])

avg_pay_high = np.mean(income_high)
avg_pay_low = np.mean(income_low)

print(round(avg_pay_high,2))
print(round(avg_pay_low,2))
