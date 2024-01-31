from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def Snippets_List(request):
    if request.method == 'GET':
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def Snippets_Detail(request, snippets_id):
    try:
        queryset = Comment.objects.get(id=snippets_id)
    except Comment.DoesNotExist:
        return Response({'message': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(queryset)
        return Response(serializer.data)

    if request.method == 'PUT':  # put= all update
        serializer = CommentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':  # patch=partial update
        serializer = CommentSerializer(
            queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        queryset.delete()
        return Response({'message': "Employee Detail deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
