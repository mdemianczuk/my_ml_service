from django.db import models

# Create your models here.

class Endpoint(models.Model):
    '''
    The endpoint object represents ML API endpoint

    Attributes:
        name: name of the endpoint, it will be used in API URL,
        owner: string with owner name,
        created_ad: data when endpoint was created
    '''

    name = models.CharField(max_length = 128)
    owner = models.CharField(max_length = 128)
    created_at = models.DateTimeField(auto_now_add = True, blank = True)

class MLAlgorithm(models.Model):
    '''
        Represent ML algorithm object

    Attributes:
        name:            name of the algorithm
        description:     short description how it works
        code:            code of the algorithm
        version:         version of he algorithm
        owner:           name of the owner
        created_at:      date algorithm were added
        parent_endpoint: reference to parent endpoint
    '''
    name = models.CharField(max_length = 128)
    description = models.CharField(max_length = 1000)
    code = models.CharField(max_length = 50000)
    version = models.CharField(max_length = 128)
    owner = models.CharField(max_length = 128)
    created_at = models.DateTimeField(auto_now_add = True, blank = True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete = models.CASCADE)
    
class MLAlgorithmStatus(models.Model):
    '''
    The MLAlgorithmStatus represent status of the MLAlgorithm which can change during the time.

    Attributes:
        status: The status of algorithm in the endpoint. Can be: testing, staging, production, ab_testing.
        active: The boolean flag which point to currently active status.
        created_by: The name of creator.
        created_at: The date of status creation.
        parent_mlalgorithm: The reference to corresponding MLAlgorithm.

    '''
    status = models.CharField(max_length = 128)
    active = models.BooleanField()
    created_by = models.CharField(max_length = 128)
    created_at = models.DateTimeField(auto_now_add = True, blank = True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete = models.CASCADE, related_name = "status")

class MLRequest(models.Model):
    '''
        The MLRequest will keep information about all requests to ML algorithms

    Attributes:
        input_data: input to ML algorithm in JSON format
        full_response: response of ML algorithm
        response: response of ML algorithm in JSON format 
        feedback: feedback from response in JSON format
        created_at: date created
        parrent_mlalgorithm: reference to MLAlgorithm to compute response
    '''
    input_data = models.CharField(max_length = 10000)
    full_response  = models.CharField(max_length = 10000)
    response = models.CharField(max_length = 10000)
    feedback = models.CharField(max_length = 10000, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True, blank = True)
    parrent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete = models.CASCADE)

