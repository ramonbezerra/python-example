from django.shortcuts import render

def meu_template(request):
    return render(request, 'template1.html', {})