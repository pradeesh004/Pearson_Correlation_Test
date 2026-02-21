📊 Pearson Correlation Test (Manual + Library Implementation)
📌 Overview

This project performs a complete Pearson Correlation Test between two variables using:

✅ Manual mathematical implementation

✅ Built-in Python library (scipy.stats.pearsonr)

The program calculates:

Pearson Correlation Coefficient (r)

t-statistic

p-value (two-tailed test)

Hypothesis test result

Correlation strength interpretation

This implementation is useful for academic research, statistical analysis, and understanding the mathematical foundation behind Pearson’s correlation.

🧮 Statistical Background
Pearson Correlation Coefficient Formula

r= sum((x_i-mean(x)*(y_i - mean(y)) / sqrt(sum(x_i - mean(x))^2 * sum(y_i - mean(y))^2)

t-Statistic Formula

t= (r*sqrt(n-2))/(sqrt(1-r^2))
p-Value (Two-Tailed Test)
p=2×(1−F(∣t∣))
p=2×(1−F(∣t∣))

Where:

n
n = sample size

df=n−2
df=n−2 = degrees of freedom

F
F = CDF of t-distribution

📂 Program Features
1️⃣ Manual Calculation

Mean of both variables

Covariance computation

Variance calculation

Pearson correlation coefficient

t-statistic

p-value using t-distribution

2️⃣ Library Verification

Uses scipy.stats.pearsonr() for validation

Compares manual results with built-in results

3️⃣ Hypothesis Testing

Null Hypothesis (H₀): No significant correlation

Rejects H₀ if p ≤ 0.05

4️⃣ Correlation Strength Classification

No correlation

Low correlation

Medium correlation

High correlation

Strong correlation

🛠 Requirements

Install required package:

pip install scipy
▶️ How to Run

Save the file as:

pearson_test.py

Open terminal in the project directory.

Run:

python pearson_test.py
📊 Output

The program prints:

Pearson correlation (manual)

Pearson correlation (library)

p-value (manual)

p-value (library)

Hypothesis test decision

Correlation strength interpretation

🎯 Sample Size

Total samples: 25

Degrees of Freedom: 23

🔍 Purpose of Dual Implementation

This project demonstrates:

Understanding of statistical foundations

Ability to implement formulas manually

Validation using industry-standard libraries

Academic-level statistical reporting

📚 Applications

Research data analysis

AI model evaluation

Academic projects

Statistical hypothesis testing

CGPA vs performance analysis

Behavioral data correlation studies

⚠ Notes

The test assumes:

Linear relationship

Continuous variables

No extreme outliers

Approximate normal distribution

This is a two-tailed significance test.

👨‍💻 Author

Developed for academic statistical analysis and research validation purposes.
