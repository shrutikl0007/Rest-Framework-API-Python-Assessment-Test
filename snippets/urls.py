from snippets import views
from django.urls import path


urlpatterns = [
    path('', views.Snippets_List, name='Snippets_List'),
    path('Snippets_Detail/<int:snippets_id>',views.Snippets_Detail, name='Snippets_Detail'),
]
