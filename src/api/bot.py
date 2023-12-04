import os

from dotenv import load_dotenv

import src.api.j2l.pytactx.agent as pytactx
from src.api.crasion import Survivor

load_dotenv()

agent = pytactx.Agent(
    playerId="feur",
    arena=os.environ["ARENA"],
    username=os.environ["JDL_USERNAME"],
    password=os.environ["JDL_PASSWORD"],
    server="mqtt.jusdeliens.com",
    verbosity=2,
)
print("zefbjhefgvgrfheilgyto")
pos = [2, int(agent.gridRows / 2)]
while True:
    print(pos)
    print(agent.x, agent.y)
    agent.moveTowards(*pos)
    agent.update()
    if agent.x == pos[0] and agent.y == pos[1]:
        x = 1 if agent.x == 30 else 30
        pos[0] = x
