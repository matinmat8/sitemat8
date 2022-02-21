from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import PostArticle, PostComment
from .forms import CommentForm, PostSearch, share_post_email
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage


def index(requests):
    return render(requests, 'article/index.html')


def Post_Article_Show_search(requests):
    Post = PostArticle.published.all()
    form = PostSearch()
    context = {'Post': Post, 'form': form}
    return render(requests, "article/postarticle.html", context)


def search_in_post(requests, search=None):
    Post = PostArticle.published.all()
    results = []
    form = PostSearch(requests.GET or None)
    if 'search' in requests.GET:
        form = PostSearch(requests.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            results = Post.annotate(Search=SearchVector('title', 'PostBody'
                                                        ), ).filter(Search=SearchQuery(search))

    context = {'form': form, 'search': search, 'results': results}
    return render(requests, "article/search_post.html", context)


def Post_detail(requests, id=None):
    template_name = 'article/detail.html'
    post = get_object_or_404(PostArticle, id=id)
    comments = post.comments.filter(active=True)
    new_comment = None
    if requests.method == 'POST':
        form = CommentForm(data=requests.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()
    return render(requests, template_name, {'post': post,
                                            'comments': comments,
                                            'form': form,
                                            'new_comment': new_comment})


@login_required
def post_share(requests, id):
    post = get_object_or_404(PostArticle, id=id, status='published')
    sent = False
    form = share_post_email(requests.POST or None)
    if requests.method == 'POST':

        if form.is_valid():
            cd = form.cleaned_data
            post_url = requests.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} Recommends you reading" \
                      f"{post.title}"
            message = f"Read{post.title} at {post_url}\n\n" \
                      f"{cd['name']}\s comments: {cd['comments']}"
            send_mail(subject,
                      message,
                      'sitemat8@gmail.com',
                      [cd['to']])
            sent = True

    return render(requests, 'article/share.html', {'post': post, 'form': form, 'sent': sent})


def upload(requests):
    if requests.method == 'POST':
        uploaded_file = requests.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

    return render(requests, 'article/upload.html')
