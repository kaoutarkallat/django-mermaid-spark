from django.urls import path, re_path
from main.views import user_view
from main.views.payment_view import PaymentView


from .views import ProductView, UserView
from .views.frontend_view import  index

urlpatterns=[
    path('', index,name ="index"),
    re_path(r'^api/payment/?$', PaymentView.as_view(),name ="payment"),
    re_path(r'^api/products/?$', ProductView.as_view(),name ="product"),
    re_path(r'^/api/user/register/?$', UserView.as_view(),name ="user__"),
    re_path(r'^cart/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^home/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^checkout/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^products/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^more-products/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^leggings/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^bras/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^shorts/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^tank_tops/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^sneakers/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^accessories/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^refund-policy/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^privacy-policy/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^detail/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^detail/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^contact/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^about-us/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^login/?(?P<path>.*)$', index ,name ="index"),
    re_path(r'^register/?(?P<path>.*)$', index ,name ="index"),


    # re_path(r'^(?P<path>.*)$', index,name ="index2")
    # re_path(r'^(?P<path>([^/]+/)*)$', index,name ="index2")

]