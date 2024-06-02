import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Define the data groups
groups = {
    "dlss_4060_1080p": [112.04, 121.79, 130.77, 183.9, 233.63],
    "dlss_4060_1440p": [103.97, 84.88, 116.41, 156.55, 173.41],
    "dlss_3060_1080p": [111.12, 111.93, 121.29, 181.85, 197.76],
    "dlss_3060_1440p": [94.54, 79.23, 103.51, 152.41, 153.84],
    "fsr_4060_1080p": [111.88, 122.48, 146.03, 186.49, 230.23],
    "fsr_4060_1440p": [102.25, 84.89, 118.56, 152.67, 168.13],
    "fsr_3060_1080p": [112.11, 111.79, 120.55, 179.83, 193.07],
    "fsr_3060_1440p": [89.13, 78.31, 103.24, 144.58, 147.83],
    "xess_4060_1080p": [112.09, 119.14, 136.26, 176.92, 213.54],
    "xess_4060_1440p": [98.57, 83.02, 110.91, 133.82, 154.29],
    "xess_3060_1080p": [107.24, 106.62, 116.2, 163.49, 173.94],
    "xess_3060_1440p": [84.62, 75.12, 93.38, 123.26, 131.42]
}

# Perform Shapiro-Wilk test for each group
for name, data in groups.items():
    stat, p_value = stats.shapiro(data)
    print(f"Group {name}: W={stat}, p-value={p_value}")
    # Q-Q plot
    plt.figure(figsize=(6, 4))
    stats.probplot(data, dist="norm", plot=plt)
    plt.title(f'Q-Q plot for {name}')
    plt.show()

# Combining data for visual inspection using a histogram or KDE plot
for name, data in groups.items():
    sns.histplot(data, kde=True, label=name)

plt.legend()
plt.title("Histogram and KDE for Each Group")
plt.show()


from scipy.stats import levene

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




# Combine all data into a list of lists
all_groups = [dlss_4060_1080p, dlss_4060_1440p, dlss_3060_1080p, dlss_3060_1440p,
              fsr_4060_1080p, fsr_4060_1440p, fsr_3060_1080p, fsr_3060_1440p,
              xess_4060_1080p, xess_4060_1440p, xess_3060_1080p, xess_3060_1440p]

# Perform Levene's test
stat, p_value = levene(*all_groups)
print(f"Levene's test statistic: {stat}, p-value: {p_value}")
