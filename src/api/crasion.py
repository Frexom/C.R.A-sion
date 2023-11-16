import j2l.pytactx.agent as pytactx

class Survivor:
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
            port, imgOutputPath, autoconnect, waitArenaConnection, verbosity,
            robotId, welcomePrint, sourcesdir)
        
        self.weapon = ""
        self.type = "survivor"
    

    def move(self, dx: int, dy: int) -> None:
        self.__agent.move(dx, dy)
    

    def moveTowards(self, x: int, y: int) -> None:
        self.__agent.moveTowards(x, y)
    

    def lookAt(self, dir: int) -> None:
        self.__agent.lookAt(dir)
    

    def fire(self, enable: bool = True) -> None:
        self.__agent.fire(enable)