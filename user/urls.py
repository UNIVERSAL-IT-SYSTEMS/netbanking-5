from django.conf.urls import include,patterns,url
urlpatterns=patterns('',
    url(r'^main/$','user.views.main', name='main'),
    url(r'^loginpage/$','user.views.renderLogin', name='rlogin'),
    url(r'^login/$','user.views.handleLogin', name='login'),
    url(r'^signup/$','user.views.handleSignup', name='signup'),
    url(r'^signuppage/$','user.views.renderSignup', name='rsignup'),
    url(r'^logout/$','user.views.logoutview', name='logout'),
)
