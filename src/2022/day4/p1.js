const readFileSync = require('fs').readFileSync;
const lines = readFileSync('./input.txt', 'utf8').split(/\n/)

let sum1 = 0;

lines.forEach(line => {
    const [elf1, elf2] = line.split(',')

    const [aL, aH] = elf1.split('-').map(string => parseInt(string))
    const [bL, bH] = elf2.split('-').map(string => parseInt(string))

    if ( (aL <= bL && aH >= bH ) || (bL <= aL && bH >= aH) ) {
        sum1++
    }
})

console.log(sum1)