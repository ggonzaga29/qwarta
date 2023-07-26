from django.shortcuts import redirect


def auth_middleware(get_response):
    session_whitelist = [
        '/login',
        '/register',
        '/logout',
        '/admin',
    ]

    def middleware(request):
        response = get_response(request)

        if not request.session.get('user_id'):
            if not any(request.path.startswith(path) for path in session_whitelist):
                return redirect('/login/')

        if request.session.get('user_id'):
            if request.path == '/login/':
                return redirect('/')

        return response

    return middleware
