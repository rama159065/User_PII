
import pandas as pd
import numpy as np
import glob
import os

class DataReader:


    def __init__(self):
        pass

    def readCsv(self, fileName):
        if (os.path.isfile(fileName)):
            return pd.read_csv(fileName)

    def readExcel(self, fileName):
        if (os.path.isfile(fileName)):
            return pd.read_excel(fileName)

    def readJson(self):
        pass

    def readFromDB(self):
        pass

    def mergeData(self, filePathDir):
        if (os.path.isdir(filePathDir)):
            allFiles = glob.glob(os.path.join(filePathDir, "*.csv"))
            df_list = []
            for file_ in allFiles:
                df = pd.read_csv(file_)
                df_list.append(df)
            final_df = pd.concat(df_list, axis=1)
            return final_df


