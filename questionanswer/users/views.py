from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm


from django.contrib.auth.models import User
from mainapp.models import Question, Answer
# Create your views here.


def register(request):
    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def display_profile(request):
    user = User.objects.get(username=request.user.username)
    questions = Question.objects.filter(asked_user=user).order_by('-date_posted')
    return render(request,'users/profile.html',{'questions':questions})


@login_required
def create_question(request):
    if(request.method == "POST"):
        title_value = request.POST['title']
        question_content = request.POST['question']
        user_name = request.user.username
        user = User.objects.get(username=user_name)
        obj = Question(title=title_value,content=question_content,asked_user=user)
        obj.save()
        messages.success(request, 'Question successfully posted')
        #return redirect('create-question')
        return render(request,'users/create_question.html')

    else:
        return render(request,'users/create_question.html')

@login_required
def create_answer(request):
    if(request.method == "GET"):
        question_id = int(request.GET['question_id'])
        request.session['question_id'] = question_id
        return render(request,'users/answer_question.html')
    else:
        if('question_id' in request.session):
            question_id = request.session['question_id']
        question_obj = Question.objects.get(id=question_id)
        answer = request.POST['answer']
        user_name = request.user.username
        user = User.objects.get(username=user_name)
        answer_obj = Answer(question=question_obj,answer_content=answer,answered_user=user)
        answer_obj.save()
        messages.success(request, 'Answer successfully posted')
        return redirect('profile')


