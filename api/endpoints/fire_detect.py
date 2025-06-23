from typing import List
from fastapi import APIRouter, File, Query, UploadFile
import torch

from core.Response import fail, success
from detect1 import detect


router = APIRouter()

@router.post("/detect",summary="火情监测",description="火情监测")
async def detect_api(file_path: str = Query(...),sava_path: str = Query(...)):
    try:

        with torch.no_grad(): 
            save_path = detect(source=file_path,output=sava_path)

    except Exception as e:
        return fail(msg=str(e))
    
    return success(msg=save_path)
