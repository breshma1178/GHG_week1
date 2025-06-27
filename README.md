# GHG – Greenhouse Gas Emission Prediction Project

This is an AI/ML-based project focused on predicting greenhouse gas emissions.

---

## 📂 Dataset Contents for Week 1

This dataset contains supply chain emission factors associated with various U.S. industries and commodities (from 2010–2016).

### Key Highlights:
- **Code**: Industry classification code  
- **Industry_Name**: Name of the industry  
- **Commodity**: Item or commodity name  
- **GHG_Emissions_kgCO2e**: GHG emissions per unit (kg CO2 equivalent)  
- **Units**: Measurement units (e.g., `[kg/2018 USD, purchaser price]`)

---
### Model 
-**Prediction Model**: GHG_Emissions_kgCO2e using regression model

---
### 🔧 Steps Involved in Week 1 Project

1. **Importing libraries** (all necessary Python libraries)  
2. **Loading dataset** (supply chain emission factors)  
3. **Data processing** (cleaning data, handling missing values, etc.)

---
### 🔧 Steps Involved in Week 2 Project

# GHG Emissions Analysis Project - Stepwise Workflow

## 1. Load the Dataset
- Import data into a pandas DataFrame.
- Verify the data loaded correctly using `df.head()` and `df.info()`.

## 2. Initial Data Inspection
- Check data types and non-null counts with `df.info()`.
- Confirm there are no missing values.
- Understand column types:
  - Categorical (encoded as integers): `Substance`, `Unit`, `Source`, DQ scores.
  - Continuous: Emission factors columns.

## 3. Data Cleaning
- Drop columns not needed for modeling:
  - Drop `Name`, `Code`, `Year` (categorical or identifiers not used for ML).
- Ensure the DataFrame contains only relevant features and target variables.

## 4. Exploratory Data Analysis (EDA)

### a. Univariate Analysis
- Plot count plots for categorical features (`Substance`, `Unit`) to check distribution.
- Check summary statistics with `describe()` for numeric features.

### b. Correlation Analysis
- Compute correlation matrix on numeric variables.
- Visualize correlations using a heatmap (`seaborn.heatmap`).
- Focus on correlations with the target variable: `Supply Chain Emission Factors with Margins`.

## 5. Identify Top Emitting Industries
- Group the original dataset by `Name`.
- Compute mean emission factors.
- Sort descending and select top 10 emitters.
- Plot results using a horizontal bar plot for clear visualization.

## 6. Prepare Features and Target
- Define:
  - `X` = All features except the target (`Supply Chain Emission Factors with Margins`).
  - `y` = Target variable (`Supply Chain Emission Factors with Margins`).

## 7. Preprocessing for Modeling
- Encode categorical features if necessary (`Substance`, `Unit`, `Source`).
- Scale numeric features if required depending on the model choice.

## 8. Model Building
- Split data into training and test sets.
- Choose regression algorithms (e.g., Linear Regression, Random Forest).
- Train the model on training data.
- Predict on test data and evaluate performance using metrics like MAE, RMSE, and R².

## 9. Model Interpretation
- Extract feature importances or coefficients.
- Optionally use explainability tools (e.g., SHAP) to understand feature impacts.

## 10. Visualization & Reporting
- Visualize model results and important features.
- Summarize key findings:
  - Top emitting industries.
  - Factors influencing emission levels.
- Provide recommendations or insights based on analysis.



