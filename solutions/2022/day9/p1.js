const readFileSync = require('fs').readFileSync;
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/)


const HCurr = { x: 0, y: 0 };
const TCurr = { x: 0, y: 0 };
const visited = ['0,0'];

const moveHead = {
    'U': () => { HCurr['y']++ },
    'R': () => { HCurr['x']++ },
    'D': () => { HCurr['y']-- },
    'L': () => { HCurr['x']-- }
}

const moveTail = {
    'U': () => { TCurr['y']++ },
    'R': () => { TCurr['x']++ },
    'D': () => { TCurr['y']-- },
    'L': () => { TCurr['x']-- }
}

const updateTail = () => {

    //positive is Head to the right
    const xDis = HCurr.x - TCurr.x;
    //positive is Head above
    const yDis = HCurr.y - TCurr.y;

    //stop if tail is adjacent to head
    if (Math.abs(xDis) <= 1 && Math.abs(yDis) <= 1) {
        return;
    }

    //moving only horizontally
    if (yDis === 0) {
        //move tail right
        if (xDis === 2) {
            moveTail['R']();
            //move tail left
        } else {
            moveTail['L']();
        }

        //moving only vertically
    } else if (xDis === 0) {
        //move tail up
        if (yDis === 2) {
            moveTail['U']();
        } else {
            moveTail['D']();
        }


        //moving diagonally
    } else {
        
        //right
        if (xDis > 0) {
            moveTail['R']();
        }

        //left
        if (xDis < 0) {
            moveTail['L']();
        }

        //up
        if (yDis > 0) {
            moveTail['U']();
        }

        //down
        if (yDis < 0) {
            moveTail['D']();
        }

    }

    //add location to visited
    visited.push(`${TCurr.x},${TCurr.y}`)
    // console.log('Tail', visited)

}




instructions.forEach(line => {
    let [direction, iterations] = line.split(' ').map((x, i) => i === 1 ? parseInt(x) : x);

    while (iterations) {
        moveHead[direction]()
        // console.log(HCurr)
        updateTail()
        iterations--;
    }

})

console.log(new Set(visited).size)