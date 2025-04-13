from typing import Optional

class Post:
    def __init__(self, id: int, name: str, content: Optional[str], publisher: Optional[str] = None):
        self.id = id
        self.name = name
        self.content = content
        self.publisher = publisher

