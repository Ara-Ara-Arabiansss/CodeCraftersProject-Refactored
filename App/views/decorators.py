from functools import wraps
from flask import abort, g

def staff_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # Assuming you have a way to identify staff users
        # For example, you might have a 'is_staff' attribute in your user model
        if not g.current_user.is_staff:
            abort(403)  # Forbidden
        return func(*args, **kwargs)

    return decorated_function