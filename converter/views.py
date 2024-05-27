from django.shortcuts import render
from .ml_model import text_to_html

def home(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        html_text = text_to_html(input_text)
        return render(request, 'home.html', {'html_text': html_text, 'input_text': input_text})
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')
