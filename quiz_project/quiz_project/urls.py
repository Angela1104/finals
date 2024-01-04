from django.contrib import admin
from django.urls import path, include
from nvento.views import HomeView, LoginView, ListOfStudentsView, QuizView, AnswerKeyView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('students/', ListOfStudentsView.as_view(), name='students'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('quiz/answerkey.html', AnswerKeyView.as_view(), name='answerkey'),
    path('quiz.html', QuizView.as_view(), name='quiz_html'),
    path('login/index.html', HomeView.as_view(), name='home_index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
