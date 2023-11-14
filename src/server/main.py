import os
from random import randint

from dotenv import load_dotenv

import src.api.j2l.pytactx.agent as pytactx

load_dotenv()

GRID_ROWS = 30
GRID_COLUMNS = 40


class MyReferee(pytactx.Agent):
    map: list[list[int]]

    def __init__(self):
        super().__init__(
            playerId=os.environ["PLAYER_ID"],
            arena=os.environ["ARENA"],
            username=os.environ["JDL_USERNAME"],
            password=os.environ["JDL_PASSWORD"],
            server="mqtt.jusdeliens.com",
            verbosity=2,
        )
        self.map = []
        for i in range(GRID_ROWS):
            self.map.append([0] * GRID_COLUMNS)

        self.init_map_values()

    def init_map_values(self):
        print("Initiating arena!")

        self.ruleArena("gridRows", GRID_ROWS)
        self.ruleArena("gridColumns", GRID_COLUMNS)
        self.ruleArena(
            "resPath",
            "https://raw.githubusercontent.com/Frexom/C.R.A-sion/init-arena-params/res/",
        )
        self.ruleArena("preview", "icon.png")
        self.ruleArena("bgImg", "floor.png")
        self.ruleArena("mapImgs", ["", "crate.png"])
        self.update()

    def spawn_random_crate(self):
        x = randint(0, GRID_ROWS - 1)
        y = randint(0, GRID_COLUMNS - 1)

        while self.map[x][y] == 1:
            x = randint(0, GRID_ROWS - 1)
            y = randint(0, GRID_COLUMNS - 1)

        self.map[x][y] = 1
        self.ruleArena("map", self.map)
        self.update()


if __name__ == "__main__":
    agent = MyReferee()
    agent.spawn_random_crate()
