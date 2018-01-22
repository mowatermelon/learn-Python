# def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries == 0:
#             raise IOError('refusenik user')
#         print(complaint)
        
# ask_ok('Do you really want to quit?')

def ask_ok(prompt, retries=10, complaint='输入0或者no，停止记录数值'):
    a = []
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            print(a)
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        a.insert(len(a)+1,ok)
        print(complaint)
        
ask_ok('开始记录数据，输入yes停止记录?')