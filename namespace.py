def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() #вызываем функцию внутри функции.

test_function()

# если вызвать inner_function() снаружи, то её не видно!
