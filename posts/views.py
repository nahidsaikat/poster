from rest_framework import viewsets, mixins
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.viewsets import GenericViewSet

from .models import Post, PostFile
from .serializers import PostSerializer, PostFileSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    A Post represents a Facebook post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostFileView(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    """
    An API endpoint to upload files for a post.

    Additional Information:
    Content-Type: multipart/form-data; boundary=<calculated when request is sent>
    """
    parser_class = [FileUploadParser, MultiPartParser]
    permission_classes = []
    serializer_class = PostFileSerializer

    def get_queryset(self):
        return PostFile.objects.all()

    def get_serializer_context(self, **kwargs):
        context = super().get_serializer_context()
        context['post_id'] = self.kwargs.get('pk')
        return context

    def create(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        return super().create(request, *args, **kwargs)
