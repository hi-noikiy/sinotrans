
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.cache import cache
from django.core.cache.backends.memcached import MemcachedCache
from .forms import UploadFileForm
import json
from django.conf import settings
import os
from PIL import Image

def get_upload_path():
    if settings.USE_SAE_BUCKET: #'SERVER_SOFTWARE' in os.environ: 
        return 'upload'
    else:
        photopath = os.path.join(settings.MEDIA_ROOT, 'upload')
        if not os.path.exists(photopath):
            os.makedirs(photopath)
        return photopath

def get_upload_url():
    photopath = os.path.join(settings.MEDIA_URL, 'upload')
    return photopath    

# Create your views here.
def upload_file(request):
    #print "upload_file"
    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            in_mem_image_file=request.FILES['image']
            filepath = os.path.join(get_upload_path(), in_mem_image_file.name)
            if in_mem_image_file:
                if settings.USE_SAE_BUCKET: #'SERVER_SOFTWARE' in os.environ: 
                    from saewrapper.storage.bucket import SAEBucket
                    SAEBucket().put_object(filepath,in_mem_image_file.file.getvalue())
                else:
                    img = Image.open(in_mem_image_file)                          
                    img.save(filepath)
                cache.set('cache_key_upload', os.path.join(get_upload_url(), in_mem_image_file.name) ,60*15)
            return HttpResponse(json.dumps({'message': 'Upload complete!','url': os.path.join(get_upload_url(), in_mem_image_file.name)}))
        else:
            return HttpResponse(json.dumps({'message': 'invalid form!'}))
    else:
        form = UploadFileForm()
        #return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))
        return HttpResponse(json.dumps({'message': 'invalid form!'}))

def upload_status(request):
    #print "upload_status"
    if request.method == 'GET':
        if request.GET['key']:
            if cache.get(request.GET['key']):
                value = cache.get(request.GET['key'])
                return HttpResponse(json.dumps(value), content_type="application/json")
            else:
                #print "cache %s not found" % request.GET['key']
                return HttpResponse(json.dumps({'error':"No csrf value in cache"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'error':'No parameter key in GET request'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'error':'No GET request'}), content_type="application/json")