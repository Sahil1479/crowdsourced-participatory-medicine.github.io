from django.contrib import admin
from .models import Queries, CovidExperience, QueryReply, Symtoms


@admin.register(QueryReply)
class QueryReplyAdmin(admin.ModelAdmin):
    list_display = ['pk', ]
    
    class Meta:
        model = QueryReply
        fields = '__all__'


@admin.register(Queries)
class QueriesAdmin(admin.ModelAdmin):
    list_display = ['subject', 'name', 'email', ]
    search_fields = ['name', 'email', 'subject', ]

    class Meta:
        model = Queries
        fields = '__all__'


@admin.register(CovidExperience)
class CovidExperienceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'islongcovid',]
    list_filter = ('islongcovid',)

    class Meta:
        model = CovidExperience
        fields = '__all__'


@admin.register(Symtoms)
class SymtomsAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', ]
    search_fields = ['name', ]

    class Meta:
        model = Symtoms
        fields = '__all__'
