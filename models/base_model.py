from datetime import datetime
from uuid import uuid4

class BaseModel ():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs:
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()




