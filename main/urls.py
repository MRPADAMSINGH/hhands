from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("newsletter", views.newsletter, name="newsletter"),
    path("SupportACause", views.support, name="SupportACause"),
    path("Members", views.members, name="Members"),
    path("Service", views.service, name="Service"),
    path("OurTeams", views.ourteam, name="Our Teams"),
    path("About", views.about, name="Helping Hands About"),
    path("PartnersCollaborators", views.partners, name="Partners Collaborators"),
    path("JoinUs", views.joinus, name="Join Us"),
    path("Contact", views.contact, name="contact"),

]