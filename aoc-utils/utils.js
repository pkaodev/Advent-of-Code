const fs = require('fs')
const path = require('path')
const exec = require('child_process').exec
// const fetch = require('node-fetch')

// Equivalent of wait_msg
function waitMsg(message) {
    return function(func) {
        return async function(...args) {
            let finished = false
            const printMessage = () => {
                process.stdout.write(`${message}`)
                let interval = setInterval(() => {
                    if (!finished) {
                        process.stdout.write(`.`)
                    } else {
                        clearInterval(interval)
                        process.stdout.write(`\n    Done!\n`)
                    }
                }, 100)
            }

            printMessage()

            try {
                let result = await func(...args)
                finished = true
                return result
            } catch (e) {
                finished = true
                process.stdout.write(`\n    Failed!\n`)
                throw e
            }
        }
    }
}

// Equivalent of get_aoc_headers
function getAocHeaders() {
        const cookieFile = '.aoc_session_cookie'
        if (fs.existsSync(cookieFile)) {
            aocSessionCookie = fs.readFileSync(cookieFile, 'utf8').trim()
        } else {
            // Handle it like python version
        }
		return { 'cookie': `session=${aocSessionCookie}` }
}

// Equivalent of get_part_day_year
function getPartDayYear(solutionFilePath) {
	console.log(123, solutionFilePath)
    const part = solutionFilePath.split('/').slice(-1)[0].includes('s2') ? '2' : '1'
	console.log(345, part)
	const solutionDir = path.dirname(solutionFilePath)

    const day = solutionDir.split(path.sep).slice(-1)[0].split('-')[0]
    const year = solutionDir.split(path.sep).slice(-2, -1)[0]

    return [part, day, year]
}

async function fetchText(url, options) {
    const { default: fetch } = await import('node-fetch')
	const response = await fetch(url, options)
	const data = await response.text()
	return data

}

// Adjusted submit function with waitMsg decorator
// TODO make possible to add part, day, year
const submit = waitMsg('Submitting answer')(async (answer) => {

	const stack = new Error().stack;
    const stackLines = stack.split('\n');
    const callerLine = stackLines[3]; // Index 2 is typically the caller
    const callerPathMatch = callerLine.match(/\((.*):\d+:\d+\)$/);

	solutionFilePath = callerPathMatch[1]

	let [part, day, year] = getPartDayYear(solutionFilePath)

	console.log(`Submitting answer for part ${part} of day ${day} of year ${year}`)

    const answerUrl = `https://adventofcode.com/${year}/day/${day}/answer`;

    const body = new URLSearchParams({
        level: part,
        answer: answer
    });

    const headers = getAocHeaders();
    headers['Content-Type'] = 'application/x-www-form-urlencoded';

    const responseText = await fetchText(answerUrl, {
        method: 'POST',
        headers: headers,
        body: body
    });

	let result
	let text

	const waitPattern = /You have (.+?) left to wait/;
    const waitMatch = responseText.match(waitPattern);

	if (waitMatch !== null) {
		result = 'wait'
		text = `Wait ${waitMatch[1]} before submitting again.`

	} else if (responseText.includes('Did you already complete it')) {
		result = 'completed'
		text = "You don't seem to be solving the right level.  Did you already complete it?"

	} else if (responseText.includes('That\'s not the right answer')) {
		result = 'wrong'
		if (responseText.includes('too high')) {
			text = `Your answer, ${answer}, is TOO HIGH.`
		} else if (responseText.includes('too low')) {
			text = `Your answer, ${answer}, is TOO LOW.`
		} else {
			text = `Your answer, ${answer}, is WRONG.`
		}
	} else if (responseText.includes('That\'s the right answer')) {
		result = 'correct'
		text = `Your answer, ${answer}, is CORRECT!`
	}

	console.log("\n", text)

	if (result==='correct' && part==='1') {
		console.log('pulling part 2')
		exec(`make day2 DAY=${day} YEAR=${year}`, (err, stdout, stderr) => {})
	}

});

module.exports = { submit };