from django.shortcuts import render

# Create your views here.


from .models import Poll, Question, Options, User, Answer
from .serializers import PollSerializer, QuestionSerializer, OptionsSerializer, UserSerializer, AnswerSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import generics, status
from rest_framework.exceptions import ParseError
from datetime import date


class AdminAPIView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]


class PollViewAdmin(generics.ListAPIView, AdminAPIView):
    """Все Опросы"""
    serializer_class = PollSerializer

    def get(self, request):
        """Получение всех созданных Опросов"""
        polls = Poll.objects.all()
        # параметр many сообщает сериализатору, что он будет сериализовать более одной статьи.
        serializer = PollSerializer(polls, many=True)
        return Response({"Опросы": serializer.data})

    def post(self, request):
        """Добавление нового Опроса"""
        try:
            serializer = PollSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            date_ = serializer.validated_data
            if date_['str_date'] > date_['end_date']:
                raise Exception('Ошибка: Старт Опроса не может быть позже окончания')
            newPoll = Poll(**date_)
            newPoll.save()
            return Response(PollSerializer(newPoll).data)
        except Exception as ex:
            raise ParseError(ex)


class PollViewAdminID(generics.RetrieveAPIView, AdminAPIView):
    """Опросы по ID"""
    serializer_class = PollSerializer

    def get(self, request, id):
        """Получение Опроса по ID"""
        poll = Poll.objects.get(id=id)
        serializer = PollSerializer(poll)
        return Response({"Опрос": serializer.data})

    def put(self, request, id):
        """Изменение Опроса по ID. После начало Опроса по дате, менять его нельзя"""
        try:
            serializer = PollSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            date_ = serializer.validated_data
            if date_['str_date'] < date.today():
                raise Exception('Ошибка: Опрос стартанул, его изменить нельзя')
            serializer.save()
            return Response({f"Опрос c номером '{id}' успешно обновлён"})
        except Exception as ex:
            raise ParseError(ex)

    def delete(self, request, id):
        """Удаление Опроса по ID"""
        poll = get_object_or_404(Poll.objects.all(), pk=id)
        poll.delete()
        return Response({f"Опрос с номером id '{id}' был успешно удалён."})


class QuestionPollViewAdmin(generics.ListAPIView, AdminAPIView):
    """Вопросы по ID Опроса"""
    serializer_class = QuestionSerializer

    def get(self, request, poll_id):
        """Получение всех вопросов определенного Опроса по его ID"""
        poll = Poll.objects.get(id=poll_id)
        serializer = PollSerializer(poll)
        question = Question.objects.filter(poll=poll_id)
        question_poll = QuestionSerializer(question, many=True)
        return Response({"Опрос": serializer.data, "Вопросы": question_poll.data})


class QuestionViewAdmin(generics.ListAPIView, AdminAPIView):
    """Абсолютно все вопросы"""
    serializer_class = QuestionSerializer

    def get(self, request):
        """Получение всех созданных вопросов"""
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response({"Вопросы": serializer.data})

    def post(self, request):
        """Добавление нового вопроса"""
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Вопрос успешно создан": serializer.data})
        else:
            return Response(serializer.errors)


class QuestionViewAdminID(generics.RetrieveAPIView, AdminAPIView):
    """Вопросы по ID"""
    serializer_class = QuestionSerializer

    def get(self, request, id):
        """Получение вопроса по ID"""
        question = Question.objects.get(id=id)
        serializer = QuestionSerializer(question)
        return Response({"Poll": serializer.data})

    def put(self, request, id):
        """Изменение вопроса по ID"""
        question = get_object_or_404(Question.objects.all(), pk=id)
        serializer = QuestionSerializer(instance=question, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {f"Вопрос c номером '{id}' успешно изменён"})

    def delete(self, request, id):
        """Удаление вопроса по ID"""
        question = get_object_or_404(Question.objects.all(), pk=id)
        question.delete()
        return Response({f"Вопрос с номером id '{id}' был успешно удалён."})


# Далее идёт возможности для обычного пользователя, без наследования AdminAPIView

class PollActivView(generics.ListAPIView):
    """Список активных Опросов"""
    serializer_class = PollSerializer

    def get(self, request):
        """Получение списка активных Опросов (по дате начались, но не закончились)"""
        today = date.today()
        polls_activ = Poll.objects.filter(str_date__lte=today, end_date__gt=today)
        return Response(PollSerializer(polls_activ, many=True).data)


