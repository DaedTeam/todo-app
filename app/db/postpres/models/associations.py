from sqlalchemy import Column, ForeignKey, Table

from app.db.postpres.base import Base

label_task = Table("label_task", Base.metadata,
                   Column("label_id", ForeignKey("labels.id"), primary_key=True),
                   Column("task_id", ForeignKey("tasks.id"), primary_key=True)
                   )

label_note = Table("label_note", Base.metadata,
                   Column("label_id", ForeignKey("labels.id"), primary_key=True),
                   Column("note_id", ForeignKey("notes.id"), primary_key=True)
                   )

label_issue = Table("label_issue", Base.metadata,
                    Column("label_id", ForeignKey("labels.id"), primary_key=True),
                    Column("issue_id", ForeignKey("issues.id"), primary_key=True)
                    )
