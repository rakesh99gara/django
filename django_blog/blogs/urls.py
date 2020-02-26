from django.urls import path
from blogs import views
# from accounts import views as account_view

urlpatterns = [
    path('', views.index, name='index'),
    path('new/',views.newPost,name="newPost"),
    path('<int:postid>/',views.showPost,name="showPost"),
    path('<int:postid>/edit',views.editPost,name="editPost"),
    path('<int:postid>/delete',views.deletePost,name="deletePost"),
    path('<int:postid>/<int:commentid>/delete',views.deleteComment,name="deleteComment"),
    path('<int:tagid>/tagPosts',views.tagPosts,name="tagPosts"),
    path("logout/",views.logoutUser, name="logout"),
    path("register/",views.registerPage, name="register"),
    path("login/",views.loginPage, name="login"),
]