from json import dumps

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic import TemplateView

from App.models import Student


# @method_decorator(decorator=csrf_exempt, name='dispatch')
class StudentsView(View):
    @method_decorator(decorator=csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(StudentsView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        name = request.GET.get('username')
        return render(request, 'StudentTemplate.html')

    def post(self, request):
        s_name = request.POST.get('username')
        s_class = request.POST.get('password')

        # student = Student()
        # student.s_name = s_name
        # student.s_class = s_class
        # student.save()

        data = {
            'u_name': s_name,
            'u_password': s_class,
        }
        data = dumps(data)
        return HttpResponse(data)


@csrf_exempt
def hello_django(request):
    u_name = request.POST.get('username')
    u_password = request.POST.get('password')
    data = {
        'u_name': u_name,
        'u_password': u_password,
    }
    data = dumps(data)
    return HttpResponse(data)


class StudentTemplateView(TemplateView):
    pass
