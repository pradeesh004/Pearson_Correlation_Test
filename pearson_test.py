import math
from scipy.stats import t,pearsonr

variable_1 =[9.17,6.11,2.5,8.61,5,2.22,7.5,7.78,6.94,8.61,6.11,5.56,8.06,9.17,8.33,9.17,9.72,8.61,7.22,6.39,3.61,8.89,3.06,2.5,1.67]
variable_2 = [6.1,5.3,5.8,8.7,2.4,0.3,7.8,8.4,5.5,10,7,4,7.1,9.8,9.3,10,9.7,8.6,6.1,5,3.7,8.3,1.3,1.3,1.7]
sample_count = len(variable_1)
degree_of_freedom = sample_count - 2

mean_variable_1= sum(variable_1)/len(variable_1)
mean_variable_2 = sum(variable_2)/len(variable_2)

sum_of_variance_of_2=0
sum_of_square_variance_variable_1 = 0
sum_of_square_variance_variable_2 = 0

for i in range(min(len(variable_1),len(variable_2))):
    sum_of_variance_of_2 += ((variable_1[i]-mean_variable_1) * (variable_2[i]-mean_variable_2))
    sum_of_square_variance_variable_1 += (variable_1[i] - mean_variable_1)**2
    sum_of_square_variance_variable_2 += (variable_2[i] - mean_variable_2)**2

pearson_correlation_coefficient = sum_of_variance_of_2 / math.sqrt(sum_of_square_variance_variable_1 * sum_of_square_variance_variable_2)
t_statistics = ((pearson_correlation_coefficient * math.sqrt(degree_of_freedom))/ math.sqrt(1-(pearson_correlation_coefficient)**2))
p_value = 2 * (1 - t.cdf(abs(t_statistics), df=degree_of_freedom))

# test result
if p_value <= 0.05:
    print("the null hypothesis is rejected..\n H0 = there is an significance corrleation between the variables...\n")
else:
    print("fail to reject null hypothesis..\n")

#correlation details of the test

if pearson_correlation_coefficient<0.1:
    print("no relation between the variables..\n")
elif pearson_correlation_coefficient<0.3 and pearson_correlation_coefficient > 0.1:
    print("low correlation between the variables...\n")
elif pearson_correlation_coefficient < 0.5 and pearson_correlation_coefficient > 0.3:
    print("medium level correlation ... \n")
elif pearson_correlation_coefficient < 0.7 and pearson_correlation_coefficient > 0.5:
    print("the variables are highly correlated....\n")
elif pearson_correlation_coefficient < 1 and pearson_correlation_coefficient > 0.7:
    print("the variables have strong correlation with each others...\n")

# test with in built library

r,p_value_lib = pearsonr(variable_1,variable_2)

print("\npearson correlation coefficient (r - library calculation) : ",r,"\n")
print("\npearson correlation coeffeccient r (through manual calculation) : ",pearson_correlation_coefficient,"\n")
print("\np-value (python library calculation): ",p_value_lib,"\n")
print("\np-value (through manual calculation) : ",p_value,"\n")
