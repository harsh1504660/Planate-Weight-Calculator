from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'wplanate/index.html')

def result(request):
    w_earth=request.POST.get('text','default')
    test=w_earth.isdigit()
    if test==True:
        w_earth=int(w_earth)
        m_earth = w_earth / 9.81
        if 'moon' in request.POST:
            w_moon=" %1.2f" % (w_earth/6)
            w_moon=str(w_moon)
            params={'purpose':'Your weight on moon is : ','result':w_moon + ' kg'}
            return render(request,'wplanate/moon.html',params)
        elif 'jupiter' in request.POST:
            w_jupiter =" %1.2f" % (m_earth * 24.79)
            w_jupiter = str(w_jupiter)
            params={'purpose':'Your weight on jupiter is : ','result':w_jupiter + ' kg' }
            return render(request,'wplanate/jupiter.html',params)
        elif 'mars' in request.POST:
            w_mars = " %1.2f" % ((m_earth) * 3.711)
            w_mars=str(w_mars)
            params = {'purpose':'Your weight on mars is : ','result': w_mars + ' kg'}
            return render(request,'wplanate/mars.html',params)
        elif 'mercury' in request.POST:
            w_mercury = "%1.2f" % (m_earth * 0.38)
            w_mercury = str(w_mercury)
            params= {'purpose':'Your weight on mercury is : ','result': w_mercury + ' kg'}
            return render(request,'wplanate/mercury.html',params)
        elif 'neptune' in request.POST:
            w_neptune = "%1.2f" % (m_earth * 1.19)
            w_neptune = str(w_neptune)
            params = {'purpose':'Your weight on neptune is : ','result': w_neptune + ' kg'}
            return render(request,'wplanate/neptune.html',params)
        elif 'pluto' in request.POST:
            w_pluto = "%1.2f" % (m_earth * 0.06)
            w_pluto = str(w_pluto)
            params= {'purpose':'Your weight on pluto is : ','result': w_pluto + ' kg'}
            return render(request,'wplanate/pluto.html',params)
        elif 'saturn' in request.POST:
            w_saturn="%1.2f" % (m_earth * 1.06)
            w_saturn=str(w_saturn)
            params= {'purpose':'Your weight on saturn is : ','result': w_saturn + ' kg'}
            return render(request,'wplanate/saturn.html',params)
        elif 'uranus' in request.POST:
            w_uranus = "%1.2f" % (m_earth * 0.92)
            w_uranus = str(w_uranus)
            params= {'purpose':'Your weight on uranus is : ','result': w_uranus + ' kg'}
            return render(request,'wplanate/uranus.html',params)
        elif 'venus' in request.POST:
            w_venus = "%1.2f" % (m_earth * 0.91)
            w_venus = str(w_venus)
            params={'purpose':'Your weight on venus is : ','result': w_venus + ' kg'}
            return render(request,'wplanate/venus.html',params)
    else:
        return render(request,'wplanate/error.html')


def about(request):
    return render(request,'wplanate/about.html')

def contact(request):
    return render(request,'wplanate/contact.html')