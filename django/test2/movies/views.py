from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from django.core.paginator import Paginator   # 分页器
from movies import models
import hashlib
import movies
# Create your views here.

# def index(request):
#     return HttpResponse("hello django")

# def index(request):
#     # 1.获取模板
#     template = loader.get_template('movies/test.html')
#     # 2.定义上下文
#     context =  {'title': '图书列表', 'list': range(10)}
#     # 3.渲染模板
#     return HttpResponse(template.render(context))

from .models import moviesInfo,heroInfo



def index(request):
    # 查询数据库里面的所有数据
    movieslist = moviesInfo.objects.all()

    # 获取前端传过来的参数
    page_number = request.GET.get('page',1)
    # 实例化分页器  参数1 ： 需要分页的内容  参数2 ： 分页数量
    p = Paginator(movieslist,1)  # 根据页码获取具体页面的数据

    # page = p.page(int(page_number))
    # page_range = p.page_range   # 获取分页的范围

    #自定义页码
    cur_number = int(page_number)   # 获取当前的页码
    page = p.page(cur_number)   # 获取当前页码的数据
    page_range = list(range(max(cur_number - 2 ,1),cur_number)) + \
                 list(range(cur_number ,min(p.num_pages,cur_number + 2)+1))
    # 当首部间隔大于2时 ，页码添加'...'
    if page_range[0] -1 > 2 :
        page_range.insert(0,'...')
    # 当尾部间隔大于2时候 。尾部添加'...'
    if p.num_pages - page_range[-1] > 2:
        page_range.append('...')
    # 当前页码不是1的时候，添加1进去
    if page_range[0] != 1:
        page_range.insert(0,1)
        # 当最后一页不是做大页码的时候，把最大页码添加进去
    if page_range[-1] != p.num_pages:
        page_range.append(p.num_pages)




    print(movieslist)   # 判断是否成功获取到数据库里面的数据
    return render(request,'movies/index.html',{'movieslist':movieslist,
                                               "page":page,"page_range":page_range})

def detail(request,id):
     # 查询电影的信息
    molist = moviesInfo.objects.get(id=int(id))
     # 根据外键关联查询所有的详情信息
    heroslist = molist.heroinfo_set.all()
    return render(request,'movies/detail.html',{"molist":molist,"heroslist":heroslist})

def cookie_set(request):
    res = HttpResponse("设置cookie成功！！！")
    # res.set_cookie()  #旧版本设置方式
    res.set_signed_cookie('jidian','123456')
    return res

def cookie_get(request):
    res = HttpResponse("读取cookie:")
    if 'jidian' in request.COOKIES:
        res.write(request.COOKIES['jidian'])
    return res

def cookie_del(request):
    res = HttpResponse("已经删除cookie！！！")
    res.delete_cookie('jidian')
    return res

def session_set(request):
    request.session['username'] = 'python'
    return HttpResponse('设置session！！！')

def session_get(request):
    name = request.session.get('username')
    return HttpResponse(name)

def session_del(request):
    request.session.flush()
    return redirect('/')  # 重定向


def login(request):
    return render(request,'movies/login.html')

def check_login(request):
    username = request.POST.get('email')
    pwd = str(request.POST.get('password'))
    print((username,pwd))
    pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
    try:
        u = models.User.objects.get(email=username, password=pwd)
    except:
        u = ''
    print(u)

    if u != '':
        res = redirect('/')
        request.session['isLogin'] = username
        return res
    else:
        return render(request, 'movies/login.html', {'res': "用户名或者密码错误！！！"})



def register(request):
    # 定义一个错误提示为空
    error_name = ''
    if request.method == 'POST':
        # user = request.POST.get('username')
        password =str(request.POST.get('password'))
        email = request.POST.get('email')
        user_list = models.User.objects.filter(email=email)
        if len(email)==0:
            print('请输入用户')
        if user_list:
            # 注册失败
            error_name = '%s邮箱已经存在了' % email
            # 返回到注册页面，并且把错误信息报出来
            return render(request, 'movies/register.html', {'error_name': error_name})
        else:
            sha1 = hashlib.sha1()
            sha1.update(password.encode('utf-8'))
            res = sha1.hexdigest()
            # 数据保存在数据库中，并返回到登录页面
            user = models.User.objects.create(email=email,
                                              password=res,
                                              )



            user.save()
 # 同ip下跳转
            return redirect('/login/')
    return render(request, 'movies/register.html')

def pasword_reset(request):
    return render(request, 'movies/pasword_reset.html')

# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名')
#     password = forms.CharField(label='密   码', widget=forms.PasswordInput())
#     # last_login = forms.DateTimeField()
#
#
# class ChangeForm(forms.Form):
#     username = forms.CharField(label='用户名')
#     old_password = forms.CharField(label='原密码', widget=forms.PasswordInput())
#     new_password = forms.CharField(label='新密码', widget=forms.PasswordInput())
#
#
# def regist(request):
#     if request.method == 'POST':
#         uf = UserForm(request.POST)
#         if uf.is_valid():
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#
#             ##判断用户原密码是否匹配
#             user = User.objects.filter(username=username)
#             if user:
#                 info = '用户名已存在!'
#             elif len(user) == 0:
#                 info = '注册成功!'
#                 user = User()
#                 user.username = username
#                 user.password = password
#                 user.save()
#
#             return HttpResponse(info)
#     else:
#         uf = UserForm()
#
#     return render_to_response('regist.html', {'uf': uf})
#
#
# def login(request):
#     if request.method == 'POST':
#         ##获取表单信息
#         uf = UserForm(request.POST)
#         if uf.is_valid():
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#
#             ##判断用户密码是否匹配
#             user = User.objects.filter(username=username)
#             if user:
#                 passwd = User.objects.filter(username=username, password=password)
#                 if passwd:
#                     info = '登录成功！'
#                 else:
#                     info = '请检查密码是否正确!'
#             elif len(user) == 0:
#                 info = '请检查用户名是否正确!'
#
#             return HttpResponse(info)
#     else:
#         uf = UserForm()
#
#     return render_to_response('login.html', {'uf': uf})
#
#
# def change_pass(request):
#     if request.method == 'POST':
#         uf = ChangeForm(request.POST)
#         if uf.is_valid():
#             username = uf.cleaned_data['username']
#             old_password = uf.cleaned_data['old_password']
#             new_password = uf.cleaned_data['new_password']
#
#             ##判断用户原密码是否匹配
#             user = User.objects.filter(username=username)
#             if user:
#                 passwd = User.objects.filter(username=username, password=old_password)
#                 if passwd:
#                     User.objects.filter(username=username, password=old_password).update(
#                         password=new_password)  ##如果用户名、原密码匹配则更新密码
#                     info = '密码修改成功!'
#                 else:
#                     info = '请检查原密码是否输入正确!'
#             elif len(user) == 0:
#                 info = '请检查用户名是否正确!'
#
#         return HttpResponse(info)
#     else:
#         uf = ChangeForm()
#
#
#     return render_to_response('change.html',{'uf':uf})


'''
第一，新建一HTML
第二 配置视图
第三配置urls name赋值
第四找到页面 设置超简介 {% url 'urls中的name值'%}

'''