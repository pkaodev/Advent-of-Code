const readFileSync = require('fs').readFileSync;
const lines = readFileSync('./input.txt', 'utf8').split(/\n/)

let sum1 = 0;
let sum2 = 0;

lines.forEach(line => {
    const [elfA, elfB] = line.split(',')

    const [aL, aH] = elfA.split('-').map(string => parseInt(string))
    const [bL, bH] = elfB.split('-').map(string => parseInt(string))


    if ( (aL <= bL && aH >= bH ) || (bL <= aL && bH >= aH) ) {
        sum1++
    }

    if (!(bL > aH || aL > bH)) {
        sum2++
    }
})

console.log(sum1)
console.log(sum2)