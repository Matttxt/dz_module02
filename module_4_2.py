def test_function():
    def inner_function():
        print('Я в области видимости функции test_funcktion')
    inner_function()

# inner_function невозможно вызвать вне функции, поскольку она вложенная. Вывод текста будет возможен, если вне функции запросить вывод test_function