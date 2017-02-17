from django.http import HttpResponse
from django.template import Context, loader 
from django.middleware.csrf import get_token

from models import Post, Category

def index(request):
    all_posts = Post.objects.all()
    template = loader.get_template('index.html')
    context = Context({
        'all_posts': all_posts,
        'title' : 'All Posts'
    })
    
    return HttpResponse(template.render(context))

def add_post(request):
    all_categories = Category.objects.all()
    template = loader.get_template('add-post.html')
    csrf_token = get_token(request)
    
    context = Context({
        'all_categories' : all_categories,
        'csrf_token' : csrf_token,
        'title' : 'Add Posts'
    })
    
    return HttpResponse(template.render(context))