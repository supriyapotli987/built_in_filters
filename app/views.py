from django.shortcuts import render

# Create your views here.
def built_in_filters(request):
    data='Hai hEllO hOW aRE you'
    d={'data':data}
    return render(request,'built_in_filters.html',d)



def customfilters(request):
    data={'hai HEllo PythoN How ARE you'}
    d={'data':data}
    return render(request,'customfilters.html',d)