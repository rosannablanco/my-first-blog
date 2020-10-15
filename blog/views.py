from django.shortcuts import render

# Create your views here.
# def is a funtion of name post_list


def post_list(request):
    return render(request, 'blog/post_list.html', {})
