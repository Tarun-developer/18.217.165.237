from django.conf.urls import url
from .views import *
# from .views import HomePage,SearchResults

urlpatterns = [
	url(r'^$', HomePage.as_view(), name='homepage'),
	# url(r'^sample_csv$', sample_csv, name='sample_csv')
        url(r'^search_results',SearchResults.as_view(),name='search_results'),
        url(r'^get_contact/$', SearchResults.get_contact),
        url(r'^ajax/validate_username/$', HomePage.validate_username, name='validate_username'),
         url(r'^ajax/register/$', HomePage.owner_register, name='owner_register'),
         url(r'^ajax/login/$', HomePage.user_login, name='user_login'),
]
