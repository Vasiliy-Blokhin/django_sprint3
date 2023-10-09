from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path(  # Страница "о проекте".
        'about/',
        views.about,
        name='about'
    ),
    path(  # Страница с правилами.
        'rules/',
        views.rules,
        name='rules'
    )
]
