class Solution:
    def rotatedDigits(self, N):
        '''
        一个数是个好数：如果这个数的每一位旋转180度后还是一个数字且和原来数字不同
        其中0,8,1旋转后和自身相等，2和5互相旋转，6和互相旋转，其余数字是无效的
        求解[1,N]中好数的个数
        '''
        counts = []
        for num in range(1,N+1):
            numbers = str(num)
            if '3' in numbers or '7' in numbers or '4' in numbers:
                continue
            if '2' in numbers or '5' in numbers or '6' in numbers or '9' in numbers:
                counts.append(numbers)
        return counts
    
    def escapeTheGhosts(self,target, ghosts):
        '''
        判断原点到目标点的距离是否小于所有鬼魂到目标点的距离即可，说实话，我愣是没清楚问题
        '''
        def taxi(P,Q):
            return abs(P[0]-Q[0])+abs(P[1]-Q[1])
        return all(taxi([0,0],target) < taxi(ghosts,target) for ghost in ghosts)

    def cheapestFlight(self, n, edges, src, dst, k):
        pass
if __name__ == '__main__':
    '''s = Solution()
    counts = s.rotatedDigits(100)
    print('[1,%s] has %s good data which are \n%s'%(100,len(counts),counts))
    '''
