from django.shortcuts import render 
from wiki.models import Category, Page

def init(request):
    #Python
    pythonCategory = popCategory('Python')
    popPage(pythonCategory, '官方 Python 教材', 'http://docs.python.org/2/tutorial/')
    popPage(category=pythonCategory,
            title='如何像電腦科學家一樣思考',
            url='http://www.greenteapress.com/thinkpython/')
    popPage(category=pythonCategory,
            title='10 分鐘內學好 Python',
            url='http://www.korokithakis.net/tutorials/python/')
     # Other languages
    languageCategory = popCategory('Other languages')
    popPage(category=languageCategory,
            title='C language',
            url='http://www.tutorialspoint.com/cprogramming/c_overview.htm')
    popPage(category=languageCategory,
            title='Java',
            url='https://www.java.com/zh_TW/')
     # Django
    djangoCategory = popCategory('Django')
    popPage(category=djangoCategory,
            title='官方 Django 教材',
            url='https://docs.djangoproject.com/en/1.5/intro/tutorial01/')
    popPage(category=djangoCategory,
            title='Django 真讚',
            url='http://www.djangorocks.com/')
    popPage(category=djangoCategory,
            title='如何和 Django 跳探戈',
            url='http://www.tangowithdjango.com/')
     # Other frameworks
    frameCategory = popCategory('其他框架')
    popPage(category=frameCategory,
            title='Bottle 框架',
            url='http://bottlepy.org/docs/dev/')
    popPage(category=frameCategory,
            title='Flask 框架',
            url='http://flask.pocoo.org')
    context = {}
    return render(request, 'init/init.html', context)


def popCategory(name):
    category=Category.objects.get_or_create(name=name)[0]
    return category


def popPage(category, title, url, views=0):
    Page.objects.get_or_create(category=category, title=title,url=url,views=views)[0]