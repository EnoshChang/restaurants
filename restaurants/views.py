from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Restaurant, Food

def menu(request):
    r = Restaurant.objects.get(id=2)

    return render(request, 'menu.html', locals())

def index(request):
    return render(request, 'index.html')

def taiwan_rest(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants.html', locals())

def new_restaurant(request):
    if request.method == 'GET':
        return render(request, 'new_restaurant.html')
    else:
        restaurant_name = request.POST['restaurant_name']
        restaurant_phone_number = request.POST['restaurant_phone_number']
        restaurant_address = request.POST['restaurant_address']
        Restaurant.objects.create(name = restaurant_name,
            phone_number = restaurant_phone_number,
            address = restaurant_address)

        return HttpResponseRedirect('/restaurants/')

def edit_restaurant(request, r_id):
    if request.method == 'GET':
        restaurants = Restaurant.objects.filter(id = r_id)
        if (len(restaurants) > 0):
            restaurant = restaurants[0]
            response = render(request, 'edit_restaurant.html', locals())
            response.set_cookie('restaurant_id', r_id)
            return response
        else:
            return HttpResponseRedirect('/restaurants/')
    else:
        restaurants = Restaurant.objects.filter(id = r_id)
        if (len(restaurants) > 0):
            restaurant = restaurants[0]
            restaurant.name = request.POST['restaurant_name']
            restaurant.phone_number = request.POST['restaurant_phone_number']
            restaurant.address = request.POST['restaurant_address']
            restaurant.save()
        return HttpResponseRedirect('/restaurants/')

def del_restaurant(request, r_id):
    Restaurant.objects.filter(id = r_id).delete()
    return HttpResponseRedirect('/restaurants/')

def foods(request, r_id):
    restaurants = Restaurant.objects.filter(id = r_id)
    if (len(restaurants) > 0):
        restaurant = restaurants[0]
        return render(request, 'foods.html', locals())
    else:
        return HttpResponseRedirect('/restaurants')

def new_food(request, r_id):
    if request.method == 'GET':
        restaurant_id = r_id
        return render(request, 'new_food.html', locals())
    else:
        food_name = request.POST['food_name']
        food_price = request.POST['food_price']
        food_comment = request.POST['food_comment']
        food_is_spicy = request.POST['food_is_spicy']
        restaurant = Restaurant.objects.get(id = r_id)
        Food.objects.create(name = food_name,
            price = food_price,
            comment = food_comment,
            is_spicy = food_is_spicy,
            restaurant = restaurant)

        return HttpResponseRedirect(f'/restaurant/{r_id}/foods/')

def edit_food(request, r_id, f_id):
    if request.method == 'GET':
        foods = Food.objects.filter(id = f_id)
        if (len(foods) > 0):
            food = foods[0]
            restaurant_id = r_id
            return render(request, 'edit_food.html', locals())
        else:
            return HttpResponseRedirect(f'/restaurant/{r_id}/foods/')
    else:
        foods = Food.objects.filter(id = f_id)
        if (len(foods) > 0):
            food = foods[0]
            food.name = request.POST['food_name']
            food.price = request.POST['food_price']
            food.comment = request.POST['food_comment']
            food.is_spicy = request.POST['food_is_spicy']
            food.save()
        return HttpResponseRedirect(f'/restaurant/{r_id}/foods/')

def del_food(request, r_id, f_id):
    Food.objects.filter(id = f_id).delete()
    return HttpResponseRedirect(f'/restaurant/{r_id}/foods/')        