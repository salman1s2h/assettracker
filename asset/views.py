from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AssetCatg,AssetManage
from .forms import AsstCatgForm,AssetManageForm,ImageForm
from django.core.paginator import Paginator
import csv
from django.http import HttpResponse
from django.db.models import Count
from django.http import JsonResponse
from django.contrib import messages


## Bellow function are used for creating asset 
@login_required
def create_asset_cat(request):
    form = AsstCatgForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard:home_pi')
    else:
        err = form.errors
        messages.warning(request, err)
    
    return render(request, "assest/asset_type_create.html")


## Bellow function are used for datatable with paggination
@login_required
def list_asset_cat(request):
    paginator = Paginator(AssetCatg.objects.all(), 2)  # Show 2 objects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "assest/list_asset_cat_view.html", {'page_obj': page_obj})

## Bellow function are used for retrive and update the asset type
@login_required
def retrive_update_asset_type(request,pk):
    if pk: # it call while retrive
        instance = get_object_or_404(AssetCatg, pk=pk)
        update = True
    else:
        instance = None
        update = False

    if request.method == 'POST': # this is call when user click update button
        form = AsstCatgForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('dashboard:home_pi') 
    else:
        form = AsstCatgForm(instance=instance)
    return render(request, 'assest/asset_type_create.html', {'form': form, 'update': update,'obj_id':instance.id})

## delete  the ass
@login_required
def delete_asst_type(request,pk):

    obj = get_object_or_404(AssetCatg, pk=pk)
    if obj:
        obj.delete()
    return redirect('dashboard:home_pi')



## Bellow function is used for asset management
@login_required
def create_asset_manage(request):
    
    if request.method == 'POST':
        form = AssetManageForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('dashboard:home_pi')
    else:
        form = AssetManageForm()
        asset_type = AssetCatg.objects.all()
        return render(request, 'assest/asset_manage_create.html', {'form': form,'asset_type':asset_type})

## datatable for asset management 
@login_required
def list_asset_manage(request):

    paginator = Paginator(AssetManage.objects.all(), 4)  # Show 1 objects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "assest/list_asset_manage.html", {'page_obj': page_obj})

## bellow function for update and retrive data
@login_required
def retrive_update_asset_manage(request,pk):

    if pk: ## Called fro datatable
        instance = get_object_or_404(AssetManage, pk=pk)
        update = True
    else:
        instance = None
        update = False

    if request.method == 'POST': ## called while update
        form = AssetManageForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('dashboard:home_pi') 
    else:
        form = AssetManageForm(instance=instance)
        images = instance.images.all()
        asset_type = AssetCatg.objects.all()
    return render(request, 'assest/asset_manage_create.html', {'form':form ,'update': update,'asset_type':asset_type,'obj_id':instance,'images':images})



## deleting the asset management
@login_required
def delete_asst_mang_new(request,pk):
    obj = get_object_or_404(AssetManage, pk=pk)
    if obj:
        obj.delete()
    return redirect('dashboard:home_pi')


@login_required
def generate_csv(request):

    queryset = AssetManage.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="AssetData.csv"'
    writer = csv.writer(response)

    writer.writerow(['Name','Type','UUID Code','Is Active','Created Date','Updated Date'])

    for item in queryset:
        writer.writerow([item.asset_name,item.asset_catg,item.asset_code,item.is_active,item.created_on,item.updated_on ])

    return response

@login_required
def pie_chart(request):
    labels = []
    data = []

    queryset = AssetManage.objects.values('asset_catg__asset_cat').annotate(num=Count('id'))
    for categ in queryset:
        labels.append(categ['asset_catg__asset_cat'])
        data.append(categ['num'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

@login_required
def bar_chart_view(request):
    data_filter = {}
    queryset = AssetManage.objects.values('asset_catg__asset_cat', 'is_active') \
                                .annotate(num=Count('is_active')) \
                                .order_by('asset_catg__asset_cat', 'is_active')

    
    for row in queryset:
        data_filter[row['asset_catg__asset_cat']] = [0,0]
    
    for row in queryset:
        if row['is_active'] == True :
            data_filter[row['asset_catg__asset_cat']][0] = row['num']
        else:
            data_filter[row['asset_catg__asset_cat']][1] = row['num']
    
    categories = list(data_filter.keys())
    active_data = []
    inactive_data = []

    for type_as in categories:
        active_data.append(data_filter[type_as][0])
        inactive_data.append(data_filter[type_as][1])
    
    bar_data = {
        'labels': categories,
        'active_data': active_data,
        'inactive_data': inactive_data
    }
    return JsonResponse(bar_data)


@login_required
def add_image_asset(request):
    asset_data = AssetManage.objects.all()
    if request.method == 'POST':  
        form = ImageForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
  
            img_object = form.instance  
            return render(request, 'assest/image_add.html', {'form': form, 'img_obj': img_object,'asset':asset_data})  
    else:  
        form = ImageForm()

    return render(request, 'assest/image_add.html', {'form': form,'asset':asset_data})  