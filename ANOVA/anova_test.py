from scipy.stats import f_oneway

# The columns are as follows:
# [Cyberpunk 2077, The Witcher 3, AC Mirage, Diablo IV, Call of Duty]

dlss_4060_1080p = [112.04, 121.79, 130.77, 183.9, 233.63]
dlss_4060_1440p = [103.97, 84.88, 116.41, 156.55, 173.41]
dlss_3060_1080p = [111.12, 111.93, 121.29, 181.85, 197.76]
dlss_3060_1440p = [94.54, 79.23, 103.51, 152.41, 153.84]

fsr_4060_1080p = [111.88, 122.48, 146.03, 186.49, 230.23]
fsr_4060_1440p = [102.25, 84.89, 118.56, 152.67, 168.13]
fsr_3060_1080p = [112.11, 111.79, 120.55, 179.83, 193.07]
fsr_3060_1440p = [89.13, 78.31, 103.24, 144.58, 147.83]

xess_4060_1080p = [112.09, 119.14, 136.26, 176.92, 213.54]
xess_4060_1440p = [98.57, 83.02, 110.91, 133.82, 154.29]
xess_3060_1080p = [107.24, 106.62, 116.2, 163.49, 173.94]
xess_3060_1440p = [84.62, 75.12, 93.38, 123.26, 131.42]

# Performing the ANOVA Test with f_oneway
anova_result = f_oneway(dlss_4060_1080p, dlss_4060_1440p, dlss_3060_1080p, dlss_3060_1440p,
    fsr_4060_1080p, fsr_4060_1440p, fsr_3060_1080p, fsr_3060_1440p,
    xess_4060_1080p, xess_4060_1440p, xess_3060_1080p, xess_3060_1440p
)

# Output the result
f_statistic, p_value = anova_result
print(f"F-statistic: {f_statistic}, p-value: {p_value}")
