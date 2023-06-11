import importlib
import pkgutil
from datetime import datetime

from bson.objectid import ObjectId
from pydantic import BaseConfig, BaseModel


class AppModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda input: input.isoformat(),
            ObjectId: lambda input: str(input),
        }


def import_routers(package_name):
    package = importlib.import_module(package_name)
    prefix = package.__name__ + "."

    for _, module_name, _ in pkgutil.iter_modules(package.__path__, prefix):
        if not module_name.startswith(prefix + "router_"):
            continue

        try:
            importlib.import_module(module_name)
        except Exception as e:
            print(f"Failed to import {module_name}, error: {e}")
