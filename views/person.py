from django.http import HttpResponse
from django.shortcuts import render
from ..models.Person import Person
person = Person()
def getFriends(request, id):
    friends = person.getFriends(int(id))
    # print (friends)
    return render(request, "person/friends.html", {"friends": friends})
def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        return HttpResponse(person.add(name, age))
    else:
        return render(request, "person/add.html")
def detail(request, id):
    detail = person.detail(id)
    return render(request, "person/detail.html", {"person": detail})