import pickle

#Class to serialize / deserialize the model
class PIIModelSerialize:

    def __init__(self):
        pass

    def dump(self, filePath, fileName, model):
        rf_model_pkl = open(filePath + fileName, 'wb')
        pickle.dump(model, rf_model_pkl)
        rf_model_pkl.close()
        return

    def load(self, filePath, fileName):
        model_pkl = open(filePath + fileName, 'rb')
        model = pickle.load(model_pkl)
        print("Loaded model :: ", model);
        return model