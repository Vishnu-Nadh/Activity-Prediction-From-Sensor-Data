import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle


class Preprocessor:
    """this class preprocess the data before sending into machine learning algorithm"""

    def __init__(self, data):
        self.data = data
        self.map_dic = {
            "bending1": 0,
            "bending2": 1,
            "cycling": 2,
            "lying": 3,
            "sitting": 4,
            "standing": 5,
            "walking": 6,
        }
        self.cols_for_transformation = ["var_rss12", "var_rss13", "var_rss23"]

    def encodeTargetFeature(self, data):
        data.activity = data["activity"].map(self.map_dic)
        return data

    def logTransformation(self, colname, data):
        return np.log1p(data[colname])

    def splitToFeaturesAndTarget(self, data):
        X = data.drop("activity", axis=1)
        Y = data.activity
        return X, Y

    def guassianTransformation(self, X):
        for col in self.cols_for_transformation:
            X[col] = self.logTransformation(col, X)
        return X

    def standerdScaling(self, X):
        scaler = StandardScaler()
        std_scaler = scaler.fit(X)
        pickle.dump(std_scaler, open("Scaler/std_scaler.sav", "wb"))
        X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
        return X

    def removeOutliers(self, data, colnames):
        for column in colnames:
            IQR = data[column].quantile(0.75) - data[column].quantile(0.25)
            upper_bridge = data[column].quantile(0.75) + (1.5 * IQR)
            lower_bridge = data[column].quantile(0.25) - (1.5 * IQR)

            data.loc[data[column] > upper_bridge, column] = upper_bridge
            data.loc[data[column] < lower_bridge, column] = lower_bridge

            uc = data.loc[data[column] > upper_bridge, column].count()
            lc = data.loc[data[column] < lower_bridge, column].count()

            sample = data.loc[
                (data[column] < upper_bridge) & (data[column] > lower_bridge), column
            ]
            filluc = sample.sample(uc, random_state=11)
            filllc = sample.sample(lc, random_state=22)

            data.loc[data[column] > upper_bridge, column] = filluc
            data.loc[data[column] < lower_bridge, column] = filllc

        return data

    def Preprocess(self):
        data = self.encodeTargetFeature(self.data)
        X, Y = self.splitToFeaturesAndTarget(data)
        X_g = self.guassianTransformation(X)
        X_s = self.standerdScaling(X_g)
        X_o = self.removeOutliers(X_s, X_s.columns)
        return X_o, Y

    def preprocessPred(self):
        data = self.guassianTransformation(self.data)
        scaler = pickle.load(open("Scaler/std_scaler.sav", "rb"))
        data_p = pd.DataFrame(scaler.transform(data), columns=data.columns)
        return data_p
