from django import template
from news.models import News, Tag

register = template.Library()


@register.inclusion_tag('blog/popular_posts.html')
def get_popular(cnt=3):
    posts = News.objects.order_by('-views')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('blog/tags.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
