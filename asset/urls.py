from django.urls import path
from .views import (create_asset_cat,list_asset_cat,list_asset_manage,retrive_asset_manage,generate_csv,add_image_asset,
                   pie_chart,retrive_asset_catg,delete_asst_cat,create_asset_manage,delete_asst_mang_new,bar_chart_view)
app_name ="asset"

urlpatterns = [
    path('asset-catg/',create_asset_cat, name='asst_catg'),
    path('list-asset-cat/',list_asset_cat,name='lst_ast_catg'),
    path('assest-type-details/<int:pk>/', retrive_asset_catg, name='record_details'),
    path('delete/<int:pk>/', delete_asst_cat, name='delete_asst_cat'),
    path('asset-manage/',create_asset_manage, name='asst_manage'),
    path('list-asset-manage/',list_asset_manage,name='lst_ast_manage'),
    path('assest-manage-details/<int:pk>/', retrive_asset_manage, name='record_manage_details'),
    # path('delete/<int:pk>/', delete_asst_mang, name='delete_asst_mang'),
    path('generate-csv/', generate_csv, name='generate_csv'),
    path('pie-chart/', pie_chart, name='pie_chart'),
    path('bar-chart/', bar_chart_view, name='bar-chart'),
    path('delete-new/<int:pk>/', delete_asst_mang_new, name='delete_asst_mang_new'),
    path('asset-images/',add_image_asset,name='add_images')

]