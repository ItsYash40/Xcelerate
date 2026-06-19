from fastapi import APIRouter

from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.user_schema import UserCreate

from app.models.user_model import User

from app.services.auth_service import hash_password



router=APIRouter()




@router.get("/test")

def test():



    return {

        "message":

        "User API Working"

    }






@router.post("/register")



def register_user(



    user:UserCreate,



    db:Session=Depends(

        get_db

    )

):



    print(user.password)

    hashed_pw=hash_password(

    user.password

    )

    

    existing_user=db.query(

    User

    ).filter(

    User.email==user.email

    ).first()



    if existing_user:



        return {

            "message":

            "Email already registered"

        }



    hashed_pw=hash_password(

    user.password

    )



    new_user=User(

    username=user.username,

    email=user.email,

    password=hashed_pw

    )  



    new_user=User(



        username=user.username,



        email=user.email,



        password=hashed_pw



    )
    db.add(

        new_user

    )
    db.commit()
    db.refresh(

        new_user
    )
    return {

        "message":
        "User Registered Successfully"

    }