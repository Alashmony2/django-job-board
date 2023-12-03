from django.urls import path ,include
from . import views
from . import api

app_name = 'job'
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.add_job,name='add_job'),
    path('<int:id>',views.job_detalis,name='job_detail'),
    path('api/jobs',api.job_lilst_api,name='job_lilst_api'),
    path('api/jobs/<int:id>',api.job_detail_api,name='job_detail_api'),
    # class based view
    path('api/v2/jobs',api.JobListApi.as_view(),name='job_lilst_api'),
    path('api/v2/jobs/<int:id>',api.JobDetail.as_view(),name='job_detail_api'),
]
