from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal,User 
from fastapi import HTTPException

def ged_db():
    """
    Dependency function to get a database session.
    This function is used to inject the database session into FastAPI endpoints.
    """
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session for use in the endpoint
    finally:
        db.close()  # Close the session after use


# Create a FastAPI application instance
app = FastAPI()

# Defining an endpoint for users
@app.get("/users/")
def read_users(db: Session = Depends(ged_db)):
    """
    Endpoint to read users from the database.
    This function uses dependency injection to get a database session.
    """
    # Here you would typically query the database for users
    # For now, we will return a placeholder response
    users = db.query(User).all()
    return users
# This approach allows us to manage database connections efficiently and ensures that each request has its own session.
# The above code sets up a FastAPI application with a database session dependency.
# The `ged_db` function is used to create and manage the database session for each request.
# The `read_users` endpoint demonstrates how to use this session to query the database.
# The code is structured to allow for easy expansion with additional endpoints and database operations.

# Defining a Request Model for User Data
from pydantic import BaseModel
class UserCreate(BaseModel):
    """
    Request model for creating a new user.
    This model defines the structure of the data required to create a user.
    """
    name: str
    email: str
# Defining an endpoint for creating a user

@app.post("/user/")
def create_user(user: UserCreate, db: Session = Depends(ged_db)):
    """
    Endpoint to create a new user in the database.
    This function uses dependency injection to get a database session.
    """
    # Create a new User instance
    print("Creating a new user:", user)
    print("User name:", user.name)
    print("User email:", user.email)
    new_user = User(name=user.name, email=user.email)
    
    # Add the new user to the session
    db.add(new_user)
    
    # Commit the session to save the user to the database
    db.commit()
    
    # Refresh the instance to get the updated data from the database
    db.refresh(new_user)
    
    return new_user

# Defining an endpoint to read a specific user by ID
@app.get("/user/{user_id}")
def read_user(user_id: int, db: Session = Depends(ged_db)):
    """
    Endpoint to read a specific user by ID from the database.
    This function uses dependency injection to get a database session.
    """
    # Query the database for the user with the specified ID
    user = db.query(User).filter(User.id == user_id).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
        return {"error": "User not found"}
    
    return user

# Defining an endpoint to update a user
@app.put("/user/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(ged_db)):
    """
    Endpoint to update an existing user in the database.
    This function uses dependency injection to get a database session.
    """
    # Query the database for the user with the specified ID
    existing_user = db.query(User).filter(User.id == user_id).first()
    
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update the user's data
    existing_user.name = user.name
    existing_user.email = user.email
    
    # Commit the changes to the database
    db.commit()
    
    # Refresh the instance to get the updated data from the database
    db.refresh(existing_user)
    
    return existing_user

# Defining an endpoint to delete a user
@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(ged_db)):
    """
    Endpoint to delete a user from the database.
    This function uses dependency injection to get a database session.
    """
    # Query the database for the user with the specified ID
    user = db.query(User).filter(User.id == user_id).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete the user from the session
    db.delete(user)
    
    # Commit the changes to the database
    db.commit()
    
    return {"detail": "User deleted successfully"}