from database import user_collection
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from bson import ObjectId

# Create a FastAPI application instance
app = FastAPI()

# Define the User model
class User(BaseModel):
    name: str
    email: EmailStr # Email validation

# Step 1: 
# Define the endpoint to get users
@app.get("/user")
async def get_users() -> list[User]:
    users = list(user_collection.find({}))
    # Check if users list is empty
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    # Convert MongoDB documents to User model instances
    users = [User(**user) for user in users]
    return users

# Step 2:
# Define the endpoint to create a new user
# We will return only the created user's user id: _id which 
# We need to define a new model for the response
class UserResponse(BaseModel):
    id: str


@app.post("/user", response_model=UserResponse)
async def create_user(user: User) -> UserResponse:
    # Insert the user into the MongoDB collection
    result = user_collection.insert_one(
        user.model_dump(exclude_none=True)  # Convert Pydantic model to dict, excluding None values
    )
    if not result.acknowledged:
        raise HTTPException(status_code=500, detail="User creation failed")
    
    print(f"User created with id: {result.inserted_id}")

    user_response = UserResponse(
        id=str(result.inserted_id),
    )
    return user_response

# Step 3:
# Read details of a specific user by ID
@app.get("/user/{user_id}", response_model=User)
async def get_user(user_id: str) -> User:
    # MongoDB stores the _id as a 12-byte binary BSON type, 
    # so we need to convert the string ID to ObjectId
    user = user_collection.find_one({
        "_id": ObjectId(user_id)
        }
    )
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user)


