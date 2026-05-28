from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Station
from .serializers import StationSerializers

def home(request):
    return render(request, 'index.html')

@api_view(['GET'])
def all_station(request):
    country = request.GET.get('country')
    qs = Station.objects.filter(country=country) if country else Station.objects.all()
    serializer = StationSerializers(qs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def country_list(request):
    countries = Station.objects.values_list('country', flat=True).distinct()
    return Response(countries)