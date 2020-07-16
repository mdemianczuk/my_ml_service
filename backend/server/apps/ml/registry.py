from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgorithm
from apps.endpoints.models import MLAlgorithmStatus

class MLRegistry:
    def __init__(self):
        self.endpoints = {} #dictionary
        
    def add_algorithm(self, endpoint_name, alg_object, alg_name,
                      alg_status, alg_version, owner, alg_desc, alg_code):
        #get endpoint
        endpoint, _ = Endpoint.objects.get_or_create(name=endpoint_name, owner=owner)
        #get algorithm
        database_object, algorithm_created = MLAlgorithm.objects.get_or_create(
            name=alg_name, description=alg_desc,
            code=alg_code, version=alg_version, owner=owner,
            parent_endpoint=endpoint
        )
        if algorithm_created:
            status = MLAlgorithmStatus(status = alg_status, created_by = owner,
                                       parent_mlalgorithm = database_object,
                                       active = True)
            status.save()
            
        #add to registry
        self.endpoints[database_object.id] = alg_object
        