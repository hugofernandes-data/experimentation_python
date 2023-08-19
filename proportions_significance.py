# Proportions significance

from statsmodels.stats.proportion import proportions_ztest

sample_1 = 317605
sample_2 = 316942
successes_1 = 5580
successes_2 = 5718

p_val = proportions_ztest(
                count=[successes_1, successes_2],
                nobs=[sample_1, sample_2],
                alternative='smaller' # larger / two-sided / smaller
            )[1]

'{:.10f}'.format(p_val)

