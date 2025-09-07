from django.urls import path

from .views import home, aboutUs, contact, showContact

urlpatterns = [
    path("", home, name="home-page"),
    path("about/", aboutUs, name="about-page"),
    path("contact/", contact, name="contact-page"),
    path("showcontact/", showContact, name="showcontact-page"),
]
