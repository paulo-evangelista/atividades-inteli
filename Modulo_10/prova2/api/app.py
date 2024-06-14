from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)
FORMAT = '%(asctime)s :: %(levelname)s :: %(message)s'
logging.basicConfig(filename='logs.log', level=logging.WARN, format=FORMAT)


app = FastAPI()

blog_posts = []

class CreateBlogPostRequest(BaseModel):
    id: int
    title: str
    content: str

class UpdateBlogPostRequest(BaseModel):
    title: str
    content: str

class BlogPost:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
    def __str__(self) -> str:
        return f'{self.id} - {self.title} - {self.content}'
    
    def toJson(self):
        return {'id': self.id, 'title': self.title, 'content': self.content}

@app.post('/blog', status_code=201)
def create_blog_post(data: CreateBlogPostRequest):
        logger.info(f'Creating blog post with title {data.title}')
        blog_posts.append(BlogPost(data.id, data.title, data.content))
        logger.info(f'Blog post with title {data.title} created')
        return {'status':'sucess'}


@app.get('/blog')
def get_blog_posts():
    logger.info('Getting all blog posts')
    return {'posts': [blog.toJson() for blog in blog_posts]}


@app.get('/blog/{post_id}')
def get_blog_post(post_id: int):
    logger.info(f'Getting blog post with id {post_id}')
    for post in blog_posts:
        if post.id == post_id:
            logger.info(f'Blog post with id {post_id} found')
            return {'post': post.__dict__}
    logger.error(f'Blog post with id {post_id} not found')
    raise HTTPException(status_code=404, detail='Post not found')


@app.delete('/blog/{id}')
def delete_blog_post(id: int):
    logger.info(f'Deleting blog post with id {id}')
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            logger.info(f'Blog post with id {id} deleted')
            return {'status':'sucess'}
    logger.error(f'Blog post with id {id} not found')
    raise HTTPException(status_code=404, detail='Post not found')


@app.put('/blog/{id}')
def update_blog_post(id:int, data: UpdateBlogPostRequest):
    logger.info(f'Updating blog post with id {id}')
    for post in blog_posts:
        if post.id == id:
            post.title = data.title
            post.content = data.content
            logger.info(f'Blog post with id {id} updated')
            return {'status':'sucess'}
    logger.error(f'Blog post with id {id} not found')
    raise HTTPException(status_code=404, detail='Post not found')

@app.get('/all_posts')
def get_all_posts():
    logger.warn(f'User called a deprecated endpoint')
    raise HTTPException(status_code=301, detail='This endpoint is deprecated, use /blog instead')
