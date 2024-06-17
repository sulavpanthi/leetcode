function isPalindrome(s: string): boolean {
    let leftPointer: number = 0;
    let rightPointer: number = s.length - 1;
    while (leftPointer < rightPointer) {
        let leftCharCode: number = s.charCodeAt(leftPointer);
        if (!isAlphaNumeric(leftCharCode)) {
            leftPointer ++;
            continue;
        }
        let rightCharCode: number = s.charCodeAt(rightPointer);
        if (!isAlphaNumeric(rightCharCode)) {
            rightPointer --;
            continue;
        }
        let asciiCheckArray: number[] = [leftCharCode, getOppositeCaseAsciiValue(leftCharCode)]
        if (!asciiCheckArray.includes(rightCharCode)) {
            return false;
        }
        leftPointer ++;
        rightPointer --;
    }
    return true;
};


function isAlphaNumeric(asciiValue: number): boolean {
    if ((48 <= asciiValue && asciiValue <= 57) || (65 <= asciiValue && asciiValue <= 90) || (97 <= asciiValue && asciiValue <= 122)) {
        return true;
    }
    return false;
};

function getOppositeCaseAsciiValue (asciiValue: number): number {
    if (65 <= asciiValue && asciiValue <= 90) {
        return asciiValue + 32;
    }
    else if (97 <= asciiValue && asciiValue <= 122) {
        return asciiValue - 32;
    }
    else {
        return asciiValue;
    }
}