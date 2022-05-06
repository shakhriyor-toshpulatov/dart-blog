from django import template
from news.models import Category

register = template.Library()


@register.inclusion_tag('blog/menu_tp1.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}
