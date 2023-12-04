function callFuncAdjTiles(func, x, y, maxX, maxY, minX = 0, minY = 0) {

	const directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

	directions.forEach(([dy, dx]) => {
		const nx = x + dx;
		const ny = y + dy;

		if (ny >= minY && ny <= maxY && nx >= minX && nx <= maxX) {
			func(nx, ny)
		}
	})
}