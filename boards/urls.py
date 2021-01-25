from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.PostingListView.as_view(), name='postings'),
    path('<int:posting_id>', views.PostingDetailView.as_view(), name='posting_detail'),
    path('', views.PostingCreateView.as_view(), name='posting_create'),
    path('<int:posting_id>', views.PostingDeleteView.as_view(), name='posting_delete'),
]
