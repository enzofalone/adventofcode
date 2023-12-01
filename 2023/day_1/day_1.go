package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func assignValues(first *string, last *string, char string) {
	if len(*first) == 0 {
		*first = char
	}
	*last = string(char)
}

func main() {
	numberWords := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	readFile, err := os.Open("input.txt")

	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)
	total := 0
	for fileScanner.Scan() {
		line := fileScanner.Text()
		first := ""
		last := ""

		for i, char := range line {
			if _, err := strconv.Atoi(string(char)); err == nil {
				assignValues(&first, &last, string(char))
			}

			// part two
			for k, _ := range numberWords {
				if i+len(k) > len(line) {
					continue
				}

				slice := line[i : i+len(k)]
				val, ok := numberWords[slice]

				if ok {
					assignValues(&first, &last, val)
				}
			}
		}

		join := first + last
		res, _ := strconv.Atoi(join)
		total += res
	}
	fmt.Println(total)
	readFile.Close()
}
