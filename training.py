from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle


class Train_Model:
    """This class used for the entire model training using logistic regression"""

    def __init__(self, features, target):
        self.X = features
        self.Y = target

    def trainTestSplit(self, X, Y):
        x_train, x_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.2, random_state=100
        )
        return x_train, x_test, y_train, y_test

    def trainModel(self):
        LogReg = LogisticRegression(multi_class="multinomial", solver="saga")
        LogReg.fit(self.X, self.Y)
        pickle.dump(LogReg, open("Model/multiclassLogReg.pickle", "wb"))

        return "Training completed succussfully"

