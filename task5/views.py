from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['admin', 'user1', 'john_doe', 'jane_doe']

def sign_up_by_django(request):
    info = {'form': UserRegister()}
    
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            
            if (password == repeat_password 
                and age >= 18 
                and username not in users):
                
                return HttpResponse(f"Приветствуем, {username}!")
            
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))
        
        if (password == repeat_password 
            and len(password) >= 8 
            and age >= 18 
            and username not in users 
            and len(username) <= 30):
            
            return HttpResponse(f"Приветствуем, {username}!")
            
    return render(request, 'fifth_task/registration_page.html', info)
