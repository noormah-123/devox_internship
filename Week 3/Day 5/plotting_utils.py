import matplotlib.pyplot as plt
import seaborn as sns


def create_bar_chart(data, x_column, y_column, title):
    """Create a bar chart."""
    plt.figure(figsize=(8, 5))

    sns.barplot(
        data=data,
        x=x_column,
        y=y_column
    )

    plt.title(title)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def create_line_chart(data, x_column, y_column, title):
    """Create a line chart."""
    plt.figure(figsize=(8, 5))

    sns.lineplot(
        data=data,
        x=x_column,
        y=y_column,
        marker="o"
    )

    plt.title(title)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.tight_layout()
    plt.show()


def create_histogram(data, column, title):
    """Create a histogram."""
    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=data,
        x=column,
        bins=10
    )

    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()