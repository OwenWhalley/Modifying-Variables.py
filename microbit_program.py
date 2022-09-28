# Created by: Owen Whalley
# Created on: 2022/09/28
#
# This sets hunger to 0 on start.
hunger = 0
# Created by: Owen Whalley
# Created on: 2022/09/28
#
# If A button is pressed, it increses hunger by one and shows the value of hunger. If B button is pressed, it resets hunger to 0 and shows the value of hunger.

def on_forever():
    global hunger
    if input.button_a_is_pressed(True):
        hunger = hunger + 1
        basic.show_number(hunger)
    elif input.button_b_is_pressed(True):
        hunger = 0
        basic.show_number(hunger)
basic.forever(on_forever)
