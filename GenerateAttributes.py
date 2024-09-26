from sklearn.base import BaseEstimator, TransformerMixin

class GenerateAttributes(BaseEstimator, TransformerMixin):
    def __init__(self,columns):
        self.columns = columns
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['rooms_per_household'] = X['total_rooms'] / X['households']
        X['population_per_household'] = X['population'] / X['households']
        X['bedrooms_per_room'] = X['total_bedrooms'] / X['total_rooms']
        X['income_per_household'] = X['median_income'] / X['households']
        return X
    
    def get_feature_names_out(self):
        pass
