from django.shortcuts import render
from .models import *


# shop functions

def demo(request, c_page=None):

    obj1 = sidebar_edit.objects.all()
    obj2 = Home_Image.objects.all()
    obj3 = About.objects.all()
    obj4 = Interests.objects.all()
    obj5 = Skills1.objects.all()
    obj5_1 = Skills2.objects.all()
    obj6 = Resume.objects.all()
    obj7 = MyProject_categories.objects.all()
    obj8 = MyProjects_Update.objects.all()
    Reverse_obj8 = reversed(obj8)
    obj9 = Services.objects.all()
    obj10 = MyTeam.objects.all()
    obj11 = Contact.objects.all()
    return render(request, "index.html",
                  {'sidebar_edit': obj1, 'First_page_edit': obj2, 'About_Update': obj3, 'Interests_update': obj4,
                   'Skills_Update': obj5, 'Skills2_Update': obj5_1, 'Resume_Projects': obj6, 'MyProject_categories': obj7,
                   'MyProjects_Update': Reverse_obj8, 'Services_Update': obj9, 'MyTeam': obj10, 'Contact': obj11})
