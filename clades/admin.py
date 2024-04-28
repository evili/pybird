from clades.models import Kingdom, Phylum, Classe, Order, Family, Genus, Species, CommonName
from clades.filters import CladisticFilter
from django.contrib import admin

class PhylumInline(admin.TabularInline):
    model = Phylum

class ClasseInline(admin.TabularInline):
    model = Classe

class OrderInline(admin.TabularInline):
    model = Order

class FamilyInline(admin.TabularInline):
    model = Family

class GenusInline(admin.TabularInline):
    model = Genus

class SpeciesInline(admin.TabularInline):
    model = Species

class CommonNameInline(admin.TabularInline):
    model = CommonName

class BasicAdmin(admin.ModelAdmin):
    pass

class KingdomAdmin(BasicAdmin):
    inlines = [PhylumInline]

class PhylumAdmin(BasicAdmin):
    inlines = [ClasseInline]
    list_filter = ['kingdom']
    
class ClasseAdmin(BasicAdmin):
    inlines = [OrderInline]
    list_filter = ['phylum', 'phylum__kingdom']

class OrderAdmin(BasicAdmin):
    inlines = [FamilyInline]
    list_filter = ['classe','classe__phylum']

class FamilyAdmin(BasicAdmin):
    inlines = [GenusInline]
    list_filter = ['order','order__classe']

class GenusAdmin(BasicAdmin):
    inlines = [SpeciesInline]
    list_filter = ['family', 'family__order']

class SpeciesAdmin(BasicAdmin):
    inlines = [CommonNameInline]
    list_filter = (CladisticFilter,)
#    list_filter = [
#                   'genus',
#                   'genus__family',
#                   'genus__family__order',
#                   'genus__family__order__classe',
#                   'genus__family__order__classe__phylum',
#                   'genus__family__order__classe__phylum__kingdom',
#                   ]

admin.site.register(Kingdom,    KingdomAdmin)
admin.site.register(Phylum,     PhylumAdmin)
admin.site.register(Classe,     ClasseAdmin)
admin.site.register(Order,      OrderAdmin)
admin.site.register(Family,     FamilyAdmin)
admin.site.register(Genus,      GenusAdmin)
admin.site.register(Species,    SpeciesAdmin)
admin.site.register(CommonName)
