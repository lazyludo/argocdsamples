# -*- coding: utf-8 -*-
# @Author: Kiran Balijepalli
# @Date:   2021-11-08 16:17:22
# @Last Modified by:   name here
# @Last Modified time: 2021-11-08 16:23:56

import uvicorn
from typing import Optional, Set
from fastapi import Body,Depends, FastAPI,Request, HTTPException,status
from fastapi import FastAPI, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.responses import PlainTextResponse
from datetime import datetime, timedelta

from starlette.middleware.cors import CORSMiddleware

origins = [
  
    "http://localhost:3000",
    "http://localhost:80",
    "http://localhost:8080",
    "http://0.0.0.0:3000"
]


app = FastAPI(
    title="Spectral Finance API microservices",
    # docs_url=None,redocs_url=None,openapi_url=None
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=False,
    allow_methods=["Get","Post","Put"],
    allow_headers=["*"],
)
@app.get("/i")
async def where_do_i_currently():
	"""
	--- Routes validation check
	"""
	return { " Welcome to Spectral.Finance MacroAPI "} 



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get('5000'), log_level="critical"))