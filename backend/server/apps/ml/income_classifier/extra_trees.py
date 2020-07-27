from apps.ml.income_classifier.algorithms import AlgorithmClassifier
import joblib

class ExtraTreesClassifier(AlgorithmClassifier):
    def __init__(self):
        super(ExtraTreesClassifier, self).__init__()
        self.model = joblib.load(self.path_to_artifacts + "extra_trees.joblib")