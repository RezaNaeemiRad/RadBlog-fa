# from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
# Create your views here.
def index(request):
    return HttpResponse("index")

# def post_list(request):
#     posts = Post.published.all()
#     paginator = Paginator(posts, 2)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     context = {
#         'posts': posts,
#     }
#     return render(request, "blog/post-list.html",context)

class PostListView(ListView):
    # model = Post
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 2
    # template_name = "blog/post_list.html"

# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
#     # try:
#     #     post = Post.published.get(id=id)
#     # except:
#     #     raise Http404("No post found!")
#     context = {
#         'post': post,
#     }
#     return render(request, 'blog/post_detail.html', context)

class PostDetailView(DetailView):
    model = Post