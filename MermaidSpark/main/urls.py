from django.urls import path, re_path


urlpatterns=[
    re_path(r'^api/signup/?$', SignUpView.as_view(), name="signup"),
]