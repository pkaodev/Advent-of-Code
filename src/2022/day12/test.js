//generic loop through 2D array
const loop2D = (yMax, xMax, callback) => {
    loopY:
    for (let y = 0; y < yMax; y++) {
        loopX:
        for (let x = 0; x < xMax; x++) {
            callback(y, x, loopY, loopX)
        }
    }
}