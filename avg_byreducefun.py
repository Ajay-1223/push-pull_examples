from functools import reduce

def find_avg(my_list):
    total_sum=reduce(lambda x,y:x+y,my_list)
    return total_sum/len(my_list)
my_list=[1,2,3,4,5,6,7,8,9,10]
result=find_avg(my_list)
print(result)