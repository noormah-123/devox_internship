import pandas as pd

from plotting_utils import (
    create_bar_chart,
    create_line_chart,
    create_histogram
)


# Sample dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 150, 180, 160, 210],
    "Customers": [30, 35, 42, 38, 50]
}

df = pd.DataFrame(data)


# Use the reusable functions
create_bar_chart(
    df,
    "Month",
    "Sales",
    "Monthly Sales"
)

create_line_chart(
    df,
    "Month",
    "Sales",
    "Sales Trend"
)

create_histogram(
    df,
    "Sales",
    "Sales Distribution"
)