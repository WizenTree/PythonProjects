import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 3000

# Generate data
employee_ids = [f"E{str(i).zfill(5)}" for i in range(1, n_samples + 1)]
names = [f"Employee_{i}" for i in range(1, n_samples + 1)]
ages = np.random.randint(22, 60, size=n_samples)
departments = np.random.choice(['Sales', 'Engineering', 'HR', 'Finance', 'IT', 'Marketing'], size=n_samples, p=[0.25, 0.25, 0.1, 0.15, 0.15, 0.1])
salaries = np.round(np.random.normal(loc=65000, scale=15000, size=n_samples), 2)
years_at_company = np.clip(np.random.normal(loc=5, scale=3, size=n_samples), 0, 40).astype(int)

# Performance Score based on years and salary (simulated logic)
performance_score = np.round(
    np.clip(
        (years_at_company / 10 + salaries / 100000 + np.random.normal(0, 0.5, n_samples)),
        1, 5
    ), 2
)

# Simulate attrition based on performance, years at company, and salary
attrition_prob = (
    0.6 * (performance_score < 2.5).astype(int) +
    0.3 * (years_at_company < 2).astype(int) +
    0.2 * (salaries < 50000).astype(int) +
    np.random.normal(0, 0.1, n_samples)
)

attrition = np.where(attrition_prob > 0.5, 'Yes', 'No')

# Final DataFrame
df = pd.DataFrame({
    "Employee ID": employee_ids,
    "Name": names,
    "Age": ages,
    "Department": departments,
    "Salary": salaries,
    "Years at Company": years_at_company,
    "Performance Score": performance_score,
    "Attrition": attrition
})

# Save to CSV
df.to_csv("improved_employee_attrition.csv", index=False)
print("Dataset saved as 'improved_employee_attrition.csv'")
