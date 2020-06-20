from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, RedirectView


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


class IndexView(RedirectView):
    url = reverse_lazy("post:index")
    permanent = True
    query_string = True


class MessageView(View):
    def get(self, request, message_type):
        message = request.GET.get('message')
        template_name = "index.html"
        context = {
            'message': message,
            'message_type': message_type
        }
        return render(request, template_name, context)
