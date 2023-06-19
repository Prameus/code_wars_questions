def solution(number):
    the_solution = 0
    if number > 0:
        for i in range(0,number):
            print(i)
            if i%3==0 or i%5==0:
                the_solution += i
        return the_solution
    else:
        return 0

print(solution(100))

# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)