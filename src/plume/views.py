from django.shortcuts import render

# Create your views here.
def plume(request):
    return render(request, 'plume/plume.html', {})