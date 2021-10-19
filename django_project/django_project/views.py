from django.shortcuts import render


def main(request):

    title = 'Магазин'

    context = {
        'title': title,
    }
    return render(request, 'django_project/index.html', context)


def contacts(request):
    title = 'Контакты'

    info_contact=[
        {'name': 'Москва', 'mobil': 'eertrtert', 'email': 'sdfsdf', 'adress': 'dasdasd'},
        {'name': 'Москва', 'mobil': 'ertert', 'email': 'sdfrsdf', 'adress': 'daserdasd'},
        {'name': 'Москва', 'mobil': 'errrtert', 'email': 'sdrfsdf', 'adress': 'dasdterasd'},
    ]

    context = {
        'title': title,
        'info_contact': info_contact,
    }
    return render(request, 'django_project/contact.html', context)
