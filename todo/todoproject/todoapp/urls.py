
from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbv<int:pk>/',views.DetailView.as_view(),name='cbv'),
    path('cbv<int:id>/',views.DetailView,name='cbv')
]
