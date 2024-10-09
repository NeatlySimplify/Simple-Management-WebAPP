from fastapi import APIRouter, Depends, HTTPException, Request

from fastapi.responses import HTMLResponse

from ..helper import get_token_header

from fastapi.templating import Jinja2Templates

from ..DRY import *


template = Jinja2Templates(directory="../Static/templates")