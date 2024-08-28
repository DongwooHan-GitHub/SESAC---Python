all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'

# --------------------------------------------
# 1. list/tuple 기초 예제들 
# 
# a는 1,2,3이 들어간 튜플, a = (1,2,3)
# b는 a부터 z까지 모든 알파벳 소문자가 들어간 리스트가 되도록 만들어보세요. b = [a-z] 
# b를 만들 때 위에 주어진 all_smallcase_letters와 for loop를 사용해도 좋고, 손으로 다 쳐도 좋습니다. 
# --------------------------------------------

all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'
a = (1, 2, 3)
b = list("abcdefghijklmnopqrstuvwxyz")
print(b)





# --------------------------------------------
# 2. dict 기초 예제 
# 
# 1) upper_to_lower
#
# upper_to_lower은 모든 대문자 알파벳(ex. A)을 key로 가지고, 대응하는 소문자 알파벳(ex. a)을 value로 가지는 dict입니다. 
# 위에서 만든 b와 for loop를 이용해서 upper_to_lower을 만들어보세요. 
# 
# 2) lower_to_upper 
#
# upper_to_lower과 반대로 된 dict를 만들어보세요. 
# 
# 3) alpha_to_number
# 
# 소문자 알파벳 각각을 key, 몇 번째 알파벳인지를 value로 가지는 dict를 만들어보세요. 
# 위 all_smallcase_letters와 enumerate함수를 사용하세요. 
# 알파벳 순서는 1부터 시작합니다. ex) alpha_to_number['a'] = 1
# 
# 4) number_to_alphabet 
#
# 1부터 26까지의 수를 key로, 소문자, 대문자로 이뤄진 문자열 2개의 튜플을 value로 가지는 dict를 만들어보세요. 
# --------------------------------------------

lower_to_upper = {}
for char in b:
    if char.islower():
        lower_to_upper[char] = char.upper()
print(lower_to_upper)  

    
upper_to_lower = {}
for char in b:
    upper_to_lower[char.upper()] = char
print(upper_to_lower)   

    
b = list("abcdefghijklmnopqrstuvwxyz")
alphabet = {}
for index, char in enumerate(b):
    alphabet[char] = index + 1

print(alphabet)


# --------------------------------------------
# 3. 주어진 문자열의 대소문자 바꾸기 
#
# 위 2에서 만든 dict들을 이용하여, 아래 문제들을 풀어보세요. 
#  
# 1) 주어진 문자열을 모두 대문자로 바꾼 문자열을 만들어보세요. 
# 2) 주어진 문자열을 모두 소문자로 바꾼 문자열을 만들어보세요. 
# 3) 주어진 문자열에서 대문자는 모두 소문자로, 소문자는 모두 대문자로 바꾼 문자열을 만들어보세요. 
# 4) 주어진 문자열이 모두 알파벳이면 True, 아니면 False를 출력하는 코드를 짜보세요. 
# --------------------------------------------
b = list("abcdefghijklmnopqrstuvwxyz")
    




# --------------------------------------------
# 4. 다양한 패턴 찍어보기 
# 
# 1) 피라미드 찍어보기 - 1 
#
# 다음 패턴을 프린트해보세요. 
#
#     *
#    ***
#   *****
#  *******
# *********
# --------------------------------------------
# n = int(input())

n = 5
for i in range(n):
    print(' ' * ((n - 1) - i), end = '')
    print('*' * (2 * i + 1))
    


# --------------------------------------------
# 2) 피라미드 찍어보기 - 2 
# 
# 다음 패턴을 프린트해보세요. 
# 
#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
# --------------------------------------------
n = 5
for i in range(n):
    print(' ' * ((n - 1) - i), end = '')
    print('* ' * (1 * i + 1))


n = 5
for i in range(n):
    print(' ' * ((n - 1) - i), end = '')
    print('*' * (1 * i + 1))
 


# --------------------------------------------
# 3) 피라미드 찍어보기 - 3 
# 
# 다음 패턴을 프린트해보세요. 
#
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# --------------------------------------------

n = 5
for i in range(n):
    print(' ' * ((n - 1) - i), end = '')
    
    for j in range((1 * i + 1)):
        if j == 0:
            print('A ', end = '')
        elif j == 1:
            print('B ', end = '')
        elif j == 2:
            print('C ', end = '')
        elif j == 3:
            print('D', end = ' ')
        elif j ==4:
            print('E', end = ' ')    
    
    print()



# --------------------------------------------
# 4) 피라미드 찍어보기 - 4 
# 
# 다음 패턴을 프린트해보세요. 
# 
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1
# --------------------------------------------

def pascal(n):
    def generate_next_line(last_line):
        n = len(last_line) + 1
        
        next_line = [last_line[0]]

        for i in range(n-2):
            next_line.append(last_line[i] + last_line[i+1])

        next_line.append(last_line[n-2])

        return next_line
    
    lines = [[1], [1,1]]
    
    while len(lines) != n:
        lines.append(generate_next_line(lines[-1]))

    space = ' '

    def fill(number, digits, fill_with = '0'):
        number_digit = get_digit(number)
        return (digits - number_digit) * fill_with + str(number)

    def get_digit(number):
        # int(log_10(n))
        # 123 
        digit = 1
        
        while True:
            if number < 10:
                break 
            else:
                digit += 1 
                number = number // 10 
        
        return digit 

    # print(fill(123, 4)) # 0123
    # print(fill(123, 5)) # 00123
    # print(fill(123, 4, '|')) # |123

    max_number = max(lines[-1])
    max_digit = get_digit(max_number)

    space = ' ' * max_digit

    for idx, line in enumerate(lines):
        print((n-1-idx)*space + space.join([\
            fill(e, max_digit, ' ') for e in line]))
    
    return lines 

for line in pascal(12):
    print(line)
# --------------------------------------------
# 5) 다음 패턴을 찍어보세요. 
# 
# *         *         * 
#   *       *       *   
#     *     *     *     
#       *   *   *       
#         * * *         
#           *           
#         * * *         
#       *   *   *       
#     *     *     *     
#   *       *       *   
# *         *         * 
# --------------------------------------------


