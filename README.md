# Task 1 - Data Preprocessing Pipeline

*company*: CODTECH IT SOLUTIONS

*NAME*: OM KUMAR

*INTERN ID*: CT04DH1971

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*:  Muzammil

*DESCRIPTION OF TASK*

Project Description – Task 1: ETL Data Pipeline using Pandas & Scikit-learn

As part of my Data Science Internship at CODTECH, I completed Task 1, which involved developing a simple yet effective ETL (Extract, Transform, Load) pipeline using Python tools such as pandas and scikit-learn. The primary goal of this task was to understand and automate the process of cleaning and preparing raw data for machine learning and data analysis tasks.

To begin with, I created a sample dataset named sample_data.csv that included a few fictional employee records. Each record contained fields like Name, Age, Salary, and Department. I intentionally included some missing values in the dataset to simulate real-world scenarios, where datasets are often incomplete or inconsistent.

Extract Phase

The first step of the ETL pipeline was data extraction, where I loaded the CSV file into a pandas DataFrame. Pandas provided a very efficient and readable way to work with tabular data. I printed the raw data to verify the contents and to get a basic understanding of missing or incorrect entries.

Transform Phase

The most critical part of this project was the transformation phase, where the actual data cleaning and preprocessing occurred. Here's what I implemented:

1. Handling Missing Values: I used SimpleImputer from scikit-learn to fill in missing values for numeric columns like Age and Salary. The strategy used was "mean" imputation, which calculates the average of the existing values and fills in the gaps.


2. Encoding Categorical Data: The "Department" column, being a string-type categorical feature, was encoded into numeric form using LabelEncoder. This step is necessary to make the data machine-readable for any future modeling tasks.


3. Scaling Numerical Features: To normalize the scale of numerical values like Age and Salary, I applied StandardScaler, which transforms the features to have a mean of 0 and a standard deviation of 1. This is especially important when different features have varying scales.



I also visualized the data before and after transformation using bar plots, which clearly showed the changes in data distribution after scaling and encoding. These visualizations not only helped validate the transformations but also enhanced my understanding of how preprocessing impacts the data.

Load Phase

The final step was the loading phase, where I exported the cleaned and transformed DataFrame to a new CSV file called processed_data.csv. This file can now be used for downstream tasks like model training, analytics, or dashboarding.

Learnings and Reflections

This task gave me hands-on experience with essential data preprocessing techniques that are foundational in any data science workflow. I learned the importance of handling missing data, encoding categorical features, and standardizing numerical values. I also gained confidence in writing clean, reusable, and well-documented Python code for data pipelines.

By the end of the task, I had a fully automated and repeatable ETL pipeline, complete with input and output files, visual plots, and a structured codebase ready to be pushed to GitHub.

*OUTPUT*

<img width="1195" height="796" alt="Image" src="https://github.com/user-attachments/assets/ffb3802a-19b0-4eed-86d3-19155a2f0aa4" />

