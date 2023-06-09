import datetime

class Todo:
    def __init__(self,task,category,date_added=None,date_completed=None,status=False,position=None) -> None:
        self.task = task
        self.category = category
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat()
        self.date_completed = date_completed #if date_completed is not None else None
        self.status = status # false = open , true = closed
        self.position = position

    def __repr__(self) -> str:
        return f"Todo({self.task},{self.category},{self.date_added},{self.date_completed},{self.status},{self.position})"
