from django.shortcuts import render

# Create your views here.
def home(request, groupName):
    return render(request, 'chat/index.html', {'groupName' : groupName})