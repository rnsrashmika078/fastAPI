from fastapi import FastAPI  # Import the FastAPI class
app = FastAPI()  # Create a FastAPI application instance
@app.get("/welcome")  # Define a GET endpoint at /welcome
def index():  # Function that runs when /welcome is requested
    return {
        "data": {" name ": "fast api"}
    }  # Response sent to the client as JSON (FastAPI converts the Python dict to JSON)


