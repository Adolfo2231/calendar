from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    """Modelo de usuario para la creación de un nuevo usuario"""
    
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)
    role: str = "user"

    class Config:
        str_strip_whitespace = True #? Para eliminar los espacios en blanco de los strings

class ResponseUser(BaseModel):
    
    id: str
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True #? Para convertir los objetos SQLAlchemy a Pydantic

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ResponseLogin(BaseModel):
    access_token: str
    refresh_token: str
    user: ResponseUser