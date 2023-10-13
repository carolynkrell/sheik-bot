import melee

class Move:
    interruptible: bool = True
    controller: melee.Controller = None
    framedata: melee.framedata.FrameData = melee.framedata.FrameData()

    def step(self, gamestate: melee.GameState, state: melee.PlayerState, opponent_state: melee.PlayerState): ...

    def give_up(self):
        self.interruptible = True
        self.controller.release_all()