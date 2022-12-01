const readFileSync = require('fs').readFileSync;

//get file as one string
const data = readFileSync('./test-input.txt', 'utf8')

//split string into array of strings at end of line
const lines = data.split(/\r?\n/);

const highestAndCurrentObj = lines.reduce((currVals, currSnack) => {

    if (currSnack === "") {

        if (currVals.currElf > currVals.highest) {

            currVals.highest = currVals.currElf
        }

        currVals.currElf = 0

        return currVals

    } else {

        currVals.currElf += parseInt(currSnack)

        return currVals

    }
}, {highest: 0, currElf: 0})

console.log(highestAndCurrentObj.highest);