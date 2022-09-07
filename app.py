import json
import os
import sys
from flask import (Flask, jsonify, abort, request)
from auth import requires_auth
from models import Actor, Movie, setup_db
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': 
            greeting = greeting + "!!!!! You are doing great in this Udacity project."
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"
    
    # actors handling
    
    @app.route('/actors')
    def get_actors():
        selection = Actor.query.order_by(Actor.id).all()
        actors = [actor.format() for actor in selection]
        if len(actors) == 0:
            abort(404)
        
        return jsonify({
            "success": True,
            "actors": actors
        })
    
    @app.route('/actors-detail/<int:actor_id>')
    @requires_auth('get:actors-detail')
    def get_actors_detail(self, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        
        return jsonify({
            "success": True,
            "actor": Actor.format(actor)
        })        
    
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def new_actors(self):
        body = request.get_json()
        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')
        actor = Actor(name=new_name, age=new_age, gender=new_gender)
        if actor is None:
            abort(404)
        actor.insert()
        
        return jsonify({
            "success": True,
            "actor": actor.format()
        })
    
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actors(self, actor_id):
        body = request.get_json()
        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        
        actor.name = new_name
        actor.age = new_age
        actor.gender = new_gender
        actor.update()
        
        return jsonify({
            "success": True,
            "actor": actor.format()
        })   
    
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(self, actor_id):
        try:
            if actor_id is None:
                abort(404)
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
            if actor is None:
                abort(404)  
            
            actor.delete()
            
            return jsonify({
            "success": True,
            "delete": actor_id
            })    
        except:    
            print(sys.exc_info())
            abort(422)         
        
    # movies handling
    
    @app.route('/movies')
    def get_movies():
        selection = Movie.query.order_by(Movie.id).all()
        movies = [movie.format() for movie in selection]
        if len(movies) == 0:
            abort(404)
        
        return jsonify({
            "success": True,
            "movies": movies
        })
    
    @app.route('/movies-detail/<int:movie_id>')
    @requires_auth('get:movies-detail')
    def get_movies_detail(self, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        
        return jsonify({
            "success": True,
            "movie": Movie.format(movie)
        })    
    
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def new_movies(self):
        body = request.get_json()
        new_title = body.get('title')
        new_release_date = body.get('release_date')
        movie = Movie(title=new_title, release_date=new_release_date)
        if movie is None:
            abort(404)
        movie.insert()
        
        return jsonify({
            "success": True,
            "movie": movie.format()
        })
    
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movies(self, movie_id):
        body = request.get_json()
        new_title = body.get('title')
        new_release_date = body.get('release_date')
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        
        movie.title = new_title
        movie.release_date = new_release_date
        movie.update()
        
        return jsonify({
            "success": True,
            "movie": movie.format()
        })    
     
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(self, movie_id):
        try:
            if movie_id is None:
                abort(404)
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            if movie is None:
                abort(404)  
            
            movie.delete()
            
            return jsonify({
            "success": True,
            "delete": movie_id
            })    
        except:    
            print(sys.exc_info())
            abort(422)
        
    # Error Handling
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "not found"
        }), 404    
        
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405 
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422        

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
