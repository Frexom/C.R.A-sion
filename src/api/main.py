import os

import j2l.pytactx.agent as pytactx
from crasion import Survivor
from dotenv import load_dotenv

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
pos = [1, int(agent.gridRows / 2)]
while True:
    print(pos)
    print(agent.x, agent.y)
    agent.moveTowards(*pos)
    agent.update()
    if agent.x == pos[0] and agent.y == pos[1]:
        x = 0 if agent.x == 39 else 39
        pos[0] = x
