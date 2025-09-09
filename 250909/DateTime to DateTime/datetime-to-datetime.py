a, b, c = map(int, input().split())

# Please write your code here.
# A일 B시 C분이 11일 11시 11분보다 더 앞서는지 확인
def is_slow(a,b,c):
    if a<11:
        return False
    
    if a==11 and b<11:
        return False
    
    if a==11 and b==11 and c<11:
        return False
        
    return True

# A일 B시 C분이 11일 11시 11분보다 더 앞서는지 확인
if is_slow(a,b,c): #앞서지 않음을 확인하면 몇분 걸리는지 계산
    print((a*24*60+b*60+c) - (11*24*60+11*60+11))
else: #A일 B시 C분이 11일 11시 11분보다 더 앞선다면 −1을 출력
    print(-1)