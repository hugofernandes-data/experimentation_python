#t-testing for segments

# segments,control_users,variant_users,control_metric,variant_metric,control_std,variant_std
data = [
  ['App',83665,83134,2.046925237554533,2.0684437173719536,1.362041115092893,1.3638586320815083],
  ['Both',11614,11695,2.0126571379369724,2.0297563061137236,1.3651737072262478,1.388142904100875],
  ['Web',19136,18899,1.493258779264214,1.4979099423249906,1.2536464791859327,1.245091270687472]
]

for c in data:
  test_stat, p_val = ttest_ind_from_stats(
    mean1=c[3], 
    std1=c[5], 
    nobs1=c[1], 
    mean2=c[4], 
    std2=c[6],
    nobs2=c[2], 
    alternative='less') #'two-sided' = two-tailed tests, 'less' = right tailed tests, 'greater' = left-tailed tests 
  print(c[0], p_val)