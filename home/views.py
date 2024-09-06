from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    # return HttpResponse("This is our home page and will be")
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        content = request.POST.get('content', '')
        if len(name)<3 or len(email)<6 or len(phone)<10 or len(content)<10:
            messages.error(request, "Please enter  data poperly")

        else:
            messages.success(request,"Your reponse has been recorded successfully")
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
    
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)>50:
        allposts = Post.objects.none()
    else:
        allposts = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(author__icontains=query) | 
            Q(content__icontains=query)
        )
    if allposts.count()==0:
        messages.warning(request, "No search results found. Please refine your query")
    output = {'allposts': allposts, 'query': query}
    return render(request, 'home/search.html', output)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        inputfname = request.POST.get('inputfname', '')
        inputlname = request.POST.get('inputlname', '')
        inputemail = request.POST.get('inputemail', '')
        inputPass1 = request.POST.get('inputPass1', '')
        inputPass2 = request.POST.get('inputPass2', '')

        if(inputPass1 != inputPass2):
            messages.error(request,"Password mismatch. Please check the password and try again")
            return redirect('home')
        
        myuser = User.objects.create_user(username, inputemail, inputPass1)
        myuser.first_name = inputfname
        myuser.last_name = inputlname
        myuser.save()
        messages.success(request,"Your account has been created successfully")
        return redirect('home')
    else:
        return HttpResponse("Error - please try again")
    

def bloglogin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername','')
        loginpassword= request.POST.get('loginpassword','')

        user = authenticate(username=loginusername, password=loginpassword)
        if user is None:
            messages.error(request,"Invalid credentials, Please try again")
            return redirect('home')
        else:
            login(request, user)
            messages.success(request,"Successfully logged in")
            return redirect('home')

    return HttpResponse("404 - Not found")

def bloglogout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('home')