from .imports import *

class CommentViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @login_required
    def list(self, request, *args, **kwargs):
        qs = Comment.objects.all()
        data = CommentSerializer(qs, many=True).data

        response = Response(data)
        response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
        response.headers["Content-Range"] = len(qs)
        return response
    
    @login_required
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @login_required
    def retrieve(self, request, *args, **kwargs):
        qs = Comment.objects.get(id=kwargs['id'])
        data = CommentSerializer(qs).data
        return Response(data)
    
    @login_required
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @login_required
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)