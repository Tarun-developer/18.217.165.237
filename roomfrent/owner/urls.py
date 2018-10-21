from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	# url(r'^$', Dashboard.as_view(), name='dashboard'),
	# url(r'^sample_csv$', sample_csv, name='sample_csv')
    url(r'^$',OwnerDashboard.as_view(),name='owner_dashboard'),
    url(r'^owner_profile',OwnerProfile.as_view(),name='owner_profile'),
    url(r'^owner_property',OwnerProperty.as_view(),name='owner_property'),
    url(r'^register',OwnerRegister.as_view(),name='register'),
    url(r'^owner_add_property',OwnerAddProperty.as_view(),name='owner_add_property'),
    url(r'^edit_property',EditProperty.as_view(),name='edit_property'),
    url(r'^owner_sitemap',OwnerSitemap.as_view(),name='owner_owner_sitemap'),
    url(r'^register', login_required(OwnerRegister.as_view())),
    url(r'^reactivate',TemplateView.as_view(template_name='reactivate.html')),

    url(r'^logout/$', OwnerRegister.logout_view),
    url(r'^forgot/$', OwnerRegister.forgotPassword),

    # url(r'^activate/$', OwnerRegister.confirm),
    url(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}[0-9A-Za-z]{1,20})/$',OwnerRegister.activate,name='activate')
    # (? url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',OwnerRegister.activate,name='activate'),)
    
]

