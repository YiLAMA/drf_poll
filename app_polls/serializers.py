from rest_framework import serializers
from .models import Poll, Question, Options, User, Answer


class PollSerializer(serializers.ModelSerializer):
    """Опросник"""

    class Meta:
        model = Poll
        fields = "__all__"

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.poll_name = validated_data.get('poll_name', instance.poll_name)
        instance.str_date = validated_data.get('str_date', instance.str_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.poll_description = validated_data.get('poll_description', instance.poll_description)
        instance.save()
        return instance


class QuestionSerializer(serializers.ModelSerializer):
    """Вопросы"""
    poll_id = serializers.IntegerField()

    class Meta:
        model = Question
        fields = ("id", "poll_id", "question_text", "question_type")
        # fields = "__all__"

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.poll_id = validated_data.get('poll_id', instance.poll_id)
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.question_type = validated_data.get('question_type', instance.question_type)
        instance.save()
        return instance


class OptionsSerializer(serializers.ModelSerializer):
    """Варианты ответа"""
    question_id = serializers.IntegerField()

    class Meta:
        model = Options
        fields = ("id", "question_id", "options_text")
        # fields = "__all__"

    def create(self, validated_data):
        return Options.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.question_id = validated_data.get('question_id', instance.question_id)
        instance.options_text = validated_data.get('options_text', instance.options_text)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    """Пользователи"""

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.mail = validated_data.get('mail', instance.mail)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):
    """Ответы"""

    user_id = serializers.IntegerField()
    poll_id = serializers.IntegerField()
    question_id = serializers.IntegerField()

    class Meta:
        model = Answer
        fields = ("id", "user_id", "poll_id", "question_id", "options_text", "options_one", "options_many")
        # fields = "__all__"

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.poll_id = validated_data.get('poll_id', instance.poll_id)
        instance.question_id = validated_data.get('question_id', instance.question_id)
        instance.options_text = validated_data.get('options_text', instance.options_text)
        instance.options_one = validated_data.get('options_one', instance.options_one)
        instance.options_many = validated_data.get('options_many', instance.options_many)
        instance.save()
        return instance
