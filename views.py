from django.shortcuts import render,redirect,reverse
# Create your views here.
from .models import *
from .forms import *
def main(request):
    return render(request,'main.html')
def home(request):
    if request.method == 'POST':
        fr = LoginForm(request.POST)
        if fr.is_valid():
            fr.save()
            username = fr.cleaned_data.get('Username')  # Extract the username from the form
            return redirect(reverse('shop') + f'?username={username}')
    else:
        fr = LoginForm()
    return render(request, 'login.html', {'ty': fr})
def showsss(request):
    username = request.GET.get('username', '')  
    obj=Ec.objects.all()
    la=Laptop.objects.all()
    wa=Watch.objects.all()
    l=[]
    p=[]
    q=[]
    for x in obj:
        l.append(x)
    for y in la:
        p.append(y)
    for i in wa:
        q.append(i)
        #fr = LoginForm()  # Instantiate an empty form for a GET request
        # 
    return render(request, 'shop.html', {'val': l, 'lap': p, 'wat': q,'username': username})
def signup(request):
    a=request.GET['na']
    b=request.GET['pass']
    c=request.GET['em']
    fr=SignupForm()
    fr.Username=a
    fr.Password=b
    fr.Email=c
    fr.save()
    return render(request,'login.html')
