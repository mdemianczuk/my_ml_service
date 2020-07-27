"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

#ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.income_classifier.extra_trees import ExtraTreesClassifier

try:
    registry = MLRegistry() #create registry
    registry.add_algorithm(endpoint_name = "income_classifier", 
                           alg_object = RandomForestClassifier(), 
                           alg_name = "Random Forest",
                           alg_status = "production",
                           alg_version = "0.0.1",
                           owner = "Piotr",
                           alg_desc = "Random Forest with pre and post processing",
                           alg_code = inspect.getsource(RandomForestClassifier)
                          )
    registry.add_algorithm(endpoint_name = "income_clasiifier",
                           alg_object = ExtraTreesClassifier(),
                           alg_name = "Extra Trees",
                           alg_status = "testing",
                           alg_version = "0.0.1",
                           owner = "Pewnie Piotr",
                           alg_desc = "Extra Trees with pre and post...",
                           alg_code = inspect.getsource(ExtraTreesClassifier)
                          )
except Exception as e:
    print("Exception while loading algorithm to registry", str(e))