class AnswerView(generics.ListAPIView):
    """Прохождение опроса"""
    serializer_class = AnswerSerializer

    def get(self, request):
        """Недоступен для Пользователей. Используйте запрос: GET /admin/answer/"""
        raise Exception('Ошибка: Данный запрос недоступен для пользователей. Используйте запрос GET /admin/answer/')

    def post(self, request):
        """Добавление нового ответа пользователя (Прохождение опроса)"""
        try:
            serializer = PollSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            date_ = serializer.validated_data
            if date_['str_date'] > date_['end_date']:
                raise Exception('Ошибка: Старт Опроса не может быть позже окончания')
            newPoll = Poll(**date_)
            newPoll.save()
            return Response(PollSerializer(newPoll).data)
        except Exception as ex:
            raise ParseError(ex)


class AnswerViewUserID(generics.RetrieveAPIView):
    """Все ответы пользователя по его ID"""
    serializer_class = AnswerSerializer

    def get(self, request, user_id):
        """
        Получение пройденных пользователем Опросов с детализацией по ответам.
        Отсортирован по ID Опроса.
        """
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        answer = Answer.objects.filter(user=user_id).order_by('poll')
        answer_user = AnswerSerializer(answer, many=True)
        return Response({"Пользователь": serializer.data, "Ответы": answer_user.data})


# Далее, по условию задачи, необязательны


class AnswerViewAdmin(generics.ListAPIView, AdminAPIView):
    """Все ответы"""
    serializer_class = AnswerSerializer

    def get(self, request):
        """Получение всех ответов"""
        answer = Answer.objects.all()
        serializer = AnswerSerializer(answer, many=True)
        return Response({"Все ответы записанные": serializer.data})


class AnswerViewAdminID(generics.RetrieveAPIView, AdminAPIView):
    """Ответы по ID"""
    serializer_class = QuestionSerializer

    def get(self, request, id):
        """Получение ответ по ID"""
        answer = Answer.objects.get(id=id)
        serializer = AnswerSerializer(answer)
        return Response({"Poll": serializer.data})

    def put(self, request, id):
        """Изменение ответа по ID"""
        answer = get_object_or_404(Answer.objects.all(), pk=id)
        serializer = AnswerSerializer(instance=answer, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {f"Ответ c номером '{id}' успешно изменён"})

    def delete(self, request, id):
        """Удаление ответа по ID"""
        answer = get_object_or_404(Answer.objects.all(), pk=id)
        answer.delete()
        return Response({f"Ответ с номером id '{id}' был успешно удалён."})


class OptionsViewAdmin(generics.ListAPIView, AdminAPIView):
    """Все варианты ответов"""
    serializer_class = OptionsSerializer

    def get(self, request):
        """Получение все записанные варианты ответа"""
        options = Options.objects.all()
        serializer = OptionsSerializer(options, many=True)
        return Response({"Все созданные варианты ответов": serializer.data})

    def post(self, request):
        """Добавление нового вопроса"""
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Вопрос успешно создан": serializer.data})
        else:
            return Response(serializer.errors)


class OptionsViewAdminID(generics.RetrieveAPIView, AdminAPIView):
    """Варианты ответа по ID"""
    serializer_class = OptionsSerializer

    def get(self, request, id):
        """Получение варианта ответа по ID"""
        options = Options.objects.get(id=id)
        serializer = OptionsSerializer(options)
        return Response({"Вариант ответа": serializer.data})

    def put(self, request, id):
        """Изменение варианта ответа по ID"""
        options = get_object_or_404(Options.objects.all(), pk=id)
        serializer = OptionsSerializer(instance=options, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {f"Вариант ответа c номером '{id}' успешно изменён"})

    def delete(self, request, id):
        """Удаление варианта ответа по ID"""
        options = get_object_or_404(Options.objects.all(), pk=id)
        options.delete()
        return Response({f"Вариант ответа с номером id '{id}' был успешно удалён."})


class UserViewAdmin(generics.ListAPIView, AdminAPIView):
    """Все пользователи"""
    serializer_class = UserSerializer

    def get(self, request):
        """Получение всех пользователей"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"Все пользователи": serializer.data})

    def post(self, request):
        """Добавление нового пользователя"""
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Пользователь успешно добавлен": serializer.data})
        else:
            return Response(serializer.errors)


class UserViewAdminID(generics.RetrieveAPIView, AdminAPIView):
    """Пользователи по ID"""
    serializer_class = UserSerializer

    def get(self, request, id):
        """Получение пользователя по ID"""
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response({"Пользователь": serializer.data})

    def put(self, request, id):
        """Изменение пользователя по ID"""
        user = get_object_or_404(User.objects.all(), pk=id)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {f"Пользователь c номером '{id}' успешно изменён"})

    def delete(self, request, id):
        """Удаление пользователя по ID"""
        user = get_object_or_404(User.objects.all(), pk=id)
        user.delete()
        return Response({f"Пользователь  с номером id '{id}' был успешно удалён."})
