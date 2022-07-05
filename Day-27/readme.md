# Day 27 of [#100DaysOfCode](https://twitter.com/Param3021/status/1542445802865696770)

## Task
1. Clustering with K-means
2. PCA                      (only video)
3. House price prediction

---

## Created `CreatePipeline` for creating pipeline and making model [🔗](./pipeline.py)
```python
class CreatePipeline:
    """Create Pipeline
    methods:
        pipeline: Create Final Pipeline
        
        create_model: Create the provided model
        
        numerical_transformer: Transform numerical cols
        
        categorical_transformer: Transform categorical cols \
        OneHotEncoding / OrdinalEncoding
        
        data_preprocessor: Preprocess the data using ColumnTransformer     
        """
    
    def pipeline(self, *, preprocessor, model, verbose=False):
        """Creates pipeline
        params:
            preprocessor
            model
        """
        steps = [("preprocessor", preprocessor),
                 ("model", model)]
        return Pipeline(steps=steps, verbose=verbose)
    
    
    def numerical_transformer(self, *, strategy="mean", **params):
        """Transform numerical columns using `SimpleImputer`.
        params:
            strategy: "mean" | "median" | "most_frequent" | "constant"
            **params: extra keyword args for SimpleImputer"""
        
        transformer = SimpleImputer(strategy=strategy, **params)
        return transformer

    
    def categorical_transformer(self, *, 
                                imp_strategy="most_frequent", 
                                encoder_type="Ordinal", 
                                imp_params={}, encoder_params={}):
        """Transform categorical columns by making Pipeline
        `SimpleImputer` | `OneHotEncoder` | `OrdinalEncoder`.
        args:
            imp_strategy: strategy for imputer values can be
                "most_frequent" | "constant"
            encoder_type: encoder type,
                "Ordinal" | "OneHot"
        kwargs:
            imp_params: keyword args for `SimpleImputer`.
            encoder_params: keyword args for encoder.`
        """
        if not encoder_type in ("Ordinal", "OneHot"):
            raise ValueError(f"Inappropriate value for encoder_type passed: {encoder_type}\
            Takes one of 'Ordinal' | 'OneHot'.")
        
        encoder = OrdinalEncoder if encoder_type=="Ordinal" else OneHotEncoder
        transformer = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy=imp_strategy, **imp_params)),
            (encoder_type, encoder(**encoder_params))
        ])
        return transformer
    
    
    def data_preprocessor(self, *, transformers):
        """Preprocess the data using `ColumnTransformer`.
        Pass extact list of transformers
        to be passed in `ColumnTransformer`.
        each tuple consist of: (transformer_name,
                                transformer,
                                list_of_columns)."""
        preprocessor = ColumnTransformer(transformers=transformers)
        return preprocessor
    
    
    def create_model(self, *, model, random_state=0, n_estimators=1000, **kwargs):
        """Creates the model.
        **kwargs: keyword args for model."""
        my_model = model(random_state=random_state, n_estimators=n_estimators, **kwargs)
        return my_model
```
- It will create transformers, preprocessors and model and final pipeline, so that all the process from data preprocessing (imputing / transforming) done in 1 place.
- Link of python file [🔗](./pipeline.py)

---

# Resources
- Kaggle's [Feature Engineering Course](https://www.kaggle.com/learn/feature-engineering)
- - Lesson 4: [Clustering with K-means](https://www.kaggle.com/code/ryanholbrook/clustering-with-k-means) - [My Notebook](https://www.kaggle.com/code/param302/exercise-clustering-with-k-means/)

- Kaggle [House price prediction Challenge](https://www.kaggle.com/competitions/home-data-for-ml-course/)
- - [My Notebook 1](https://www.kaggle.com/param302/house-price-prediction-12)
- - [My Notebook 1](https://www.kaggle.com/param302/house-price-prediction-13)

### Topics I have learnt
1. Clustering with K-means
2. PCA
3. House price prediction
- One with Mutual Information and used `XGBRegressor`       (Score: 14900.48264)
- One with creating new features and used `XGBRegressor`    (Score: 15078.56818)

### Software used
- Jupyter Notebook
- Python 3.10.2
- Numpy 1.22.4
- pandas 1.4.2
- Matplotlib 3.5.2
- Seaborn 0.11.2
- scikit-learn 1.1.1
- XGBoost 1.6.1

### My Notebooks
- [House_price_prediction_12.ipynb](./House_price_prediction_12.ipynb)
- [House_price_prediction_13.ipynb](./House_price_prediction_13.ipynb)
- [L4 - Clustering_with_K-means.ipynb](./L4%20-%20Clustering_with_k-means.ipynb)

### Conclusion:
Today I learned about K-means clustering and PCA. Also did house price prediction with `XGBRegressor` and feature engineering.
