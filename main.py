from fastapi import FastAPI, Body, Path
from typing import List

tags_metadata = [{"name": "web", "description": "Endpoints of example"}  ,  { "name": "users", "description": "User handling endpoints"},]

app = FastAPI(openapi_tags=tags_metadata)