from rest_framework import generics

from api import models, serializers

class ThreadListView(generics.ListAPIView):
    """ Threads List view """
    queryset = models.Thread.objects.all()
    serializer_class = serializers.ThreadSerializer


class ThreadDetailView(generics.RetrieveAPIView):
    """ Thread Detail view """
    queryset = models.Thread.objects.all()
    serializer_class = serializers.LiteThreadSerializer


class PostListView(generics.ListAPIView):
    """ Post list of the Thread view """
    serializer_class = serializers.PostSerializer

    def get_queryset(self, *args, **kwargs):
        tid = self.kwargs['tid']
        self.queryset = models.Post.objects.filter(thread_id=tid).all()
        return self.queryset
