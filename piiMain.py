
from piiFeatureCreation import *
from PIITrainTestSplit import *
from PIIModelBuilder import *
from PIIModelSerialize import *
from PIIMetrics import *
from PIIEvaluateModel import *

inputDir = 'D:\\python_examples\\PII_DATA\\files\\'
fileName = "generic_model.pkl"
filePath = "D:\python_examples\PII_DATA\pickle\\"
cols, features_df = prepareData(inputDir)

train, test, y, test_y = PIITrainTestSplit().split_data(features_df, cols)
builder = PIIModelBuilder()
model = builder.trainModel(train, y)
predictions, predictions_proba = builder.testModel(test, test_y, model)
merics = PIIMetrics()
merics.test_accuracy(test_y, predictions)
merics.test_confusion_matrix(test_y, predictions)

PIIModelSerialize().dump(filePath, fileName, model)


############Evaluate############33
testDir = 'D:\\python_examples\\PII_DATA\\test\\'
ser = PIIModelSerialize()
model = ser.load(filePath, fileName)
cols, df = prepareData(testDir)
evaluate = PIIEvaluateModel()
evaluate.predict_proba(model, test)
evaluate.predict(model, test)



