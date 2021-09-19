from django import template
from django.contrib.auth.models import Group 

register = template.Library() 

@register.filter(name='ver_group') 
def ver_group(user, group_name):
    group = Group.objects.get(name=group_name)
    if user.groups == group:
        return True
    else:
        return False