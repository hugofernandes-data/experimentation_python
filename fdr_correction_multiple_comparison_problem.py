#FDR correction for multiple comparison problem

from statsmodels.stats.multitest import fdrcorrection
original_p_vals = [
  0.969, 0.031
]
rejected, corrected_p_val = fdrcorrection(original_p_vals, alpha=0.05) # <--- you can change as more strict you want
corrected_p_val