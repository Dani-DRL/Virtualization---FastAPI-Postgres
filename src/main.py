import logging
from fastapi import FastAPI, Request
import api.routers.tasks_rt as task_router
from config.postgres import init_db
from api.middleware.logmiddleware import LoggingMiddleware

app = FastAPI(
    title="Task Manager API",
    description="FastAPI app fot the final project of Advanced Programming at PontIA",
    version="0.1.0",
)
init_db()
app.include_router(task_router.router, prefix="/tasks")
app.add_middleware(LoggingMiddleware)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.info(r"""
-----------------------------------------------------------------------------------
===================================================================================
  _______       _____ _  __   __  __          _   _          _____ ______ _____  
 |__   __|/\   / ____| |/ /  |  \/  |   /\   | \ | |   /\   / ____|  ____|  __ \ 
    | |  /  \ | (___ | ' /   | \  / |  /  \  |  \| |  /  \ | |  __| |__  | |__) |  
    | | / /\ \ \___ \|  <    | |\/| | / /\ \ | . ` | / /\ \| | |_ |  __| |  _  /   
    | |/ ____ \____) | . \   | |  | |/ ____ \| |\  |/ ____ \ |__| | |____| | \ \   
    |_/_/    \_\_____/_|\_\  |_|  |_/_/    \_\_| \_/_/    \_\_____|______|_|  \_\
===================================================================================
-----------------------------------------------------------------------------------
""")



