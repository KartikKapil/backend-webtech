from main.models import Customer
from main.serialzier import CustomerSerializer

def jwt_response_handler(token,user = None,request = None):
    return {
        'token':token,
        'Customer':CustomerSerializer(user,context={'request':request}).data
    }