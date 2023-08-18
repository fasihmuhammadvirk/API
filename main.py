#importing the FastAPI to create apis and status to check their status and HTTPException to handle exception 
from fastapi import FastAPI, status, HTTPException
#to return the list type 
from typing import List
from fastapi.middleware.cors import CORSMiddleware

#creating the app for making apis 
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# starting
@app.get('/')
def greet():
    return{'Message':'Hello User'}


lst = [[1,2],[4,4],[5,5],[6,7],[7,8],[8,9],[9,10]]



# creating the get response to get all the data from the database
@app.get("/items", response_model=List,status_code= status.HTTP_200_OK)
def get_all_items():
    return lst
