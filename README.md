Medical Insurance Cost Prediction


Project Overview :
This project predicts medical insurance costs based on a person's demographic and health-related information using regression techniques in machine learning . The dateset includes factores such as age , sex , BMI,Children , smoker status and Region

Dataset :
Source: 'https://www.kaggle.com/code/maverickss26/regression-modellng-using-insurance-dataset/input?select=insurance.csv#:~:text=Input%20Data-,insurance.csv,-(55.63%20kB'
Features:
age: Age of the person.
sex: Gender (male/female).
bmi: Body Mass Index.
children: Number of children/dependents covered by insurance.
smoker: Smoking status.
region: Residential region in the US.
charges: Medical insurance cost (target variable).


Project Steps :
-Data Loading & Exploration

-Read the dataset and explored its structure.
-Displayed first and last rows.
-Checked for missing values and duplicates.
-Data Cleaning & Preprocessing

-Removed duplicates.
-Encoded categorical variables (sex, smoker, region) into numeric form.
-Exploratory Data Analysis (EDA)

-Used matplotlib and seaborn for visualization.
-Analyzed correlations between features and target.
-Model Building

-Chose a regression algorithm ( Gradient Boosting Regressor ,Rondom Forest Regressor).
Trained the model using the processed dataset.
Model Evaluation

-Calculated metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² Score.


-Technologies Used :

Python
Pandas, 
NumPy,
Matplotlib, 
Seaborn,
Scikit-learn.
