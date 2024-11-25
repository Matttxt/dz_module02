calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    length = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    return (length, upper_string, lower_string)
def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    for i in list_to_search:
        if string_lower == i.lower():
            return True
    return False
result1 = string_info('Capybara')
print(result1)
result2 = string_info('Armageddon')
print(result2)
result3 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
print(result3)
result4 = is_contains('cycle', ['recycling', 'cyclic'])
print(result4)
print(calls)


