from .models import SupportTicket
from rest_framework import generics
from .serializers import SupportTicketSerializer
from rest_framework.permissions import IsAuthenticated


class SupportTicketListCreateView(generics.ListCreateAPIView):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class SupportTicketRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
    permission_classes = [IsAuthenticated]