// const utils = require('../../../templates/javascript/utils.js')
const { endianness } = require('os')
const { submit } = require('../../../lib/aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input_example')
const data = readFileSync(inputPath, 'utf8')

let zone = data.split(/\n/).map(row => row.split(''))

function tiltNorth(zone) {
    for (let i = 1; i < zone.length; i++) {
        for (let j = 0; j < zone[i].length; j++) {
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
function tiltSouth(zone) {
    for (let i = zone.length - 2; i >= 0; i--) {
        for (let j = 0; j < zone[i].length; j++) {
            if (zone[i][j] !== 'O') {
                continue
            }

            const newI = findMostSouthernFreeSpace(zone, i, j)

            if (newI !== i) {
                zone[newI][j] = 'O'
                zone[i][j] = '.'

            }
        }
    }

    return zone
}
function tiltWest(zone) {
    for (let j = 1; j < zone[0].length; j++) {
        for (let i = 0; i < zone.length; i++) {
            if (zone[i][j] !== 'O') {
                continue
            }

            const newJ = findMostWesternFreeSpace(zone, i, j)

            if (newJ !== j) {
                zone[i][newJ] = 'O'
                zone[i][j] = '.'

            }
        }
    }
    return zone
}
function tiltEast(zone) {
    for (let j = zone[0].length - 2; j >= 0; j--) {
        for (let i = 0; i < zone.length; i++) {
            if (zone[i][j] !== 'O') {
                continue
            }

            const newJ = findMostEasternFreeSpace(zone, i, j)

            if (newJ !== j) {
                zone[i][newJ] = 'O'
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
function findMostSouthernFreeSpace(zone, startI, startJ) {
    let endI = startI
    while (true) {
        endI++
        if (zone[endI][startJ] !== '.') {
            return --endI
        }
        if (endI === zone.length - 1) {
            return zone.length - 1
        }
    }
}
function findMostWesternFreeSpace(zone, startI, startJ) {
    let endJ = startJ
    while (true) {
        endJ--
        if (zone[startI][endJ] !== '.') {
            return ++endJ
        }
        if (endJ === 0) {
            return 0
        }
    }
}
function findMostEasternFreeSpace(zone, startI, startJ) {
    let endJ = startJ
    while (true) {
        endJ++
        if (zone[startI][endJ] !== '.') {
            return --endJ
        }
        if (endJ === 0) {
            return 0
        }
    }
}

function scoreZone(zone) {
    const topRowPoints = zone.length

    let score = 0

    for (let i = 0; i < zone.length; i++) {
        for (let j = 0; j < zone[i].length; j++) {
            if (zone[i][j] === 'O') {
                score += topRowPoints - i
            }
        }
    }
    return score
}

// function rotateClockwise(zone) {
//     const newZone = new Array(zone[0].length)

//     //new first row (left->right) is old first column (bot->top)

//     // create new row by reading each column from the bottom
//     for (let j=0; j<zone[0].length; j++) {
//         let newRow = ''
//         for (let i=zone.length-1; i>=0; i--) {
//             newRow += zone[i][j]
//         }
//         newZone[j] = newRow.split('')
//     }

//     return newZone
// }

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
    let oldState = JSON.stringify(zone)
    // for (let cycle=0; cycle<1; cycle++) {
    for (let cycle = 0; cycle < 1000000000; cycle++) {

        zone = tiltNorth(zone)
        // printZone(zone)

        zone = tiltWest(zone)
        // printZone(zone)

        zone = tiltSouth(zone)
        // printZone(zone)

        zone = tiltEast(zone)
        // printZone(zone)
        if (cycle % 10000000 === 0) {
            printZone(zone)
            console.log(cycle / 10000000, '%')
        }

        const newState = JSON.stringify(zone)
        if (newState === oldState) {
            break
        } else {
            oldState = newState
        }
    }
    solution2 = scoreZone(zone)
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