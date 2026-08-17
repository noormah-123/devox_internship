import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [200, 250, 300, 280, 320]
}

df = pd.DataFrame(data)

# Bar Chart
plt.figure()
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Line Chart
plt.figure()
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Pie Chart
plt.figure()
plt.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%')
plt.title("Sales Distribution - Pie Chart")
plt.show()