from Moves.move import Move
from melee import Action, Button

class Grab(Move): # maybe should be a tactic?

    # 3f boost grab covers ~32.0 units
    # 2f boost grab covers ~28.7 units
    # 1f boost grab covers ~23.9 units
    #      dashgrab covers ~12.6 units
    #        jcgrab covers ~11.2 units

    def step(self, gamestate, state, opponent_state):

        distance = abs(opponent_state.x - state.x)
        opponent_left = -1 if opponent_state.x < state.x else 1

        if not opponent_state.on_ground: #give up for now
            self.give_up()
            return

        if distance > 65: # too far!
            self.give_up()
            return

        match state.action:
            case Action.SHIELD_STUN:
                self.give_up()
            case Action.STANDING:
                if (distance < 8):
                    self.controller.tilt_analog_unit(Button.BUTTON_MAIN, 0, 0)
                    self.controller.press_button(Button.BUTTON_Z)
                    self.interruptible = True
                    return
                self.controller.tilt_analog_unit(Button.BUTTON_MAIN, opponent_left, 0)
            case Action.DASHING | Action.RUNNING:
                    self.controller.release_all()
                    self.controller.tilt_analog_unit(Button.BUTTON_MAIN, opponent_left, 0)
                    if distance < 35 and distance > 16 and state.action_frame > 3:
                        self.controller.press_button(Button.BUTTON_A)
                        self.interruptible = False
                    elif distance <= 16 and state.action_frame > 3:
                        self.controller.press_button(Button.BUTTON_Y)
                        self.interruptible = False
            case Action.DASH_ATTACK:
                self.controller.release_all()
                if state.action_frame < 3:
                    if self.framedata.slide_distance(state, state.speed_ground_x_self, 1) > distance + (opponent_state.speed_ground_x_self * opponent_left):
                        self.controller.press_button(Button.BUTTON_Z)
                        self.interruptible = True
                else:
                    self.controller.press_button(Button.BUTTON_Z)
                    self.interruptible = True
            case Action.KNEE_BEND:
                self.controller.release_all()
                self.controller.press_button(Button.BUTTON_Z)
                self.interruptible = True