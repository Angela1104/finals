from django.shortcuts import render
from django.views import View
from .models import QuizQuestion

class HomeView(View):
    def get(self, request):
        # Example logic: Get some data from the database
        data = {'welcome_message': 'Welcome to the Quiz App!'}
        return render(request, 'index.html', context=data)

class LoginView(View):
    def get(self, request):
        # Example logic: Check if the user is already authenticated
        if request.user.is_authenticated:
            return render(request, 'already_logged_in.html')
        return render(request, 'login.html')

class ListOfStudentsView(View):
    def get(self, request):
        # Example logic: Retrieve a list of students from the database
        students = ['Student1', 'Student2', 'Student3']
        return render(request, 'list_of_students.html', context={'students': students})

class QuizView(View):
    def get(self, request):
        # Example logic: Fetch quiz questions from the database
        questions = QuizQuestion.objects.all()
        return render(request, 'quiz.html', context={'questions': questions})

class AnswerKeyView(View):
    def get(self, request):
        # Example logic: Display the answer key for the quiz
        answer_key = {'Question1': 'OptionA', 'Question2': 'OptionB', 'Question3': 'OptionC'}
        return render(request, 'answerkey.html', context={'answerkey': answer_key})

# Add the quiz_view function as a separate view
def quiz_view(request):
    return render(request, 'quiz.html')

def answerkey(request):
    # Your logic for handling the answerkey.html page
    return render(request, 'answerkey.html')