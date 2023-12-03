const readFileSync = require('fs').readFileSync;

const data = readFileSync('./input.txt', 'utf8')

const lines = data.split(/\n/);

const myMoves = {
    //rock
    "X": 1,
    //paper
    "Y": 2,
    //scissors
    "Z": 3
}

const resultScore = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

const matchScore = {
    //rock
    "A": {
        //lose
        "X": "Z",
        //draw
        "Y": "X",
        //win
        "Z": "Y"
    },
    //paper
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z"
    },
    //scissors
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X"
    }
}

const score = lines.reduce((currScore, currLine) => {
    return (
        currScore + resultScore[currLine[2]] + myMoves[matchScore[currLine[0]][currLine[2]]]
    )
}, 0)

console.log(score);