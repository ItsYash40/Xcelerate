from fastapi import APIRouter

from fastapi import Depends

from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.user_model import User

from app.schemas.auth_schema import LoginRequest

from app.services.auth_service import verify_password

from app.services.jwt_service import create_access_token




router=APIRouter()




@router.post(

"/login"

)

def login(



login_data:LoginRequest,



db:Session=Depends(

get_db

)



):




    user=db.query(

    User

    ).filter(

    User.email==login_data.email

    ).first()




    if not user:



        raise HTTPException(

        status_code=404,

        detail="User Not Found"

        )




    if not verify_password(

    login_data.password,

    user.password

    ):



        raise HTTPException(

        status_code=401,

        detail="Incorrect Password"

        )




    token=create_access_token(

    {

    "user_id":user.id,

    "email":user.email

    }

    )

    return {

    "access_token":token,

    "token_type":"bearer"

    }