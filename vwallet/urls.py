from django.urls import path
from . import views

urlpatterns = [
    path('',views.PocketList.as_view(),name="pockets"),
    path('<int:id>',views.PocketDetail.as_view(),name="pocket")
]