from django.shortcuts import redirect, render
from django.urls import reverse_lazy

def index(request):
    return redirect(reverse_lazy('post:index'))


def message(request, message_type):
    message = request.GET.get('message')
    template_name = "index.html"
    context = {
        'message': message,
        'message_type': message_type
    }
    return render(request, template_name, context)
