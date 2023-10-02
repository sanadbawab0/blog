from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(
                request, "تهانينا {} لقد تمت عملية التسجيل بنجاح".format(new_user))
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {
        'title': 'التسجيل',
        "form": form,
    })


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.warning(
                request, 'هناك خطأ في اسم المستخدم او كلمة المرور')

    return render(request, 'user/login.html', {
        'title': 'تسجيل الدخول',
    })


def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': "تسجيل الخروج",
    })


@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'user/profile.html', {
        'title': "الملف الشخصي",
        'posts': posts,
        'page': page,
        'post_list': post_list,
    })


@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        Profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and Profile_form.is_valid:
            user_form.save()
            Profile_form.save()
            messages.success(request, 'تم تحديث الملف الشخصي')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        Profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'تعديل الملف الشخصي',
        'user_form': user_form,
        'profile_form': Profile_form,
    }
    return render(request, 'user/profile_update.html', context)
