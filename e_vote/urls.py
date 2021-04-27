from django.urls import path
from django.views.generic.base import RedirectView
from e_vote import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='index'),
    path('voter/<str:pk>',views.voter,name='voter'),
    path('candidateregistration/',views.candidate,name='candidate'),
    path('castvote/',views.votes,name='voting_page'),
    path('votecount/<str:pk>/',views.give_vote,name='votecount'),
    #path('adminsignup/',views.admin_signup,name='adminsignup'),
    path('login/',views.login_view,name='admin_login'),
    path('election/',views.election,name='election'),
    #path('yourelection/',views.select_election,name='select_election'),
    path('winner/',views.winner,name='winner')
  
]

urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)