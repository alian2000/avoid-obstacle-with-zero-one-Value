basic.show_icon(IconNames.HAPPY)

def on_forever():
    if mbit_Robot.Avoid_Sensor(mbit_Robot.enAvoidState.OBSTACLE):
        basic.show_number(pins.digital_read_pin(DigitalPin.P3))
        x=pins.digital_read_pin(DigitalPin.P0)
        print(x)
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_SPINLEFT, 100)
        basic.pause(400)
    else:
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, 200)
        basic.show_number(pins.digital_read_pin(DigitalPin.P3))
        print(x)
basic.forever(on_forever)
