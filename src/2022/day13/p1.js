const readFileSync = require('fs').readFileSync
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/).filter(line => line !== '')

const allPackets = [];
instructions.forEach(line => {
    allPackets.push(JSON.parse(line))
})

//returns true if left is in the correct position
const comparePair = (left, right) => {

    for (let i = 0; i < left.length; i++) {

        //true = int, false = array
        const leftIsInt = Number.isInteger(left[i])
        const rightIsInt = Number.isInteger(right[i])

        //if right has run out
        if (right[i] === undefined) {
            return false
        }

        //both numbers

        if (leftIsInt && rightIsInt) {

            //correct order
            if (left[i] < right[i]) {
                return true
                //wrong order
            } else if (left[i] > right[i]) {
                return false
            }
            //same number

            //both arrays
        } else if (!leftIsInt && !rightIsInt) {

            //recursive step - returns true/false if resolved, or null if carrying on
            const resolved = comparePair(left[i], right[i])

            if (resolved !== null) {
                return resolved
            }

            //one is an array
        } else {

            //left is an array
            if (!leftIsInt) {

                const resolved = comparePair(left[i], [right[i]])

                if (resolved !== null) {
                    return resolved
                }

                //right is an array
            } else {

                const resolved = comparePair([left[i]], right[i])

                if (resolved !== null) {
                    return resolved
                }
            }
        }
    }

    if (left.length < right.length) {
        return true
    }

    //if same length return 'carry on'
    if (left.length === right.length) {
        return null

    }
}


let sum = 0;

allPackets.forEach((singlePacket, index) => {

    if (index % 2 === 0) {

        if (comparePair(singlePacket, allPackets[index + 1])) {
            sum += Math.floor(index / 2) + 1
        }
    }
})

console.log(sum)
