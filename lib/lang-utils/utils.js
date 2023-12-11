export function getLines() {
	
}

export function pipe(...funcs) {
	// get input or pass it?
	let input = 'meow'
	for (const func in funcs) {
		input = func(input)
	}
	console.log(input)
	return input
}