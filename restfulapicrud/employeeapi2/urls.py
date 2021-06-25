from django.urls import path
from employeeapi2 import views
#from views.ListAPIView import delete
urlpatterns = [
    path('emp/',views.ListAPIView.as_view(),name="e_list"),
    path('emp/<int:pk>/',views.ListAPIView.as_view(),name="e_list"),
    path('punch/',views.InOutview.as_view(),name="e_list"),
    path('display/',views.displayemp.as_view(),name="e_list")
    
]
