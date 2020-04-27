from django.shortcuts import render,redirect
from .models import User,Movie
from django.contrib import messages
import bcrypt
import requests, json

def index_login(request):

    return render(request,'login.html')

def create_user(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            print("User's password entered was " + request.POST['password'])
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode() 
            user = User.objects.create(name=request.POST['name'],email=request.POST['email'], password=hashed_pw, date=request.POST['date'])
            print("User's password has been changed to " + user.password)
            
    return redirect('/')

def login(request):
    if request.method == "POST":
        users_with_name = User.objects.filter(email=request.POST['email'])
        if users_with_name:
            user = users_with_name[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):#This is checking if password are equal to the creation password
                request.session['user_id'] = user.id #IMPORTANT!!! this is how we know this user id is logged in
                return redirect('/planair')
            else:
                print("Password didn't match")
                messages.error(request, "Incorrect name or password")
        else:
            print("Name not found")
            messages.error(request, "Incorrect name or password")
    return redirect('/homepage')

def homepage(request):
    if 'user_id'  in request.session :
        apikey = "58beb94f"
        ids = ['tt0944835','tt0848228','tt3076658','tt1502397','tt6450804','tt0120802','tt0328107','tt0118799','tt0069197','tt7975244','tt1067224','tt7286456','tt2024469','tt1895587']
        movies = []
        for id in ids:
            r = requests.get("http://www.omdbapi.com/?apikey="+apikey+"&i="+id+"")
            r = json.loads(r.text)
            info = {
                'title': r['Title'],
                'year': r['Year'],
                'image': r['Poster'],
                'id': r['imdbID'],
            }
            movies.append(info)
        favorite_ids = []
        user = User.objects.get(id=request.session['user_id'])
        for movie in user.movies.all():
            favorite_ids.append(movie.favorite_id)

        context = {
            'user' : User.objects.get(id=request.session['user_id']),
            'api_movies': movies,
            'favorite_movies': favorite_ids
        }
        return render(request, 'homepage.html' , context)
    else:
        return redirect('/')
    
def add_favorite(request):
    if 'user_id' in request.session:
        Movie.objects.create(
            favorite_id = request.POST['movie_id'],
            user = User.objects.get(id=request.session['user_id'])
        )
        return redirect('/homepage')
    else:
        return redirect('/')

def remove_favorite(request):
    if 'user_id' in request.session:
        movie = Movie.objects.filter(favorite_id=request.POST['movie_id'], user=User.objects.get(id=request.session['user_id']))
        if len(movie) > 0:
            movie.delete()
            return redirect('/favorites')

        else:
            return redirect('/favorites')
    else:
        return redirect('/login')
    

def delete_session(request):
    request.session.clear()
    return redirect('/')

def view_favs(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        favs = []
        apikey = "58beb94f"
        for movie in user.movies.all():
            r = requests.get("http://www.omdbapi.com/?apikey="+apikey+"&i="+movie.favorite_id+"")
            r = json.loads(r.text)
            info = {
                'title': r['Title'],
                'year': r['Year'],
                'image': r['Poster'],
                'id': r['imdbID'],
            }
            favs.append(info)
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "favorites": favs
        }
        return render(request, "favorites.html", context)

    return redirect("/")
    
def remove_favorite_homepage(request):
    if 'user_id' in request.session:
        movie = Movie.objects.filter(favorite_id=request.POST['movie_id'], user=User.objects.get(id=request.session['user_id']))
        if len(movie) > 0:
            movie.delete()
            return redirect('/homepage')

        else:
            return redirect('/homepage')
    else:
        return redirect('/login')

def new_release(request):
    if 'user_id' in request.session:
        apikey = "58beb94f"
        ids = ['tt0944835','tt0848228','tt3076658','tt1502397','tt6450804','tt0120802','tt0328107','tt0118799','tt0069197','tt7975244','tt1067224','tt7286456','tt2024469','tt1895587']
        movies = []
        for id in ids:
            r = requests.get("http://www.omdbapi.com/?apikey="+apikey+"&i="+id+"")
            r = json.loads(r.text)
            info = {
                'title': r['Title'],
                'year': r['Year'],
                'image': r['Poster'],
                'id': r['imdbID'],
            }
            movies.append(info)
        favorite_ids = []
        user = User.objects.get(id=request.session['user_id'])
        for movie in user.movies.all():
            favorite_ids.append(movie.favorite_id)

        context = {
            'user' : User.objects.get(id=request.session['user_id']),
            'api_movies': movies,
            'favorite_movies': favorite_ids
        }
        
        return render(request, 'new_release.html',context)
    else:
        return redirect('/')

def action(request):
    if 'user_id' in request.session:
        apikey = "58beb94f"
        ids = ['tt0944835','tt0848228','tt3076658','tt1502397','tt6450804','tt0120802','tt0328107','tt0118799','tt0069197','tt7975244','tt1067224','tt7286456','tt2024469','tt1895587']
        movies = []
        for id in ids:
            r = requests.get("http://www.omdbapi.com/?apikey="+apikey+"&i="+id+"")
            r = json.loads(r.text)
            info = {
                'title': r['Title'],
                'year': r['Year'],
                'image': r['Poster'],
                'id': r['imdbID'],
                'genre': r['Genre'],
            }
            movies.append(info)
        favorite_ids = []
        user = User.objects.get(id=request.session['user_id'])
        for movie in user.movies.all():
            favorite_ids.append(movie.favorite_id)

        context = {
            'user' : User.objects.get(id=request.session['user_id']),
            'api_movies': movies,
            'favorite_movies': favorite_ids
        }
        return render(request, 'action.html', context)
    else:
        return redirect('/')

def drama(request):
    if 'user_id' in request.session:
        apikey = "58beb94f"
        ids = ['tt0944835','tt0848228','tt3076658','tt1502397','tt6450804','tt0120802','tt0328107','tt0118799','tt0069197','tt7975244','tt1067224','tt7286456','tt2024469','tt1895587']
        movies = []
        for id in ids:
            r = requests.get("http://www.omdbapi.com/?apikey="+apikey+"&i="+id+"")
            r = json.loads(r.text)
            info = {
                'title': r['Title'],
                'year': r['Year'],
                'image': r['Poster'],
                'id': r['imdbID'],
                'genre': r['Genre'],
            }
            movies.append(info)
        favorite_ids = []
        user = User.objects.get(id=request.session['user_id'])
        for movie in user.movies.all():
            favorite_ids.append(movie.favorite_id)

        context = {
            'user' : User.objects.get(id=request.session['user_id']),
            'api_movies': movies,
            'favorite_movies': favorite_ids
        }
        return render(request, 'drama.html', context)
    else:
        return redirect('/')

def comedy(request):
    if 'user_id' in request.session:
        apikey = "58beb94f"
        ids = ['tt0944835','tt0848228','tt3076658','tt1502397','tt6450804','tt0120802','tt0328107','tt0118799','tt0069197','tt7975244','tt1067224','tt7286456','tt2024469','tt1895587']
        movies = []
        for id in ids:
            r = requests.get("http://www.omdbapi.com/?apikey="+apikey+"&i="+id+"")
            r = json.loads(r.text)
            info = {
                'title': r['Title'],
                'year': r['Year'],
                'image': r['Poster'],
                'id': r['imdbID'],
                'genre': r['Genre'],
            }
            movies.append(info)
        favorite_ids = []
        user = User.objects.get(id=request.session['user_id'])
        for movie in user.movies.all():
            favorite_ids.append(movie.favorite_id)

        context = {
            'user' : User.objects.get(id=request.session['user_id']),
            'api_movies': movies,
            'favorite_movies': favorite_ids
        }
        return render(request, 'comedy.html', context)
    else:
        return redirect('/')


def planair(request):
    if 'user_id' in request.session:

        return render(request,'planair.html')

def register(request):
        
        return render(request, 'register.html')