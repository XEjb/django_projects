from django.shortcuts import render
from django.http import HttpResponse
from .forms import AuthorForm
from django.views import View
from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializers


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class AuthorDetailViews(generics.RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers




def index(request):
    return render(request, 'articles/index.html')


class PostView(View):

    def get(self, request):
        form = AuthorForm()
        context = {
            "form": form,
        }
        return render(request, 'articles/check.html', context)

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request)

# def check_post(request):
#     if request.method == "POST":
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = AuthorForm()
#     context = {
#         "form": form,
#     }
#     return render(request, 'articles/check.html', context)
