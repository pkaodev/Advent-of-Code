const readFileSync = require('fs').readFileSync
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/).filter(line => line !== '')

const allPackets = [];
instructions.forEach(line => {
    allPackets.push(JSON.parse(line))
})

//returns true if in correct positions
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

const result = allPackets.reduce((prev, curr, index) => {

    if (index % 2 === 0) {
        
        if (comparePair(curr, allPackets[index + 1])) {
            return prev + Math.floor(index / 2) + 1
        }
    }
    return prev
}, 0)

console.log('result 1: ', result)


//part 2
allPackets.push([[2]], [[6]])

const bubbleSort = (arr) => {

    let sorted = false

    while (!sorted) {

        sorted = true

        for (let i = 0; i < arr.length - 1; i++) {

            if (!comparePair(arr[i], arr[i + 1])) {

                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]
                sorted = false
            }
        }
    }
}

bubbleSort(allPackets)

const result2 = allPackets.reduce((prev, curr, index) => {

    if (JSON.stringify(curr) === '[[2]]' || JSON.stringify(curr) === '[[6]]') {
        return prev * (index + 1)
    }

    return prev

}, 1)

console.log('part 2: ', result2)

