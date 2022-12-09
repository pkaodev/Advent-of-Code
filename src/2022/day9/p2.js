const readFileSync = require('fs').readFileSync;
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/)

//store coordinates of all knots
const currPos = {
    0: { x: 0, y: 0 },  //head
    1: { x: 0, y: 0 },
    2: { x: 0, y: 0 },
    3: { x: 0, y: 0 },
    4: { x: 0, y: 0 },
    5: { x: 0, y: 0 },
    6: { x: 0, y: 0 },
    7: { x: 0, y: 0 },
    8: { x: 0, y: 0 },
    9: { x: 0, y: 0 }   //tail
}

//coordinates visited by tail
const visited = ['0,0'];

//moves a knot
const move = (position, direction) => {
    switch (direction) {
        case 'U':
            currPos[`${position}`].y++;
            break;
        case 'R':
            currPos[`${position}`].x++;
            break;
        case 'D':
            currPos[`${position}`].y--;
            break;
        case 'L':
            currPos[`${position}`].x--;
            break;
    }
}

//updates knot coordinates based on the knot ahead of it
const updateKnot = (knotNum) => {

    //positive is 'head' to right
    const xDis = currPos[`${knotNum - 1}`].x - currPos[`${knotNum}`].x
    //positive is 'head' above
    const yDis = currPos[`${knotNum - 1}`].y - currPos[`${knotNum}`].y

    //stop if tail is adjacent to head
    if (Math.abs(xDis) <= 1 && Math.abs(yDis) <= 1) {
        return;
    }

    //moving only horizontally
    if (yDis === 0) {
        if (xDis === 2) {
            move(knotNum, 'R')
        } else {
            move(knotNum, 'L')
        }

        //moving only vertically
    } else if (xDis === 0) {
        if (yDis === 2) {
            move(knotNum, 'U')
        } else {
            move(knotNum, 'D')
        }


        //moving diagonally
    } else {

        //right
        if (xDis > 0) {
            move(knotNum, 'R')
        }

        //left
        if (xDis < 0) {
            move(knotNum, 'L')
        }

        //up
        if (yDis > 0) {
            move(knotNum, 'U')
        }

        //down
        if (yDis < 0) {
            move(knotNum, 'D')
        }

    }
}


instructions.forEach(line => {
    let [direction, iterations] = line.split(' ').map((x, i) => i === 1 ? parseInt(x) : x);

    while (iterations) {

        move(0, direction)

        for (let i = 1; i <=9; i++) {
            updateKnot(i)
        }

        visited.push(`${currPos[9].x},${currPos[9].y}`)

        iterations--;
    }

})


console.log(new Set(visited).size)