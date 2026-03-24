#1
dna = "ATGCGATCGATCGATCGATCGA"
print("The total lenght is:",len(dna))
print("The first five ccharacters are:",dna[0:5])
print("last three characters:",dna[-4:-1])
print("lowrcase:",dna.lower())
print("ATC number:",dna.count("ATC"))
print("T replaced by U:",dna.replace("T","U"))
#2
text = "  Hello, World! Welcome to Python Programming.  "
print("stripped:",text.strip())
print("The number of words:",len(text.strip().split(" ")))
print(text.title())
print(text.strip().startswith("Hello"))
print(text.strip().endswith("ing."))
print(text.strip().find("Python"))
x = text.strip().split(" ")
print("-".join(x))
#3
temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
print("temp wednesday:",temperatures[2])
min= 1000
max = 0
total = 0
days=[]
for i in range(len(temperatures)):
    total +=  temperatures[i]
    if temperatures[i] > max:
        max = temperatures[i]
    if temperatures[i] < min:
        min = temperatures[i]
    if temperatures[i] > 17 :
        days.append(temperatures[i])


print("min:",min)
print("max:",max)
print("Average:",round(total/len(temperatures),1))
print("Days above 17:",len(days))
temperatures.sort()
print(temperatures)
#4
mark = 7
def marking(a) :
    if 7< a <= 9.5:
        print("A")
    elif 5.5< a <= 7:
        print("B")
    elif 3.2< a <= 5.5:
        print("C")
    elif 1< a <= 3.2:
            print("D")
    elif 0< a <= 1:
        print("F")
marking(mark)
#5 loops
words = ["Python", "is", "a", "programming", "language"]
#A
for i in range(len(words)):
    print(words[i] ,"---->",len(words[i]))
#B
n = 1
while n <1000:
    n = n * 2
    print(n)
#6 functions
#A
numbers = [4, 7, 0, -3, 10]
def is_even(number) :
    if number % 2 == 0 :
        print("true")
    else:
        print("false")

for i in range(len(numbers)):
    is_even(numbers[i])
#b
def classify_triangle(a, b, c):
    if (a +b+c)/3  == a :
        print("equilateral")
    elif a == b or a == c or c == b :
        print("isosceles")
    else:
        print("scalane")



classify_triangle(5, 5, 5)
classify_triangle(3, 3, 4)
classify_triangle(3, 4, 5)
#7 dictionaries
student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print(student["name"])
print(len(student["subjects"]))
if "PNE" in student["subjects"]:
    print("true")

print(student["grades"]["Databases"])
total2 = 0
for key  , value  in student["grades"].items():
    total2 += value
    print(f'{key} : {value}')

average =round(total2/len(student["grades"]),2)
print(average)
#8 combinig everything
students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]
def average(grades):
    total3 = 0
    for i in range(len(grades)):
        total3 += grades[i]

    return total3/len(grades)

def get_status(avg):
    if avg >= 5 :
        return "pass"
    else:
        return "fail "


for i in range(0,len(students)):
    print(students[i]["name"],end=" ")
    avg = average(students[i]["grades"])
    status = get_status(avg)
    print(status)