import json
import os
import unittest
from wsgiref import headers
from app import create_app
from models import setup_db
from flask_sqlalchemy import SQLAlchemy

class CapstoneTestCase(unittest.TestCase):
    executive_produce_token = os.getenv('EXECUTIVE_PRODUCE_TOKEN')
    def setUp(self, executive_produce_token = executive_produce_token) :
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        if self.database_path.startswith("postgres://"):
            self.database_path = self.database_path.replace("postgres://", "postgresql://", 1)
        setup_db(self.app, self.database_path)
        self.headers = {'Authorization': executive_produce_token}
        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
        
        self.new_actor = {"name": "name 01", "age": 20, "gender": True}    
        self.new_movie = {"title": "title 01", "release_date": "06/09/2022"}
          
    def tearDown(self):
        pass   
    
    # actors handling
    
    def test_get_actors_successfully(self):
        res = self.client().get("/actors")    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])
    
    def test_get_actors_unsuccessfully(self):
        res = self.client().get("/actors/10", headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")    

    def test_get_actors_detail_successfully(self):
        res = self.client().get("/actors-detail/1", headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])
    
    def test_get_actors_detail_unsuccessfully(self):
        res = self.client().get("/actors-detail/1000", headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "not found")       

    def test_post_actors_successfully(self):
        res = self.client().post("/actors", json=self.new_actor, headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])
    
    def test_post_actors_unsuccessfully(self):
        res = self.client().post("/actors/10", json=self.new_actor, headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")   
    
    def test_patch_actors_successfully(self):
        res = self.client().patch("/actors/1", json=self.new_actor, headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])
    
    def test_patch_actors_unsuccessfully(self):
        res = self.client().patch("/actors/100", json=self.new_actor, headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "not found")
             
    def test_delete_actors_successfully(self):
        res = self.client().delete("/actors/3", headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["delete"], 3)  
    
    def test_delete_actors_unsuccessfully(self):
        res = self.client().delete("/actors/10000", headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")  
        
    # movies handling       
    
    def test_get_movies_successfully(self):
        res = self.client().get("/movies")    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])
    
    def test_get_movies_unsuccessfully(self):
        res = self.client().get("/movies/10", headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")    

    def test_get_movies_detail_successfully(self):
        res = self.client().get("/movies-detail/3", headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])
    
    def test_get_movies_detail_unsuccessfully(self):
        res = self.client().get("/movies-detail/1000", headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "not found")       

    def test_post_movies_successfully(self):
        res = self.client().post("/movies", json=self.new_movie, headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])
    
    def test_post_movies_unsuccessfully(self):
        res = self.client().post("/movies/10", json=self.new_movie, headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")   
    
    def test_patch_movies_successfully(self):
        res = self.client().patch("/movies/3", json=self.new_movie, headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])
    
    def test_patch_movies_unsuccessfully(self):
        res = self.client().patch("/movies/100", json=self.new_movie, headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "not found")
             
    def test_delete_movies_successfully(self):
        res = self.client().delete("/movies/1", headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["delete"], 1)  
    
    def test_delete_movies_unsuccessfully(self):
        res = self.client().delete("/movies/10000", headers=self.headers)    
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable") 
if __name__ == '__main__':
    unittest.main() 