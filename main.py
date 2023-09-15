basic.show_icon(IconNames.HAPPY)

def on_forever():
    if mbit_Robot.Avoid_Sensor(mbit_Robot.enAvoidState.OBSTACLE):
        basic.show_number(pins.digital_read_pin(DigitalPin.P3))
        x=pins.digital_read_pin(DigitalPin.P0)
        print(x)
        
    else:
        
        basic.show_number(pins.digital_read_pin(DigitalPin.P3))
        print(x)
basic.forever(on_forever)
