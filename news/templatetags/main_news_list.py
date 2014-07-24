__author__ = 'gauee'
from django import template
from ..models import News

register = template.Library()

# @register.simple_tag()
@register.inclusion_tag('news_main_block.html')
def get_main_news_list():
    top_three_news = list(News.objects.order_by('create_date').reverse()[0:3])
    return {'top_three_news': top_three_news}


@register.inclusion_tag('big_news.html')
def get_big_news():