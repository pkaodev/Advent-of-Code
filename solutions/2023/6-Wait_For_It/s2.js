const utils = require('../../../language-setups/javascript/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input')
const data = readFileSync(inputPath, 'utf8')
const lines = data.split(/\n/)

const [times, distances] = lines.map(line => line.split(/:\s*/)[1].split(/\s+/).join('').split(' ').map(Number))

function findSolution2(raceTime, winDistance) {

    const sol1 = (-raceTime + Math.sqrt((raceTime**2) - (4*winDistance))) / -2
    const sol2 = (-raceTime - Math.sqrt((raceTime**2) - (4*winDistance))) / -2

    return Math.floor(Math.abs(sol1-sol2))
}

// function beatsRecord(raceTime, recordDistance, timePressed) {
//     const speed = timePressed
//     const distanceTravelled = speed * (raceTime - timePressed)
//     return distanceTravelled > recordDistance
// }

// function findRaceWinPossibilities(raceTime, recordDistance) {
//     let raceWinPossibilities = 0

//     for (let timePressed = 0; timePressed <= raceTime; timePressed++) {
//         if (beatsRecord(raceTime, recordDistance, timePressed)) {
//             raceWinPossibilities++
//         }
//     }

//     return raceWinPossibilities
// }

// function findSolution2(times, distances) {
//     const winPossibilities = []

//     for (let i = 0; i < times.length; i++) {
//         winPossibilities.push(findRaceWinPossibilities(times[i], distances[i]))
//     }

//     return winPossibilities.reduce((p, c) => p * c, 1)
// }

const SOLUTION_2 = findSolution2(times, distances)

console.log(`SOLUTION_2: ${SOLUTION_2}`)
// Example Solution: 288
