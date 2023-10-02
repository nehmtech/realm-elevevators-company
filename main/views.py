
from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage






def blogs(request):
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    try:
        last_post = Post.objects.latest("date")
    except:
        last_post = []

    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post,
        "title": "Realm Elevators Company"
    }
    return render(request, "forums.html", context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user)
    
    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        commenr_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=commenr_id)
        new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
        comment_obj.replies.add(new_reply.id)


    context = {
        "post":post,
        "title": "Realm Elevators: "+post.title,
    }
    update_views(request, post)

    return render(request, "detail.html", context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 

    context = {
        "posts":posts,
        "forum": category,
        "title": "Realm Elevators: Posts"
    }

    return render(request, "posts.html", context)


@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("blogs")
    context.update({
        "form": form,
        "title": "Realm Elevators: Create New Post"
    })
    return render(request, "create_post.html", context)

def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts":posts,
        "title": "Realm Elevators: Latest 10 Posts"
    }

    return render(request, "latest-posts.html", context)

def search_result(request):

    return render(request, "search.html")




 #================= Main views functions here ============#

def main(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def services(request):
  return render(request, 'services.html')

def projects(request):
  return render(request, 'projects.html')

def contact(request):
  return render(request, 'contactpage.html')

def quote(request):
  return render(request, 'quote.html')

def app_development(request):
  return render(request, 'App Development.html')

def broadcasting(request):
  return render(request, 'Broadcasting.html')

def cyber_security(request):
  return render(request, 'Cyber Security.html')

def data_analysis(request):
  return render(request, 'Data Analysis.html')

def database_development(request):
  return render(request, 'Database Development.html')

def digital_marketing(request):
  return render(request, 'Digital Marketing.html')

def graphic_design(request):
  return render(request, 'Graphic Design.html')

def terms_and_conditions(request):
  return render(request, 'Terms and Conditions.html')

def privacy_policy(request):
  return render(request, 'Privacy Policy.html')

def digital_marketing(request):
  return render(request, 'Digital Marketing.html')

def it_consultancy(request):
  return render(request, 'IT Consultancy.html')

def it_hardware_configuration(request):
  return render(request, 'IT Hardware Configuration.html')

def networking(request):
  return render(request, 'Networking.html')

def online_writing(request):
  return render(request, 'Online Writing.html')

def photography(request):
  return render(request, 'Photography.html')

def software_development(request):
  return render(request, 'Software Development.html')

def videography(request):
  return render(request, 'Videography.html')

def web_development(request):
  return render(request, 'Web Development.html')







