# -*- coding: utf-8 -*-
__author__ = 'bhe001'


from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.conf import settings
import sae.storage
import re


class SAEStorage(Storage):
    def __init__(self, domain_name = ''): 
        if not domain_name:                  
            domain_name = settings.STORAGE_BUCKET_NAME
        self.__bucket = sae.storage.Bucket(domain_name) 

    def delete(self, name): 
        self.__bucket.delete_object(name)

    def exists(self, name): 
        try:
            self.__bucket.stat_object(name)
            return True
        except sae.storage.Error:
            return False
    def size(self, name):   
        try:
            stat = self.__bucket.stat_object(name)
        except sae.storage.Error:
            return -1
        return int(stat['bytes'])

    def url(self, name):  
        return self.__bucket.generate_url(name)

    def _open(self, name, mode = 'rb'): 
        try:
            return ContentFile(self.__bucket.get_object_contents(name))
        except:
            return None

    def _save(self, name, content): 
        self.__bucket.put_object(name, content)
        return name

    def listdir(self, path): 
        r = re.compile('^%s' % path)
        remove_prefix = lambda name: r.sub('', name)
        return [(remove_prefix(attr['name']), None) for attr inself.__bucket.list(path = path)]

