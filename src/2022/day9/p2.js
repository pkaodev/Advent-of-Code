const readFileSync = require('fs').readFileSync;
const instructions = readFileSync('./input.txt', 'utf8').split(/\n/)

//2/10 for part 1/2
const numberofKnots = 10;

//array of arrays representing [x,y] coordinates of each knot.  index 0 is head
const currentPositions = new Array(numberofKnots).fill(0).map( x => [0,0] )

//coordinates visited by tail
const visited = ['0,0'];

//move a knot in a given direction
const moveKnot = (index, direction) => {
    switch (direction) {
        case 'U':   //up
            currentPositions[index][1]++;
            break;
        case 'R':   //right
            currentPositions[index][0]++;
            break;
        case 'D':   //down
            currentPositions[index][1]--;
            break;
        case 'L':   //left
            currentPositions[index][0]--;
            break;
    }
}

//update non-head knot based on knot ahead of it
const updateKnot = (index) => {

    //+ve means knot closer to head is to the right 
    const xDis = currentPositions[index - 1][0] - currentPositions[index][0];
    //+ve means knot closer to head is above
    const yDis = currentPositions[index - 1][1] - currentPositions[index][1];

    //don't move if knots are adjacent
    if (Math.abs(xDis) <= 1 && Math.abs(yDis) <= 1) {
        return;
    }

    //move closer to knot ahead in x- and/or y-direction
    if (xDis > 0) {
        moveKnot(index, 'R')
    }
    if (xDis < 0) {
        moveKnot(index, 'L')
    }
    if (yDis > 0) {
        moveKnot(index, 'U')
    }
    if (yDis < 0) {
        moveKnot(index, 'D')
    }
}

//main loop
instructions.forEach(line => {

    let [direction, iterations] = line.split(' ');
    iterations = parseInt(iterations);

    while (iterations) {

        //move head
        moveKnot(0, direction)

        //move rest of knots
        for (let i = 1; i <=numberofKnots-1; i++) {
            updateKnot(i)
        }

        //add position of tail to visited
        visited.push(`${currentPositions[numberofKnots-1]}`)

        iterations--;
    }
})

//unique locations visited by tail
console.log(new Set(visited).size)