
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.

def home(request):
    return render(request,'index.html')


def first(request):
    return render(request,'third.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        password=request.POST['pass']
        cnfpassword = request.POST['cnfpass']

        if password==cnfpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'already used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'already used this mail')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                print('registration completed')
                return HttpResponse('''<script>alert("registration compleated");window.location='/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("password not matching");window.location='/cred/register/'</script>''')
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return HttpResponse('''<script>alert("login compleated");window.location='/first/'</script>''')
        else:
            messages.info(request,'invalid user')
            return redirect('login')

    return render(request,'login.html')


def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['Department']
        course = request.POST['course']
        purpose = request.POST['purpose']
        materials = request.POST['materials']

        return HttpResponse(f'<center><p>Order Confirmed </p><p><a href="/">Return to Home Page</a></p></center>')


    return render(request,'result.html')




def logout(request):
    auth.logout(request)
    return redirect('/')