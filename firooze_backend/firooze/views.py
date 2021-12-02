import random

from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name': user.first_name + ' ' + user.last_name,
        })


class SendMessage(APIView):
    def post(self, request, format=None):
        try:
            serializer = serializers.SendMessageSerializer(data=request.data)
            if serializer.is_valid():
                senderName = serializer.data.get('senderName')
                senderEmail = serializer.data.get('senderEmail')
                message = serializer.data.get('message')
            else:
                return Response({'status': "Bad Request."}, status=status.HTTP_400_BAD_REQUEST)

            msg = Message()
            msg.senderName = senderName
            msg.senderEmail = senderEmail
            msg.message = message
            msg.save()

            return Response({'status': "OK"}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetResidentsAdmin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            residents = Residents.objects.all().order_by('id')
            data = []

            for r in residents:
                data.append({
                    'name': r.name,
                    'number': r.number,
                    'unit': r.block,
                    'debt': r.debt,
                    'id': r.id
                })

            return Response({'data': data}, status=status.HTTP_200_OK)


        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitDebtAdmin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            debtList = request.data.get('debtList')
            serializer = serializers.EditDebtSerializer(data=request.data)
            # print(debtList)
            print(debtList[0]['id'])
            if serializer.is_valid():
                serializer2 = self.serializer_class(data=request.data,
                                                   context={'request': request})
                serializer2.is_valid(raise_exception=True)
                user = serializer2.validated_data['user']
                token, created = Token.objects.get_or_create(user=user)

                for d in debtList:
                    debt = d['debt']
                    resId = d['id']

                    Residents.objects.filter(id=resId).update(debt=debt)

                return Response({'status': 'OK'}, status=status.HTTP_200_OK)

            else:
                return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetMessageAdmin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):

        try:
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            message = Message.objects.all().order_by('-send_at')

            data = []
            import jdatetime
            for m in message:
                data.append({
                    'id': m.id,
                    'name': m.senderName,
                    'email': m.senderEmail,
                    'msg': m.message,
                    'time': str(m.send_at.hour) + ':' + str(m.send_at.minute) + '\n' + str(jdatetime.date.fromgregorian(day=m.send_at.day, month=m.send_at.month, year=m.send_at.year))
                })

            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteMessage(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            print('test')
            dID = request.data.get('id')
            print(type(dID))
            Message.objects.all().filter(id=dID).delete()

            return Response({'data': 'ok'}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetPosts(APIView):

    def post(self, format=None):

        try:
            import jdatetime
            posts = Notif.objects.all().order_by('-created_at')
            postData = []
            for post in posts:
                postData.append({
                    'title': post.title,
                    'content': post.content,
                    'created_at': str(post.created_at.hour) + ':' + str(post.created_at.minute)  + ' | ' +
                                  str(jdatetime.date.fromgregorian(day=post.created_at.day, month=post.created_at.month, year=post.created_at.year)),
                    'id': post.id,
                    'author': post.author.first_name + ' ' + post.author.last_name if post.author else None
                })

            return Response({'postData': postData}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitNotif(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        try:
            serializer = serializers.SubmitPostSerializer(data=request.data)

            if serializer.is_valid():
                title = serializer.data.get('title')
                content = serializer.data.get('content')

            else:
                return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            post = Notif()
            post.title = title
            post.content = content
            post.created_at = datetime.now()
            post.author = user
            post.save()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)



        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EditPostAdmin(ObtainAuthToken):
    def post(self, request, format=None):
        try:
            serializer = serializers.EditPostAdminSerializer(data=request.data)
            if serializer.is_valid():
                id = serializer.data.get('id')
                title = serializer.data.get('title')
                content = serializer.data.get('content')

            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            Notif.objects.filter(id=id).update(title=title, content=content, created_at=datetime.now(), author=user)
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)


        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeletePostAdmin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:

            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            serializerID = serializers.DeletePostSerializer(data=request.data)

            if serializerID.is_valid():
                id = serializerID.data.get('id')

                Notif.objects.filter(id=id).delete()

                return Response({'status': 'OK'}, status=status.HTTP_200_OK)

            else:
                return Response({'status': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetDebt(APIView):
    def post(self, request):
        try:
            serializer = serializers.GetDebtSerialiser(data=request.data)

            if serializer.is_valid():
                block = serializer.data.get('block')
                floor = serializer.data.get('floor')
                unit = serializer.data.get('unit')
                try:
                    data = []
                    debt = Residents.objects.filter(block=block, floor=floor, unit=unit)
                    for d in debt:
                        data.append({
                            'debt': d.debt,
                            'name': d.name,
                        })
                    return Response({'data': data[0]}, status=status.HTTP_200_OK)

                except:
                    return Response({'data': 'Resident Not Found'}, status=status.HTTP_404_NOT_FOUND)

            else:
                return Response({'data': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


