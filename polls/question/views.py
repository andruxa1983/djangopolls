# coding: utf-8
from django.shortcuts import render, redirect
from question.models import Question
from django.http import Http404
from django import forms


def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'question/question_list.html', {
        'question': questions
    })



def question_create(request):
    form = QuestionForm(request.GET or None)
    if form.is_valid():
        form.save()
    return render(request, 'question/question_create.html', {'form': form})
    # if not 'phone_number' in request.GET:
    #     return render(request, 'question/question_create.html')
    # #request_num = request.GET['request_num']
    # title = request.GET['title']
    # text = request.GET['text']
    # phone_number = request.GET['phone_number']
    # full_name = request.GET['full_name']
    # user_email = request.GET['user_email']




    # Question.objects.create(
    #     #request_num = request_num,
    #     title = title,
    #     text = text,
    #     full_name = full_name,
    #     phone_number = phone_number,
    #     user_email = user_email,
    # )

    return render(request, 'question/question_create.html')
    return redirect('/')
    
def delete_question(request, question_id):
    if not request.user.is_superuser:
        raise Http404
    question = Question.objects.get(id=question_id)
    question.delete()
    return redirect('/')

class  QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text', 'full_name', 'phone_number', 'user_email', )
        #exclude = ('request_num', )



# def question_status_new(request, question_id):
#     new = Question.objects.get(id=question_id)
#     new.status = 'new'
#     new.save()
#     return redirect('/')
    
# def question_status_published(request, question_id):
#     published = Question.objects.get(id=question_id)
#     published.status = 'published'
#     published.save()
#     return redirect('/')
    
# def question_status_decline(request, question_id):
#     decline = Question.objects.get(id=question_id)
#     decline.status = 'decline'
#     decline.save()
#     return redirect('/')

# def question_status_duplicate(request, question_id):
#     duplicate = Question.objects.get(id=question_id)
#     duplicate.status = 'duplicate'
#     duplicate.save()
#     return redirect('/')



def pub_view(request):
    questions = Question.objects.filter(status='published')
    return render(request, 'question/question_list.html', {
        'question': questions
    })

def change_status(request, question_id, status_name):
    q = Question.objects.get(id=question_id)
    q.status = status_name
    q.save()
    return redirect('/')
    # {% url 'change_status' question_id 'published' %}
    # {% url 'change_status' question_id 'new' %}

def question_detail(request, question_id):
    qs = Question.objects.get(id=question_id)
    return render(request,'question/question_detail.html', { 'question': qs })
  
    
# Create your views here.
