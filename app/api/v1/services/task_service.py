from app.repositories.task_repos import TaskRepository


class TaskService:
    def __init__(self, task_repos: TaskRepository):
        self.task_repos = task_repos
