from django.shortcuts import redirect, render, get_object_or_404, render_to_response
from .forms import queryForm
from .models import query
from django.contrib import messages
import webbrowser as wb
from google import search


# Create your views here.


def home(request):
    if request.method == "POST":
        form = queryForm(request.POST)
        if form.is_valid():
            new_ques = form.save(commit=False)
            new_ques.save()
            return redirect('result', pk=new_ques.pk)
    else:
        form = queryForm
        return render(request, 'quora/home.html', {'form': form})


def result(request, pk):
    qt = " "
    question = get_object_or_404(query, pk=pk)
    q = str(question)
    qt += q
    qt += 'Quora'
    for j in search(qt, tld="co.in", num=1, stop=1, pause=2):
        urll = j;
        wb.open_new_tab(urll)
    form =queryForm
    return render(request, 'quora/result.html', {})

