from django.shortcuts import render
from models import News

# Create your views here.
def index(request):
    top_three_news = list(News.objects.order_by('create_date').reverse()[0:3])
    context = {'top_three_news': top_three_news}
    return render(request, 'news_main_block.html', context)

def detail(request, news_id):
    news = News.objects.get(id=news_id)
    print news
    context = {'news': news}
    return render(request, 'news_details.html', context)
