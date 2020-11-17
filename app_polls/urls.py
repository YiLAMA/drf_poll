from django.urls import path, include
from .views import (
    PollViewAdmin, PollViewAdminID,
    QuestionViewAdmin, QuestionViewAdminID,
    QuestionPollViewAdmin,
    PollActivView, AnswerView, AnswerViewUserID,
    # Дополнение:
    AnswerViewAdmin, AnswerViewAdminID,
    OptionsViewAdmin, OptionsViewAdminID,
    UserViewAdmin, UserViewAdminID
)

app_name = 'app_polls'
urlpatterns = [
    path('admin/', include([
        path('polls/', PollViewAdmin.as_view()),
        path('polls/<int:id>', PollViewAdminID.as_view()),
        path('polls/<int:poll_id>/questions/', QuestionPollViewAdmin.as_view()),
        path('questions/', QuestionViewAdmin.as_view()),
        path('questions/<int:id>', QuestionViewAdminID.as_view()),
        # Дополнение:
        path('answer/', AnswerViewAdmin.as_view()),
        path('answer/<int:id>', AnswerViewAdminID.as_view()),
        path('options/', OptionsViewAdmin.as_view()),
        path('options/<int:id>', OptionsViewAdminID.as_view()),
        path('users/', UserViewAdmin.as_view()),
        path('users/<int:id>', UserViewAdminID.as_view()),
    ])),
    path('user/', include([
        path('polls_activ/', PollActivView.as_view()),
        path('answer/', AnswerView.as_view()),
        path('answer/<int:user_id>', AnswerViewUserID.as_view()),
    ])),
]
