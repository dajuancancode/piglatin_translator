from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def translate(request):

    toTranslate = request.GET['translation']
    translationArray = toTranslate.split(" ")
    consonantList = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    for i in range(len(translationArray)):
        if translationArray[i][0].lower() in ["a","e","i","o","u"]:
            translationArray[i]= translationArray[i]+"yay".lower()
        elif translationArray[i][0].lower() and translationArray[i][1].lower() in consonantList:
            translationArray[i] = translationArray[i][2:] + translationArray[i][0:2] + "ay".lower()
        else:
            translationArray[i]= translationArray[i][1:] + translationArray[i][0]+"ay".lower()
    translation = " ".join(translationArray).capitalize()

    return render(request, 'translate.html', {'original':toTranslate.capitalize(), 'translation':translation})
def about(request):
    return render(request, 'about.html')