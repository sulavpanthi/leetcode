function numberOfMatches(n: number): number {
    let totalMatchPlayed: number = 0;
    let subsequentMatchPlayed: number = 0;
    if (n==1) {
        return 0;
    }
    if (n % 2 == 0) {
        totalMatchPlayed = n / 2;
        subsequentMatchPlayed = numberOfMatches(totalMatchPlayed);
    }
    else {
        totalMatchPlayed = (n-1) / 2;
        subsequentMatchPlayed = numberOfMatches(totalMatchPlayed + 1);
    }
    return totalMatchPlayed + subsequentMatchPlayed;
};