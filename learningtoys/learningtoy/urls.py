from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('learningtoyapp.urls'))#included the learningtoy app's urls file 
]
