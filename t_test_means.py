### T-testing for mean

from scipy.stats import ttest_ind_from_stats
#input parameters - control vs treatment
mean = [x,y] #[control value (x),treatment value (y)]
std = [x,y] #[control value,treatment value]
sample = [x,y] #[control value,treatment value]

test_stat, p_val = ttest_ind_from_stats(
  mean1=mean[0], 
  std1=std[0], 
  nobs1=sample[0], 
  mean2=mean[1], 
  std2=std[1],
  nobs2=sample[1], 
  alternative='less') #'two-sided' = two-tailed tests, 'less' = right tailed tests, 'greater' = left-tailed tests

print("{:.5f}".format(p_val)) #If less than pre-defined alpha then is statistically significant 
print(test_stat)
print(round(100*(mean[1]-mean[0])/mean[0],2))