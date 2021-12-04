import pickle


class Predict_Output:
    """This class used to predict the output from input data using saved machine learning model"""

    def __init__(self, data):
        self.data = data
        self.map_dic = {
            "0": "bending1",
            "1": "bending2",
            "2": "cycling",
            "3": "lying",
            "4": "sitting",
            "5": "standing",
            "6": "walking",
        }

    def preditOutput(self):
        model = pickle.load(open("Model/multiclassLogReg.pickle", "rb"))
        output_value = str(int(model.predict(self.data)[0]))
        output = self.map_dic[output_value]
        return output
