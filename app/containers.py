from dependency_injector import containers, providers

from app.api.v1.services.issue_service import IssueService
from app.api.v1.services.label_service import LabelService
from app.api.v1.services.note_service import NoteService
from app.api.v1.services.task_service import TaskService
from app.api.v1.services.user_service import UserService
from app.db.mongo.base import MongoDatabase
from app.db.mongo.collections import COLLECTION_ISSUE, COLLECTION_USER, COLLECTION_LABEL, COLLECTION_NOTE, COLLECTION_TASK
from app.db.postpres.postpresdatabase import PostpresDatabase
from app.repositories.issue_repos import IssueRepository
from app.repositories.label_repos import LabelRepository
from app.repositories.note_repos import NoteRepository
from app.repositories.task_repos import TaskRepository
from app.repositories.user_repos import UserRepository


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    postpres_db = providers.Singleton(PostpresDatabase, db_url=config.db.postpres.url)
    mongodb = providers.Singleton(
        MongoDatabase,
        db_url=config.db.mongo.url,
        db_name=config.db.mongo.db_name
    )

    user_repos = providers.Factory(
        UserRepository,
        db=postpres_db,
        mongodb=mongodb,
        collection_name=COLLECTION_USER
    )

    user_service = providers.Factory(
        UserService,
        repos=user_repos,
    )

    issue_repos = providers.Factory(
        IssueRepository,
        db=postpres_db,
        mongodb=mongodb,
        collection_name=COLLECTION_ISSUE
    )

    issue_service = providers.Factory(
        IssueService,
        repos=issue_repos
    )

    label_repos = providers.Factory(
        LabelRepository,
        db=postpres_db,
        mongodb=mongodb,
        collection_name=COLLECTION_LABEL
    )

    label_service = providers.Factory(
        LabelService,
        repos=label_repos,
    )

    note_repos = providers.Factory(
        NoteRepository,
        db=postpres_db,
        mongodb=mongodb,
        collection_name=COLLECTION_NOTE
    )

    note_service = providers.Factory(
        NoteService,
        repos=note_repos
    )

    task_repos = providers.Factory(
        TaskRepository,
        db=postpres_db,
        mongodb=mongodb,
        collection_name=COLLECTION_TASK
    )

    task_service = providers.Factory(
        TaskService,
        repos=task_repos
    )
