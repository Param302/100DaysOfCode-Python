# Day 21 of [#100DaysOfCode](https://twitter.com/Param3021/status/1540276365777580032)

## Task
1. Intermediate Machine Learning Course
2. House price prediction

# Resources
- Kaggle's [Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) course
- - Lesson 4: [Pipelines](https://www.kaggle.com/code/alexisbcook/pipelines) - [My Notebook](https://www.kaggle.com/code/param302/exercise-pipelines)
- - Lesson 5: [Cross Validation](https://www.kaggle.com/code/alexisbcook/cross-validation) - [My Notebook](https://www.kaggle.com/code/param302/exercise-cross-validation)
- - Lesson 6: [XGBoost](https://www.kaggle.com/code/alexisbcook/xgboost) - [My Notebook](https://www.kaggle.com/code/param302/exercise-xgboost)
- - Lesson 7: [Data Leakage](https://www.kaggle.com/code/alexisbcook/data-leakage) - [My Notebook](https://www.kaggle.com/code/param302/exercise-data-leakage)

- Kaggle [House price prediction Challenge](https://www.kaggle.com/competitions/home-data-for-ml-course/)
- - [My Notebook 1](./House_price_prediction_4.ipynb)
- - [My Notebook 2](https://www.kaggle.com/code/param302/house-price-prediction-5)
- - [My Notebook 3](https://www.kaggle.com/code/param302/house-price-prediction-6)

### Topics I have learnt
1. Intermediate Machine Learning Course
- Using Pipelines to write structural code
- Cross validation using `cross_val_score`, (use when data is less, takes more time than `train_test_split`)
- XGBoost using `XtremeGradientRegressor` aka `XGBRegressor`
- Data Leakage, how to handle data leakage
2. House price prediction
- One by Imputing missing values, doing Ordinal Encoding using `RandomForestRegressor`.
- One mostly same as above but used more features
- One using `Cross Validation` and `Pipelines` with `RandomForestRegressor`.

### Software used
- Jupyter Notebook
- Python 3.10.2
- Numpy 1.22.4
- pandas 1.4.2
- scikit-learn 1.1.1
- XGBoost 1.6.1

### My Notebooks
- [L4 - Pipelines.ipynb](./L4%20-%20Pipelines.ipynb)
- [L5 - Cross_validation.ipynb](./L5%20-%20Cross_validation.ipynb)
- [L6 - XGBoost.ipynb](./L6%20-%20XGBoost.ipynb)
- [L7 - Data_leakage.ipynb](./L7%20-%20Data_leakage.ipynb)
- [House_price_prediction_4.ipynb](./House_price_prediction_4.ipynb)
- [House_price_prediction_5.ipynb](./House_price_prediction_5.ipynb)
- [House_price_prediction_6.ipynb](./House_price_prediction_6.ipynb)

### Conclusion:
Today I learned how to use pipelines to write cleaner code, cross validation using cross_val_score, XGBRegressor and how to handle data(Target) leakage and train_test_contamination. Also, did house price prediction using cross validation.
