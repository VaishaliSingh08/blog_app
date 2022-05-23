from django.db.models import Q
from blogging.models import User

def get_detials_from_id_all(tablename, id, field_name):
    # # print(id)
    kwargs = {
        '{0}'.format(field_name): id
    }
    # # print(kwargs)
    object_values = tablename.objects.filter(Q(**kwargs)).values()
    object_values = list(object_values)
    return object_values

def update_user_status(user_id):
    User.objects.filter(pk=user_id).update(is_active = True)
    return True

def check_user_exist(email, password):
    object_values = User.objects.filter(user_email=email, password=password)
    return object_values

def get_id(table_name, email):
    object_values = table_name.objects.filter(user_email=email).values()
    object_values = list(object_values)
    return object_values

def get_all_object_from_id(table_name,key):
    object_values = table_name.objects.filter(pk=key).values()
    object_values = list(object_values)
    return object_values

def get_detials_from_id(tablename, id, field_name):
    # print(id)

    kwargs = {
        '{0}'.format(field_name): id
    }
    # # print(kwargs)
    object_values = tablename.objects.filter(Q(**kwargs)).values()
    object_values = list(object_values)
    return object_values

def get_detials_from_field(tablename, id, field_name, value):
    kwargs = {
        '{0}'.format(field_name): id
    }
    object_values = tablename.objects.filter(Q(**kwargs)).values("{0}".format(value))
    # # print(object_values)
    object_values = list(object_values)
    return object_values


def get_detials_from_id_with_user_id(tablename, id, field_name, uid):
    # # print(id)
    # id = id.split(',')

    kwargs = {
        '{0}'.format(field_name): id
    }
    # # print(kwargs)
    object_values = tablename.objects.filter(Q(**kwargs), Q(user_id_fk=uid)).values()
    # object_values = list(object_values)
    # # print(object_values)
    return object_values



def create_edit_listing_web(request, email, id):
    # # print(request.POST)

    p_name = request.POST['p_name']
    p_desc = request.POST['p_desc']
    p_price = request.POST['p_price']
    p_image = request.POST['p_image']
    u_id = get_detials_from_field(User, email, 'user_email', 'user_id_pk')

    user = Products.objects.filter(p_id_pk=u_id).update(p_name=p_name, p_price=p_price, p_desc=p_desc,
                                           p_image=p_image)

    return id



