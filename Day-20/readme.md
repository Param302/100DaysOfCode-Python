# Day 20 of [#100DaysOfCode](https://twitter.com/Param3021/status/1539895073093353472)

## Task
1. Intermediate Machine Learning Course    (40% done)
2. House price prediction

# Resources
- Kaggle's [Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) course
- - Lesson 1: [Introduction](https://www.kaggle.com/code/alexisbcook/introduction) - [My Notebook](https://www.kaggle.com/code/param302/exercise-introduction/)
- - Lesson 2: [Missing Values](https://www.kaggle.com/code/alexisbcook/missing-values) - [My Notebook](https://www.kaggle.com/code/param302/exercise-missing-values)
- Lesson 3: [Categorical Variables](https://www.kaggle.com/code/alexisbcook/categorical-variables) - [My Notebook](https://www.kaggle.com/code/param302/exercise-categorical-variables)

- Kaggle [House price prediction Challenge](https://www.kaggle.com/competitions/home-data-for-ml-course/)
- - [My Notebook 1](./House_price_prediction_2.ipynb)
- - [My Notebook 2](./House_price_prediction_3.ipynb)
- - [My Notebook 3](https://www.kaggle.com/code/param302/exercise-categorical-variables)

### Topics I have learnt
1. Intermediate Machine Learning Course
- Handling Missing values in data
- - by dropping columns
- - by imputing the mean values of the columns
- - by imputing the mean values and adding another column having True/False for respected imputed values
- Handling Categorical columns in data
- - by dropping categorical columns
- - Changing them to numbers using **Ordinal Encoder**
- - Creating each numerical column for every unique value using **One Hot Encoding**
2. Also House price prediction
- One by dropping missing columns using `DecisionTreeRegressor`.
- One by dropping missing columns using `RandomForestRegressor`.
- One by Imputing missing values, doing Ordinal Encoding using `RandomForestRegressor`.

### Software used
- Jupyter Notebook
- Python 3.10.2
- Numpy 1.22.4
- pandas 1.4.2
- scikit-learn 1.1.1

### My Notebooks
- [L1 - Introduction.ipynb](./L1%20-%20Introduction.ipynb)
- [L2 - Missing_values.ipynb](./L2%20-%20Missing_values.ipynb)
- [L3 - Categorical_variables.ipynb](./L4%20-%20Categorical_variables.ipynb)
- [House_price_prediction_2.ipynb](./House_price_prediction_2.ipynb)
- [House_price_prediction_3.ipynb](./House_price_prediction_3.ipynb)
- [House_price_prediction_4.ipynb](https://www.kaggle.com/code/param302/exercise-categorical-variables)

### Conclusion:
Today I learned how to handle misisng values using SimpleImputer and categorical columns using One Hot Encoding & Ordinal Encoding. Also, did house price prediction using `DecisionTreeRegressor` and `RandomForestRegressor` applied imputer & ordinal encoding too. Today was great!!!
