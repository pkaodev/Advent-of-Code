// const utils = require('../../../lib/lang-utils/javascript/utils.js')
const { endianness } = require('os')
const {submit} = require('../../../lib/aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input')
const data = readFileSync(inputPath, 'utf8')

//convert into array of array of chars
const zone = data.split(/\n/).map(row=>row.split(''))

// console.log(zone)

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

const northZone = tiltNorth(zone).map(row=>row.join(''))

for (const row of northZone) {
    console.log(row)
}

// console.log(northZone)

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

const SOLUTION_1 = scoreZone(northZone)

module.exports = {}

// submit(SOLUTION_1)

console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example solution: 136