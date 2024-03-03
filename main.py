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
import uvicorn
from fastapi import FastAPI
from blog.models import Base
from blog.database import engine
from blog.routers import blog, user, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

#testing pep8speaks :)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blog"])
# def publish_blog(blog: Blog, db: Session = Depends(get_db)):
#     new_Blog = Blog_db(title=blog.title, body=blog.body)
#     db.add(new_Blog)
#     db.commit()
#     db.refresh(new_Blog)
#     return new_Blog


# @app.get("/blog", tags=["blog"])
# def get_all(db: Session = Depends(get_db)):
#     blogs = db.query(Blog_db).all()
#     return blogs


# @app.get("/blog/{id}", response_model=ShowBlogs, status_code=status.HTTP_200_OK, tags=["blog"])
# def get_byId(id: int, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(Blog_db).filter(Blog_db.id == id).first()
#     if blog:
#         return blog
#     else:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"details": f"Response with this {id} is not available in the database"}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Response with this {id} is not available in the database")
#
#
# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blog"])
# def Update_ById(id: int, blog_schema: Blog, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(Blog_db).filter(Blog_db.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The Searched Blog is not found")
#     blog.update(blog_schema.dict())
#     db.commit()
#     return {"Details": "Successfully Updated"}
#
#
# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blog"])
# def delete_ById(id: int, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(Blog_db).filter(Blog_db.id == id).delete(synchronize_session=False)
#     db.commit()
#     if blog:
#         return {"Details": "Done"}
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Response with this {id} is not available in the database")


# @app.post("/user", tags=["user"])
# def create_user(user: User_Schema, db: Session = Depends(get_db)):
#     new_user = User(name=user.name, email=user.email, password=CreateHash.bcrypt(user.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
#
# @app.get("/user/{id}", response_model=UserResponseSchema, status_code=status.HTTP_200_OK, tags=["user"])
# def get_userList(id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Response with this {id} is not available in the database")
#     else:
#         return user


# @app.get("/user/list", response_model=UserResponseSchema, tags=["user"])
# def getUserList(db: Session = Depends(get_db)):
#     users = db.query(User).all()
#     if not users:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Response with this data is not available in the database")
#     else:
#         return users


