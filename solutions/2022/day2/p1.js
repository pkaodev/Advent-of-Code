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

const matchScore = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    }
}

const score = lines.reduce((currScore, currLine) => {
    //currLine[0] is enemy move
    //currLine[2] is my move
    return (
        currScore + myMoves[currLine[2]] + matchScore[currLine[0]][currLine[2]]
    )
}, 0)

console.log(score);

P = {
    prep: T => T.split('\n').map(L => [L.charCodeAt(0) - 64, L.charCodeAt(2) - 87]),
    score: p => p.map(r => r[0] + r[1] * 3).reduce((a, b) => a + b),
    part_1: T => P.score(P.prep(T).map(L => [L[1], (L[1] - L[0] + 4) % 3])),
    part_2: T => P.score(P.prep(T).map(L => [(L[0] + L[1]) % 3 + 1, L[1] - 1]))
    }