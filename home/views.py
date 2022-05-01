from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Queries, CovidExperience, QueryReply, Symptom

def home(request):
    total_experiences = len(CovidExperience.objects.all())
    normal_covid_experiences = len(CovidExperience.objects.filter(islongcovid=False))
    long_covid_experiences = len(CovidExperience.objects.filter(islongcovid=True))

    quora_covid_experiences = len(CovidExperience.objects.filter(source="Quora"))
    reddit_covid_experiences = len(CovidExperience.objects.filter(source="Reddit"))
    survey_covid_experiences = len(CovidExperience.objects.filter(source="Survey"))

    return render(request, 'home.html', {'total_experiences': total_experiences, 'normal_covid_experiences': normal_covid_experiences, 'long_covid_experiences': long_covid_experiences, 'quora_covid_experiences': quora_covid_experiences, 'reddit_covid_experiences': reddit_covid_experiences, 'survey_covid_experiences': survey_covid_experiences})


def query(request):
    if(request.method == "POST"):
        data = request.POST
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        query = Queries.objects.create(name=name, email=email, subject=subject, message=message)
        query.save()

    return redirect('/')


def covid_experience(request):
    if(request.method == "POST"):
        data = request.POST
        name = data['name']
        email = data['email']
        age = data['age']
        mobile = data['mobile']
        gender = data['gender']
        time_of_infection = data['time_of_infection']
        testing_date1 = data['testing_date1']
        testing_date2 = data['testing_date2']
        experience = data['experience']

        covid_experience = CovidExperience.objects.create(experience=experience)
        covid_experience.save()

    return render(request, 'form.html')


def read_experience(request):
    experiences = CovidExperience.objects.all()
    replies = QueryReply.objects.all()
    
    return render(request, 'experiences.html', {'experiences': experiences, 'replies': replies})


def symptoms_wordcloud(request):
    return render(request, 'wordcloud.html')


def population_chart(request):
    labels = []
    data = []
    symptoms = Symptom.objects.all()
    for obj in symptoms:
        labels.append(obj.name)
        data.append(obj.count)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })