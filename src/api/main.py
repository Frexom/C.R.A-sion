import j2l.pytactx.agent as pytactx
from crasion import Survivor
from dotenv import load_dotenv
import os

load_dotenv()

agent = pytactx.Agent(
    playerId=os.environ["PLAYER_ID"],
    arena=os.environ["ARENA"],
    username=os.environ["JDL_USERNAME"],
    password=os.environ["JDL_PASSWORD"],
    server="mqtt.jusdeliens.com",
    verbosity=2,
)
print("zefbjhefgvgrfheilgyto")
while True:
    agent.update()
    agent.lookAt((agent.dir + 1) % 4)
