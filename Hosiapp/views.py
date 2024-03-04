from django.shortcuts import render,redirect
from Hosiapp.models import Member
from Hosiapp.models import Message,ImageModel
from Hosiapp.forms import ImageUploadForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        messages = Message(name = request.POST['name'],
                         email=request.POST['email'],
                         subject= request.POST['subject'],
                         message= request.POST['message'])
        messages.save()
        return redirect('/')
    else:
        return render(request, 'index.html')



def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
         members = Member(username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'])
         members.save()
         return redirect('/login')

    else:
        return render(request,'register.html')


def login(request):
    return render(request, 'log in.html')



def detail(request):
    details = Message.objects.all()
    return render(request,'details.html',{'details':details})


def info(request):
    information = Message.objects.all()
    return render(request,'details2.html',{'information':information})

def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            members = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request,'adminhome.html',{'members':members})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimages.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')