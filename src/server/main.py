import os
from random import randint

from dotenv import load_dotenv
from loguru import logger

import src.api.j2l.pytactx.agent as pytactx

load_dotenv()


class MyReferee(pytactx.Agent):
    map: list[list[int]]
    mapBackup: list[list[int]]

    def __init__(self):
        super().__init__(
            playerId=os.environ["PLAYER_ID"],
            arena=os.environ["ARENA"],
            username=os.environ["JDL_USERNAME"],
            password=os.environ["JDL_PASSWORD"],
            server="mqtt.jusdeliens.com",
            verbosity=2,
        )
        self.update()

        self.map = []
        self.init_map_values()
        self.add_walls(10)

    def init_map_values(self):
        print("Initiating arena!")

        self.ruleArena("gridRows", self.gridRows)
        self.ruleArena("gridColumns", self.gridColumns)
        path = (
            "https://raw.githubusercontent.com/Frexom/C.R.A-sion/init-arena-params/res/"
        )
        self.ruleArena("preview", path + "icon.png")
        self.ruleArena("bgImg", path + "floor.png")
        self.ruleArena("mapImgs", ["", path + "crate.png", path + "super_crate.png"])
        self.ruleArena("mapFriction", [0, 0, 0, 1])

        self.update()
        self.map = self.game["map"]

    def clear_walls(self):
        logger.info("Clearing map")
        counter = 0
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                self.map[x][y] = 0 if self.map[x][y] == 3 else 0

    def invalid(self, x, y):
        if x <= 0 or x >= self.gridRows - 1:
            return True
        if y <= 0 or y >= self.gridColumns - 1:
            return True
        if self.map[x][y] == 3:
            return True
        return False

    def add_walls(self, concentration: int):
        logger.info(f"Generating walls with concentration {concentration}")
        self.clear_walls()

        for i in range(concentration):
            initX = randint(0 + 5, self.gridRows - 6)
            initY = randint(0 + 5, self.gridColumns - 6)
            # Vertical or not, direction
            head = [randint(0, 1), randint(-1, 1)]

            fail_count = 0
            x, y = initX, initY
            while x not in [0, self.gridRows - 1] and y not in [
                0,
                self.gridColumns - 1,
            ]:
                if fail_count > 5:
                    break
                if (
                    (randint(0, 6) == 1)
                    or (head[0] == 0 and (self.invalid(x, y + head[1] * 2)))
                    or (head[0] == 1 and (self.invalid(x + head[1] * 2, y)))
                ):

                    head = [randint(0, 1), randint(-1, 1)]
                    fail_count += 1
                    continue

                if head[0]:
                    x += head[1]
                else:
                    y += head[1]

                self.map[x][y] = 3
                fail_count = 0
        self.ruleArena("map", self.map)
        self.update()

    def count_map_crates(self):
        counter = 0
        for column in self.map:
            for el in column:
                counter += int(el in [1, 2])
        return counter

    def spawn_random_crate(self):
        is_super = randint(1, 10)

        x = randint(0, self.gridRows - 1)
        y = randint(0, self.gridColumns - 1)

        while self.map[x][y] != 0:
            x = randint(0, self.gridRows - 1)
            y = randint(0, self.gridColumns - 1)

        self.map[x][y] = 1 + int(is_super == 1)
        self.ruleArena("map", self.map)
        self.update()
        logger.info(f"Spawned {'legendary ' if is_super else ''}crate at X={x}, Y={y}")
        return is_super == 1

    def check_player_on_crate(self):
        for player, data in self.range.items():
            cell = self.map[data["y"]][data["x"]]
            if cell != 0:
                # Give player weapon
                self.map[data["y"]][data["x"]] = 0
                logger.info(player + " has collected a crate!")
        self.ruleArena("map", self.map)
        self.update()

    def infinite_ammos(self):
        for player in self.range.keys():
            self.rulePlayer(player, "ammo", 10000)
        agent.update()


if __name__ == "__main__":
    agent = MyReferee()
    while True:
        if agent.count_map_crates() < 3:
            agent.spawn_random_crate()
            agent.infinite_ammos()
        agent.check_player_on_crate()
