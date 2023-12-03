const readFileSync = require('fs').readFileSync;
const line = readFileSync('./input.txt', 'utf8').split(/\n/)[0]

for (let i = 0; i < line.length-3; i++) {
    if (new Set(line.slice(i, i+4).split('')).size === 4) {
        console.log(i + 4)
        break
    }
}