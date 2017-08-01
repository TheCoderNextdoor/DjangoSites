from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')
    
def contact(request):
    return render(request, 'personal/basic.html', {'content':['Email me at a.banerjee6762@gmail.com']})

