input.onButtonPressed(Button.A, function () {
    worp = randint(1, 6)
    basic.showNumber(worp)
    totaal += worp
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(totaal)
})
let worp = 0
let totaal = 0
music.playMelody("C5 A B G A F G E ", 225)
basic.showIcon(IconNames.Yes)
totaal = 0
