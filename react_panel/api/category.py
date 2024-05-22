from .imports import *

class CategoryViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @login_required
    def list(self, request, *args, **kwargs):
        qs = Category.objects.all()
        data = CategorySerializer(qs, many=True).data
        for item in data:
            if item['image']:
                item['image'] = HOST + item['image']

        response = Response(data)
        response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
        response.headers["Content-Range"] = len(qs)
        return response
    
    @login_required
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @login_required
    def retrieve(self, request, *args, **kwargs):
        qs = Category.objects.get(id=kwargs['id'])
        data = CategorySerializer(qs).data
        if data['image']:
            data['image'] = HOST + data['image']
        return Response(data)  
    
    @login_required
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @login_required
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)