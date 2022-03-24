from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, token):
        model = get_user_model()
        try:
            user = model.objects.get(api_key=token)
        except model.DoesNotExist:
            raise AuthenticationFailed(_("Invalid API Key."))

        return (user, None)
