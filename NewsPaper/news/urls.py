from django.urls import path

from .views import NewsList, NewsSearch, PostCreate, PostDelete, PostDetail, PostUpdate

urlpatterns = [
    path("", NewsList.as_view()),
    path("search", NewsSearch.as_view()),
    path("<int:pk>", PostDetail.as_view(), name="post_detail"),
    path("add/", PostCreate.as_view(), name="post_create"),
    path("<int:pk>/edit", PostUpdate.as_view(), name="post_update"),
    path("<int:pk>/delete", PostDelete.as_view(), name="post_delete"),
]
