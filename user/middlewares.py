from rest_framework.exceptions import NotAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from user.models import User


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # admin はログイン求めるので確認しなくて平気
        if request.path.startswith("/admin"):
            return self.get_response(request)

        # header の Authorization を読み、api_key を取得する。Authorization が存在しない 又は 値が空文字 の場合は status_code: 401
        api_key: Optional[str] = request.headers.get("Authorization", None)
        if api_key is None or api_key == "":
            raise NotAuthenticated

        # api_key を元に、User を取ってくる。存在しない場合は status_code: 401
        try:
            accessed_user = User.objects.get(api_key=api_key)
        except ObjectDoesNotExist:
            raise NotAuthenticated

        request.accessed_user = accessed_user

        response = self.get_response(request)
        return response
