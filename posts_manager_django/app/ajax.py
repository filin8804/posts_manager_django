import json

from django.http import JsonResponse
from models import Post, Category
from unicodedata import category

def post_add(request):
    message = ''
    if request.method == 'POST':
        json_post = json.loads(request.body)          
        json_post = json_post['post']
        post_category = Category.objects.get(id=json_post["categoryId"])
        post = Post(text = json_post["author"], author = json_post["author"], category = post_category)
        post.save()
        message = 'Post saved'
        return JsonResponse({'status':'OK', 'message' : message})
    else:
        message = 'Only POST request are supported'  

    return JsonResponse({'status':'FAILED', 'message' : message}, status=400)