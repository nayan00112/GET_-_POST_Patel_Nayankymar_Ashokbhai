from django.shortcuts import render
import requests

# Create your views here.
def home(request):

    url = 'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=gprKtWCe1IxmB3xvzf7xts4V3t7yrGTK'
    datas = requests.get(url)
    d = datas.json()
    
    data = d['results']
    data = data['books']
    return render(request, 'index.html', {'data':data})