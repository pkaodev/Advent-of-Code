const readFileSync = require('fs').readFileSync;
const lines = readFileSync('./input.txt', 'utf8').split(/\n/)

//create boxState
const setupEndIndex = lines.indexOf('') - 1
const boxState = [];

for (let i = 0; i < setupEndIndex; i++) {
    for (let j = 0; j < lines[i].length; j+=4) {
        
        if (i === 0) {
            boxState.push([])
        }

        if (lines[i][j+1] !== ' ') {
             boxState[Math.ceil(j / 4)] = boxState[Math.ceil(j / 4)] + lines[i][j+1]
        }
    }
}


//2 move
for (let i = setupEndIndex + 2; i < lines.length; i++) {

    const [howMany, from, to] = lines[i].split(' ').filter(value => !isNaN(parseInt(value)))

    //part 1
    // for (let j = 0; j < howMany; j++) {
    //     boxState[to-1] = boxState[from-1][0] + boxState[to-1]
    //     boxState[from-1] = boxState[from-1].slice(1)
    // }

    //part 2
    boxState[to-1] = boxState[from-1].slice(0, howMany) + boxState[to-1]
    boxState[from-1] = boxState[from-1].slice(howMany)

}

//3 get solution
const solution = boxState.reduce((acc, column) => acc + column[0], '')
console.log(solution)