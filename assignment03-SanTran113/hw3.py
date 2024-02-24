# Name: San Tran
# Date: 10 / 31 / 22
# Github: SanTran113
from typing import Optional


class Book:
    def __init__(self, title: str, authors: list[str], year: int):
        self.title = title
        self.authors = authors
        self.year = year

    def __repr__(self) -> str:
        return f"Book({self.title},{self.authors}, {self.year})"


    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Book and
                self.title == other.title and
                self.authors == other.authors and
                self.year == other.year)

# Part 1
def getBooksByAuthors(a = list[str], b =list[Book]):
    books = []
    for Book1 in b:
        for elements in a:
            if elements in Book1.authors:
                books.append(Book1)
    return books



class Employee:
    def __init__(self, name: str, pay_rate: int, job_code: int):
        self.name = name
        self.pay_rate = pay_rate
        self.job_code = job_code

    def __repr__(self):
        return f"Employee({self.name},{self.pay_rate},{self.job_code})"


    def __eq__(self, other):
        return (other is self or
                type(other) == Employee and
                self.name == other.name and
                self.pay_rate == other.pay_rate and
                self.job_code == other.job_code)

def belowAvergePay(e = list[Employee], j = int) -> list[str]:
    employees = []
    sum1 = 0
    for Employees in e:
        sum1 += Employees.pay_rate
    ave = sum1 / len(e)

    for Employees in e:
        if Employees.pay_rate < ave and Employees.job_code == j:
            employees.append(Employees.name)
    return employees

def validate_route(c = list[list[str]], n = list[str]) ->bool:
    route = {}
    #part 1
    if n == []:
        return True
    elif len(n) == 1:
        return True

    count = 0
    #part 2
    for links in c:
        # so the "-1" is for not going over the limit of the length of n(nextCity)
        for city in range(len(n)-1):
            currentCity = n[city]
            nextCity = n[city + 1]
            route[currentCity] = nextCity
            print ("Current City: " + currentCity)
            print ("Next City: " + nextCity)
            #print(f"Route: {route}")
            print (f"Links: {links}")
            #check if the program has check n
            if currentCity in links and nextCity in links:
                count += 1
                print (f"Count: {count}")
            print (" ")

    #check if lit through list
    print(f"Count: {count}")
    print(len(n)-1)

    if count == len(n)-1:
        return True
    else:
        return False

# if route in link and route in link - 1

def groupIntoThrees(l = list[int]) -> list[list[int]]:
    list1 = []
    x = 0
    y = 0
    for elements in range(len(l)):
        x += 3
        list1.append(l[y:x])
        y += 3
    list2 = [element for element in list1 if element != []]
    print(list1)
    print(list2)
    return list2

def getLongestRepetition(l = list[int]) -> Optional[int]:
    count = []
    index = 0
    each = 0
    #PART 1
    for currentElement in l:
        # print(f"this is currentIndex:{currentIndex}")
        # print(f"this is prevIndex: {prevIndex}")
        prevElement = l[index - 1]
        print(f"currentElement:{currentElement}")
        print(f"prevElement: {prevElement}")
        print(f"Index:{index}")
        if index != 0:
            # main comparison count
            if currentElement == prevElement:
                count[each] += 1
            # creating a second count to compare
            # current != prev
            else:
                each += 1
                count.append(1)
        # if current element is the first element
        else:
            count.append(1)
        print(l)
        index += 1
        print(" ")

    #PART 2
    finIndex = 0
    maximum = count[0]
    for i in count:
        if i > maximum:
            maximum = i
    print(f"maximum:{maximum}")

    #PART 3
    for element in count:
        print(f"finIndex:{finIndex}")
        print(f"element:{element}")
        if element == maximum:
            break
        else:
            finIndex += element

    print(f"this is finIndex:{finIndex}")
    return finIndex