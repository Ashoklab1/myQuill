# myQuill/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Post, Category, Tag, Comment
# Import PostImageFormSet from forms.py
from .forms import PostForm, CommentForm, PostImageFormSet
from datetime import datetime
from django.contrib.auth.decorators import login_required

def post_list(request):
    query = request.GET.get("q")
    author = request.GET.get("author")
    category = request.GET.get("category")
    tag = request.GET.get("tag")
    sort = request.GET.get("sort", "date")
    tags_selected = request.GET.getlist("tags")
    month = request.GET.get("month")
    year = request.GET.get("year")
    start_date = request.GET.get("start")
    end_date = request.GET.get("end")

    posts = Post.objects.all()

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(body__icontains=query))
    if author:
        posts = posts.filter(author__username=author)
    if category:
        posts = posts.filter(category__name=category)
    if tag:
        posts = posts.filter(tags__name=tag)
    if tags_selected:
        posts = posts.filter(tags__name__in=tags_selected).distinct()
    if month and year:
        posts = posts.filter(date__month=month, date__year=year)
    if start_date and end_date:
        posts = posts.filter(date__range=[start_date, end_date])

    if sort == "title":
        posts = posts.order_by("title")
    else:
        posts = posts.order_by("-date")

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    months = [
        ("01", "Jan"), ("02", "Feb"), ("03", "Mar"), ("04", "Apr"),
        ("05", "May"), ("06", "Jun"), ("07", "Jul"), ("08", "Aug"),
        ("09", "Sep"), ("10", "Oct"), ("11", "Nov"), ("12", "Dec"),
    ]

    context = {
        "page_obj": page_obj,
        "query": query,
        "sort": sort,
        "category": category,
        "month": month,
        "year": year,
        "months": months,
        "start_date": start_date,
        "end_date": end_date,
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "popular_tags": Tag.objects.annotate(post_count=Count('post')).order_by('-post_count')[:10],
        "popular_categories": Category.objects.annotate(post_count=Count('post')).order_by('-post_count')[:10],
        "selected_tags": tags_selected,
    }

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        html = render_to_string("posts/_posts_partial.html", context, request=request)
        next_page = page_obj.next_page_number() if page_obj.has_next() else None
        return JsonResponse({"html": html, "next_page": next_page})

    return render(request, "posts/posts_list.html", context)

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # Instantiate formset with POST data and FILES, and link to the post instance
        formset = PostImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Save the tags

            # Save the formset instances and link them to the newly created post
            # commit=False allows you to set the foreign key before saving
            instances = formset.save(commit=False)
            for instance in instances:
                instance.post = post # Link each image to the post
                instance.save()
            formset.save() # Save the formset to handle deletions/updates if any

            return redirect('myQuill:post_list')
        else:
            # If forms are not valid, re-render with errors
            return render(request, 'posts/post_new.html', {'form': form, 'formset': formset})
    else:
        form = PostForm()
        formset = PostImageFormSet() # Pass an empty formset for GET request
    return render(request, 'posts/post_new.html', {'form': form, 'formset': formset})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved_comment=True).order_by('date')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('users:login')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(post.get_absolute_url())
        else:
            return render(request, 'posts/post_page.html', {
                'post': post,
                'comments': comments,
                'comment_form': comment_form
            })
    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_page.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })
