from django.shortcuts import render
from . import models


def index(request):
    noticias_recentes = models.Notice.objects.all().order_by('-id')[:10]
    slides = models.HomeSlide.objects.all()
    categorias = models.Categoria.objects.all()

    pesquisa = request.GET.get('news-querry')
    filter = request.GET.get('filter')

    if filter:
        if filter == 'Todas':
            noticias_recentes = models.Notice.objects.all().order_by('-id')[:10]
        else:
            noticias_recentes = models.Notice.objects.all().filter(notice_category__name=filter)[:10]

    return render(request, 'informatica/index.html', {
        'slides': slides,
        'noticias_recentes': noticias_recentes,
        'categorias': categorias,
        'filter': filter
    })


# Noticias
def noticias(request):
    noticias = models.Notice.objects.all().order_by('-id')
    noticias_recentes = models.Notice.objects.all().order_by('-id')[:5]
    
    return render(request, 'informatica/noticias.html', {
        'noticias': noticias,
        'noticias_recentes': noticias_recentes
    })

# Noticia (Noticias/<id>)
def noticia(request, notice_id):
    noticias = models.Notice.objects.all().order_by('-id')
    noticias_recentes = models.Notice.objects.all().reverse()[:5]

    return render(request, 'informatica/noticia.html', {
        'noticia': models.Notice.objects.get(id=notice_id),
        'noticias': noticias,
        'noticias_recentes': noticias_recentes
    })

# Sobre o Curso
def sobre_o_curso(request):
    return render(request, 'informatica/sobre_o_curso.html')

# Sobre a escola
def sobre_a_escola(request):
    return render(request, 'informatica/sobre_a_escola.html')