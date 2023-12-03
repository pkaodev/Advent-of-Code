const readFileSync = require('fs').readFileSync
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/)

//test
// const LCM = BigInt(23 * 19 * 13 * 17)

const LCM = BigInt(2 * 17 * 7 * 11 * 19 * 5 * 13 * 3)


function primeFactors(n) {
    const factors = [];
    let divisor = BigInt(2);
  
    while (n >= 2) {
        // console.log(n)
      if (n % divisor == 0) {
        factors.push(divisor);
        n = n / divisor;
      } else {
        divisor++;
      }
    }
    return factors;
  }

class Monkey {
    constructor({ startingItems, operation, test, trueResult, falseResult, name }) {
        this.items = startingItems.map(x => BigInt(x))
        this.operation = operation
        if (this.operation[1] !== 'old') this.operation[1] = BigInt(this.operation[1])
        this.test = BigInt(test)
        this.trueResult = trueResult
        this.falseResult = falseResult
        this.numberOfItemsInspected = 0
        this.name = name
    }
    takeTurn = (monkeyArray) => {
        while (this.items.length) {
            this.numberOfItemsInspected++

            if (this.operation[1] === 'old') {
                if (this.operation[0] === '*') {
                    this.items[0] = this.items[0] * this.items[0]
                } else {
                    this.items[0] = this.items[0] + this.items[0]
                }
            
            } else {
                if (this.operation[0] === '*') {
                    this.items[0] = this.items[0] * this.operation[1]
                } else {
                    this.items[0] = this.items[0] + this.operation[1]
                }
            }

            this.items[0] = this.items[0] % LCM

                if(this.items[0] % this.test === 0n) {
                monkeyArray[this.trueResult].items.push(this.items.shift())
            } else {
                monkeyArray[this.falseResult].items.push(this.items.shift())
            }
        }
    }
}

function createInitialMonkeys(inputLineByLine) {
    const initialState = []
    let currentMonkey
    let name = -1
    inputLineByLineLoop:
    for (let lineNum = 0; lineNum < inputLineByLine.length; lineNum++) {
        switch (lineNum % 7) {
            case 0:
                name++
                currentMonkey = {}
                currentMonkey.name = name
                break
            case 1:
                currentMonkey.startingItems = inputLineByLine[lineNum].trim().split(' ').splice(2).map(x => parseInt(x))
                break
            case 2:
                currentMonkey.operation = inputLineByLine[lineNum].trim().split(' ').splice(4)
                break
            case 3:
                currentMonkey.test = parseInt(inputLineByLine[lineNum].trim().split(' ').splice(3)[0])
                break
            case 4:
                currentMonkey.trueResult = parseInt(inputLineByLine[lineNum].trim().split(' ').splice(5)[0])
                break
            case 5:
                currentMonkey.falseResult = parseInt(inputLineByLine[lineNum].trim().split(' ').splice(5)[0])
                initialState.push(new Monkey(currentMonkey))
                break
        }
    }
    return initialState
}
const monkeyState = createInitialMonkeys(instructions)
let round = 0
while (round < 10000) {
    round++
    console.log('round: ',round)
    monkeyState.forEach(monkey => {
        monkey.takeTurn(monkeyState)
    })
}
let resultsArray = []
monkeyState.forEach(monkey => {
    resultsArray.push(monkey.numberOfItemsInspected)
})

// console.log(monkeyState)
resultsArray.sort((a, b) => b - a)
// console.log(resultsArray)
console.log(resultsArray[0] * resultsArray[1])

