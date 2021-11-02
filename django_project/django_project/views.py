from django.shortcuts import render
from mainapp.models import Product, Contacts


def main(request):

    title = 'Магазин'

    product = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': product,
    }
    return render(request, 'django_project/index.html', context)


def contacts(request):
    title = 'Контакты'

    info_contact = Contacts.objects.all()

    context = {
        'title': title,
        'info_contact': info_contact,
    }
    return render(request, 'django_project/contact.html', context)



