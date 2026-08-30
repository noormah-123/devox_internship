import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --------------------------------------------------
# EDA MINI-DASHBOARD
# --------------------------------------------------

# Get the folder where this Python file is located
BASE_DIR = Path(__file__).resolve().parent

# Load the local penguins dataset
csv_file = BASE_DIR / "penguins.csv"
data = pd.read_csv(csv_file)

# Remove rows containing missing values
data = data.dropna()

# Set Seaborn style
sns.set_theme(style="whitegrid")

# --------------------------------------------------
# Create 4 charts
# --------------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Penguin count by species
sns.countplot(
    data=data,
    x="species",
    ax=axes[0, 0]
)

axes[0, 0].set_title("Penguin Count by Species")
axes[0, 0].set_xlabel("Species")
axes[0, 0].set_ylabel("Number of Penguins")


# 2. Bill length distribution
sns.histplot(
    data=data,
    x="bill_length_mm",
    hue="species",
    kde=True,
    ax=axes[0, 1]
)

axes[0, 1].set_title("Bill Length Distribution")
axes[0, 1].set_xlabel("Bill Length (mm)")
axes[0, 1].set_ylabel("Frequency")


# 3. Body mass by species
sns.boxplot(
    data=data,
    x="species",
    y="body_mass_g",
    ax=axes[1, 0]
)

axes[1, 0].set_title("Body Mass by Species")
axes[1, 0].set_xlabel("Species")
axes[1, 0].set_ylabel("Body Mass (g)")


# 4. Flipper length vs body mass
sns.scatterplot(
    data=data,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Flipper Length vs Body Mass")
axes[1, 1].set_xlabel("Flipper Length (mm)")
axes[1, 1].set_ylabel("Body Mass (g)")


# --------------------------------------------------
# Final dashboard formatting
# --------------------------------------------------

fig.suptitle(
    "Penguins EDA Mini-Dashboard",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

# Save the dashboard inside the Mini Project folder
output_file = BASE_DIR / "EDA_Mini_Dashboard.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight")

# Display the dashboard
plt.show()


# --------------------------------------------------
# Insights
# --------------------------------------------------

print("\nEDA MINI-DASHBOARD INSIGHTS")
print("----------------------------")

print(
    "1. The dataset contains three penguin species: "
    "Adelie, Chinstrap, and Gentoo."
)

print(
    "2. Gentoo penguins generally have greater body mass "
    "and longer flippers than the other species."
)

print(
    "3. Bill length differs across species, with Gentoo "
    "penguins generally having larger bill measurements."
)

print(
    "4. The scatter plot shows a positive relationship "
    "between flipper length and body mass."
)

print("\nDashboard saved successfully!")
print(f"File: {output_file}")