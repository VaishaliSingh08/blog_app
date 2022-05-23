from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from blog import  utilities as utl
from blogging.models import User, Blogpost

## function for dashboard page
def dash(request):
    uid  = request.session['user_id_pk']
    details = utl.get_all_object_from_id(User, uid)
    username = details[0]['user_name']
    return  render(request, 'dashboard/index.html', {'username':username})


# ## To show final listing blog page
def all_blogs(request):
    uid = request.session['user_id_pk']
    details = utl.get_all_object_from_id(User, uid)
    username = details[0]['user_name']
    if Blogpost.objects.filter(author_id=uid).exists():
        p = Blogpost.objects.filter(author_id=uid).values()
        data= {"p": p, "username" :username}
        return  render(request, 'dashboard/blog-list.html', data)
    return render(request, 'dashboard/blog-list.html', {'username':username})


# # Function for adding products
def add_blog_post(request):
    uid = request.session['user_id_pk']
    details = utl.get_all_object_from_id(User, uid)
    username = details[0]['user_name']
    if request.method == "POST":
        # print(request.POST['trash'])

        title = request.POST['title']
        content = request.POST['content']
        myfile = request.FILES['image']

        fs = FileSystemStorage(location='media/blog/')

        filename = fs.save(myfile.name, myfile)

        f_name = 'blog/' + filename
        uploaded_file_url = fs.url(f_name)

        blog = Blogpost.objects.create(title=title, content=content,
                                           image=uploaded_file_url, author_id=uid)

        blog.save()

        return redirect('all_blogs')

    return render(request, 'dashboard/blog-edit.html', {'username':username})


# Function to delete any product
def delete(request, id):
    uid = request.session['user_id_pk']
    blog = Blogpost.objects.filter(author_id=uid, id=id).values()
    blog_id = blog[0]['id']

    Blogpost.objects.filter(id=blog_id).delete()

    return redirect('all_blogs')


# # Function to edit any product information
def edit_blog(request, id):
    uid = request.session['user_id_pk']
    details = utl.get_all_object_from_id(User, uid)
    username = details[0]['user_name']
    blog = Blogpost.objects.filter(author_id=uid, id = id).values()

    title =  blog[0]['title']

    content =  blog[0]['content']
    image = blog[0]['image']
    id = blog[0]['id']

    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']


        if request.method == "FILES":
            myfile = request.FILES['update']
            fs = FileSystemStorage(location='media/blog/')
            filename = fs.save(myfile.name, myfile)
            f_name = 'blog/' + filename
            uploaded_file_url = fs.url(f_name)
            Blogpost.objects.filter(id=id).update(title=title, content=content,
                                               image=image)


            return render(request, 'dashboard/profile11.html',{'title': title,  'content': content,
                                                                   'image': uploaded_file_url, 'username':username})


        Blogpost.objects.filter(id=id).update(title=title, content=content)
        return render(request, 'dashboard/profile11.html', {'title': title, 'content': content,
                                                            'username':username,'image': image, 'id':id})


    return render(request, 'dashboard/profile11.html',{'title': title, 'content': content,
                                                            'username':username,'image': image, 'id':id})


def home(request):
    return render(request, 'blog/index.html')


