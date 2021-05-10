from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import PostArticle, PostComment
from .forms import CommentForm, PostSearch, share_post_email
from django.contrib.postgres.search import SearchRank, SearchVector, SearchQuery
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.urls import reverse


def index(requests):
    return render(requests, 'article/index.html')


#def LikeView(request):
#    post = get_object_or_404(PostArticle, id=request.POST.get('post_id'))
#    post.likes.add(request.user)
#    return HttpResponseRedirect(reverse('article:post_datail', args=[str(pk)]))


#def LikeView(request, pk):
#    post = get_object_or_404(PostArticle, id=request.POST.get('PostArticle_id'))
#    if post.likes.filter(id=request.user.id).exists():
#        post.likes.remove(request.user)
#    else:
#        post.likes.add(request.user)
#
#    return HttpResponseRedirect(reverse('article:post_detail', args=[str(pk)]))


#class BlogPostDetailView(DetailView):
#    model = PostArticle
    # template_name = MainApp/BlogPost_detail.html
    # context_object_name = 'object'

#    def get_context_data(self, **kwargs):
#        data = super().get_context_data(**kwargs)

#        likes_connected = get_object_or_404(PostArticle, id=self.kwargs['pk'])
#        liked = False
#        if likes_connected.likes.filter(id=self.request.user.id).exists():
#            liked = True
#        data['number_of_likes'] = likes_connected.number_of_likes()
#        data['post_is_liked'] = liked
#        return data


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


def register(requests):
    return render(requests, 'article/registration.html')
