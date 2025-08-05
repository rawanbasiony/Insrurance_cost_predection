{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f35a5dff-c006-4ee3-90db-909a80532a2a",
   "metadata": {},
   "source": [
    "# Medical Insurance Cost Prediction \n",
    "\n",
    "\n",
    "## Projes=ct Overview \n",
    "This project predicts medical insurance costs based on a person's demographic and health-related information using regression techniques in machine learning .\n",
    "The dateset includes factores such as **age** , **sex** , **BMI**,**Children** , **smoker status** and **Region**\n",
    "\n",
    "\n",
    "                                                                                                         \n",
    " ## Dataset      \n",
    "- **Source**:\n",
    "    'https://www.kaggle.com/code/maverickss26/regression-modellng-using-insurance-dataset/input?select=insurance.csv#:~:text=Input%20Data-,insurance.csv,-(55.63%20kB'\n",
    "- **Features**:\n",
    "  - *age*: Age of the person.\n",
    "  - *sex*: Gender (male/female).\n",
    "  - *bmi*: Body Mass Index.\n",
    "  - *children*: Number of children/dependents covered by insurance.\n",
    "  - *smoker*: Smoking status.\n",
    "  - *region*: Residential region in the US.\n",
    "  - *charges*: Medical insurance cost (target variable).  \n",
    "\n",
    "\n",
    "## Project Steps\n",
    "1. **Data Loading & Exploration**  \n",
    "   - Read the dataset and explored its structure.\n",
    "   - Displayed first and last rows.\n",
    "   - Checked for missing values and duplicates.\n",
    "\n",
    "2. **Data Cleaning & Preprocessing**  \n",
    "   - Removed duplicates.\n",
    "   - Encoded categorical variables (`sex`, `smoker`, `region`) into numeric form.\n",
    "\n",
    "3. **Exploratory Data Analysis (EDA)**  \n",
    "   - Used `matplotlib` and `seaborn` for visualization.\n",
    "   - Analyzed correlations between features and target.\n",
    "\n",
    "4. **Model Building**  \n",
    "   - Chose a regression algorithm (e.g., Linear Regression / Random Forest Regressor).\n",
    "   - Trained the model using the processed dataset.\n",
    "\n",
    "5. **Model Evaluation**  \n",
    "   - Calculated metrics such as **Mean Absolute Error (MAE)**, **Mean Squared Error (MSE)**, and **R² Score**.\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "## Technologies Used\n",
    "- **Python**\n",
    "- **Pandas**, **NumPy**\n",
    "- **Matplotlib**, **Seaborn**\n",
    "- **Scikit-learn**                                                             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90d7f163-b698-4aaf-abd6-25e82334a4c1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.21"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
