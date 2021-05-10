from django.urls import path

from admin_dashboard import views

urlpatterns = [
    path('', views.SummaryDashboardView.as_view(), name='admin_dashboard'),

    path('food/', views.FoodDashboardView.as_view(), name='food'),
    path('food/add', views.FoodCreatePageView.as_view(), name='add_food'),
    path('food/<int:pk>', views.FoodUpdatePageView.as_view(), name='upd_food'),
    path('food/<int:pk>/delete', views.FoodDeletePageView.as_view(), name='del_food'),

    path('sleep/', views.SleepDashboardView.as_view(), name='sleep'),
    path('sleep/add', views.SleepCreatePageView.as_view(), name='add_sleep'),
    path('sleep/<int:pk>', views.SleepUpdatePageView.as_view(), name='upd_sleep'),
    path('sleep/<int:pk>/delete', views.SleepDeletePageView.as_view(), name='del_sleep'),

    path('walk/', views.WalkDashboardView.as_view(), name='walk'),
    path('walk/add', views.WalkCreatePageView.as_view(), name='add_walk'),
    path('walk/<int:pk>', views.WalkUpdatePageView.as_view(), name='upd_walk'),
    path('walk/<int:pk>/delete', views.WalkDeletePageView.as_view(), name='del_walk'),

    path('toilet/', views.ToiletDashboardView.as_view(), name='toilet'),
    path('toilet/add', views.ToiletCreatePageView.as_view(), name='add_toilet'),
    path('toilet/<int:pk>', views.ToiletUpdatePageView.as_view(), name='upd_toilet'),
    path('toilet/<int:pk>/delete', views.ToiletDeletePageView.as_view(), name='del_toilet'),

    path('gymnastics/', views.GymnasticsDashboardView.as_view(), name='gymnastics'),
    path('gymnastics/add', views.GymnasticsCreatePageView.as_view(), name='add_gymnastics'),
    path('gymnastics/<int:pk>', views.GymnasticsUpdatePageView.as_view(), name='upd_gymnastics'),
    path('gymnastics/<int:pk>/delete', views.GymnasticsDeletePageView.as_view(),
         name='del_gymnastics'),

    path('other_event/', views.OtherEventDashboardView.as_view(), name='other_event'),
    path('other_event/add', views.OtherEventCreatePageView.as_view(), name='add_other_event'),
    path('other_event/<int:pk>', views.OtherEventUpdatePageView.as_view(), name='upd_other_event'),
    path('other_event/<int:pk>/delete', views.OtherEventDeletePageView.as_view(),
         name='del_other_event'),

]
