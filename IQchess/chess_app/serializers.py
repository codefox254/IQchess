from rest_framework import serializers
from .models import Game, Move, UserProfile, Chessbot, Analysis

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ChessbotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chessbot
        fields = '__all__'

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    moves = MoveSerializer(many=True, required=False)
    analysis = AnalysisSerializer(many=True, required=False)
    player = serializers.StringRelatedField()  # To display the username instead of the user ID
    chessbot = ChessbotSerializer()

    class Meta:
        model = Game
        fields = '__all__'

    def create(self, validated_data):
        moves_data = validated_data.pop('moves', [])
        analysis_data = validated_data.pop('analysis', [])
        game = Game.objects.create(**validated_data)
        for move_data in moves_data:
            Move.objects.create(game=game, **move_data)
        for analysis in analysis_data:
            Analysis.objects.create(game=game, **analysis)
        return game

    def update(self, instance, validated_data):
        moves_data = validated_data.pop('moves', [])
        analysis_data = validated_data.pop('analysis', [])
        instance.player = validated_data.get('player', instance.player)
        instance.chessbot = validated_data.get('chessbot', instance.chessbot)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.moves = validated_data.get('moves', instance.moves)
        instance.result = validated_data.get('result', instance.result)
        instance.save()

        for move_data in moves_data:
            move = Move.objects.get(id=move_data['id'])
            move.move_number = move_data.get('move_number', move.move_number)
            move.move_notation = move_data.get('move_notation', move.move_notation)
            move.is_correct = move_data.get('is_correct', move.is_correct)
            move.feedback = move_data.get('feedback', move.feedback)
            move.save()

        for analysis in analysis_data:
            analysis_instance = Analysis.objects.get(id=analysis['id'])
            analysis_instance.analysis_data = analysis.get('analysis_data', analysis_instance.analysis_data)
            analysis_instance.save()

        return instance