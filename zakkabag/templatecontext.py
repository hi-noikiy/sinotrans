def lang_context_processor(request):    
    
    return {'LANG': request.LANGUAGE_CODE}