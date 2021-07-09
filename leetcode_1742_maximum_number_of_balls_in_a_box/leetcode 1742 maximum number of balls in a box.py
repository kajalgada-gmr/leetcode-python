class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        # Variables. Given lowLimit & highLimit inclusive, min ball count will be 1.
        max_ball_count = 1
        box_num_dict = {}
        
        # Loop through all ball numbers
        for ball_num in range(lowLimit, highLimit+1):
            
            # Compute box_num (hash)
            box_num = 0
            while ball_num > 0:
                box_num += (ball_num % 10)
                ball_num = ball_num // 10
            
            # Add ball to box and keep track of max ball count
            if box_num in box_num_dict:
                box_num_dict[box_num] += 1
                max_ball_count = max(max_ball_count, box_num_dict[box_num])
                
            else:
                box_num_dict[box_num] = 1
        
        return max_ball_count
