# Employee Performance and Retention Analysis


## Objective
This project aims to develop an Employee Performance and Retention Analysis using a real-world dataset. The goal is to apply concepts from probability, statistics, machine learning, and deep learning to analyze employee data and predict performance and retention trends. 

## Libraries Required
Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, TensorFlow / Keras

## Project Phases
The project is divided into four phases, which guide you through data collection, analysis, prediction, and reporting.

### Phase 1 - Data Collection and Exploratory Data Analysis (EDA)

#### Step 1 - Data Collection and Preprocessing
- Dataset - Use a sample employee dataset. The dataset should contain features such as:
  - Employee ID
  - Name
  - Age
  - Department
  - Salary
  - Years at Company
  - Performance Score
  - Attrition (Yes/No)
- Tasks -
  - Load the dataset (Employee_data.csv)  using Pandas.
  - Handle missing values, remove duplicates, and clean inconsistent data entries.

#### Step 2 - Exploratory Data Analysis (EDA)
- Objective - Perform an initial analysis to understand the dataset and its key trends.
- Tasks -
  - Calculate descriptive statistics like mean, median, mode, variance, and standard deviation for numerical columns.
  - Use Matplotlib and Seaborn to visualize:
  - Pairplot to explore relationships between multiple features.
  - Heatmap for correlation analysis.
  - Identify any outliers in numerical features (using boxplots).

#### Step 3 - Probability and Statistical Analysis
- Objective - Apply probability concepts and statistical tests to better understand the dataset.
- Tasks -
  - Probability - Calculate the probability of an employee leaving based on factors like performance scores and department.
  - Bayes' Theorem - Use Bayes' Theorem to find the probability of employee attrition given performance score.
  - Hypothesis Testing - Test whether the mean performance score differs across departments.

### Phase 2 - Predictive Modeling

#### Step 4 - Feature Engineering and Encoding
- Objective - Prepare the data for machine learning models.
- Tasks -
  - Scale numerical features such as Salary and Performance Scores using Min-Max Scaling or Standardization.
  - Apply Label Encoding to categorical features (e.g., Attrition, Department).

#### Step 5 - Employee Attrition Prediction Model
- Objective - Build a machine learning model to predict employee attrition (i.e., whether an employee will leave or stay).
- Tasks -
  - Split the dataset into training and testing sets using Scikit-learn.
  - Choose a classification model (e.g., Logistic Regression, Random Forest Classifier).
  - Evaluate the model using accuracy, precision, recall, and F1-score.
  - Visualize the confusion matrix to check the model’s performance.

#### Step 6 - Employee Performance Prediction Model
- Objective - Build a regression model to predict employee performance based on various features.
- Tasks -
  - Split the dataset into training and testing sets.
  - Build a Linear Regression model to predict Performance Score.
  - Evaluate the model using R-squared (R²) and Mean Squared Error (MSE).
  - Visualize predicted vs. actual performance scores.

### Phase 3 - Deep Learning Models

#### Step 7 - Deep Learning for Employee Performance Prediction
- Objective - Apply deep learning techniques to predict employee performance using neural networks.
- Tasks -
  - Prepare the dataset for use with TensorFlow or Keras.
  - Build a feedforward neural network:
  - Input layer - Employee features like Age, Salary, Department.
  - Hidden layers - Dense layers with activation functions (e.g., ReLU).
  - Output layer - Predicted Performance Score.
  - Train the model using Mean Squared Error as the loss function.
  - Evaluate the model's performance on the test set.

#### Step 8 - Employee Attrition Analysis with Deep Learning
- Objective - Use deep learning for classification to predict employee attrition based on various features.
- Tasks -
  - Build a neural network model with input features like Age, Department, Performance Score, etc.
  - Evaluate the model using accuracy, precision, recall, and F1-score.

### Phase 4 - Reporting and Insights

#### Step 9 - Insights and Recommendations
- Objective - Derive actionable insights based on your analysis and predictions.
- Tasks -
  - Summarize key findings, such as:
  - Key factors contributing to employee performance.
  - High-risk departments or employee groups for attrition.
  - Recommend strategies to improve retention, such as:
  - Department-wise performance improvement plans.
  - Targeted employee engagement programs.

#### Step 10 - Data Visualization and Reporting
- Objective - Present the findings in a visually appealing and easy-to-understand manner.
- Tasks -
  - Generate interactive data visualizations such as:
  - Line Plots to show performance trends.
  - Bar Charts for department-wise attrition.
  - Scatter Plots for salary vs. performance.
  - Prepare a detailed project report summarizing:
  - The analysis and insights derived.
  - Model evaluation and predictive capabilities.
  - Visualizations and recommendations.

##### All of the above have been done in the file named "[Employee Performance and Retention Analysis](Employee Performance and Retention Analysis)" along with the dataset named "[employee_data.csv](employee_data.csv)" with the python code to generate the dataset named "[Dataset_generator.py](Dataset_generator.py)"
