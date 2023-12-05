import os

import keyboard
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
# pos = [1, int(agent.gridRows / 2)]
# while True:
#     print(pos)
#     print(agent.x, agent.y)
#     agent.moveTowards(*pos)
#     agent.update()
#     if agent.x == pos[0] and agent.y == pos[1]:
#         x = 0 if agent.x == 39 else 39
#         pos[0] = x
while True:
    if keyboard.is_pressed("z"):
        agent.moveTowards(agent.x + 0, agent.y - 1)
    if keyboard.is_pressed("q"):
        agent.moveTowards(agent.x - 1, agent.y + 0)
    if keyboard.is_pressed("s"):
        agent.moveTowards(agent.x + 0, agent.y + 1)
    if keyboard.is_pressed("d"):
        agent.moveTowards(agent.x + 1, agent.y + 0)
    if keyboard.is_pressed("space"):
        agent.fire(True)

    agent.update()
