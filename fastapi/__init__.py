"""FastAPI framework, high performance, easy to learn, fast to code, ready for production"""

__version__ = "0.66.0"

from starlette import status

from .applications import FastAPI
from .background import BackgroundTasks
from .datastructures import UploadFile
from .exceptions import HTTPException
from .param_functions import Body
from .param_functions import Cookie
from .param_functions import Depends
from .param_functions import File
from .param_functions import Form
from .param_functions import Header
from .param_functions import Path
from .param_functions import Query
from .param_functions import Security
from .requests import Request
from .responses import Response
from .routing import APIRouter
from .websockets import WebSocket
from .websockets import WebSocketDisconnect
