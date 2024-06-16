class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b_num = int("".join(list(map(str, b))))
        # final_b = ""
        # for i in b:
        #     final_b += str(i)
        # b_num = int(final_b)
        print(a, b, b_num)
        if b_num == 0:
            return 1
        else:
            return pow(a,b_num,1337)


    def pow(self, a: int, b: int) -> int:
        if b == 0:
            return 1
        else:
            if b%2 == 0:
                return self.pow(a*a, b//2)
            else:
                return a * self.pow(a*a, (b-1)//2)