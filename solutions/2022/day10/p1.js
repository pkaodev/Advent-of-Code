const readFileSync = require('fs').readFileSync
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/)

let cycle = 0
let register = 1
let signalStrengthSum = 0

let CPUInstructions = []

instructions.forEach(line => {
    const [instructionName, ...addedValue] = line.split(' ')

    if (instructionName === 'noop') {
        CPUInstructions.push(() => cycle++)
        CPUInstructions.push(() => {
            if (cycle % 40 === 20) {
                signalStrengthSum += cycle * register
            }
        })
    } else {
        CPUInstructions.push(() => cycle++)
        CPUInstructions.push(() => {
            if (cycle % 40 === 20) {
                signalStrengthSum += cycle * register
            }
        })
        CPUInstructions.push(() => cycle++)
        CPUInstructions.push(() => {
            if (cycle % 40 === 20) {
                signalStrengthSum += cycle * register
            }
        })
        CPUInstructions.push(() => register += parseInt(addedValue))
    }
})

//main loop

while (CPUInstructions.length) {
    
    CPUInstructions.shift()()

    // if (cycle % 40 === 20) {
    //     signalStrengthSum += cycle * register
    // }
    // console.log('cycle', cycle, 'register', register, 'signalStrength', cycle * register)

}

console.log(signalStrengthSum)


//signal strength = cycle * register value
//DURING 20th cycle and every 40 cycles after that
