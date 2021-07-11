from app.repositories.label_repos import LabelRepository


class LabelService:
    def __init__(self, label_service: LabelRepository):
        self.label_service = label_service
