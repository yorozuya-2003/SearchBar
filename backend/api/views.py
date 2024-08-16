from django.shortcuts import render
from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer


class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'


class ProfileList(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query')
        query = query.strip() if query is not None else None

        # if query is not None and query != '':
        #     profiles = Profile.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))

        if query:
            query_parts = query.split()
            
            query_filters = Q()
            for part in query_parts:
                # query_filters |= Q(first_name__icontains=part) | Q(last_name__icontains=part)
                query_filters |= Q(first_name__trigram_similar=part) | Q(last_name__trigram_similar=part)

            profiles = Profile.objects.filter(query_filters).order_by('first_name').values()
        else:
            profiles = []

        serializer = ProfileSerializer(profiles, many=True)

        # limit the number of profiles returned
        profile_limit = 10
        return Response(serializer.data[:profile_limit])

        return Response(serializer.data)

