def find_missing(list1,list2):
		
    difference= set(list1) ^ set(list2)
    if list1 ==[] or list2==[]: 
        return 0

    elif len(list11) == len(list2): 
        return 0
        
    else:
        return (list(difference)[0])
            