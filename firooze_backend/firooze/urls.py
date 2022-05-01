from django.urls import path
from . import views
from django.contrib import admin

from .views import CustomAuthToken

urlpatterns = [
    path('', admin.site.urls),
    path('SendMessage/', views.SendMessage.as_view()),
    path('GetMessageAdmin/', views.GetMessageAdmin.as_view()),
    path('GetResidentsAdmin/', views.GetResidentsAdmin.as_view()),
    path('SubmitDebtAdmin/', views.SubmitDebtAdmin.as_view()),
    path('GetPosts/', views.GetPosts.as_view()),
    path('SubmitNotif/', views.SubmitNotif.as_view()),
    path('DeletePost/', views.DeletePostAdmin.as_view()),
    path('EditPost/', views.EditPostAdmin.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('GetDebt/', views.GetDebt.as_view()),
    path('DeleteMessage/', views.DeleteMessage.as_view()),
]
