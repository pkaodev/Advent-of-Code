const readFileSync = require('fs').readFileSync;
const lines = readFileSync('./input.txt', 'utf8').split(/\n/)

const getPriority = (letter) => {
    const char = letter.charCodeAt(0)

    if (char < 91) return char - 38
    
    return char - 96
}

let sum = 0;

for (let i = 0; i < lines.length; i++) {

    const secondHalf = lines[i].substring(lines[i].length / 2)
    
    for (let j = 0; j < (lines[i].length / 2); j++) {

        if (secondHalf.includes(lines[i][j])) {
            sum += getPriority(lines[i][j])
            break
        }
    }
}

console.log(sum)