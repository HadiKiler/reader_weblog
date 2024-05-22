from .imports import *


class TagViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @login_required
    def list(self, request, *args, **kwargs):
        qs = Tag.objects.all()
        data = TagSerializer(qs, many=True).data
        response = Response(data)
        response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
        response.headers["Content-Range"] = len(qs)
        return response
    
    @login_required
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @login_required
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @login_required
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @login_required
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)