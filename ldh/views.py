from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from .models import Title, Chunk, Alert, Panel, Thumbnail

def index(request):
    """

    :param request:
    :return: render_to_response
    """
    sorl_thumbnail = extra_fields = False
    if 'inplaceeditform_extra_fields' in settings.INSTALLED_APPS:
        extra_fields = True
    if 'sorl.thumbnail' in settings.INSTALLED_APPS:
        sorl_thumbnail = True
        
    #define variable for database field
    heading_title_1 = get_object_or_404(Title, key="heading_title_1")
    heading_title_2 = get_object_or_404(Title, key="heading_title_2")
    about_me_title = get_object_or_404(Title, key ="about_me_title")
    about_me_content = get_object_or_404(Chunk, key ="about_me_content")
    specials = get_object_or_404(Chunk, key ="specials")
    contact_title = get_object_or_404(Title, key ="contact_title")
    contact_content = get_object_or_404(Chunk, key ="contact_content")
    education_title = get_object_or_404(Title, key ="education_title")
    education_content = get_object_or_404(Chunk, key ="education_content")
    services_title = get_object_or_404(Title, key ="services_title")
    services_content = get_object_or_404(Chunk, key ="services_content")





    #return variable in idex.html
    return render_to_response("index.html",
                              {'heading_title_1': heading_title_1,
                               'heading_title_2' : heading_title_2,
                               'about_me_title' : about_me_title,
                               'about_me_content' : about_me_content,
                               'specials' : specials,
                               'contact_title' : contact_title,
                               'contact_content' : contact_content,
                               'extra_fields' : extra_fields,
                               'education_title' : education_title,
                               'education_content' : education_content,
                               'services_title' : services_title,
                               'services_content' : services_content
                                },
                              context_instance=RequestContext(request))



def example(request):
    """

    :param request:
    :return: render_to_response
    """
    sorl_thumbnail = extra_fields = False
    if 'inplaceeditform_extra_fields' in settings.INSTALLED_APPS:
        extra_fields = True
    if 'sorl.thumbnail' in settings.INSTALLED_APPS:
        sorl_thumbnail = True
    alerts = Alert.objects.all()
    panels = Panel.objects.all()
    thumbnails = Thumbnail.objects.all()

    title = get_object_or_404(Title, key="title")
    alert_title = get_object_or_404(Title, key="alert_title")
    panel_title = get_object_or_404(Title, key="panel_title")
    well_title = get_object_or_404(Title, key="well_title")
    thumbnail_title = get_object_or_404(Title, key="thumbnails_title")
    chunk_content = get_object_or_404(Chunk, key="content")
    chunk_well_content = get_object_or_404(Chunk, key="well_content")
    return render_to_response('example.html',
                              {'alerts': alerts,
                               'panels': panels,
                               'thumbnails': thumbnails,
                               'title': title,
                               'chunk_content': chunk_content,
                               'alert_title': alert_title,
                               'panel_title': panel_title,
                               'well_title': well_title,
                               'thumbnail_title': thumbnail_title,
                               'chunk_well_content': chunk_well_content,
                               'extra_fields': extra_fields,
                               'sorl_thumbnail': sorl_thumbnail},
                              context_instance=RequestContext(request))


def index2(request):
    """

    :param request:
    :return: render_to_response
    """
    sorl_thumbnail = extra_fields = False
    if 'inplaceeditform_extra_fields' in settings.INSTALLED_APPS:
        extra_fields = True
    if 'sorl.thumbnail' in settings.INSTALLED_APPS:
        sorl_thumbnail = True
    alerts = Alert.objects.all()
    panels = Panel.objects.all()
    thumbnails = Thumbnail.objects.all()
    title = get_object_or_404(Title, key="title")

    alert_title = get_object_or_404(Title, key="alert_title")
    panel_title = get_object_or_404(Title, key="panel_title")
    well_title = get_object_or_404(Title, key="well_title")
    thumbnail_title = get_object_or_404(Title, key="thumbnails_title")
    chunk_content = get_object_or_404(Chunk, key="content")
    chunk_well_content = get_object_or_404(Chunk, key="well_content")
    return render_to_response('example.html',
                              {'alerts': alerts,
                               'panels': panels,
                               'thumbnails': thumbnails,
                               'title': title,
                               'chunk_content': chunk_content,
                               'alert_title': alert_title,
                               'panel_title': panel_title,
                               'well_title': well_title,
                               'thumbnail_title': thumbnail_title,
                               'chunk_well_content': chunk_well_content,
                               'extra_fields': extra_fields,
                               'sorl_thumbnail': sorl_thumbnail},
                              context_instance=RequestContext(request))

