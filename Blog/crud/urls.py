from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("create/", views.AddPost.as_view()),
    path("show/",views.Myview.as_view()),
    # path("search/",views.SearchView),
    path("search/",views.SearchView.as_view()),
    path('delete/<slug:pk>/',views.DeletePost.as_view(),name="delete"),
    path('updtae/<slug:pk>/',views.UpdatePost.as_view(),name="update"),
    path("details/<slug:pk>/", views.PostDetail.as_view(), name="post_detail"),
   
]
