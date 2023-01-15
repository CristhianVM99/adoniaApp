from . models import Users,Membership,Tribe,Ministry,Red
from rest_framework import viewsets, permissions
from . serializer import UsersSerializer,MembershipSerializer,TribeSerializer,MinistrySerializer,RedSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MembershipSerializer

class TribeViewSet(viewsets.ModelViewSet):
    queryset = Tribe.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TribeSerializer

class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MinistrySerializer

class RedViewSet(viewsets.ModelViewSet):
    queryset = Red.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RedSerializer