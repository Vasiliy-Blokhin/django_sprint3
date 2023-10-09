from django.shortcuts import render


# Страница с описанием.
def about(request):
    return render(request, 'pages/about.html')


# Страница с правилами.
def rules(request):
    return render(request, 'pages/rules.html')
