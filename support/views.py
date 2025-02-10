from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from support.models import SupportTicket
from support.serializers import SupportTicketSerializer


class SupportTicketListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class SupportTicketRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer