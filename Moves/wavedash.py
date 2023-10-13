from Moves.move import Move
from melee import Action, Button

class Wavedash(Move):

    # distance is a float between 0 and 1
    def __init__(self, distance: float, towards=True):
        self.distance = distance
        self.towards = towards

    def step(self, gamestate, state, opponent_state):
        match state.action:
            case Action.SHIELD_STUN:
                self.controller.release_all()
                self.interruptible = True
            case Action.STANDING | Action.SHIELD | Action.RUNNING | Action.DASHING:
                self.controller.release_all()
                self.controller.press_button(Button.BUTTON_Y)
                self.interruptible = False
            case Action.KNEE_BEND:
                self.controller.release_button(Button.BUTTON_Y)
                if state.action_frame == 3:
                    opponent_left = -1 if opponent_state.x < state.x else 1
                    stick_y = ((self.distance / 2) + 0.5) * opponent_left
                    self.controller.tilt_analog_unit(Button.BUTTON_MAIN, stick_y, -0.325)
                    self.controller.press_button(Button.BUTTON_L)
            case Action.LANDING_SPECIAL:
                self.interruptible = True
                self.controller.release_all()