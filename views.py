from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import members,active_periods
from user_app.serializers import member_ser,activity_ser


def team_members(request):
    if request.method=="GET":  #getting from db
        team=members.objects.all()
        serializer=member_ser(team,many=True)
        return JsonResponse(serializer.data,safe=True)
    elif request.method=="POST":  #posting data to api
        data=JsonResponse.Parse(request)
        serializer=member_ser(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

