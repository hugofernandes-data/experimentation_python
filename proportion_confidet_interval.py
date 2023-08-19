# Confidence Interval around a proportion

from statsmodels.stats.proportion import proportion_confint

#calculate 95% confidence interval with 56 successes in 100 trials
print(proportion_confint(count=0.66*439, nobs=439, alpha=0.1))
print(proportion_confint(count=0.60*506, nobs=506, alpha=0.1))