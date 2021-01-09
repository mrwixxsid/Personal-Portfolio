from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
# from .forms import CommentForm
from .models import Post, Portfolio
# Create your views here.


def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


def index(request):
    featured = Post.objects.filter(featured=True)[0:3]
    portfolio = Portfolio.objects.all()
    # categories = Category
    context = {
        'featured':  featured,
        'portfolio_list': portfolio,
        # 'categories': categories,
        'object_list':  featured,
    }
    return render(request, 'index.html', context)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })


def blog(request):
    category_count = get_category_count()
    latest = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(latest, 1)
    page_request_ver = 'page'
    page = request.GET.get(page_request_ver)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(1)
        # paginated_queryset = paginator.page(paginator.num_page)
    context = {
        'queryset': paginated_queryset,
        'page_request_ver': page_request_ver,
        'category_count': category_count
    }
    return render(request, 'blog.html', context)


def post(request, id):
    post = get_object_or_404(Post, id=id)
    category_count = get_category_count()
    # form = CommentFrom(request.POST or None)
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.instance.user = request.user
    #         form.instance.post = request.post
    #         form.save()
    context = {
        # 'form': form,
        'post': post,
        'category_count': category_count
    }
    return render(request, 'post.html', context)
