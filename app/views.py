from django.shortcuts import render,redirect
from app.models import Reciepe
from django.core.mail import EmailMessage
from django.contrib import messages

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