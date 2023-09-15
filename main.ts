basic.showIcon(IconNames.Happy)
basic.forever(function on_forever() {
    let x: number;
    if (mbit_Robot.Avoid_Sensor(mbit_Robot.enAvoidState.OBSTACLE)) {
        basic.showNumber(pins.digitalReadPin(DigitalPin.P3))
        x = pins.digitalReadPin(DigitalPin.P0)
        console.log(x)
        mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_SpinLeft, 100)
        basic.pause(400)
    } else {
        mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Run, 200)
        basic.showNumber(pins.digitalReadPin(DigitalPin.P3))
        console.log(x)
    }
    
})
