from django.urls import path
from .views.frontend import index, detail

urlpatterns = [
    # ex: "/polls/"
    path("", index, name="index"),
    path("<int:question_id>/", detail, name="detail")
]