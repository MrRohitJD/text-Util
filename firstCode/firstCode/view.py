from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("Hello")
    return render(request, 'index.html')

def Contact(request):
    return render(request , 'Contact_US.html')


def analyze(request):
    # get request
    djtext = request.POST.get('text', 'default')
    removePanch = request.POST.get('remove','off')
    upperC = request.POST.get('upperC','off')
    removeES = request.POST.get('removeES','off')
    removenextline =request.POST.get('removenextline','off')

    # removePanch
    if removePanch =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyezed = ""
        for char in djtext:
            if char not in punctuations:
                analyezed= analyezed+char
        param ={'purpose':'remove panctuation','analyzed_text':analyezed}
        # return render(request , 'analyze.html', param)
        djtext= analyezed

    # TO UPPER CASE
    if(upperC=="on"):
        analyezed = ""
        for char in djtext:
            analyezed=analyezed+char.upper()
        param = {'purpose': 'to upper case', 'analyzed_text': analyezed}
        # return render(request, 'analyze.html', param)
        djtext = analyezed

    if (removeES == "on"):
        analyezed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == "  "):
                analyezed = analyezed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyezed}
        # return render(request, 'analyze.html', params)
        djtext = analyezed

    if( removenextline=="on"):
        analyezed =""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyezed = analyezed+char
        params ={'purpose':'Remove Next Line','analyzed_text': analyezed}
        # return render(request, 'analyze.html',params)
        djtext = analyezed


    if(removenextline != "on" and removeES!="on" and upperC!="on" and removePanch !="on"):
        return HttpResponse("please select any operation and try again")

    return render(request ,'analyze.html', params)




