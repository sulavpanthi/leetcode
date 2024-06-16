function isPalindrome(x: number): boolean {
    const original_number: number = x
    let reverse_number: number = 0
    while (x > 0){
        let last_digit: number = x % 10
        x = Math.floor(x / 10)
        reverse_number = reverse_number * 10 + last_digit
    }
    return original_number === reverse_number ? true : false
};