function isPalindrome(s: string): boolean {
    let leftPointer: number = 0;
    let rightPointer: number = s.length - 1;
    while (leftPointer < rightPointer) {
        let leftCharCode: number = s.charCodeAt(leftPointer);
        console.log("leftCharCode", leftCharCode)
        if (!isAlphaNumeric(leftCharCode)) {
            leftPointer ++;
            continue;
        }
        let rightCharCode: number = s.charCodeAt(rightPointer);
        console.log("rightCharCode", rightCharCode)
        if (!isAlphaNumeric(rightCharCode)) {
            rightPointer --;
            continue;
        }
        let asciiCheckArray: number[] = [leftCharCode, getOppositeCaseAsciiValue(leftCharCode)]
        console.log("asciiCheckArray", asciiCheckArray)
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
        let difference: number = asciiValue - 65;
        return 97 + difference;
    }
    else {
        let difference: number = asciiValue - 97;
        return 65 + difference;
    }
}