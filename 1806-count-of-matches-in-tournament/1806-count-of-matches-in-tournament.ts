function numberOfMatches(n: number): number {
    let totalMatchPlayed: number = 0;
    while (n>=2) {
        if (n%2 == 0) {
            n = n / 2
            totalMatchPlayed = totalMatchPlayed + n
        }
        else {
            n = (n-1) / 2;
            totalMatchPlayed = totalMatchPlayed + n + 1
        }
    }
    return totalMatchPlayed;
};