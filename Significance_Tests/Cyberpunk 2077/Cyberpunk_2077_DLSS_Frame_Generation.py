import numpy as np
from scipy import stats

# Genre: Science Fiction RPG
# Game: Cyberpunk 2077
# T-Test: Native and DLSS (Frame Generation Results) at 1080p and 1440p

# The array contains the following values: average FPS, 1% low FPS, and 0.1% low FPS.


# Sample data: FPS values for Native and DLSS modes
native_fps = np.array([98, 67, 57])
dlss_performance_fps = np.array([188, 141, 121])
dlss_balanced_fps = np.array([176, 150, 122])
dlss_quality_fps = np.array([162, 143, 120])

# Perform normality tests using Shapiro-Wilk test
normality_tests = {
    "native_fps": stats.shapiro(native_fps),
    "dlss_performance_fps": stats.shapiro(dlss_performance_fps),
    "dlss_balanced_fps": stats.shapiro(dlss_balanced_fps),
    "dlss_quality_fps": stats.shapiro(dlss_quality_fps)
}

# Perform variance tests using Levene's test
variance_tests = {
    "native_vs_performance": stats.levene(native_fps, dlss_performance_fps),
    "native_vs_balanced": stats.levene(native_fps, dlss_balanced_fps),
    "native_vs_quality": stats.levene(native_fps, dlss_quality_fps)
}

# Perform t-tests (using Welch's t-test if variances are not equal)
t_test_performance = stats.ttest_ind(native_fps, dlss_performance_fps, equal_var=variance_tests["native_vs_performance"].pvalue > 0.05)
t_test_balanced = stats.ttest_ind(native_fps, dlss_balanced_fps, equal_var=variance_tests["native_vs_balanced"].pvalue > 0.05)
t_test_quality = stats.ttest_ind(native_fps, dlss_quality_fps, equal_var=variance_tests["native_vs_quality"].pvalue > 0.05)

# Print normality test results with colored p-values
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

# Print variance test results with colored p-values
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

# Print t-test results with colored p-values
print("T-test Results:")
t_test_results = {
    "DLSS Performance vs Native": t_test_performance,
    "DLSS Balanced vs Native": t_test_balanced,
    "DLSS Quality vs Native": t_test_quality
}

for key, value in t_test_results.items():
    print(f"{key}:")
    print(f"  T-statistic: {value.statistic:.4f}")

    if value.pvalue <= 0.05:
        p_value_color = "\033[92m"  # Green
    else:
        p_value_color = "\033[91m"  # Red

    reset_color = "\033[0m"  # Reset to default color

    print(f"  P-value: {p_value_color}{value.pvalue:.4f}{reset_color}")
    print()
