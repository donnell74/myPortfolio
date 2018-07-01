from django.shortcuts import redirect


class AuthRedirectMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith("/accounts/login/"):
            if not request.user.is_authenticated:
                return redirect('/accounts/login/', permanent=True)

        return self.get_response(request)
