const readFileSync = require('fs').readFileSync;
const line = readFileSync('./input.txt', 'utf8').split(/\n/)[0]

//part 1
// const segmentSize = 4;
//part 2
const segmentSize = 14;

for (let i = 0; i < line.length + 1 - segmentSize; i++) {
    if (new Set(line.slice(i, i + segmentSize).split('')).size === segmentSize) {
        console.log(i + 14)
        break
    }
}