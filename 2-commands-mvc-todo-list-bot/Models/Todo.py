class Todo:
    def __init__(self, title) -> None:
        self.title = title
        self.is_completed = False

    def set_completed(self):
        self.is_completed = True