from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Images,ContactMessage,buyproduct
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.

@login_required(login_url='/')

def home(request):
    image = Images.objects.all()
    return render(request,'home.html',{'image': image})

@login_required(login_url='/')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        contact_message = ContactMessage(name=name, mobile=mobile, message=message)
        contact_message.save()
        messages.success(request, 'Your Response has been saved successfuly')
        return redirect('contact')
        
    return render(request,'contact.html')


@csrf_exempt
def save_product_details(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.POST.get('image')  # Use FILES instead of POST for file upload
        # You can access other fields similarly
        
        # Save product details to your table
        product = buyproduct(title=title, desc=desc, image=image,price=price)
        product.save()
        
        return JsonResponse({'message': 'Product details saved successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)


# def show_category(request , cid):
#     cats = Category.objects.all()
#     category = Category.objects.get(pk=cid)
#     image = Images.objects.filter(cat=category)
#     return render(request,'home.html',{'image':image,'cats':cats})




def userlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            messages.error(request,'User not Signup')
            return redirect('/') 
    return render(request,'login.html')
    
    
def handlelogout(request):
    logout(request)
    return redirect('/')



def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            request.session['username'] = username
            return redirect('reset_password')
        else:
            messages.error(request, 'Invalid username!')
            return redirect('forgot_password')
    return render(request, 'forgot_password.html')

def reset_password(request):
    if request.method == 'POST':
        username = request.session.get('username')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        if new_password1 == new_password2:
            user = User.objects.filter(username=username).first()
            if user:
                user.set_password(new_password1)
                user.save()
                return redirect('login')
            else:
                messages.error(request, 'Invalid username!')
                return redirect('forgot_password')
        else:
            return redirect('reset_password')
    return render(request, 'reset_password.html')  # Redirect to login page if someone tries to access reset_password page directly

    
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'You are now registered and can log in.')
                return redirect('/')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'register.html')
        
    
    
   


 

    