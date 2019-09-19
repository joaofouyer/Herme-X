from django.shortcuts import render


def index(request):
    try:
        return render(request, 'index.html')

    except Exception as e:
        print("Exceção no método index: ", e)
        return True
