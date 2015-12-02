from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .forms import ProductUploadForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.http import HttpResponse
import json
from .models import *
from .forms import ProductUploadForm, BidPostForm, SearchProductForm
from django.core import serializers
# Create your views here.
#@require_http_methods(["GET", "POST"])
@require_POST
@login_required
def uploadProduct(request):
        form = ProductUploadForm(request.POST, request.FILES)
        if (form.is_valid()):
            product = form.save(commit= False);
            product.By = request.user
            product.save();
            return JsonResponse(data= {'id' : product.BidStart, 'name' : product.Title })
        else:
            return JsonResponse(status = 400, data = { 'errors' : dict(form.errors.items())})

@require_POST
#@require_http_methods(['GET', 'POST'])
@login_required
def postBid(request, id):
        print('hey')
        form = BidPostForm(request.POST)
        if(form.is_valid()):
          print('hey')
          bid = form.save(commit = False)
          bid.By = request.user
          ret = get_object_or_404(Product, id = id)
          bid.Item = ret
          ret.BidPrice = bid.BidPrice
          ret.save();
          #bid.Item = get_object_or_404(Product, id = id)
          bid.save();
          return JsonResponse(data= {'id' : bid.BidPrice, 'by' : request.user.id})
        else:
          return JsonResponse(status = 400, data = { 'errors' : dict(form.errors.items())})

@require_GET
def productBidded(request, id):
    item = get_object_or_404(Product, id = id)
    obj = serializers.serialize('json',[item,])
    return JsonResponse(data= {'item' : obj})



@require_GET
def viewProduct(request, id):
    item = get_object_or_404(Product, id = id)  
    return render(request, 'product/product_view.html',{'item':item})


@require_GET
@login_required
def product_list(request):
    products = Product.objects.all()
    context = { 'courses' : products }
    #context['form5'] = SearchProductForm
    if request.user.is_superuser or request.user.is_admin:
      context['form'] = ProductUploadForm();
    return render(request, 'product/product_upload.html', context)



#@login_required
#@require_GET
#def bid_list(request):
#    products = Product.objects.all()
#    context = { 'courses' : products }
#    if request.user.is_superuser or request.user.is_admin:
#      context['form'] = ProductUploadForm();
#    return render(request, 'product/product_upload.html', context)


@require_GET
def time_over(request, id):
    bids = Bid.objects.filter(Item_id = id).order_by('-BidPrice')
    winner = bids[1]
    return JsonResponse(data= {'winner': winner.By.first_name} )  


@require_GET
def search_product(request):
    name = request.GET.get('name')
    data = []
    if name:
        products = Product.objects.filter(Title__icontains == name)
        data = [{'id': item.id, 'title' : item.Title } for item in products ]
    return JsonResponse(data = { 'item' : data })

@require_GET
def category_search(request, id):
    products = Product.objects.filter(Category = id)
    f = ProductUploadForm()
    form1 = BidPostForm();
    data = { 'items': products, 'form' : f, 'form1': form1  }
    return render( request,'product/product_upload_category.html', data)

@require_GET
def all_products(request):
    return render(request, 'product/product_all.html')

@require_GET
def bid_show(request, id):
    bids = Bid.objects.filter(Item_id = id)
    item = get_object_or_404(Product, id = id)
    name = item.Title
    #by_id = item.By
    #user = get_object_or_404(Myuser, id = by_id)
    data = { 'bids' : bids, 'name' : name }
    return render( request, 'product/product_bid.html',data)


@require_GET
@login_required
def follow(request, id):
    follower = request.user
    item = get_object_or_404(Product, id = id)
    response_data = {'result': 0}
    if follower not in item.Followedby.all():
        item.Followedby.add(follower)
        response_data['result'] = 1
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_data['error']  = 'You are already following the product'
        return HttpResponse(json.dumps(response_data), content_type="application/json")


@require_GET
@login_required
def unfollow(request, id):
    follower = request.user
    item = get_object_or_404(Product, id = id)
    response_data = {'result': 0}
    if follower in item.Followedby.all():
        item.Followedby.remove(follower)
        response_data['result'] = 1
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_data['error']  = 'You are not following the product'
        return HttpResponse(json.dumps(response_data), content_type="application/json")


@require_GET
def showfollowing(request):
    follower = request.user
    followerid = follower.id
    items = Product.objects.filter(Followedby__id = followerid)
    print(items)
    data = { 'items' : items }
    return render( request, 'product/product_followed.html',data)
