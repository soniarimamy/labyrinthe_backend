import uvicorn
from routers import Game

uvicorn.run(app=Game.app, host='0.0.0.0', port=8000)
