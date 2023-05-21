from company.models import Company, Users
from .serializer import CompanySerializer, UsersSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view('GET')
@permission_classes([IsAuthenticated])
def company(request):
    queryset = Company.objects.all()
    data = CompanySerializer(queryset, many=True).data
    return Response({'all_company':data})

@api_view('GET')
@permission_classes([IsAuthenticated])
def users(request):
    queryset = Users.objects.all()
    data = UsersSerializer(queryset, many=True).data
    return Response({'all_users':data})

