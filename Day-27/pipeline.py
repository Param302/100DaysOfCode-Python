import pandas as pd
from xgboost import XGBRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder


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


if __name__ == "__main__":
    # Loading data
    house_data = pd.read_csv("./data/train.csv", index_col="Id")
    test_data = pd.read_csv("./data/test.csv", index_col="Id")
    X = house_data.drop(columns="SalePrice")
    Y = house_data["SalePrice"]
    num_cols = X.select_dtypes(exclude="object").columns
    cat_cols = X.select_dtypes("object").columns
    print("Data loaded and ready")

    print("Creating Pipeline")
    # Creating Pipeline class
    cp = CreatePipeline()
    num_transformer = cp.numerical_transformer()
    cat_transformer = cp.categorical_transformer(
                        encoder_params={
                            "handle_unknown":"use_encoded_value", 
                            "unknown_value":-1
                    })
    print("Preprocessing data")
    # preprocessor
    preprocessor = cp.data_preprocessor(
        transformers=[("num", num_transformer, num_cols),
                    ("cat", cat_transformer, cat_cols)
                    ])
    
    print("Creating model (XGBRgressor)")
    # Creating model (XGBRgressor)
    model = cp.create_model(model=XGBRegressor, n_estimators=500, learning_rate=0.05)
    pipeline = cp.pipeline(preprocessor=preprocessor, model=model)

    print("Training my model")
    pipeline.fit(X, Y)
    
    print("Predictions are:")
    test_preds = pipeline.predict(test_data)
    print(test_preds)