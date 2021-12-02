import os
import pandas as pd



class Create_Dataset:
    """This class is used to create model training data from the data folders given"""

    def __init__(self, dirname):
        self.path = os.path.join(os.getcwd(), dirname)

    def cleanData(self, csv_file_path):
        data = pd.read_csv(
            csv_file_path, usecols=[1, 2, 3, 4, 5, 6], skiprows=[0, 1, 2, 3], header=0
        )
        return data
    
    def createDataforSingleClass(self, foldername):
        path = os.path.join(self.path, foldername)
        files = os.listdir(path)
        dataSingleClass = pd.DataFrame(
            columns=[
                "avg_rss12",
                "var_rss12",
                "avg_rss13",
                "var_rss13",
                "avg_rss23",
                "var_rss23",
            ]
        )
        for file in files:
            csvpath = os.path.join(path, file)
            data = self.cleanData(csvpath)
            dataSingleClass = dataSingleClass.append(data, ignore_index=True)

        dataSingleClass["activity"] = foldername

        return dataSingleClass
    
    def getAllData(self):
        foldernames = [foldername for foldername in os.listdir(self.path) if os.path.isdir(os.path.join(self.path,foldername))]
        
        data = pd.DataFrame()
        for foldername in foldernames:           
            df = self.createDataforSingleClass(foldername)
            data = pd.concat([data, df], ignore_index=True)
            data.to_csv('TrainData/data.csv', index=False)
        return data
    