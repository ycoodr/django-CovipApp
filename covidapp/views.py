from django.shortcuts import render

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Key": "fadea049ddmsh166e1e67d36ad17p1bc9e1jsn3250f26f3d5a",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()



# Create your views here.

def helloworldview(request):
    if request.method == 'POST':
        selectedcountry = request.POST['selectedcountry']
        print(selectedcountry) 
    noofresults = int(response['results'])
    mylist = []

    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    context = { 'mylist' : mylist}
    return render(request, 'helloworld.html', context)