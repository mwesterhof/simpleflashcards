from django.urls import path

from .views import CardList, ShowCard

urlpatterns = [
    path('all/', CardList.as_view(), name='card_list'),
    path('', ShowCard.as_view(), name='random_card'),
    path('en/', ShowCard.as_view(), name='random_card'),
]
