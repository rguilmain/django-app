from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        text = request.POST.get('text_field', '')
        # You can process the text here
        return render(request, 'index.html', {'submitted_text': text})
    return render(request, 'index.html')