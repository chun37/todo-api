from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, token):
        model = get_user_model()
        try:
            user = model.objects.get(api_key=token)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_("Invalid API Key."))

        return (user, None)
