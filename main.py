# FastAPI is a Python library that 
# allows us to 
# - take in a request (typically sent from the client)
# - send back a response
from fastapi import FastAPI

# CORS (Cross-Origin Resource Sharing)
# allows us to restrict/enable which
# client urls are allowed to call 
# this backend code. 
# CORS is part of the FastAPI library.
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI application
app = FastAPI(
    title="FastAPI Example",
    description="This is an example of using FastAPI"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # star means all client urls allowed 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Define default route
@app.get("/")           
def default_route():    
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."

# 2. Define the endpoint at the path /madlib/
# It accepts three query parameters: noun, adjective, and verb
@app.get("/madlib/")
def generate_madlib(noun, adjective, verb):
    """
    Generates a silly sentence using the provided words.    
    """
    
    # 3. Construct the sentence (the "Mad Lib") using an f-string
    sentence = (
        f"The {adjective} {noun} decided to {verb} "
        f"loudly in the park today, much to everyone's surprise!"
    )
    
    # 4. Return a JSON response containing the full sentence
    return {
        "title": "Your Generated Mad Lib",
        "adjective": adjective,
        "noun": noun,
        "verb": verb,
        "madlib_sentence": sentence
    }

# TO RUN:
# 1. Put this code in api/main.py and deploy to Vercel
# 2. Test by using your-vercel-backend-url/docs
# 3. Later call from front-end using JavaScript fetch()