from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Scope, Article, Topic


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        checked = 0
        
        for form in self.forms:

            if form.cleaned_data.get('DELETE', False):
                continue
                
            if form.cleaned_data.get('is_main', False):
                checked += 1
                
        if checked > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif checked == 0:
            raise ValidationError('Укажите основной раздел')
            
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    

@admin.register(Topic)
class ScopesAdmin(admin.ModelAdmin):
    pass