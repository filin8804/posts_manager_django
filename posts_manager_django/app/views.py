from django.http import HttpResponse
from django.template import Context, loader 

from models import Post, Category

def index(request):
    all_posts = Post.objects.all()
    template = loader.get_template('index.html')
    context = Context({
        'all_posts': all_posts,
        'title' : "All Posts"
    })
    
    return HttpResponse(template.render(context))

def add_post(request):
    all_categories = Category.objects.all()
    template = loader.get_template('add-post.html')
    context = Context({
        'all_categories' : all_categories,
        'title' : "Add Posts"
    })
    
    return HttpResponse(template.render(context))