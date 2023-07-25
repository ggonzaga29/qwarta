from django.shortcuts import redirect


def auth_middleware(get_response):
    session_whitelist = [
        '/login/',
        '/register/',
        '/logout/',
        '/login',
        '/register',
        '/logout'
    ]

    def middleware(request):
        # redirect to login page if user is not logged in
        if not request.session.get('user_id'):
            if request.path not in session_whitelist:
                return redirect('/login/')

        if request.session.get('user_id'):
            if request.path == '/login/':
                return redirect('/')

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
