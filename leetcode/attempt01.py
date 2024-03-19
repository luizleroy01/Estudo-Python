zeros = []
        uns = []
        count1 = 0
        count2 = 0
        result =0
        for i in range(len(nums)):
            if nums[i] == 1:
                count1+=1
            else:
                count2+=1

            zeros.append(count2)
            uns.append(count1)
        i =0
        j =0
        while i < len(zeros) and j < len(uns):
            if uns[j] == zeros[i]:
                if (i+1) > result:
                    result = (i+1)
            
            if i < len(zeros): i+=1
            if j < len(uns): j+=1
        
        return result