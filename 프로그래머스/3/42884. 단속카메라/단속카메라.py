def solution(routes):
    for i in range(len(routes)):
        s, e = routes[i]
        routes[i] = [e, s]
        
    routes = sorted(routes) #NlogN 나가는 시점이 가장 빠른 차들 순
    camera = 1 
    ec = routes[0][0]
    
    for i in range(1, len(routes)):
        if not(routes[i][1] <=ec <= routes[i][0]): #진입 - 진출 안 카메라  
            camera +=1
            ec = routes[i][0]  #카메라 추가 설치 
    
    return camera