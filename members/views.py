from django.template import loader
from django.http import HttpResponse
from members.models import Member

# Create your views here.

def members(request):
    members = Member.objects.all().values()
    template =  loader.get_template('all_members.html')
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'members': member
    }
    return HttpResponse(template.render(context, request))
def badrequest(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())