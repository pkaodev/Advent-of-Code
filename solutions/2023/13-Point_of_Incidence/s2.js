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

// change to find multiple solutions
function findCommonNums(arrArr) {

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

    const solutions = []

    // assume there is only one solution
    for (const numCount of Object.entries(numCounts)) {
        if (numCount[1] === arrArr.length) {
            solutions.push(Number(numCount[0]))
        }
    }

    return solutions
}


// part 2
function getPatternValue(pattern) {
    colSyms = getPatternColSyms(pattern)
    rowSyms = getPatternRowSyms(pattern)
    colNums = findCommonNums(colSyms)
    rowNums = findCommonNums(rowSyms)

    if (!colNums && !rowNums) {
        // no solutions at all
        return false
    }

    valObj = {
        colNums,
        rowNums
    }

    return valObj
}

function part2(pattern) {
    // get original reflection value (NEW HAS TO BE DIFFERENT)
    orgValObj = getPatternValue(pattern)

    
    // swap each value
    for (let i = 0; i < pattern.length; i++) {
        for (let j = 0; j < pattern[i].length; j++) {
            const patternCopy = structuredClone(pattern)

            const newRowArr = patternCopy[i].split('')
            const currChar = newRowArr[j]
            if (currChar === '#') {
                newRowArr[j] = '.'
            } else {
                newRowArr[j] = '#'
            }
            const newRowStr = newRowArr.join('')

            patternCopy[i] = newRowStr // smudged patternCopy is ready now

            newValObj = getPatternValue(patternCopy)
            // check if sym line exists -> if diff then solution find -> same or none continue
            if (newValObj.colNums.length || newValObj.rowNums.length) {
                // how can i do a deep comparison between nested reference by value objects
                if (JSON.stringify(newValObj) != JSON.stringify(orgValObj)) {
                    console.log('org', orgValObj)
                    console.log('new', newValObj)
                    console.log(Boolean(newValObj.colNums), Boolean(newValObj.rowNums))
                    // find the new line of symmetry
                    for (const val of newValObj['colNums']) {
                        if (!orgValObj['colNums'].includes(val)) {
                            console.log(val)
                            return Number(val)
                        }
                    }

                    for (const val of newValObj['rowNums']) {
                        if (!orgValObj['rowNums'].includes(val)) {
                            console.log(val)
                            return Number(val * 100)
                        }
                    }

                    
                    return 1
                }
            }
        }
    }
}

SOLUTION_2 = 0

for (const pattern of patterns) {
    SOLUTION_2 += part2(pattern)
}


module.exports = {}


// Example solution: 405
console.log(`SOLUTION_2: ${SOLUTION_2}`)

// submit(SOLUTION_1)