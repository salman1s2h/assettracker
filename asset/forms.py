from django import forms
from .models import AssetCatg,AssetManage,Image


class AsstCatgForm(forms.ModelForm):

    class Meta:
        model = AssetCatg
        fields = ['asset_cat','asset_discription']


class AssetManageForm(forms.ModelForm):

    class Meta :
        model = AssetManage
        fields = ['asset_name','asset_catg','is_active']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','main_model']

