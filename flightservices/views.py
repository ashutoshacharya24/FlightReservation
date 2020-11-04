from django.shortcuts import render
from flightservices.models import Flight,Passenger,Reservation
from flightservices.serializers import FlightSerializer,PassengerSerializer,ReservstionSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity= request.data['arriavalCity'])
    serializer = FlightSerializer(flights,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightid'])
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lasttName = request.data['lasttName']
    passenger.middletName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    Reservation.save()
    return Response(status=status.HTTP_201_CREATED)

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservstionSerializer