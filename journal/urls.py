from django.urls import path

from journal.views import (
    ToiletRetrieveUpdateDestroyView, ToiletListCreateView,
    FoodRetrieveUpdateDestroyView, FoodListCreateView,
    WalkListCreateView, WalkRetrieveUpdateDestroyView,
    SleepListCreateView, SleepRetrieveUpdateDestroyView,
    OtherEventListCreateView, OtherEventRetrieveUpdateDestroyView,
    GymnasticsRetrieveUpdateDestroyView, GymnasticsListCreateView,
    SummaryListView, SummaryRetrieveView
)

urlpatterns = [
    path('toilet/', ToiletListCreateView.as_view()),
    path('toilet/<int:pk>', ToiletRetrieveUpdateDestroyView.as_view()),
    path('food/', FoodListCreateView.as_view()),
    path('food/<int:pk>', FoodRetrieveUpdateDestroyView.as_view()),
    path('walk/', WalkListCreateView.as_view()),
    path('walk/<int:pk>', WalkRetrieveUpdateDestroyView.as_view()),
    path('sleep/', SleepListCreateView.as_view()),
    path('sleep/<int:pk>', SleepRetrieveUpdateDestroyView.as_view()),
    path('gymnastics/', GymnasticsListCreateView.as_view()),
    path('gymnastics/<int:pk>', GymnasticsRetrieveUpdateDestroyView.as_view()),
    path('other_event/', OtherEventListCreateView.as_view()),
    path('other_event/<int:pk>', OtherEventRetrieveUpdateDestroyView.as_view()),
    path('summary/', SummaryListView.as_view()),
    path('summary/<int:pk>', SummaryRetrieveView.as_view()),
]
