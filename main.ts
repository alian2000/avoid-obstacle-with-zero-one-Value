basic.showIcon(IconNames.Happy)
basic.forever(function () {
    let x: number;
if (mbit_Robot.Avoid_Sensor(mbit_Robot.enAvoidState.OBSTACLE)) {
        basic.showNumber(pins.digitalReadPin(DigitalPin.P3))
        console.log(x)
    } else {
        basic.showNumber(pins.digitalReadPin(DigitalPin.P3))
        console.log(x)
    }
})
