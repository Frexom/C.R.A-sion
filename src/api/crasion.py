import j2l.pytactx.agent as pytactx
from enum import Enum
from random import randint

class Weapons(Enum):
  BASIC = 1
  AK47 = 2
  BAZOOKA = 3
  LEGENDARY = 4
  

class Survivor:
  
  class FirePath:
    '''handles the shooting pattern'''
    def __init__(self, player):
      self.player = player
    
    def __call__(self):
      return 0

  def __init__(
      self,
      playerId: str or None = None,
      arena: str or None = None,
      username: str or None = None,
      password: str or None = None,
      server: str or None = None,
      port: int = 1883,
      imgOutputPath: str or None = "img.jpeg",
      autoconnect: bool = True,
      waitArenaConnection: bool = True,
      verbosity: int = 3,
      robotId: str or None = "_",
      welcomePrint: bool = True,
      sourcesdir: str or None = None,
  ):
    self.__agent = pytactx.Agent(playerId, arena, username, password, server,
                                 port, imgOutputPath, autoconnect,
                                 waitArenaConnection, verbosity, robotId,
                                 welcomePrint, sourcesdir)

    self.weapon = Weapons.BASIC
    self.type = "survivor"
    self.__CRATE = 1
    self.__LEGENDARY_CRATE = 2
    self.__previous_box = 0

  def move(self, dx: int, dy: int) -> None:
    self.__agent.move(dx, dy)


  def moveTowards(self, x: int, y: int) -> None:
    self.__agent.moveTowards(x, y)


  def lookAt(self, dir: int) -> None:
    self.__agent.lookAt(dir)


  def fire(self, enable: bool = True) -> None:
    self.__agent.fire(enable, self.FirePath(self))

  
  def __get_weapon(self)->None:
    self.weapon = randint(1, len(Weapons))
  
  
  def handle_crate_collection(self)->None:
    next_box = self.__agent.game["map"][self.__agent.y][
        self.__agent.x]
    if next_box == self.__previous_box:
      return
    
    self.__previous_box = next_box
    if self.__agent.game["map"][self.__agent.y][
        self.__agent.x] == self.__CRATE:
      print("crate !!!")
      self.__get_weapon()
      print(self.weapon)
    elif self.__agent.game["map"][self.__agent.y][
        self.__agent.x] == self.__LEGENDARY_CRATE:
      self.weapon = Weapons.LEGENDARY
      print(self.weapon)
    else:
      return


  def update(self) -> None:
    self.handle_crate_collection()
      
    self.__agent.update()
