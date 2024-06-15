import numpy as np
from scipy import stats

# Genre: First Person Shooter
# Game: Call of Duty Modern Warfare III
# T-Test: Native and DLSS (Average across all modes and graphics settings) at 1080p and 1440p

# The array contains the following values: average FPS, 1% low FPS, and 0.1% low FPS.

# Nvidia GeForce RTX 4060
native_4060_1080p = np.array([186, 146, 116])
dlss_4060_1080p = np.array([234, 172, 146])
native_4060_1440p = np.array([120, 105, 90])
dlss_4060_1440p = np.array([173, 146, 113])

# Nvidia GeForce RTX 3060
native_3060_1080p = np.array([153, 122, 88])
dlss_3060_1080p = np.array([198, 153, 111])
native_3060_1440p = np.array([114, 92, 75])
dlss_3060_1440p = np.array([154, 129, 102])

# Perform normality tests using Shapiro-Wilk test

normality_tests = {
    "native_4060_1080p": stats.shapiro(native_4060_1080p),
    "dlss_4060_1080p": stats.shapiro(dlss_4060_1080p),
    "native_4060_1440p": stats.shapiro(native_4060_1440p),
    "dlss_4060_1440p": stats.shapiro(dlss_4060_1440p),
    "native_3060_1080p": stats.shapiro(native_3060_1080p),
    "dlss_3060_1080p": stats.shapiro(dlss_3060_1080p),
    "native_3060_1440p": stats.shapiro(native_3060_1440p),
    "dlss_3060_1440p": stats.shapiro(dlss_3060_1440p)
}

# Check for equal variances using Levene's test

variance_tests = {
    "4060_1080p": stats.levene(native_4060_1080p, dlss_4060_1080p),
    "4060_1440p": stats.levene(native_4060_1440p, dlss_4060_1440p),
    "3060_1080p": stats.levene(native_3060_1080p, dlss_3060_1080p),
    "3060_1440p": stats.levene(native_3060_1440p, dlss_3060_1440p)
}

# Perform t-tests
t_test_4060_1080p = stats.ttest_ind(native_4060_1080p, dlss_4060_1080p)
t_test_4060_1440p = stats.ttest_ind(native_4060_1440p, dlss_4060_1440p)
t_test_3060_1080p = stats.ttest_ind(native_3060_1080p, dlss_3060_1080p)
t_test_3060_1440p = stats.ttest_ind(native_3060_1440p, dlss_3060_1440p)

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
