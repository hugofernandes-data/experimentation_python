
#mde function for means and proportions

import numpy as np
import scipy.stats as stats
        
def mde_mean(n, mew1, std, r=1, alpha=0.05, beta=0.2, two_tailed=True):
    '''
    Credit: Jonny White
    Function to return the predicted minimum detectable effect of a mean, given the size, mean and standard deviation
    of the control.

    Params:
        n - int, size of the control group
        mew1 - float, mean of the test metric for the control
        std - float, standard deviation of the test metric for the control
        r - float or int, the ration between control and test, 1 being a 50/50 split
        alpha - float, significance level
        beta - float, power
        two_tailed - boolean, indicates if the experiment is two tailed or not

    Returns:
        MDE - float, the minimum detectable variation (in percentage) the variant group would need in order to
                     accept the hypothesis
    '''
    if two_tailed:
        numerator = np.sqrt((r + 1) / r) * std * (stats.norm.ppf(1 - (alpha / 2)) + stats.norm.ppf(1 - beta))
        denominator = mew1 * np.sqrt(n)
    else:
        numerator = np.sqrt((r + 1) / r) * std * (stats.norm.ppf(1 - (alpha)) + stats.norm.ppf(1 - beta))
        denominator = mew1 * np.sqrt(n)

    return numerator / denominator

  
def mde_proportion(n, p1, r=1, alpha=0.05, beta=0.2, two_tailed=True):
    '''
    Credit: Jonny White
    Function to return the predicted minimum detectable effect of a proportion, given the size and proportion
    of the control.

    Params:
        n - int, size of the control group
        p1 - float, the success proportion of the control
        r - float or int, the ration between control and test, 1 being a 50/50 split
        alpha - float, significance level
        beta - float, power
        two_tailed - boolean, indicates if the experiment is two tailed or not

    Returns:
        MDE - float, the minimum detectable difference (in percentage) the variant group would need in order to
                     accept the hypothesis

    '''
    if two_tailed:
        l = ((stats.norm.ppf(1 - (alpha / 2)) + stats.norm.ppf(1 - beta)) ** 2) / n
        t = ((stats.norm.ppf(1 - (alpha / 2)) + stats.norm.ppf(1 - beta)) ** 2) / (n * p1)

        numerator = (t - 2 * l) + np.sqrt((2 * l - t) ** 2 + 4 * (1 - l) * (2 * l + 2 * t))
        denominator = 2 * (1 - l)
    else:
        l = ((stats.norm.ppf(1 - (alpha)) + stats.norm.ppf(1 - beta)) ** 2) / n
        t = ((stats.norm.ppf(1 - (alpha)) + stats.norm.ppf(1 - beta)) ** 2) / (n * p1)

        numerator = (t - 2 * l) + np.sqrt((2 * l - t) ** 2 + 4 * (1 - l) * (2 * l + 2 * t))
        denominator = 2 * (1 - l)

    return numerator / denominator


#means examples

mde = mde_mean(24230, 1.2182, 2.342004061, alpha=0.1, two_tailed=False) #add means and std deviation
print(mde)

#proportion examples

per_variant = 520000
baseline_cr = 0.04

mde_equal = mde_proportion(per_variant, baseline_cr, r=1, alpha=0.1, beta=0.2, two_tailed=False)
mde_unequal = mde_proportion(per_variant, baseline_cr, r=0.001, alpha=0.1, beta=0.2, two_tailed=False)
print(mde_equal)
print(mde_unequal)