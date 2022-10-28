from django.shortcuts import render
import json
def home(request):
    
    if request.method == "GET":
        return render(request,"index.html") 
    
    if request.method == "POST":
        if 'search' in request.POST:
            option = request.POST['options']
            search_by = request.POST.get("search_by")
            search_value = request.POST.get("search_value")
            if search_by == "_id" and option != "tickets":
                try:
                    search_value = int(search_value)
                except: 
                    context = {
                            "message": "Id must be in integer"
                            }
                    return render(request,"index.html", context) 
                

            jdata = json.loads(open(f'app/static/{option}.json').read())
                
            for data in jdata:
                if  search_value in data.values() and search_by in data.keys():
                    if data[search_by] == search_value:
                        context = {
                            "value" : zip(data.keys(), data.values()),
                            "message" : 'successful',
                            "status_code" : 200,
                            "Result": "Result:"
                            }
                        break
                else:
                    context = {
                            "key": "Key",
                            "Result": "Result:",
                            "value" : "data not found!",
                            "message" : 'unsuccessful',
                            "status_code" : 200 
                            }
            return render(request,"index.html", context) 
        
        elif 'list' in request.POST:

            user = json.loads(open('app/static/users.json').read())
            ticket = json.loads(open('app/static/tickets.json').read())
            org = json.loads(open('app/static/organizations.json').read())
  
            tickets = ticket[0].keys()
            user = user[0].keys()
            org = org[0].keys()
            context = {"users": user, "tickets": tickets, "org": org, "name1": "Users", "name2": "Tickets", "name3": "Organizations"}
        return render(request,"index.html", context) 


# Create your views here.
