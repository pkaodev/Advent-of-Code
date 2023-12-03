const readFileSync = require('fs').readFileSync;
const lines = readFileSync('./input.txt', 'utf8').split(/\n/)

let width = lines.length;

let visibleTrees = 0;

//add edge trees
visibleTrees += 4 * width - 4;

//for every tree
for (let y = 1; y < width - 1; y++) {
    outerLoop:
    for (let x = 1; x < width - 1; x++) {

        //above
        innerLoopAbove:
        for (let y2 = 0; y2 < y; y2++) {

            if (lines[y2][x] >= lines[y][x]) {
                break innerLoopAbove;
            }


            if (y2 === y - 1) {
                visibleTrees++;
                continue outerLoop;
            }
        }

        //below
        innerLoopBelow:
        for (let y2 = y + 1; y2 < width; y2++) {

            if (lines[y2][x] >= lines[y][x]) {
                break innerLoopBelow;
            }

            if (y2 === width - 1) {
                visibleTrees++;
                continue outerLoop;
            }
        }

        //Right
        innerLoopRight:
        for (let x2 = x + 1; x2 < width; x2++) {

            if (lines[y][x2] >= lines[y][x]) {
                break innerLoopRight;
            }

            if (x2 === width - 1) {
                visibleTrees++;
                continue outerLoop;
            }
        }

        //Left
        innerLoopLeft:
        for (let x2 = 0; x2 < x; x2++) {

            if (lines[y][x2] >= lines[y][x]) {
                break innerLoopLeft;
            }

            if (x2 === x - 1) {
                visibleTrees++;
                continue outerLoop;
            }
        }


    }
}

console.log(visibleTrees)