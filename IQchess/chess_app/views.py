from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Game, Move, UserProfile, Chessbot, Analysis
from .serializers import GameSerializer, MoveSerializer, UserProfileSerializer, ChessbotSerializer, AnalysisSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['player__username', 'chessbot__level']
    ordering_fields = ['start_time', 'end_time']

    def perform_create(self, serializer):
        serializer.save(player=self.request.user)

class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['game__player__username', 'move_notation']
    ordering_fields = ['move_number']

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class ChessbotViewSet(viewsets.ModelViewSet):
    queryset = Chessbot.objects.all()
    serializer_class = ChessbotSerializer
    permission_classes = [IsAuthenticated]

class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['game__player__username', 'move__move_notation']
    ordering_fields = ['game', 'move']