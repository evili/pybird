from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _
# from clades.models import Kingdom, Phylum, Classe, \
#        Order, Family, Genus, Species


class CladisticFilter(SimpleListFilter):
    title = _('Cladistic filter')
    parameter_name = 'clade_filter'
    hierarchy = ['Kingdom', 'Phylum', 'Classe', 'Order', 'Family',
                 'Genus', 'Species']

    def __init__(self, request, params, model, model_admin):
        super(CladisticFilter, self).__init__(
                request, params, model, model_admin
                )

        for h in CladisticFilter.hierarchy:
            if (globals()[h] == model):
                kls = h
                break
        l = CladisticFilter.hierarchy.index(kls)
        if l >= 1:
            self.hierarchy = CladisticFilter.hierarchy[0:l]
        else:
            self.hierarchy = [CladisticFilter.hierarchy[0]]

    def lookups(self, request, model_admin):
        level = request.session.get('level', default=0)
        clade_name = self.hierarchy[level]
        clade = globals()[clade_name]
        choices = clade.objects.all()
        if (level < len(self.hierarchy)):
            lkp = [(-2, _('by ')+self.hierarchy[level+1])]
        else:
            lkp = []

        for c in choices:
            lk = (c.id, c.name)
            lkp.append(lk)
        if level >= 1:
            lk = (-1, _('by')+self.hierarchy[level-1])
            lkp.append(())
        return lkp

    def queryset(self, request, queryset):
        level = request.session.get('level', default=0)
        qset = queryset

        if request.GET.has_key(self.parameter_name):
            flt = request.GET[self.parameter_name]
            if flt == -1:
                if level < len(self.hierarchy):
                    level += 1
                    request.session['level'] = level
            elif flt == -2:
                if level > 0:
                    level -= 1
                    request.session['level'] = level

            clade_name = self.hierarchy[level]
            clade = globals()[clade_name]
            atfields = self.hierarchy[level:]
            atfields.reverse()
            attr = '__'.join(atfields).lower()
            if flt >= 0:
                c = clade.objects.get(pk=flt)
                kwargs = {attr: c}
                qset = queryset.filter(**kwargs)
            else:
                qset = queryset

        return qset
