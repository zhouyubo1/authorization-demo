from pydantic import BaseModel


class BaseInfo(BaseModel):

    username: str
    password: str