def on_forever():
    pass
basic.forever(on_forever)
global direction, is_ball
    if pins.analog_read_pin(AnalogPin.P0) < 100:
        direction = 1
    elif pins.analog_read_pin(AnalogPin.P0) < 200:
        direction = 2
    elif pins.analog_read_pin(AnalogPin.P0) < 300:
        direction = 3
    elif pins.analog_read_pin(AnalogPin.P0) < 400:
        direction = 4
    elif pins.analog_read_pin(AnalogPin.P0) < 460:
        is_ball = 0
        basic.pause(200)