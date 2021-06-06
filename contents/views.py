from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404
from os.path import splitext
from .models import (Certification, Education, Focus, ProfessionalSkill,
                     Profile, Project, ProjectCategory, Recommendation,
                     Seminar, TechnicalSkill, WorkExperience, Contactus)


def certification(request, pk):
    file = get_object_or_404(Certification, pk=pk)
    file_path = str(file.document)
    file_type = ''

    try:
        # Get the file extension:
        extension = splitext(file_path[16:])[1]
        if extension == '.pdf':
            file_type = 'application/pdf'

        response = FileResponse(open(f'media/{file_path}', 'rb'), content_type=file_type)
        response['Content-Disposition'] = f'filename={file_path[16:]}'

        return response
    except FileNotFoundError:
        raise Http404()


def home(request):
    vj = User.objects.get(id=1)
    top_skills = TechnicalSkill.objects.filter(is_top_skill=True)
    focus = Focus.objects.filter(is_active=True)
    technical_skills = TechnicalSkill.objects.order_by('id')
    professional_skills = ProfessionalSkill.objects.order_by('id')
    education = Education.objects.order_by('-id')
    work_experience = WorkExperience.objects.order_by('-id')
    categories = ProjectCategory.objects.order_by('name')
    projects = Project.objects.order_by('title')
    certs = Certification.objects.order_by('-id')
    seminars = Seminar.objects.order_by('-id')
    recommendations = Recommendation.objects.order_by('id')

    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        phoneno = request.POST.get('phoneno')
        contact = Contactus(name=name, email=email, msg=msg, phoneno=phoneno,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')

    context = {
        'vj': vj,
        'top_skills': top_skills,
        'focus': focus,
        'technical_skills': technical_skills,
        'professional_skills': professional_skills,
        'education': education,
        'work_experience': work_experience,
        'categories': categories,
        'projects': projects,
        'certs': certs,
        'seminars': seminars,
        'recommendations': recommendations
    }
    return render(request, 'contents/portfolio.html', context)


def project_document(request, pk):
    file = get_object_or_404(Project, pk=pk)
    file_path = str(file.document)
    file_type = ''

    try:
        # Get the file extension:
        extension = splitext(file_path[16:])[1]
        if extension == '.pdf':
            file_type = 'application/pdf'

        response = FileResponse(open(f'media/{file_path}', 'rb'), content_type=file_type)
        response['Content-Disposition'] = f'filename={file_path[16:]}'

        return response
    except FileNotFoundError:
        raise Http404()


def resume(request, pk):
    file = get_object_or_404(Profile, pk=pk)
    file_path = str(file.cv)
    file_type = ''

    try:
        # Get the file extension:
        extension = splitext(file_path[16:])[1]
        if extension == '.pdf':
            file_type = 'application/pdf'

        response = FileResponse(open(f'media/{file_path}', 'rb'), content_type=file_type)
        response['Content-Disposition'] = f'filename={file_path[16:]}'

        return response
    except FileNotFoundError:
        raise Http404()


def seminar(request, pk):
    file = get_object_or_404(Seminar, pk=pk)
    file_path = str(file.document)
    file_type = ''

    try:
        # Get the file extension:
        extension = splitext(file_path[16:])[1]
        if extension == '.pdf':
            file_type = 'application/pdf'

        response = FileResponse(open(f'media/{file_path}', 'rb'), content_type=file_type)
        response['Content-Disposition'] = f'filename={file_path[16:]}'

        return response
    except FileNotFoundError:
        raise Http404()

# def contactus(request):
#   if (request.method == 'POST'):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     msg = request.POST.get('msg')
#     phoneno = request.POST.get('phoneno')
#     contact = Contactus(name=name, email=email, msg=msg, phoneno=phoneno,date=datetime.today())
#     contact.save()
#   return render(request, 'contents/portfolio.html')
