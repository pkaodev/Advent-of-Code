import os
current_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(os.path.dirname(__file__), 'input_example')
# input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    
def solution_1(data):
    disk_map = list(map(int, data[0]))

    new_disk = []
    
    li = 0
    ri = ((len(disk_map) - 1) // 2) * 2 
    
    while li <= ri:
        
        if li % 2 == 0:
            for _ in range(disk_map[li]):
                new_disk.append(li//2)
            li += 1
            continue
        
        if disk_map[li] < disk_map[ri]:
            for _ in range(disk_map[li]):
                new_disk.append(ri//2)
            disk_map[ri] -= disk_map[li]
            li += 1
            continue
        
        if disk_map[li] == disk_map[ri]:
            for _ in range(disk_map[li]):
                new_disk.append(ri//2)
            li += 1
            ri -= 2
            continue
        
        if disk_map[li] > disk_map[ri]:
            for _ in range(disk_map[ri]):
                new_disk.append(ri//2)
            disk_map[li] -= disk_map[ri]
            ri -= 2
            continue
       
    # Could do counting withing the while loop         
    solution = 0
    for i in range (len(new_disk)):
        solution += (i * new_disk[i])
    
    print(solution)

# solution_1(data)

def solution_2(data):
    s=data[0].strip()
    parts=[]
    for i,c in enumerate(s):
        v=int(c)
        if i%2==0:
            parts.append((v,))
        else:
            parts.append(['.']*v)
    files=[]
    idx=0
    for i,(p,) in enumerate(parts[0::2]):
        files.append((p,i))
    arr=[]
    file_id=0
    for i,p in enumerate(parts):
        if i%2==0:
            length=p[0]
            for _ in range(length):
                arr.append(files[i//2][1])
        else:
            arr.extend(p)
    file_positions=[]
    cur_id=0
    i=0
    while i<len(arr):
        if arr[i]=='.':
            i+=1
            continue
        cid=arr[i]
        start=i
        while i<len(arr) and arr[i]==cid:
            i+=1
        file_positions.append((cid,start,i-start))
    file_positions.sort(key=lambda x:x[0],reverse=True)
    for cid,start,length in file_positions:
        free_ranges=[]
        sz=0
        st=0
        in_free=False
        for i,a in enumerate(arr):
            if a=='.':
                if not in_free:
                    in_free=True
                    st=i
                sz+=1
            else:
                if in_free:
                    free_ranges.append((st,sz))
                in_free=False
                sz=0
        if in_free:
            free_ranges.append((st,sz))
        left_candidates=[(fs,fl) for fs,fl in free_ranges if fs<start and fl>=length]
        if left_candidates:
            fs,fl=min(left_candidates,key=lambda x:x[0])
            for i in range(length):
                arr[fs+i]=cid
            for i in range(start,start+length):
                arr[i]='.'
    ans=0
    for i,a in enumerate(arr):
        if a!='.':
            ans+=i*a
    print(ans)

    disk_map = list(map(int, data[0]))

    new_disk = []

    li = 0
    ri = ((len(disk_map) - 1) // 2) * 2 
    
    while li < ri:
        
        if disk_map[li] == 'x':
            li += 1
            new_disk.append('x')
            continue
        
        if li % 2 == 0:
            for _ in range(disk_map[li]):
                new_disk.append(li//2)
            li += 1
            continue
        
        nothing_added = True
        i = ri
        while i > li:
            if disk_map[i] == 'x':
                i -= 2
                continue
            
            if disk_map[i] <= disk_map[li]:
                for _ in range(disk_map[i]):
                    new_disk.append(i//2)
                disk_map[li] -= disk_map[i]
                disk_map[i] = 'x'
                nothing_added = False
                break
            
            i -= 2
            
        if nothing_added:
            for _ in range(disk_map[li]):
                    new_disk.append('x')
            li += 1
        
    print(new_disk)
    
    solution = 0
    for i in range (len(new_disk)):
        if new_disk[i] == 'x':
            continue
        solution += (i * new_disk[i])
    
    print(solution)

solution_2(data)

# def solution_2(data):
#     s=data[0].strip()
#     parts=[]
#     for i,c in enumerate(s):
#         v=int(c)
#         if i%2==0:
#             parts.append((v,))
#         else:
#             parts.append(['.']*v)
#     files=[]
#     idx=0
#     for i,(p,) in enumerate(parts[0::2]):
#         files.append((p,i))
#     arr=[]
#     file_id=0
#     for i,p in enumerate(parts):
#         if i%2==0:
#             length=p[0]
#             for _ in range(length):
#                 arr.append(files[i//2][1])
#         else:
#             arr.extend(p)
#     file_positions=[]
#     cur_id=0
#     i=0
#     while i<len(arr):
#         if arr[i]=='.':
#             i+=1
#             continue
#         cid=arr[i]
#         start=i
#         while i<len(arr) and arr[i]==cid:
#             i+=1
#         file_positions.append((cid,start,i-start))
#     file_positions.sort(key=lambda x:x[0],reverse=True)
#     for cid,start,length in file_positions:
#         free_ranges=[]
#         sz=0
#         st=0
#         in_free=False
#         for i,a in enumerate(arr):
#             if a=='.':
#                 if not in_free:
#                     in_free=True
#                     st=i
#                 sz+=1
#             else:
#                 if in_free:
#                     free_ranges.append((st,sz))
#                 in_free=False
#                 sz=0
#         if in_free:
#             free_ranges.append((st,sz))
#         left_candidates=[(fs,fl) for fs,fl in free_ranges if fs<start and fl>=length]
#         if left_candidates:
#             fs,fl=min(left_candidates,key=lambda x:x[0])
#             for i in range(length):
#                 arr[fs+i]=cid
#             for i in range(start,start+length):
#                 arr[i]='.'
#     ans=0
#     for i,a in enumerate(arr):
#         if a!='.':
#             ans+=i*a
#     print(ans)

#     disk_map = list(map(int, data[0]))

#     new_disk = []

#     li = 0
#     ri = ((len(disk_map) - 1) // 2) * 2 
    
#     while li < ri:
        
#         if disk_map[li] == 'x':
#             li += 1
#             new_disk.append('x')
#             continue
        
#         if li % 2 == 0:
#             for _ in range(disk_map[li]):
#                 new_disk.append(li//2)
#             li += 1
#             continue
        
#         nothing_added = True
#         i = ri
#         while i > li:
#             if disk_map[i] == 'x':
#                 i -= 2
#                 continue
            
#             if disk_map[i] <= disk_map[li]:
#                 for _ in range(disk_map[i]):
#                     new_disk.append(i//2)
#                 disk_map[li] -= disk_map[i]
#                 disk_map[i] = 'x'
#                 nothing_added = False
#                 break
            
#             i -= 2
            
#         if nothing_added:
#             for _ in range(disk_map[li]):
#                     new_disk.append('x')
#             li += 1
        
#     # print(new_disk)
    
#     solution = 0
#     for i in range (len(new_disk)):
#         if new_disk[i] == 'x':
#             continue
#         solution += (i * new_disk[i])
    
#     print(solution)

# solution_2(data)