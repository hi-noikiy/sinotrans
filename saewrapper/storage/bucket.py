from sae import storage

class SAEBucket(object):
    conn = None
    def __init__(self, bucket_name='media'):
        if not SAEBucket.conn:
            SAEBucket.conn = storage.Connection()
        if not bucket_name:
            bucket_name = 'media'
        self.__bucket = SAEBucket.conn.get_bucket(bucket_name)

    def put_object(self, name, content): 
        self.__bucket.put_object(name, content)
        return name

    def delete(self, name): 
        self.__bucket.delete_object(name)
        
    def url(self, name):  
        return self.__bucket.generate_url(name)     