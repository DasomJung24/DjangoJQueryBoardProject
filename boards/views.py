from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import FormView, DeleteView
from django.http import JsonResponse

from .models import Posting
from .forms import PostingForm


class PostingListView(ListView):
    """
    게시물 리스트 불러오기
    """
    model = Posting
    template_name = 'boards/boards.html'
    http_method_names = ['get']
    context_object_name = 'postings'

    def get_queryset(self):
        return Posting.objects.select_related(
            'writer',
        ).all()


class PostingDetailView(DetailView):
    """
    게시물 상세 페이지
    """
    model = Posting
    template_name = 'boards/board_detail.html'
    http_method_names = ['get']
    context_object_name = 'posting'
    pk_url_kwarg = 'posting_id'

    def get_queryset(self):
        return Posting.objects.select_related(
            'writer',
        ).all()


class PostingCreateView(FormView):
    """
    게시물 생성하기
    """
    model = Posting
    http_method_names = ['post']
    form_class = PostingForm

    def post(self, request, *args, **kwargs):
        print(11111)
        data = request.POST
        if data is None:
            return render(request, 'boards/posting_create.html')

    def form_valid(self, form):
        posting = form.save()
        return JsonResponse({'writer': posting.writer, 'id': posting.id, 'content': posting.content,
                             'created_datetime': posting.created_datetime}, status=200)

    def form_invalid(self, form):
        return JsonResponse({'msg': {**form.errors.get_json_data()}}, status=400)


class PostingDeleteView(DeleteView):
    """
    게시물 삭제하기
    """
    model = Posting
    http_method_names = ['delete']
    pk_url_kwarg = 'posting_id'

    def delete(self, request, *args, **kwargs):
        posting = get_object_or_404(Posting, pk=self.kwargs.get(self.pk_url_kwarg))
        print(11111)
        posting.delete()
        return JsonResponse({'msg': 'success'}, status=200)