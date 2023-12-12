import j2l.pytactx.agent as pytactx
from crasion import Survivor
from dotenv import load_dotenv
from random import randint
import os

load_dotenv()

agent = Survivor( 
    playerId=os.environ["PLAYER_ID"],
    arena=os.environ["ARENA"],
    username=os.environ["JDL_USERNAME"],
    password=os.environ["JDL_PASSWORD"],
    server="mqtt.jusdeliens.com",
    verbosity=2,
)
while True:
  agent.move(randint(-1, 2) , randint(-1, 2))
  #agent.fire(True)
  #agent.lookAt(2)
  #print(agent.map)
  agent.update()
