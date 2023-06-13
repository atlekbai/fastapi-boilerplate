from app.config import database

from .repository.repository import ShanyraksRepository


class Service:
    def __init__(
        self,
        repository: ShanyraksRepository,
    ):
        self.repository = repository


def get_service():
    repository = ShanyraksRepository(database)

    svc = Service(repository)
    return svc
