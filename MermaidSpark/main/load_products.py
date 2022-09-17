from main.generator import ProductLoader

if __name__ == 'django.core.management.commands.shell':
    productLoader = ProductLoader()
    print(productLoader.products[0])
    productLoader.upload_to_database()