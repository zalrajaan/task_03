from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    'my_list': [
    	{
    	'restaurant_name': 'Stuffed',
    	'food_type':'Comfort Food',},
    	{'restaurant_name': 'Solo',
    	'food_type':'Pizza',},
    	{'restaurant_name': 'KFC',
    	'food_type':'Fried Chicken',

    	}
    	]
    	}

  
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { 
    'my_object':{
    	'restaurant_name': 'Stuffed',
    	'food_type':'Comfort Food'
    }

    }
    return render(request, 'detail.html', context)
