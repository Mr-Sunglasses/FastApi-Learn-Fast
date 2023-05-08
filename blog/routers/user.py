#  Copyright (c) 2023 Kanishk Pachauri.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from fastapi import APIRouter, Depends, HTTPException, status
from blog.schemas import User_Schema, UserResponseSchema
from blog.hashing import CreateHash
from sqlalchemy.orm import Session
from blog.database import get_db
from blog.models import User
from blog.oauth2 import get_current_user

router = APIRouter(
    tags=["User"],
    prefix="/user"
)


@router.post("/")
def create_user(user: User_Schema, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email, password=CreateHash.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
def get_userList(id: int, db: Session = Depends(get_db),
                 current_user: User_Schema = Depends(get_current_user)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Response with this {id} is not available in the database")
    else:
        return user
