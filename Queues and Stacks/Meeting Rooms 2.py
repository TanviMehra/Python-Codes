import heapq
def minMeetingRooms(intervals):
    intervals.sort(key= lambda x:(x[0]))
    rooms=1
    room_list=[intervals[0][1]]
    heapq.heapify(room_list)
    for i in range(1,len(intervals)):
        if intervals[i][0]<room_list[0]:
            heapq.heappush(room_list,intervals[i][1])
            rooms=rooms+1
        else:
            heapq.heappop(room_list)
            heapq.heappush(room_list,intervals[i][1])
    print (rooms)








intervals=[[7,10],[2,4]]
minMeetingRooms(intervals)