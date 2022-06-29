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
    noofresults = int(response['results'])
    mylist = []
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])

         
    
        
    
    if request.method == 'POST':
        selectedcountry = request.POST['selectedcountry']
        
        for x in range(0, noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        
        context = { 
          'selectedcountry': selectedcountry,
          'new' : new,
          'active': active,
          'critical': critical, 
          'recovered': recovered,
          'deaths' : deaths,
          'total': total,
          'mylist': mylist
          }
        return render(request, 'helloworld.html', context)
    
    
    context = { 'mylist' : mylist}
    return render(request, 'helloworld.html', context)