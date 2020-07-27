from apps.ml.income_classifier.algorithms import AlgorithmClassifier
import joblib

class RandomForestClassifier(AlgorithmClassifier):
    def __init__(self):
        super(RandomForestClassifier, self).__init__()
        self.model = joblib.load(self.path_to_artifacts + "random_forest.joblib")
