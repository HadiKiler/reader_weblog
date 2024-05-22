from .imports import *

class LikeViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    @login_required
    def list(self, request, *args, **kwargs):
        qs = Like.objects.all()
        data = LikeSerializer(qs, many=True).data

        response = Response(data)
        response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
        response.headers["Content-Range"] = len(qs)
        return response

    @login_required
    def retrieve(self, request, *args, **kwargs):
        qs = Like.objects.get(id=kwargs['id'])
        data = LikeSerializer(qs).data
        return Response(data)