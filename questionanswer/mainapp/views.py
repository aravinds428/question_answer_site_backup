from django.shortcuts import render
from .models import Question, Answer

# Create your views here.


def home(request):
    questions = Question.objects.all().order_by('-date_posted')
    return render(request, 'mainapp/home_page.html', {'questions': questions})


def display_content(request):
	question_id = int(request.POST['question_id'])
	print(question_id)
	question = Question.objects.get(id=question_id)
	answers = Answer.objects.filter(question=question_id).order_by('-date_posted')
	return render(request,'mainapp/question_content.html',{'question':question,'answers':answers})


def display_about(request):
	return render(request,'mainapp/about.html')