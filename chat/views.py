from django.shortcuts import render, redirect

# Create your views here.
def homeViews(request):
    if request.method == 'POST':
        second_url = request.POST.get('second_url')
        print('seconde... ',second_url)
        if second_url:
            # Redirect to the second view with the provided endpoint
            return redirect('index', groupName=second_url)
    return render(request, 'chat/home.html')

def indexViews(request, groupName):
    return render(request, 'chat/index.html', {'groupName' : groupName})