from django.shortcuts import render

def home(request):
    context={'title':'home'}
    return render(request, 'blog/index.html',context)

# Create your views here.
