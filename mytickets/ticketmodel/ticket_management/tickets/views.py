from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tickets
from .serializers import TicketsSerializer
from rest_framework import viewsets


# class TicketsViewSet(viewsets.ModelViewSet):
#     queryset = Tickets.objects.all()
#     serializer_class = TicketsSerializer


@api_view(['POST'])
def create_ticket(request):
    serializer = TicketsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_ticket(request, pk):
    try:
        ticket = Tickets.objects.get(pk=pk)
    except Tickets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TicketsSerializer(ticket, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
