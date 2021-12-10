
"app URL Configurations"



from django.urls import path
from Myapp1 import views


urlpatterns = [
    path('',views.input, name='input'),
    path('delete/<task_id>',views.delete_task,name='delete_task'),
    path('edit/<task_id>',views.edit_task,name='edit_task'),
    path('complete/<task_id>',views.complete_task,name='complete_task'),
    path('incomplete/<task_id>',views.incomplete_task,name='incomplete_task'),



]
