const readFileSync = require('fs').readFileSync
const instructions = readFileSync('./input-test.txt', 'utf8').split(/\n/)

// console.log(instructions)
const primeProduct = 23 * 19 * 13 * 17
class Monkey {
    constructor({ startingItems, operation, test, trueResult, falseResult, name }) {
        this.items = startingItems
        this.operation = operation
        this.test = test
        this.trueResult = trueResult
        this.falseResult = falseResult
        this.numberOfItemsInspected = 0
        this.name = name
    }

    takeTurn = (monkeyArray) => {
        console.log(`Monkey ${this.name} is taking a turn`)

        while (this.items.length) {

            this.numberOfItemsInspected++

            console.log(`is inspecting item ${this.items[0]}`)


            //use operation and boredom to get new worry level of item
            if (this.operation[1] === 'old') {
                this.items[0] = Math.floor(eval(`${this.items[0]} ${this.operation[0]} ${this.items[0]}`) / 3)
            } else {
                this.items[0] = Math.floor(eval(`${this.items[0]} ${this.operation.join(' ')}`) / 3)
            }

            this.items[0] = this.items[0] % primeProduct

            if (this.items[0] % this.test === 0) {
                //true throw
                monkeyArray[this.trueResult].items.push(this.items.shift())
            } else {
                //false throw
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

console.log(monkeyState)
console.log(`----------------------------------------------------------------`)

while (round < 20) {
    round++

    monkeyState.forEach(monkey => {
        monkey.takeTurn(monkeyState)
    })




}

console.log(monkeyState)

//get result
let resultsArray = []
monkeyState.forEach(monkey => {
    resultsArray.push(monkey.numberOfItemsInspected)
})

resultsArray.sort((a, b) => b - a)
console.log(resultsArray)
console.log(resultsArray[0] * resultsArray[1])