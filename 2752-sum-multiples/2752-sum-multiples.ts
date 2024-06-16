function sumOfMultiples(n: number): number {
    let sum: number = 0
    for (let i: number = 1; i<=n; i++) {
        if (i%3 == 0 || i%5 == 0 || i%7 == 0) {
            sum = sum + i;
        }
    }
    return sum;
};