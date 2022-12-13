const readFileSync = require('fs').readFileSync;

let oceanState = readFileSync('./input.txt', 'utf8').split(/\n/).map(x => x.split(''));
// const oceanState = [`...>>>>>...`].map(x => x.split(''));

// console.table(oceanState)
// console.log(`------------------------------------------------`)

const xLength = oceanState[0].length;
const yLength = oceanState.length;

let hasMoved = true;

let generation = 0;

while (hasMoved) {

    generation++;
    let oldState = JSON.stringify(oceanState)

    //-->east
    for (let y = 0; y < yLength; y++) {
        const addToLeft = oceanState[y][0] === '.' && oceanState[y][xLength - 1] === '>';

        for (let x = 0; x < xLength - 1; x++) {
            if (oceanState[y][x] === '>' && oceanState[y][(x + 1)] === '.') {
                oceanState[y][x] = '.';
                oceanState[y][x + 1] = '>';
                x++;
            }
        }

        if (addToLeft) {
            oceanState[y][0] = '>';
            oceanState[y][xLength - 1] = '.';
        }
    }

    //-->south
    for (let x = 0; x < xLength; x++) {
        const addToTop = oceanState[0][x] === '.' && oceanState[yLength - 1][x] === 'v';

        for (let y = 0; y < yLength - 1; y++) {
            if (oceanState[y][x] === 'v' && oceanState[(y + 1)][x] === '.') {
                oceanState[y][x] = '.';
                oceanState[y + 1][x] = 'v';
                y++;
            }
        }

        if (addToTop) {
            oceanState[0][x] = 'v';
            oceanState[yLength - 1][x] = '.';
        }
    }


    hasMoved = oldState !== JSON.stringify(oceanState)

    // console.log('generation: ', generation)
    // console.table(oceanState)
    // console.log(`------------------------------------------------`)

}

// console.table(oceanState)
console.log(generation)

