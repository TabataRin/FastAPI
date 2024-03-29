import os
from typing import Dict, List, TypedDict

from fastapi import APIRouter, Depends, HTTPException

ENVIRON = os.environ['ENVIRON']

router = APIRouter()


@router.get("/v1/list/fruit")
async def get_list_fruit() -> Dict:

    if ENVIRON == 'dev':
        response = {
                    'name': 'apple',
                    'price': '100',
                   }
    elif ENVIRON == 'prd':
        response = {
                    'name': 'orange',
                    'price': '100',
                   }                   
        
    return response

