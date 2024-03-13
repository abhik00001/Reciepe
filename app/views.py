from django.shortcuts import render,redirect
from app.models import Reciepe
from django.core.mail import EmailMessage
from django.contrib import messages

from django.contrib.auth.models import User

# Create your views here.
def home(request):
    data = Reciepe.objects.all()
    context={
        "show":data
    }
    return render(request, "home.html", context)

def savedata(request):
    if request.method == "POST":
        name = request.POST["rname"]
        description = request.POST["description"]
        imgx = request.FILES.get("imgx")

        val = Reciepe(Name = name , Description = description , Image = imgx)
        val.save()

        mymessage = f"""

        Reciepe Name = {name}
        Reciepe Description ={description}
                
        """
        mail = EmailMessage("NEW Reciepe added", mymessage , "sahilk786786123@gmail.com" , ["sahilk786786123@gmail.com"])
        mail.send()

        messages.success(request,"Reciepe Added Successfully!")

        return redirect("home")
    
def deletethis(request , id):
    data = Reciepe.objects.filter(id = id)
    data.delete()
    return redirect("home")

def updatethis(request , id):
    data = Reciepe.objects.get(id = id)
    context = {
        "data":data
    }
    return render(request,"update.html" , context)

def updatedata(request , up_id):
    if request.method == "POST":
        data = Reciepe.objects.get(id = up_id)

        name = request.POST["rname"]
        description = request.POST["description"]
        imgx = request.FILES.get("update_img")
        if imgx:
            data.Image=imgx 
            
        data.Name = name
        data.Description = description
        messages.success(request,"Reciepe Updated Successfully!")

        data.save()
        return redirect("home")
    
def search(request):
    query = request.GET['query']
    get = Reciepe.objects.filter(Name__icontains=query)  or  Reciepe.objects.filter(Description__icontains=query)
    
    context = {"show":get}

    return render( request ,"home.html",context)

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def add_data(request):
    if request.method == "POST":
        full_name = request.POST["fullname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]

        # Checking the fields are empty

        if password != cpassword:
            messages.warning(request , "Password doesn't Match")
            return redirect('signup')

        else:
          val = User.objects.create_user(username=username , first_name = full_name , email=email , password=password) 
          val.save()       
          messages.success(request,'Account Created Successfully')
          return redirect("login")