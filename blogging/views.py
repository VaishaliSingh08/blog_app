from django.shortcuts import render, redirect
from blogging.models import User, Blogpost
import re
from blog import utilities as utl

# Create your views here.
# Function to show all blogs on website page
def index(request):
    blog = Blogpost.objects.all().values()
    data = {"blog": blog}
    return render(request, 'blog/index.html', data)


def login(request):
    if request.method == 'POST':
        user_email = request.POST['cEmail']
        password_one = request.POST['password']
        user_valid = utl.check_user_exist(user_email, password_one)
        error_msg = ''
        if user_valid:
            request.session['email'] = user_email
            uid = utl.get_id(User, user_email)

            user_id = uid[0]['user_id_pk']
            request.session['user_id_pk'] = user_id
            return redirect('dash')
        else:
            error_msg = "Credentials do not match !!"
            return render(request, 'blog/login.html', {'error_msg':error_msg})
    else:
        return render(request, 'blog/login.html')


def blog_detail(request, id):
    blog = Blogpost.objects.filter(id=id).values()

    username = User.objects.filter(user_id_pk= blog[0]['author_id']).values_list('user_name', flat=True)

    data = {"blog": blog, "username" :username[0]}
    return  render(request, 'blog/single-standard.html', data)


def register(request):
    if request.method == 'POST':
        user_name = request.POST['cName']
        user_email = request.POST['cEmail']
        user_contact = request.POST['cContact']
        password_one = request.POST['password_one']
        password_two = request.POST['password_two']


        #validation
        value = {
            'user_name':user_name,
            'user_email' : user_email,
            'user_contact' : user_contact,
        }

        error_msg = " "

        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if (re.search(regex, user_email)):
            print("okay")
        else:
            error_msg = "Invalid Email !!"

        if len(user_contact) < 4:
            error_msg = "Phone number must be of 10 digits !!"
        elif len(user_contact) > 10 :
            error_msg = "Phone number must be of 10 digits !!"
        elif password_one != password_two:
            error_msg = "Passwords not matching !!"
        elif User.objects.filter(user_name = user_name).exists():
            error_msg = "Username taken !!"
        elif User.objects.filter(user_email = user_email).exists():
            error_msg = "Email taken !!"
        success = ""
        if error_msg == " ":
            user = User.objects.create(user_name = user_name, user_email=user_email,password= password_one,
                                       cnfrm_pass=password_two, user_contact= user_contact, is_active='true')
            user.save()

            return render(request, 'blog/sign_up.html', {'success': success})

        else:
            data = {
                'error_msg' : error_msg,
                'values' : value
            }
            return render(request, 'blog/sign_up.html',data)

    else:
        return render(request, 'blog/sign_up.html')



## Function to logout from dashboard
def logout(request):
    try:
        del request.session['email']
        del request.session['user_id_pk']
        return redirect('login')
    except KeyError:
        pass
        return redirect('login')

