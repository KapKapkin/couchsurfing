from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from couchsurfing.mixins import (
    AjaxFormMixin,
    reCAPTCHAValidation,
    FormErrors,
    RedirectParams,
    Directions,
    is_ajax,
)
from .forms import (
    UserAddressForm,
    CustomUserSignupForm,
    CustomUserChangeForm,
)

CustomUser = get_user_model()
result = "Error"
message = "There was an error, please try again"


class AccountView(DetailView):
    model = CustomUser
    context_object_name = 'profile_user'
    template_name = 'account/profile.html'
    login_url = 'account_login'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request_user'] = self.request.user
        return context


def profile_view(request):
    '''
    function view to allow users to update their profile
    '''
    user = request.user
    up = user

    form = UserAddressForm(instance=up)

    if is_ajax(request):
        form = UserAddressForm(data=request.POST, instance=up)
        if form.is_valid():
            obj = form.save()
            obj.has_profile = True
            obj.save()
            result = "Success"
            message = "Your profile has been updated"
        else:
            message = FormErrors(form)
        data = {'result': result, 'message': message}
        return JsonResponse(data)

    else:

        context = {'form': form}
        context['google_api_key'] = settings.GOOGLE_API_KEY
        context['base_country'] = settings.BASE_COUNTRY

        return render(request, 'users/profile.html', context)


class UserSignUpView(AjaxFormMixin, FormView):
    template_name = 'account/signup.html'
    form_class = CustomUserSignupForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recaptcha_site_key'] = settings.RECAPTCHA_PUBLIC_KEY
        return context

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if is_ajax(self.request):
            token = form.cleaned_data['token']
            captcha = reCAPTCHAValidation(token)
            if captcha['success']:
                obj = form.save()
                obj.save()
                up = obj
                up.captcha_score = float(captcha['score'])
                up.save()

                login(self.request, obj,
                      backend='django.contrib.auth.backends.ModelBackend')

                result = 'Success'
                message = 'Thank you for signing up.'
            data = {'result': result, 'message': message}
            return JsonResponse(data)
        return response


class UserChangeView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'account/change.html'
    login_url = 'account_login'

    def post(self, request, *args, **kwargs):
        super(UserChangeView, self).post(request, *args, **kwargs)
        return redirect(request.user.get_absolute_url())

    def get_object(self, queryset=None):
        user = super(UserChangeView, self).get_object(queryset)
        if user.id != self.request.user.id:
            raise Http404()
        return user
