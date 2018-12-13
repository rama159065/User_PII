
from sklearn.ensemble import RandomForestClassifier


#Class for Training the Model
class PIIModelBuilder:

    def __init__(self):
        pass

    def trainModel(self, trainX, target):

        clf = RandomForestClassifier(n_jobs=3, criterion='entropy', random_state=0)
        clf.fit(trainX, target)
        return clf

    def testModel(self, test, test_y, trained_model):
        predictions = trained_model.predict(test)
        predictions_proba = trained_model.predict_proba(test)
        return (predictions, predictions_proba)

    def testModel_proba(self, test, test_y, trained_model):
        predictions_proba = trained_model.predict_proba(test)
        return predictions_proba
