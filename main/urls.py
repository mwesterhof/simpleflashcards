from django.urls import path

from .views import CardList, ShowCard

urlpatterns = [
    path('', CardList.as_view(), name='card_list'),
    path('random/', ShowCard.as_view(), name='random_card'),
]
