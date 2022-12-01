package main

import (
	"fmt"
	"strconv"
	"bufio"
	"log"
	"os"
)

func main() {

	var highestCalories int = 0;

	var currentElfCalories int;

	file, err1 := os.Open("./input.txt")

	if err1 != nil {
		log.Fatal(err1)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {

		if (len(scanner.Text()) == 0) {

			if (currentElfCalories > highestCalories) {
				highestCalories = currentElfCalories
			}

			currentElfCalories = 0

		} else {

			currentSnackCalories, err2 := strconv.Atoi(scanner.Text())

			if err2 != nil {
				log.Fatal(err2)
			}

			currentElfCalories = currentElfCalories + currentSnackCalories
		}
	}

	if err1 := scanner.Err(); err1 != nil {
	log.Fatal(err1)
	}

	fmt.Println(highestCalories)
}
