from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def count(request, count):
    response_message = ''
    if count == 'first':
        response_message = 'This is first message.'
    elif count == 'second':
        response_message = 'This is second message.'
    else:
    	return HttpResponseNotFound("This is not supported count")
    
    return HttpResponse(response_message)
