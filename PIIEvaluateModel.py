
class PIIEvaluateModel:

    def __init__(self):
        pass

    def predict(self, model, input):
        predictions = model.predict(input)
        return predictions

    def predict_proba(self, model, input):
        predict_proba = model.predict_proba(input)
        return predict_proba
