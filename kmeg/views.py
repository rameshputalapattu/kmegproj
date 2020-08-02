from django.contrib import messages
from .models import KmegImage
from django.shortcuts import render, redirect
from .forms import FileUpload
from .quantisation import to_reconst_kmeg
from .kmegpublish import add_quantize_task
import os
import logging






# Create your views here.


def home_page(request):
    logging.debug("in the home request page")

    images = KmegImage.objects.all()

    context = {'title': 'KMEG-home', 'images': images}
    return render(request, 'kmeg/home.html', context=context)


def image(request, image_id):
    img = KmegImage.objects.get(pk=image_id)
    context = {
        'image': img,
    }
    return render(request,'kmeg/image.html',context=context)


def kmegimage(request, image_id):
    img = KmegImage.objects.get(pk=image_id)
    context = {
        'image': img,
    }
    return render(request,'kmeg/kmegimage.html',context=context)


def upload_page(request):
    # checks if the request type is post To the upload form  we pass the post request Since it is a image  we need to
    # add the enctype in the  HTML and CSRF token Check if the form is valid  and Use the FileSyatemStorage in Django
    # to handel it . By default it goes to the Media root
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            form_save_obj = form.save()
            id = int(form_save_obj.pk)
            clusters = int(form.cleaned_data['colors'])
            kmegImg = KmegImage.objects.get(pk=id)
            original_img_path = kmegImg.jpeg_picture.path
            pay_load = {"id": id, "clusters": clusters,"jpeg_picture_path": original_img_path}
            add_quantize_task(pay_load)
            original_img_filenm, ext = os.path.splitext(original_img_path)
            tb_nail_img_path = original_img_filenm + "_tb" + ext
            original_img_reconst_path = original_img_filenm + "_reconst" + ext
            tb_nail_img_filenm, ext = os.path.splitext(tb_nail_img_path)
            tb_nail_reconst_path = tb_nail_img_filenm + "_reconst" + ext
            kmegImg.quantized_picture = os.path.basename(original_img_reconst_path)
            kmegImg.quantized_thumb_nail = os.path.basename(tb_nail_reconst_path)
            kmegImg.thumb_nail = os.path.basename(tb_nail_img_path)
            kmegImg.save()
            messages.success(request, 'File Uploaded Successfully')
            return redirect('kmeg-home')
        else:
            form.errors
            messages.ERROR('File Uploaded Failed')
    else:
        # By Default it loads a blank form
        form = FileUpload()
        context = {'title': 'KMEG-upload',
                   'form': form,
                   }
        return render(request, 'kmeg/upload.html', context=context)



