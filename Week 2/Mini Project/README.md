# Week 2 - Mini Project: Data Cleaning Tool

## 📌 Project Overview

The Data Cleaning Tool is a Python project developed using the Pandas library to clean a messy CSV dataset. The program identifies and fixes common data quality issues such as duplicate records, missing values, inconsistent text formatting, and invalid numeric data. It then saves the cleaned dataset and generates a summary report of the cleaning process.

---

## 🎯 Objectives

- Learn how to read CSV files using Pandas.
- Remove duplicate records from a dataset.
- Clean and standardize text data.
- Handle missing and invalid values.
- Save the cleaned dataset to a new CSV file.
- Generate a summary report automatically.
- Practice working with file paths using the `pathlib` module.

---

## 🛠️ Features

- Loads data from a CSV file.
- Removes duplicate rows.
- Removes extra spaces from text fields.
- Standardizes customer and city names.
- Converts invalid sales values into numeric format.
- Handles missing values using appropriate methods.
- Calculates and fills missing sales values using the average.
- Saves the cleaned dataset.
- Creates a detailed summary report.
- Displays both the original and cleaned datasets.

---

## 📂 Project Structure

```
Week 2
└── Mini Project
    ├── data
    │   ├── messy_sales.csv
    │   └── cleaned_sales.csv
    │
    ├── data_cleaning_tool.py
    ├── summary_report.txt
    ├── README.md
    └── Learning.md
```

---

## 📄 Files Description

### `messy_sales.csv`
Contains the original dataset with:
- Duplicate records
- Missing values
- Extra spaces
- Inconsistent text formatting
- Invalid numeric values

### `data_cleaning_tool.py`
Main Python program that performs all data cleaning operations.

### `cleaned_sales.csv`
The cleaned dataset generated after processing.

### `summary_report.txt`
Contains a report describing the cleaning operations performed and dataset statistics.

---

## 💻 Technologies Used

- Python 3
- Pandas
- Pathlib

---

## 📚 Concepts Covered

- File Handling
- CSV File Processing
- Pandas DataFrames
- Data Cleaning
- Handling Missing Values
- Duplicate Removal
- String Manipulation
- Numeric Data Conversion
- Report Generation
- File Path Management using `pathlib`

---

## 🚀 How to Run

1. Open the project in Visual Studio Code.
2. Open the terminal.
3. Navigate to the Mini Project folder.
4. Run the following command:

```bash
python data_cleaning_tool.py
```

---

## 📊 Expected Output

The program will:

- Display the original dataset.
- Remove duplicate rows.
- Clean customer and city names.
- Handle missing and invalid values.
- Save the cleaned dataset as `cleaned_sales.csv`.
- Generate `summary_report.txt`.
- Display the cleaned dataset.
- Show a success message after completion.

---

## ✅ Learning Outcomes

After completing this project, I learned how to:

- Read and write CSV files using Pandas.
- Clean messy datasets efficiently.
- Detect and remove duplicate records.
- Handle missing and invalid data.
- Standardize inconsistent text formatting.
- Generate reports automatically.
- Use the `pathlib` module to manage file paths.
- Apply data preprocessing techniques used in real-world data analysis projects.

---

## 🎯 Conclusion

This mini project demonstrates the practical application of Python and Pandas for data cleaning. It provides hands-on experience with preprocessing real-world datasets, improving data quality, and generating useful reports. These skills are essential for data analysis, machine learning, and software development projects.