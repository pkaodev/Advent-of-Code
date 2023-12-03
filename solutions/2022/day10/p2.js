const readFileSync = require('fs').readFileSync
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/)

let cycle = 0
let register = 1


let outputString = ''
let outputArray = []

let CPUInstructions = []

instructions.forEach(line => {
    const [instructionName, ...addedValue] = line.split(' ')

    if (instructionName === 'noop') {
        CPUInstructions.push(() => cycle++)
        CPUInstructions.push(() => {
            if (cycle >= register && cycle <= register + 2) {
                outputString += '#'
            } else {
                outputString += '.'
            }
        })
    } else {
        CPUInstructions.push(() => cycle++)
        CPUInstructions.push(() => {
            if (cycle >= register && cycle <= register + 2) {
                outputString += '#'
            } else {
                outputString += '.'
            }
        })
        CPUInstructions.push(() => cycle++)
        CPUInstructions.push(() => {
            if (cycle >= register && cycle <= register + 2) {
                outputString += '#'
            } else {
                outputString += '.'
            }
        })
        CPUInstructions.push(() => register += parseInt(addedValue))
    }
})

//main loop

while (CPUInstructions.length) {

    CPUInstructions.shift()()

    if (outputString.length === 40) {
        outputArray.push(outputString)
        outputString = ''
        cycle -= 40
    }

}

console.log(outputString)
console.log(outputArray)




