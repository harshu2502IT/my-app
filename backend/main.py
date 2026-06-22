from jose import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client
from dotenv import load_dotenv
import os

SECRET_KEY = "ASK_MEDICAL_STORE_SECRET_KEY"
ALGORITHM = "HS256"

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# -----------------------------
# Models
# -----------------------------

class LoginData(BaseModel):
    email: str
    password: str


class UserData(BaseModel):
    email: str
    password: str
    full_name: str
    mobile_no: str
    address: str


# -----------------------------
# Home API
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "ASK Medical Store API Running"
    }


# -----------------------------
# Login API
# -----------------------------

@app.post("/login")
def login(user: LoginData):

    result = (
        supabase
        .table("OrderList")
        .select("*")
        .eq("email", user.email)
        .eq("password", user.password)
        .execute()
    )

    if len(result.data) > 0:

        payload = {
            "sub": user.email,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }

        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm=ALGORITHM
        )

        return {
            "success": True,
            "message": "Login Successful",
            "access_token": token,
            "token_type": "bearer"
        }

    return {
        "success": False,
        "message": "Invalid Email or Password"
    }


# -----------------------------
# Secure Profile API
# -----------------------------

@app.get("/secure-profile")
def secure_profile(authorization: str = Header(None)):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Token Missing"
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return {
            "message": "Token Valid",
            "email": payload["sub"]
        }

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )


# -----------------------------
# CREATE USER
# -----------------------------

@app.post("/create-user")
def create_user(user: UserData):

    result = (
        supabase
        .table("OrderList")
        .insert({
            "email": user.email,
            "password": user.password,
            "full_name": user.full_name,
            "mobile_no": user.mobile_no,
            "address": user.address
        })
        .execute()
    )

    return {
        "success": True,
        "message": "User Created Successfully",
        "data": result.data
    }


# -----------------------------
# GET ALL USERS
# -----------------------------

@app.get("/users")
def get_users():

    result = (
        supabase
        .table("OrderList")
        .select("*")
        .execute()
    )

    return result.data


# -----------------------------
# GET SINGLE USER
# -----------------------------

@app.get("/user/{user_id}")
def get_user(user_id: int):

    result = (
        supabase
        .table("OrderList")
        .select("*")
        .eq("id", user_id)
        .execute()
    )

    return result.data


# -----------------------------
# UPDATE USER
# -----------------------------

@app.put("/update-user/{user_id}")
def update_user(user_id: int, user: UserData):

    result = (
        supabase
        .table("OrderList")
        .update({
            "email": user.email,
            "password": user.password,
            "full_name": user.full_name,
            "mobile_no": user.mobile_no,
            "address": user.address
        })
        .eq("id", user_id)
        .execute()
    )

    return {
        "success": True,
        "message": "User Updated Successfully",
        "data": result.data
    }


# -----------------------------
# DELETE USER
# -----------------------------

@app.delete("/delete-user/{user_id}")
def delete_user(user_id: int):

    result = (
        supabase
        .table("OrderList")
        .delete()
        .eq("id", user_id)
        .execute()
    )

    return {
        "success": True,
        "message": "User Deleted Successfully"
    }