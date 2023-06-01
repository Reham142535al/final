input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
})
input.onGesture(Gesture.Shake, function () {
    for (let _1 = 0; _1 <= 10; _1++) {
        basic.showNumber(_1)
    }
})
input.onButtonPressed(Button.AB, function () {
    if (Gread >= 90) {
        basic.showString("excellent")
    } else if (Gread >= 50) {
        basic.showString("Pass")
    } else {
        basic.showString("Fail")
    }
})
input.onButtonPressed(Button.B, function () {
    X += 1
    basic.showNumber(X)
})
let X = 0
let Gread = 0
Gread = 50
basic.showString("Reham Masoud")
