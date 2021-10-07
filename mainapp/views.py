from django.shortcuts import render


def products(request):
    title = 'Каталог'
    links_menu = [
        {'href': 'products', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    same_products = [
        {'name': 'Стул', 'dec': 'Крутой стул', 'img': 'https://i.ibb.co/CHKsHZv/product-11.jpg', 'hover': 'https://i.ibb.co/5hqsJYg/icon-hover.png'},
        {'name': 'Стул', 'dec': 'Крутой стул', 'img': 'https://i.ibb.co/pXjS7R4/product-21.jpg', 'hover': 'https://i.ibb.co/5hqsJYg/icon-hover.png'},
        {'name': 'Стул', 'dec': 'Крутой стул', 'img': 'https://i.ibb.co/qYz4fVr/product-31.jpg', 'hover': 'https://i.ibb.co/5hqsJYg/icon-hover.png'},
    ]

    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
    }

    return render(request, 'mainapp/products.html', context=context)
