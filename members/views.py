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