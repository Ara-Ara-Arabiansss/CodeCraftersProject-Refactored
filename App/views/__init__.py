# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .staff import staff_views
from .student import student_views
from .courses import course_views

views = [user_views, index_views, auth_views, staff_views, student_views, course_views] 
# blueprints must be added to this list