const path = require('path');
const readFileSync = require('fs').readFileSync;

const inputPath = path.join(__dirname, 'input');
const data = readFileSync(inputPath, 'utf8');
const lines = data.split(/\n/);
