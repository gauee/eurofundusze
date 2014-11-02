from django import template
from ..models import Video_YU

register = template.Library()

@register.inclusion_tag('youtube_movies_list.html')
def get_multimedia_videos():
    videos = Video_YU.objects.all()
    print videos

    titles = []
    iframes = []
    for idx, v in enumerate(videos):
        titles.append(v.video_title)
        iframes.append(v.getIframeUrl())

    print 'Titles',titles
    print  'Iframes',iframes

    elements = []
    idx = 0
    limit = len(videos)
    while (idx +1 < limit):
        element = []
        element.append(iframes[idx])
        element.append(iframes[idx+1])
        elements.append(element)
        element = []
        element.append(titles[idx])
        element.append(titles[idx+1])
        elements.append(element)
        idx=idx+2

    if(idx<limit):
        element = []
        element.append(iframes[idx])
        elements.append(element)
        element = []
        element.append(titles[idx])
        elements.append(element)

    print elements


    return {'videos':elements}
