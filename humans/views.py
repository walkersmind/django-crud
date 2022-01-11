import json
from django.http.response import HttpResponse
from django.views import View
from django.http import JsonResponse, HttpResponse
from humans.models import Human, Dog

class HumanView(View):
    def get(self, request):

        humans = Human.objects.all()
        humans_dogs = Dog.objects.all()

        humanList = []
        humans_dogs_list =[]

        for human in humans:
            humanList.append(
                {
                    "human_name": human.human_name,
                    "human_email": human.human_email,
                    "human_age": human.human_age,
                    "human_id": human.id,
                }
            )
        

        for human_dog in humans_dogs:
            humans_dogs_list.append(
                {
                    "개 친구 이름": human_dog.dog_name,
                    "개 친구 나이": human_dog.dog_age,

                    #"인간 id": humanList[human_dog.human_id-1]["human_id"]
                    "이름": humanList[human_dog.human_id-1]["human_name"],
                    "이메일": humanList[human_dog.human_id-1]["human_email"],
                    "나이": humanList[human_dog.human_id-1]["human_age"]
                }
            )


        return JsonResponse({"humans_and_dogs": humans_dogs_list}, status=200)

    def post(self, request):
        data = json.loads(request.body)

        human = Human.objects.create(human_name=data["human_name"], human_email=data["human_email"], human_age=data["human_age"])

        return JsonResponse({"message": "SUCCESS"}, status=201)

class DogView(View):
    def get(self, request):

        humans = Human.objects.all()
        dogs = Dog.objects.all()

        humanList = []
        dogList = []

        for human in humans:
            humanList.append(
                {
                    "human_name": human.human_name,
                    "human_email": human.human_email,
                    "human_age": human.human_age,
                    "human_id": human.id,
                }
            )
        
        for dog in dogs:
            dogList.append(
                {
                    "개 이름": dog.dog_name,
                    "개 나이": dog.dog_age,
                    "인간 친구 이름": humanList[dog.human_id-1]["human_name"],
                }
            ) 

        return JsonResponse({"dogs": dogList}, status=200)

    def post(self, request):
        data = json.loads(request.body)

        dog = Dog.objects.create(dog_name=data["dog_name"], dog_age=data["dog_age"], human=Human.objects.get(human_name=data["human_name"]))

        return JsonResponse({"message": "SUCCESS"}, status=201)


def welcome(request):
    return HttpResponse("Welcome!")