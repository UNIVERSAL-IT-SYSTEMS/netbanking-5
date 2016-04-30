from django.conf.urls import include,patterns,url
urlpatterns=patterns('',
    url(r'^balance/$','account.views.balEnquiry',name='balance'),
    url(r'^transactions/$','account.views.transDetails', name='transDetails'),
    url(r'^transfer/$','account.views.Transfer', name='transfer'),
    url(r'^handleTransfer/$','account.views.handleTransfer', name='transferHandle'),
)
