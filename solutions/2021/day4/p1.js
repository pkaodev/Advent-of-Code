const readFileSync = require('fs').readFileSync
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/)

const bingoNumbers = instructions.shift().split(',')
console.log(bingoNumbers)

const bingoCards = [];

instructions.forEach(line => {
    if (line === '') {
        bingoCards.unshift([])
    } else {
        bingoCards[0].push(line.split(' ').filter(x => x !== '').map(x => parseInt(x)))
    }
})

console.log(bingoCards)

let won = false;

let wonIndices = new Set();
let generation = 0;
let currentNumber;

while(!(wonIndices.size === bingoCards.length)) {
    generation++;

    currentNumber = parseInt(bingoNumbers.shift());

    bingoCards.forEach(card => {
        card.forEach(row => {
            row.forEach((cell, index) => {
                if (cell === currentNumber) {    
                    row[index] = `X${cell}`
                }
            })
        })
    })


bingoCards.forEach((card, index) => {
    card.forEach(row => {
        if (row.every(cell => cell[0] === 'X')) {
            wonIndices.add(index)
            console.log('won')
        }
    })

    for (let i = 0; i < card[0].length; i++) {
        if (card[0][i][0] === 'X' && card[1][i][0] === 'X' && card[2][i][0] === 'X' && card[3][i][0] === 'X' && card[4][i][0] === 'X') {
            console.log('won')
            wonIndices.add(index)
        }
    }
})
    

}

console.log('generation', generation)
console.log(wonIndices)
let wonIndices2 = Array.from(wonIndices)
console.log(wonIndices2)
let lastWinner = bingoCards[wonIndices2[0]]
console.log(lastWinner)
console.log('currentNumber: ', currentNumber)
//find sum of non  X cells in lastWinner
let sum = 0;
lastWinner.forEach(row => {
    row.forEach(cell => {
        if (cell[0] !== 'X') {
            sum += parseInt(cell)
        }
    })
}
)
console.log(sum)
console.log(sum * currentNumber)




