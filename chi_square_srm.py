#Testing for SMR
#Testing for sample ratio mis-matches.

from scipy import stats
from scipy.stats import ttest_ind_from_stats
values = [63680,64279] # commas separate as many treatments as are in test
print([sum(values) / len(values) for value in values])
chi, p = stats.chisquare(values, f_exp=[sum(values) / len(values) for value in values])
print("p="+str(p))


#The above p-value should be higher than 0.01 to pass the Chi test

