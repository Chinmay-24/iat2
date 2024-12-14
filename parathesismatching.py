'''You are given a list of strings containing letters, (,),{,},[,].Write a python program to print the strings in paranthesis are matched
Input Description: First integer represents the length of the list
Then the list elements are entered one below the other
Sample input:
4
[ra(vee{s}h)]
ra(vee{s}h)]
]ra(vee{s}h)[
[ra{vee(s)h}]
Sample output:
[ra(vee{s}h)]
[ra{vee(s)h}]'''
n=int(input())
list1=[]
for i in range(n):
    list1.append(input())

def match(str1):
    ob=0
    cb=0
    for i in str1:
        if i=='(':
            ob=ob+1
        elif i==')':
            cb=cb+1
        if cb>ob:
            return False
    if cb==ob:
        return True
    else:
        return False
list2=[]
for i in list1:
    if match(i)==True:
        list2.append(i)
print(*list2,sep='\n')
