from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponse
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
        #context['form'] = form
        #context['search_term'] = searchWord
        #context['object_list'] = post_list

        return render(self.request, self.template_name, context)

#    def download_pdf(self, certi):
#
#        print('--download log--')

#def certi_print(reauest, result_id):
#    print("--test print log--")
#    poll = result.objects.get(pk = id)
#    selection = request.POST['certi']
#
#    return HttpResponse("finish")


## result url, views, html ; certi_print 문제


# post_serach.html
#<div class="click_bt" style="margin: 10px">
#    <a href="{% url 'download_pdf' %}">출력하기</a></div>


#<form action = "." method="post"> {% csrf_token %}
#    <button name="certi" value="{{df.id}}">
#        <a href = {% url 'download_pdf' %}">출력하기</a></button>
#</form>
