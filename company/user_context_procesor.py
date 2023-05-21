from .models import Users

def get_user(request):
    if request.user.is_authenticated:
        quary_user = Users.objects.get(user=request.user)
        return {'user_user':quary_user}
    else:
        return {}