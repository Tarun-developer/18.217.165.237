from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from search.models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
import json
from django.core import serializers
# from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
import googlemaps
import datetime
from django.utils.dateparse import parse_datetime
import os
import string
import random
from django.core.files.storage import FileSystemStorage
gmaps = googlemaps.Client(key='AIzaSyC95eHImBVWI4SbTc3DD2zruYGcWdI6xD0')


# Create your views here.
class LoggedInMixin(object):
    @method_decorator(login_required(login_url='/owner/register/'))
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class OwnerDashboard(LoggedInMixin, TemplateView):
    template_name = "owner_dashboard.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerDashboard, self).get_context_data()
        context['user'] = self.request.user.first_name
        return context


class OwnerProfile(LoggedInMixin, TemplateView):
    template_name = "owner_profile.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerProfile, self).get_context_data()

        return context


class OwnerSitemap(LoggedInMixin, TemplateView):
    template_name = "owner_sitemap.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerSitemap, self).get_context_data()

        return context


class OwnerProperty(LoggedInMixin, TemplateView):
    template_name = "owner_property.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerProperty, self).get_context_data()
        owner = self.request.user.id
        all_prop = list(Property.objects.filter(owner_id=(owner)))
        context['user'] = self.request.user.first_name
        context['propertys'] = all_prop

        return context


class OwnerRegister(TemplateView):
    template_name = "owner_register.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerRegister, self).get_context_data()
        return context

    def logout_view(request):
        logout(request)
        return HttpResponseRedirect("/")

    def reactivate(request):
        print(request)
        return HttpResponseRedirect("")
        pass

    def forgotPassword(request, email):
        print(request)

    def post(self, request):
        islogin = request.POST.get('islogin')
        password = request.POST.get('password')
        mobile = request.POST.get('moblie')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')

        if islogin:

            try:
                user = authenticate(username=mobile, password=password)
                print(user)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect("/owner/?own=" + str(user.id))
                    else:
                        messages.info(
                            request, 'Your Email is not verifyed please check email')
                        return HttpResponseRedirect("/owner/reactivate")
                else:
                    messages.info(
                        request, 'invalid password. please try again')
                    return HttpResponseRedirect("/owner/register")
            except Exception as r:
                messages.info(request, 'invalid password. please try again')
                return HttpResponseRedirect("/owner/register")
        else:
            try:
                owner_obj = OwnerInfo.objects.get(owner_mobile=mobile)
                if owner_obj:
                    messages.info(request, 'please login at your right')
                    return HttpResponseRedirect("/owner/register")
            except Exception as r:
                print(r)
            user = User.objects.create_user(mobile, email, password)
            user.first_name = first_name
            user.is_active = False
            user.save()
            confirmation_code = ''.join(random.choice(
                string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33))
            owner_register = OwnerInfo(user=user)
            owner_register.owner_mobile = mobile
            owner_register.confirmation_code = confirmation_code
            owner_register.save()
            # user = authenticate(username=mobile, password=password)
            self.send_registration_confirmation(user, request)
            # return HttpResponseRedirect("/owner/owner_add_property/?own=" + str(user.id))
            messages.info(
                request, 'Please confirm your email address to complete the registration')

            return HttpResponseRedirect("/owner/")

    def send_registration_confirmation(self, user, request):
        p = OwnerInfo.objects.get(user=user)
        current_site = get_current_site(request)
        content = current_site.domain+"/owner/activate" + \
            user.username + "/" + str(p.confirmation_code)
        send_mail("Email Verify", content, 'no-reply@gsick.com',
                  [user.email], fail_silently=False)

    def activate(request, uid, token):
        try:
            user = User.objects.get(username=uid)
            if user.is_active == str(0):
                profile = OwnerInfo.objects.get(user=user)
                created_date = (user.date_joined.date())
                if profile.confirmation_code == token and created_date > (datetime.datetime.now()-datetime.timedelta(days=1)).date():
                    user.is_active = True
                    user.save()
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                    return HttpResponseRedirect("/owner/owner_property")
                else:
                    messages.info(request, 'Your token is expired')
                    return HttpResponseRedirect("/owner/register")
            else:
                messages.info(request, 'Your account is activated')
                return HttpResponseRedirect("/owner/register")
        except:
            return HttpResponseRedirect('/owner/register')


class OwnerAddProperty(LoggedInMixin, TemplateView):
    template_name = "owner_add_property.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(OwnerAddProperty, self).get_context_data()
        context['user'] = self.request.user.first_name
        context['preference'] = Preference.objects.all()
        context['property_type'] = PropertyType.objects.all()
        context['property_status'] = PropertyStatus.objects.all()
        context['additional_features'] = AdditionalFeatures.objects.all()

        return context

    def post(self, request):

        # try:
            # images_file = request.FILES['images']
            # fs = FileSystemStorage(
            #     location='media/properties/'+str(request.user.id))
            # filename = fs.save(images_file.name, images_file)
            # file_url = fs.url(filename)
            # uploaded_file_url = file_url.replace(
            #     'media', 'media/properties/'+str(request.user.id))
        property_type = request.POST.get('property_type')
        property_status = request.POST.get('property_status')
        loaction_title = request.POST.get('loaction')
        loaction = request.POST.get('lat_lng')
        lat_lng = loaction.split(',')
        lat = float(lat_lng[0])
        lng = float(lat_lng[1])

        price = request.POST.get('price')
        city = request.POST.get('city')
        preference_list = request.POST.getlist('preference[]')
        feature_list = request.POST.getlist('additional_features[]')
        bachelor = request.POST.get('bachelor')
        girls = request.POST.get('girls')

        # result_add_query = gmaps.places(loaction)
        # lat = result_add_query['results'][0]['geometry']['location']['lat']
        # lng = result_add_query['results'][0]['geometry']['location']['lng']
        furn_obj = PropertyStatus.objects.get(id=int(property_status))

        property_type_get = PropertyType.objects.get(name=property_type)

        new_property = Property.objects.create(name=str(property_type) + str(" - ") + str(property_status), created_at=timezone.now(
        ), location=loaction_title, status=1, budget=price, property_type=property_type_get, property_status=furn_obj, lat=lat, lng=lng, owner_id=request.user.id)

        for p in preference_list:
            preference_get = Preference.objects.get(id=p)
            new_property.preference.add(preference_get)
        for a in feature_list:
            feature_get = AdditionalFeatures.objects.get(id=a)
            new_property.add_feature.add(feature_get)

        # pref=property_preference.objects
        # images = Images.objects.create(
        #     url=uploaded_file_url, property_id=new_property)
        # except Exception as rr:
        #     print (rr)

        return HttpResponseRedirect("/owner/edit_property/?property=" + str(new_property.id))


class EditProperty(LoggedInMixin, TemplateView):
    template_name = "edit_property.html"

    def get_context_data(self, * args, ** kwargs):
        context = super(EditProperty, self).get_context_data()
        context['user'] = self.request.user.first_name
        property_obj = Property.objects.get(
            id=self.request.GET.get('property'))
        context['property'] = property_obj
        # context['preference']=Preference.objects.get(id=property_obj.preference.id)

        return context
