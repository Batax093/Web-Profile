from django.shortcuts import render, redirect
from .models import Feature
from .models import Form

# Create your views here.

def index(request):

    feature_1 = Feature(intro='Halo, Saya',
                        content='Fredrik Sahalatua Pakpahan')

    feature_2 = Feature(intro='Tentang Saya', content='Saya merupakan seorang mahasiswa UPN "Veteran" Jawa Timur Fakultas Ilmu Komputer jurusan Informatika. Saya sangat tertarik dengan dunia Informatika terutama data analyst, data science, back-end developement, dan software developement.')

    feature_3 = Feature(intro='"Only in the darkness can you see the stars."',
                        content='~Martin Luther King Jr')

    features = [
        Feature(intro='Basket', content='Saya menyukai basket karena sejak kecil telah dikenalkan oleh saudara saya.',
                photo='basketball.png'),
        Feature(intro='Music', content='Saya memang berasal dari keluarga musik sehingga sedari kecil saya sudah diajarkan tentang musik.', photo='guitar.png'),
        Feature(intro='Coding', content='Saya merasa coding membuat saya lebih memikirkan untuk memecahkan berbagai masalah dengan berbagai metode.', photo='code.png')
    ]

    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        pesan = request.POST.get('pesan')

        form = Form(nama=nama, email=email, pesan=pesan)
        form.save()

        return redirect('response')
    else:
        return render(request, 'index.html', {'features': features, 'feature_1': feature_1, 'feature_2': feature_2, 'feature_3': feature_3})
    

def response(request):
    index_url = '/'

    forms = Form.objects.all()

    return render(request, 'response.html', {'index_url': index_url, 'forms': forms})