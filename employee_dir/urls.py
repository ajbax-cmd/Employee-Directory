from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('add_employee/', views.add_employee, name = "add_employee"),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('edit_employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('employee_directory/', views.employee_directory, name = "employee_directory")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)