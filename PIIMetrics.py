from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


#Class to print the metrics
class PIIMetrics:

    def __init__(self):
        pass

    def test_accuracy(self, predictions, test_y):
        print("Model Accuracy is : ", accuracy_score(test_y, predictions))

    def test_confusion_matrix(self, predictions, test_y):
        print("confusion matrix is \n", confusion_matrix(test_y, predictions))