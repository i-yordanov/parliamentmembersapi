from rest_framework import generics
from .serializers import ParliamentMemberSerializer
from pmapi.models import ParliamentMember
from datetime import datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.db.models import Q

# Create your views here.


class RetrieveByIDParliamentMemberAPIVIEW(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ParliamentMember.objects.all()
    serializer_class = ParliamentMemberSerializer


class SearchParliamentMemberAPIView(generics.ListAPIView):
    serializer_class = ParliamentMemberSerializer
    queryset = ParliamentMember.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']


class ListParliamentMemberAPIView(generics.ListAPIView):
    serializer_class = ParliamentMemberSerializer

    def get_queryset(self):

        queryset = ParliamentMember.objects.all()

        first_name = self.request.query_params.get('fn', None)
        profession = self.request.query_params.get('prof', None)
        last_name = self.request.query_params.get('ln', None)
        date_of_birth = self.request.query_params.get('dob', None)
        place_of_birth = self.request.query_params.get('pob', None)
        political_force = self.request.query_params.get('pp', None)
        if political_force == 'GERB':
            political_force = 'ГЕРБ'
        elif political_force == 'BSP':
            political_force = 'БСП'
        elif political_force == 'DPS':
            political_force = 'ДПС'
        elif political_force == 'OP':
            political_force = 'ОП'
        elif political_force == 'VOLQ':
            political_force = 'ВОЛЯ'
        language = self.request.query_params.get('language', None)
        email = self.request.query_params.get('email', None)

        if first_name is not None:
            queryset = queryset.filter(first_name=first_name)
        if profession is not None:
            queryset = queryset.filter(Q(profession1=profession) | Q(profession2=profession))
        if last_name is not None:
            queryset = queryset.filter(last_name=last_name)
        if date_of_birth is not None:
            date_of_birth = datetime.strptime(str(date_of_birth), '%Y%m%d').date()
            queryset = queryset.filter(date_of_birth=date_of_birth)
        if place_of_birth is not None:
            queryset = queryset.filter(place_of_birth=place_of_birth)
        if political_force is not None:
            queryset = queryset.filter(political_force=political_force)
        if language is not None:
            queryset = queryset.filter(Q(language1=language) | Q(language2=language) | Q(language3=language) | Q(language4=language) | Q(language5=language))
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset
