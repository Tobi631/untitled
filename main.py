def on_forever():
    basic.show_icon(IconNames.HEART)
    music.play_melody("C E F A G E F C ", 273)
    music.play_melody("E G E F E D F D ", 263)
    basic.show_string("\"happy Valentines\"")
basic.forever(on_forever)
