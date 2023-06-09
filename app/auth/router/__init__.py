from fastapi import APIRouter

from app.utils import import_routers

router = APIRouter()
import_routers(__name__)
