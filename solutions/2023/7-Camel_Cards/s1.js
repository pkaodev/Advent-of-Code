const utils = require('../../../language-setups/javascript/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input_example')
const data = readFileSync(inputPath, 'utf8')

parseInput = (data) => {
    const lines = data.split(/\n/)

   const  handBets = lines.map(line=>line.split(' ')).map(handBet=>[handBet[0],Number(handBet[1])])

    return handBets
}

// strong -> weak
const handStrength = ["five", "four", "full", "three", "two", "one", "high"]
const cardStrength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

getHandType = (hand) => {
// assumes hand is length 5 and valid

    if (/(.)\1{4}/.test(hand)) {
        return 'five'
    } else if (/(.).*\1.*\1.*\1/.test(hand)) {
        return 'four'
    } else if (//.test(hand)) {
        return 'full'
    } else if () {
        return 'three'
    } else if () {
        return 'two'
    } else if () {
        return 'one'
    } else {
        return 'high'
    }
}

const handBets = parseInput(data)
console.log(handBets)

// sort by strength of hand weak->strong
// multiply index+1 by bet
// sum









const SOLUTION_1 = undefined

console.log(`SOLUTION_1: ${SOLUTION_1}`)
// Example solution: 6440

module.exports = {parseInput, getHandType}