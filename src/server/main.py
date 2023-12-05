import os
from random import randint
from time import time

from dotenv import load_dotenv
from loguru import logger

import src.api.j2l.pytactx.agent as pytactx

load_dotenv()


class MyReferee(pytactx.Agent):
    map: list[list[int]]
    concentration: int
    last_map_reset: time

    def __init__(self):
        super().__init__(
            playerId=os.environ["PLAYER_ID"],
            arena=os.environ["ARENA"],
            username=os.environ["JDL_USERNAME"],
            password=os.environ["JDL_PASSWORD"],
            server="mqtt.jusdeliens.com",
            verbosity=2,
        )
        self.concentration = 10
        self.map = []
        self.last_map_reset = time()
        self.weapons = [1, 3, 4, 5]
        self.ammos = [1000, 200, 10, 10000]

        self.rulePlayer(self.clientId, "x", 1000)
        self.rulePlayer(self.clientId, "y", 1000)
        self.update()

        self.init_map_values()
        if 3 not in self.game["map"][int(self.gridRows / 2)]:
            self.add_walls()

    def init_map_values(self):
        print("Initiating arena!")

        self.ruleArena("gridRows", 30)
        self.ruleArena("gridColumns", 40)
        path = "http://raw.githubusercontent.com/Frexom/C.R.A-sion/main/res/"
        self.ruleArena("preview", path + "icon.png")
        self.ruleArena("bgImg", path + "floor.png")
        self.ruleArena(
            "mapImgs",
            ["", path + "crate.png", path + "super_crate.png", path + "wall.png"],
        )
        self.ruleArena("mapFriction", [0, 0, 0, 1])
        self.ruleArena("mapHit", [0, 0, 0, 0])
        self.ruleArena("mapBreakable", [False, False, False, False])
        self.ruleArena("ownerFire", [False, False, False, False, False, False])

        self.update()
        self.map = self.game["map"]

    def clear_walls(self):
        logger.info("Clearing map")
        counter = 0
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                self.map[x][y] = 0 if self.map[x][y] == 3 else self.map[x][y]

    def invalid(self, x, y):
        if x <= 0 or x >= self.gridRows - 1:
            return True
        if y <= 0 or y >= self.gridColumns - 1:
            return True
        if self.map[x][y] == 3:
            return True
        return False

    def add_walls(
        self,
    ):
        logger.info(f"Generating walls with concentration {self.concentration}")
        self.last_map_reset = time()

        for i in range(self.concentration):
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
        is_super = randint(1, 30)

        x = randint(2, self.gridRows - 3)
        y = randint(2, self.gridColumns - 3)

        while self.map[x][y] != 0:
            x = randint(2, self.gridRows - 3)
            y = randint(2, self.gridColumns - 3)

        self.map[x][y] = 1 + int(is_super == 1)
        self.ruleArena("map", self.map)
        self.update()
        logger.info(
            f"Spawned {'legendary ' if is_super == 1 else ''}crate at X={x}, Y={y}"
        )
        return is_super == 1

    def check_player_on_crate(self):
        for player, data in self.range.items():
            cell = self.map[data["y"]][data["x"]]
            if cell in [1, 2]:
                if cell == 2:
                    # Legendary crate!
                    self.rulePlayer(player, "weapon", 2)
                    self.rulePlayer(player, "ammo", 20)

                    self.clear_walls()
                    self.add_walls()
                else:
                    chosen = randint(0, len(self.weapons) - 1)
                    self.rulePlayer(player, "weapon", self.weapons[chosen])
                    self.rulePlayer(player, "ammo", self.ammos[chosen])

                self.map[data["y"]][data["x"]] = 0
                logger.info(player + " has collected a crate!")
        self.ruleArena("map", self.map)
        self.update()

    def gameloop(self):
        number_of_crates = int((self.gridRows * self.gridColumns) / 175)
        logger.info(f"Chosen number of crates : {number_of_crates}")

        while True:
            if self.count_map_crates() < number_of_crates:
                self.spawn_random_crate()

            if time() - self.last_map_reset > 120:
                self.clear_walls()
                self.add_walls()

            self.check_player_on_crate()


if __name__ == "__main__":
    agent = MyReferee()
    agent.gameloop()
