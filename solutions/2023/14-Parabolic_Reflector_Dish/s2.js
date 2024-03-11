// const utils = require('../../../lib/lang-utils/javascript/utils.js')
const { endianness } = require('os')
const {submit} = require('../../../lib/aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input_example')
const data = readFileSync(inputPath, 'utf8')

let zone = data.split(/\n/).map(row=>row.split(''))

function tiltNorth(zone) {
    //move rocks in each row, from north to south
    // ignore top row
    for (let i=1; i<zone.length; i++) {
        //each rock
        for (let j=0; j<zone[i].length; j++) {
            //ignore non rolling rocks
            if (zone[i][j] !== 'O') {
                continue
            }

            const newI = findMostNorthernFreeSpace(zone, i, j)

            if (newI !== i) {
                zone[newI][j] = 'O'
                zone[i][j] = '.'

            }
        }
    }

    return zone
}

function findMostNorthernFreeSpace(zone, startI, startJ) {
    let endI = startI
    while (true) {
        endI--
        if (zone[endI][startJ] !== '.') {
            return ++endI
        }
        if (endI === 0) {
            return 0
        }
    }
}

function scoreZone(zone) {
    const topRowPoints = zone.length

    let score = 0

    for (let i=0; i<zone.length; i++) {
        for (let j=0; j<zone[i].length; j++) {
            if (zone[i][j] === 'O') {
                score += topRowPoints - i
            }
        }
    }
    return score
}

function rotateClockwise(zone) {
    const newZone = new Array(zone[0].length)

    //new first row (left->right) is old first column (bot->top)

    // create new row by reading each column from the bottom
    for (let j=0; j<zone[0].length; j++) {
        let newRow = ''
        for (let i=zone.length-1; i>=0; i--) {
            newRow += zone[i][j]
        }
        newZone[j] = newRow.split('')
    }

    return newZone
}

// for (let row of zone) {
//     row = row.join('')
//     console.log(row)
// }

// console.log()
// zone = rotateClockwise(zone)

// for (let row of zone) {
//     // row = row.join('')
//     console.log(row)
// }

function solve2(zone) {
    let zone2 = zone
    // for (let cycle=0; cycle<1; cycle++) {
    for (let cycle=0; cycle<1000000000; cycle++) {
        if (cycle % 100000 === 0) {
            console.log(cycle)
        }


        zone2 = tiltNorth(zone2)
        zone2 = rotateClockwise(zone2)
        // printZone(zone2)
        
        zone2 = tiltNorth(zone2)
        zone2 = rotateClockwise(zone2)
        // printZone(zone2)
        
        zone2 = tiltNorth(zone2)
        zone2 = rotateClockwise(zone2)
        // printZone(zone2)

        zone2 = tiltNorth(zone2)
        zone2 = rotateClockwise(zone2)
        // printZone(zone2)

    }
    solution2 = scoreZone(zone2)
    return solution2
}

function printZone(zone) {
    for (let row of zone) {
        console.log(row.join(''))
        }
        console.log()
}

const SOLUTION_2 = solve2(zone)

console.log(`SOLUTION_2: ${SOLUTION_2}`)
// Example solution: 136