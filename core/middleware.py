from django.shortcuts import redirect


def user_type_middleware(get_response):
    def middleware(request):
        response = get_response(request)

        if request.path.startswith('/dashboard'):
            if request.session.get('user_id'):
                if request.session.get('user_type') != 'admin':
                    return redirect('/client')

        if request.path.startswith('/client'):
            if request.session.get('user_id'):
                if request.session.get('user_type') != 'client':
                    return redirect('/dashboard')

        return response

    return middleware


def admin_middleware(get_response):
    session_whitelist = [
        '/login',
        '/register',
        '/logout',
        '/admin',
    ]

    def middleware(request):
        response = get_response(request)

        if request.path == '/':
            return response

        if not request.session.get('user_id'):
            if not any(request.path.startswith(path) for path in session_whitelist):
                return redirect('/login')

        if request.session.get('user_id'):
            if request.path == '/login':
                return redirect('/dashboard')

        return response

    return middleware

# def admin_middleware(get_response):
#     def middleware(request):
#         response = get_response(request)
#
#         if request.path.startswith('/dashboard'):
#             if request.session.get('user_id'):
#                 if request.session.get('user_type') != 'admin':
#                     return redirect('/')
#
#         return response
#
#     return middleware

# def client_middleware(get_response):
#     def middleware(request):
#         response = get_response(request)
#
#         if request.path.startswith('/'):
#             if request.session.get('user_id'):
#                 if request.session.get('user_type') != 'client':
#                     return redirect('/dashboard')
#
#         return response
#
#     return middleware
