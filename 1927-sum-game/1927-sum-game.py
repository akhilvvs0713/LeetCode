class Solution:
    def sumGame(self, num: str) -> bool:
        mid=len(num)//2
        left_sum=0
        right_sum=0

        left_ques=0
        right_ques=0

        for i,char in enumerate(num):
            if i < mid:
                if char=='?':
                    left_ques+=1
                else:
                    left_sum+=int(char)
            else:
                if char=='?':
                    right_ques+=1
                else:
                    right_sum+=int(char)

        return 2*(left_sum-right_sum) !=\
                9*(right_ques - left_ques)