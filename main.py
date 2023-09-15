basic.show_icon(IconNames.HAPPY)

def on_forever():
    if mbit_Robot.Avoid_Sensor(mbit_Robot.enAvoidState.OBSTACLE):
        basic.show_number(pins.analog_read_pin(AnalogPin.P3))
        
        print(x)
    else:
        basic.show_number(pins.analog_read_pin(AnalogPin.P3))
        print(x)
basic.forever(on_forever)
