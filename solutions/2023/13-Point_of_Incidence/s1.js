// const utils = require('../../../lib/lang-utils/javascript/utils.js')
const {submit} = require('../../../lib/aoc-utils/utils.js')
const path = require('path')
const readFileSync = require('fs').readFileSync
const inputPath = path.join(__dirname, 'input')
const data = readFileSync(inputPath, 'utf8')
const lines = data.split(/\n/)

// make array of each pattern (array of strings)
const patterns = [[]]
for (let i = 0; i < lines.length; i++) {
    if (lines[i] === '') {
        patterns.push([])
        continue
    }
    patterns[patterns.length - 1].push(lines[i])
}

// move first element of rightArr to end of leftArr
// mutates
function moveArrVal(leftArr, rightArr) {
    if (!rightArr.length) {
        throw Error('nothing to move')
    }
    leftArr.push(rightArr.shift())
}

function isSymPossible(leftArr, rightArr) {
    const minLen = Math.min(leftArr.length, rightArr.length)
    for (i = 0; i < minLen; i++) {
        if (leftArr[leftArr.length - 1 - i] !== rightArr[i]) {
            return false
        }
    }
    return true
}

// return arr of possible lines of sym (num chars left/above)
function checkLineSym(rowCol) {
    right = rowCol.split('')
    left = []
    possibleSyms = []
    while (right.length - 1) {
        moveArrVal(left, right)
        if (isSymPossible(left, right)) {
            possibleSyms.push(left.length)
        }
    }
    return possibleSyms
}

function getPatternColSyms(pattern) {
    syms = []
    for (const row of pattern) {
        syms.push(checkLineSym(row))
    }
    return syms
}

function getPatternRowSyms(pattern) {
    syms = []
    for (let i = 0; i < pattern[0].length; i++) {
        col = ''
        for (let j = 0; j < pattern.length; j++) {
            col = col + pattern[j][i]
        }
        syms.push(checkLineSym(col))
    }
    return syms
}

function findCommonNum(arrArr) {

    numCounts = arrArr.reduce((countObj, currArr) => {
        currArr.forEach(num => {
            if (countObj[num]) {
                countObj[num]++
            } else {
                countObj[num] = 1
            }
        })
        return countObj
    }, {})

    // assume there is only one solution
    for (const numCount of Object.entries(numCounts)) {
        if (numCount[1] === arrArr.length) {
            return Number(numCount[0])
        }
    }
}

let SOLUTION_1 = 0

for (const pattern of patterns) {
    colSyms = getPatternColSyms(pattern)
    rowSyms = getPatternRowSyms(pattern)

    colNum = findCommonNum(colSyms)
    rowNum = findCommonNum(rowSyms)

    if (colNum) {
        SOLUTION_1 += colNum
    }

    if (rowNum) {
        SOLUTION_1 += (rowNum * 100)
    }

}

// console.log(findCommonNum(getPatternColSyms(patterns[0])))

// const SOLUTION_1 = undefined

module.exports = {}


// Example solution: 405
console.log(`SOLUTION_1: ${SOLUTION_1}`)

submit(SOLUTION_1)