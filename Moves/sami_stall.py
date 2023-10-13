from Moves.move import Move
from melee import Action, Button

class Sami_Stall(Move):
    def step(self, gamestate, state, opponent_state):
        direction = 1 if state.x < 0 else -1
        match state.action:
            case Action.EDGE_CATCHING:
                self.controller.release_all()
                self.interruptible = True
            case Action.EDGE_HANGING:
                    self.interruptible = False
                    self.controller.tilt_analog_unit(Button.BUTTON_MAIN, -direction, -1)
            case Action.FALLING:
                self.controller.tilt_analog_unit(Button.BUTTON_MAIN, 0, -1)
                if state.invulnerability_left < 20:
                    self.controller.press_button(Button.BUTTON_B)
                    self.controller.tilt_analog_unit(Button.BUTTON_MAIN, 0, 1)