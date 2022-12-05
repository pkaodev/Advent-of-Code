const readFileSync = require('fs').readFileSync;

let oceanState = readFileSync('./input-test.txt', 'utf8').split(/\n/)

let oldState;

let xLength = oceanState[0].length;
let yLength = oceanState.length;

let generation = 0;

let hasMoved = false;

// while (hasMoved) {

    generation++;

    oldState = oceanState.map(x=>x);
    hasMoved = false;

    //-->east
    for (let y = 0; y < yLength; y++ ) {

        const leftTaken = oceanState[y][0] !== '.'

        for (let x = 0; x < xLength - 1; x++) {

            if (oceanState[y][x] === '>' && oceanState[y][(x+1)] === '.') {
                oceanState[y] = oceanState[y].slice(0, x) + `.>` + oceanState[y].slice(x+2, xLength);
                x++;
            }
        }

        if (oceanState[y][xLength - 1] === '>' && !leftTaken) {
            oceanState[y] = `>${oceanState[y].slice(0, xLength - 1)}.`;
        }
    }

    //-->south
    for (let x = 0; x < xLength; x++ ) {

        const topTaken = oceanState[0][x] !== '.'

        for (let y = 0; y < yLength - 1; y++) {

            if (oceanState[y][x] === 'v' && oceanState[(y+1)][x] === '.') {
                oceanState[y] = oceanState[y].slice(0, x) + `.` + oceanState[y].slice(x+1, xLength);
                oceanState[y+1] = oceanState[y+1].slice(0, x) + `v` + oceanState[y+1].slice(x+1, xLength);
                y++;
            }
        }
        

        if (oceanState[yLength - 1][x] === 'v' && !topTaken) {
            oceanState[yLength - 1] = oceanState[yLength - 1].slice(0, x) + `.` + oceanState[yLength - 1].slice(x+1, xLength);
            oceanState[0] = oceanState[0].slice(0, x) + `v` + oceanState[0].slice(x+1, xLength);
        }
    }




    if (JSON.stringify(oldState) !== JSON.stringify(oceanState)) {
        hasMoved = true;
    }

// }

// console.log(generation)
console.log(oceanState)