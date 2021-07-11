from app.api.v1.services.base import ServiceBase
from app.repositories.note_repos import NoteRepository


class NoteService(ServiceBase):
    def __init__(self, note_repos: NoteRepository):
        super().__init__(note_repos)
