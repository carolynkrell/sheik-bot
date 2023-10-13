import melee, random
from melee import Action, Button
from Moves.move import Move
import Moves

class MoveDecider:

    controller: melee.Controller = None
    current_move: Move = None
    frame_data: melee.framedata.FrameData = melee.framedata.FrameData()

    def choose_move(self, move: Move, args=[]):
        if type(self.current_move) != move:
            self.current_move = move(*args)
            self.current_move.controller = self.controller
            self.current_move.frame_data = self.frame_data
        self.current_move.step(self._propagate[0], self._propagate[1], self._propagate[2])

    def step(self, gamestate: melee.GameState, state: melee.PlayerState, opponent_state: melee.PlayerState):
        self._propagate  = (gamestate, state, opponent_state)

        print("Move: " + type(self.current_move).__name__, "| Action State: [" + str(state.action), str(state.action_frame) + "]", "| Dist: " +  str(opponent_state.x - state.x))

        if self.current_move != None and not self.current_move.interruptible:
            self.current_move.step(gamestate, state, opponent_state)
            return
        
        if state.action in [Action.STANDING, Action.RUNNING, Action.DASHING]:
            if abs(state.x - opponent_state.x) < 55:
                self.choose_move(Moves.Grab)
            else:
                self.choose_move(Moves.Wavedash, [1, random.randint(0,1) == 1])
        elif state.action == Action.EDGE_CATCHING:
            self.choose_move(Moves.Sami_Stall)
        else:
            self.controller.release_all()