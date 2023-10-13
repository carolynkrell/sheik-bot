from Moves.move import Move
from melee import Action, Button

# 11 galint ledgedashes. 12max on most stages, but requires a sweetspot jump

class Ledgedash(Move):
    def step(self, gamestate, state, opponent_state):
        direction = 1 if state.x < 0 else -1
        match state.action:
            case Action.EDGE_HANGING:
                self.controller.tilt_analog_unit(Button.BUTTON_MAIN, 0, -1)
                self.interruptible = False
            case Action.FALLING:
                self.controller.tilt_analog_unit(Button.BUTTON_MAIN, direction, 0)
                self.controller.press_button(Button.BUTTON_Y)
            case Action.JUMPING_ARIAL_FORWARD:
                if state.invulnerability_left == 22:
                    self.controller.tilt_analog_unit(Button.BUTTON_MAIN, direction * 0.7125, -1)
                    self.controller.press_button(Button.BUTTON_L)
            case Action.LANDING_SPECIAL:
                if state.action_frame == 8:
                    self.controller.release_all()
                    self.interruptible = True