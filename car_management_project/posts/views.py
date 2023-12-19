from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from posts.models import UserPostModel
from django.views.generic import DetailView
from django.contrib.auth.forms import User

from posts.forms import commentForm


def show_data(request):
    Userdata = UserPostModel.objects.all()
    return render(request, "profile.html", {"Userdata": Userdata})


class Details(DetailView):
    model = UserPostModel
    pk_url_kwarg = "id"
    context_object_name = "post"
    template_name = "details.html"

    def post(self, request, *args, **kwargs):
        comment_form = commentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.userPost = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = self.object
        comments = post.comments.all()
        commment_form = commentForm()
        context["comments"] = comments
        context["commets_form"] = commment_form
        return context





        
