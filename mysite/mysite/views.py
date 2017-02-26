from django.http import HttpResponse
from books.models import Book
from django.shortcuts import render_to_response

def hello(requets):
#    msg="you are requets"
    ua = requets.META['HTTP_USER_AGENT']
    page= requets.path
    rip= requets.META['REMOTE_ADDR']
    values=requets.META.items()
    values.sort()
    html=[]
    for k,v in values:
        html.append('<str><td>%s</td><td>%s</td></str>' % (k, v))
   # return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return HttpResponse(html)
#    return HttpResponse("you request path is %r; you come from %r; your agent is %s!" %(page,rip,ua))

def get_blogs(request):
    pass

def search_form(request):
    # if 'q' in request.GET:
    #     message = 'you searched for: %r' %request.GET['q']
    # else:
    #     message= 'you submitted an empty form.'
    # return HttpResponse(message)
    return render_to_response('search_form.html')

def search(request):
    error = False
    if 'q' in request.GET['q']:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title_icontains=q)
            return render_to_response('search_result.html',
                                      { 'books':books,'query': q })

    return render_to_response('search_form.html',
                               { 'error': error })
 #       return HttpResponse('please submit a search term.')