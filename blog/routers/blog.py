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

from fastapi import APIRouter, Depends, HTTPException, status, Response
from blog.database import get_db
from blog.models import Blog_db
from blog.schemas import Blog, ShowBlogs, User_Schema
from sqlalchemy.orm import Session
from blog.oauth2 import get_current_user

router = APIRouter(
    tags=['blogs'],
    prefix="/blog"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def publish_blog(blog: Blog, db: Session = Depends(get_db)):
    new_Blog = Blog_db(title=blog.title, body=blog.body)
    db.add(new_Blog)
    db.commit()
    db.refresh(new_Blog)
    return new_Blog


@router.get("/")
def get_all(db: Session = Depends(get_db), current_user: User_Schema = Depends(get_current_user)):
    blogs = db.query(Blog_db).all()
    return blogs


@router.get("/{id}", response_model=ShowBlogs, status_code=status.HTTP_200_OK)
def get_byId(id: int, response: Response, db: Session = Depends(get_db),
             current_user: User_Schema = Depends(get_current_user)):
    blog = db.query(Blog_db).filter(Blog_db.id == id).first()
    if blog:
        return blog
    else:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f"Response with this {id} is not available in the database"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Response with this {id} is not available in the database")


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def Update_ById(id: int, blog_schema: Blog, response: Response, db: Session = Depends(get_db),
                current_user: User_Schema = Depends(get_current_user)):
    blog = db.query(Blog_db).filter(Blog_db.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The Searched Blog is not found")
    blog.update(blog_schema.dict())
    db.commit()
    return {"Details": "Successfully Updated"}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ById(id: int, response: Response, db: Session = Depends(get_db),
                current_user: User_Schema = Depends(get_current_user)):
    blog = db.query(Blog_db).filter(Blog_db.id == id).delete(synchronize_session=False)
    db.commit()
    if blog:
        return {"Details": "Done"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Response with this {id} is not available in the database")
