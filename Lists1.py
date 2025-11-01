# Find all even numbers from a given list
num=[10, 21, 4, 45, 66, 93, 11]
even=[]
for i in num:
    if i%2==0:
        num.append(i)
print(even)

# Find all odd numbers and print them in a single line
num=[10, 21, 4, 45, 66, 93, 11]
print("Odd numbers:", end=" ")
for i in num:
    if i%2!=0:
        print(i,end=" ")
        
# Replace all negative numbers with 0
nums=[12, -7, 5, 64, -14, 0, 99]
for i in range(len(nums)):
    if nums[i]<0:
        nums[i]=0
print(nums)

# Print only names starting with a vowel
names=["Anu","Isha","Vinaya","Sai","Meena","Uma","Krishna"]
vowels=['A', 'E', 'I', 'O', 'U']
list=[]
for name in names:
    if name[0].upper() in vowels:
        list.append(name)
print(list)