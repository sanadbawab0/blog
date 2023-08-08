from django.shortcuts import render

posts = [
    {
        'title' : 'التدوينة الأولى',
        'content' : 'نص التدوينة الأولى كنص تجريبي',
        'post_date' : '15-3-2019',
        'author' : 'Sanad Bawab'
    },
    {
        'title' : 'التدوينة الثانية',
        'content' : 'نص التدوينة الثانية كنص تجريبي',
        'post_date' : '20-3-2020',
        'author' : 'Yanal Esaied'
    },
    {
        'title' : 'التدوينة الثالثة',
        'content' : 'نص التدوينة الثالثة كنص تجريبي',
        'post_date' : '28-6-2022',
        'author' : 'Wajd Bawab'
    },
    {
        'title' : 'التدوينة الرابعة',
        'content' : 'نص التدوينة الرابعة كنص تجريبي',
        'post_date' : '12-9-2021',
        'author' : 'Own Esaied'
    },
]

def home(request):
    context={'title':'الصفحة الرئيسية',
             "posts": posts}
    return render(request, 'blog/index.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'من انا'})
