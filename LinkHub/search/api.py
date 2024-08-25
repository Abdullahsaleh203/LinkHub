from django.http import JsonResponse
from rest_framework.decorators import  permission_classes, authentication_classes ,api_view


@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']
    print('query',query)
    return JsonResponse({'query': query})
  
