const readFileSync = require('fs').readFileSync;
const lines = readFileSync('./input.txt', 'utf8').split(/\n/)

let width = lines.length;

const scenicScores = [];

//for every tree
for (let y = 1; y < width - 1; y++) {
    outerLoop:
    for (let x = 1; x < width - 1; x++) {

        let currScenic = 1;

        //to above
        innerLoopAbove:
        for (let y2 = y - 1; y2 >= 0; y2--) {

            if (lines[y2][x] >= lines[y][x] || y2 === 0) {
                currScenic *= (y-y2)
                break innerLoopAbove;
            }
        }

        //to below
        innerLoopBelow:
        for (let y2 = y + 1; y2 < width; y2++) {

            if (lines[y2][x] >= lines[y][x] || y2 === width - 1) {
                currScenic *= (y2-y)
                break innerLoopBelow;
            }
        }

        //to right
        innerLoopRight:
        for (let x2 = x + 1; x2 < width; x2++) {

            if (lines[y][x2] >= lines[y][x] || x2 === width - 1) {
                currScenic *= (x2-x)
                break innerLoopRight;
            }
        }

        //to left
        innerLoopLeft:
        for (let x2 = x - 1; x2 >= 0; x2--) {

            if (lines[y][x2] >= lines[y][x] || x2 === 0) {
                currScenic *= (x - x2)
                break innerLoopLeft;
            }
        }

        scenicScores.push(currScenic)
    }
}

scenicScores.sort((a, b) => b - a)

console.log(scenicScores[0])