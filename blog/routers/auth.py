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
from blog.schemas import Login
from sqlalchemy.orm import Session
from blog.database import get_db
from blog.models import User
from blog.hashing import CreateHash
from blog.token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["auth"]
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user with this Creds are Available")
    if not CreateHash.verify(user.password, request.password):
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong Password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
