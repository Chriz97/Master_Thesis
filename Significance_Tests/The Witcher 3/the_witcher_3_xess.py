import numpy as np
from scipy import stats

# Genre: Fantasy Open World RPG
# Game: The Witcher 3: Wild Hunt
# T-Test: Native and XeSS (Average across all modes and graphics settings) at 1080p and 1440p

# Nvidia GeForce RTX 4060
native_4060_1080p = np.array([81, 63, 55])
xess_4060_1080p = np.array([119, 80, 70])
native_4060_1440p = np.array([50, 39, 27])
xess_4060_1440p = np.array([83, 62, 52])

# Nvidia GeForce RTX 3060
native_3060_1080p = np.array([75, 55, 44])
xess_3060_1080p = np.array([107, 70, 57])
native_3060_1440p = np.array([45, 35, 26])
fsr_3060_1440p = np.array([75, 52, 39])

# Perform normality tests using Shapiro-Wilk test
normality_tests = {
    "native_4060_1080p": stats.shapiro(native_4060_1080p),
    "dlss_4060_1080p": stats.shapiro(xess_4060_1080p),
    "native_4060_1440p": stats.shapiro(native_4060_1440p),
    "dlss_4060_1440p": stats.shapiro(xess_4060_1440p),
    "native_3060_1080p": stats.shapiro(native_3060_1080p),
    "dlss_3060_1080p": stats.shapiro(xess_3060_1080p),
    "native_3060_1440p": stats.shapiro(native_3060_1440p),
    "dlss_3060_1440p": stats.shapiro(fsr_3060_1440p)
}

# Check for equal variances using Levene's test
variance_tests = {
    "4060_1080p": stats.levene(native_4060_1080p, xess_4060_1080p),
    "4060_1440p": stats.levene(native_4060_1440p, xess_4060_1440p),
    "3060_1080p": stats.levene(native_3060_1080p, xess_3060_1080p),
    "3060_1440p": stats.levene(native_3060_1440p, fsr_3060_1440p)
}


# Perform t-tests (using Welch's t-test if variances are not equal)
t_test_4060_1080p = stats.ttest_ind(native_4060_1080p, xess_4060_1080p, equal_var=variance_tests["4060_1080p"].pvalue > 0.05)
t_test_4060_1440p = stats.ttest_ind(native_4060_1440p, xess_4060_1440p, equal_var=variance_tests["4060_1440p"].pvalue > 0.05)
t_test_3060_1080p = stats.ttest_ind(native_3060_1080p, xess_3060_1080p, equal_var=variance_tests["3060_1080p"].pvalue > 0.05)
t_test_3060_1440p = stats.ttest_ind(native_3060_1440p, fsr_3060_1440p, equal_var=variance_tests["3060_1440p"].pvalue > 0.05)

# Print normality test results,if p value > 0.05 the color is green otherwise red
print("Normality Test Results:")
for key, value in normality_tests.items():
    print(f"{key}:")
    print(f"  Statistic: {value.statistic:.4f}")

    if value.pvalue > 0.05:
        p_value_color = "\033[92m"  # Green
    else:
        p_value_color = "\033[91m"  # Red

    reset_color = "\033[0m"  # Reset to default color

    print(f"  P-value: {p_value_color}{value.pvalue:.4f}{reset_color}")
    print()

# Print variance test results if p value > 0.05 the color is green otherwise red
print("Variance Test Results:")
for key, value in variance_tests.items():
    print(f"{key}:")
    print(f"  Statistic: {value.statistic:.4f}")

    if value.pvalue > 0.05:
        p_value_color = "\033[92m"  # Green
    else:
        p_value_color = "\033[91m"  # Red

    reset_color = "\033[0m"  # Reset to default color

    print(f"  P-value: {p_value_color}{value.pvalue:.4f}{reset_color}")
    print()

# Print t-test results
t_test_results = {
    "RTX 4060 1080p": {
        "T-statistic": t_test_4060_1080p.statistic,
        "P-value": t_test_4060_1080p.pvalue
    },
    "RTX 4060 1440p": {
        "T-statistic": t_test_4060_1440p.statistic,
        "P-value": t_test_4060_1440p.pvalue
    },
    "RTX 3060 1080p": {
        "T-statistic": t_test_3060_1080p.statistic,
        "P-value": t_test_3060_1080p.pvalue
    },
    "RTX 3060 1440p": {
        "T-statistic": t_test_3060_1440p.statistic,
        "P-value": t_test_3060_1440p.pvalue
    }
}

# Print t-test results, if p value < 0.05 the color is green otherwise red
print("T-test Results:")
for key, value in t_test_results.items():
    print(f"{key}:")
    print(f"  T-statistic: {value['T-statistic']:.4f}")

    if value['P-value'] <= 0.05:
        p_value_color = "\033[92m"  # Green
    else:
        p_value_color = "\033[91m"  # Red

    reset_color = "\033[0m"  # Reset to default color

    print(f"  P-value: {p_value_color}{value['P-value']:.4f}{reset_color}")
    print()
