# Experimentation_python

# Statistical Tests for Sample Analysis

This repository provides Python code snippets to perform various statistical tests. These tests are essential for understanding and interpreting sample data in experimental and control groups.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
  - [Chi-square Test for Sample Ratio Mismatches](#chi-square-test-for-sample-ratio-mismatches)
  - [T-testing for Mean](#t-testing-for-mean)
  - [T-testing for Segments](#t-testing-for-segments)
  - [FDR Corrections](#fdr-corrections)
- [Contributors](#contributors)

## Setup

1. Clone this repository:

git clone [repository-url]


2. Ensure you have the required libraries installed:
   pip install scipy statsmodels

   
## Usage

### Chi-square Test for Sample Ratio Mismatches

This test checks if there's a significant difference between observed and expected frequencies in one or more categories of a contingency table. Refer to [chi_square_srm.py](chi_square_srm.py) for the implementation.

### T-testing for Mean

This test compares the means of two independent samples. There are two versions available:

- See [t_test_means.py](t_test_means.py) 


### T-testing for Segments

This test is applied multiple times in a loop for different segments. For detailed implementation, check [t_test_segments.py](t_test_segments.py).

### FDR Corrections

This provides a method to correct the false discovery rate. Implementation can be found in [fdr_correction_multiple_comparison_problem.py](fdr_correction_multiple_comparison_problem.pyy).

## Contributors

- Hugo Fernandes
- Nick Koronka




