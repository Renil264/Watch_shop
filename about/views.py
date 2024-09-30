from django.shortcuts import render, HttpResponseRedirect


# Create your views here.
def about(request):
    context = {
        'title': 'О нас',
    }
    return render(request, 'about/about.html', context)  # 1
