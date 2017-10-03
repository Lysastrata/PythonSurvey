from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'dojo_survey/index.html')
def process(request):
    result = {
        'name': request.POST['name'],
        'location': request.POST['city'],
        'language': request.POST['language'],
        'comments': request.POST['comments']
        }
    try:
        request.session['count'] += 1
    except:
        request.session['count'] = 0
    # request.session.modified = True
    return render(request, 'dojo_survey/result.html', result)
