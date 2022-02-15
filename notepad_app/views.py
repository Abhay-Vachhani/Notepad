from django.shortcuts import redirect, render, HttpResponse
from notepad.settings import URL_LENGTH
from notepad_app.models import Note
import string
import random

# Create your views here.
def home(request):
    while True:
        randomStr = ''.join(random.choices(string.ascii_uppercase + string.digits, k = URL_LENGTH)).lower()
        note = Note.objects.filter(url=randomStr)
        if note.__len__() == 0:
            obj = Note()
            obj.url = randomStr
            obj.save()
            break
    return redirect(f'/{randomStr}')

def homeWithNote(request, noteId):
    if request.method=='POST':
        obj = Note.objects.filter(url=noteId)
        if obj.__len__() > 0:
            obj = obj[0]
            obj.note=request.POST.get('note')
            obj.save()
        else:
            obj = Note()
            obj.url = noteId
            obj.note=request.POST.get('note')
            obj.save()

    obj = Note.objects.filter(url=noteId)
    if obj.__len__() > 0:
        obj = obj[0]
        return render(request, 'home.html', {'note': obj.note})

    return render(request, 'home.html')
