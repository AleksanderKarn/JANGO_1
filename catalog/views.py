from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home_page.html')


def contacts(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('message'))
    return render(request, 'catalog/contacts_page.html')
# Create your views here.
