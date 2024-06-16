function xorOperation(n: number, start: number): number {
    let xorResult: number = 0;
    let i: number = 0;
    while (i<n) {
        const arrayElement: number = start + 2 * i;
        xorResult = xorResult ^ arrayElement;
        i++;
    }
    return xorResult;
};