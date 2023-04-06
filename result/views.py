from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from result.models import result
from django.db.models import Q
import pandas as pd
from .forms import PostSearchForm

# Create your views here.
class SearchFormView(FormView):
    print("---------SearchFormview log")
    form_class = PostSearchForm
    template_name = 'main/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = result.objects.filter(Q(name__icontains=searchWord)).values()
        data = pd.DataFrame(post_list)
        context = {'df': data.to_html(justify='center')}
        print(data.columns)
        #context['form'] = form
        #context['search_term'] = searchWord
        #context['object_list'] = post_list

        return render(self.request, self.template_name, context)

