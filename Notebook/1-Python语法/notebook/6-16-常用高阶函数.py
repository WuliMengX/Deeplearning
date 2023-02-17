"""常用高阶函数"""
"""
    定义：参数或（和）返回值为其他函数的函数
    
    filter(function, iterable)              #返回值为可迭代对象
        function：函数（function 的必需参数只能有一个），也可以为None
        iterable：可迭代对象
        将iterable中每个元素作为参数传递给函数，根据函数的返回结果进行判断 True 或 False，将判断为 True 的 iterable 中的元素构建新的迭代器并返回
        如果 function 为 None，直接判断 iterable 中元素 True 或 False，再返回为 True 的元素构建的新的迭代器
        
        
    map(func,*iterables)                    #返回值为可迭代对象
        func：函数（func 的必需参数要和 iterables 个数相同）
        iterables：可迭代对象
        用 iterables 中的每个元素作为函数的参数来调用函数，以迭代器形式返回所有结果
        当有多个 iterables 对象时，最短的 iterables 耗尽则函数停止

        print(list(map(lambda x:x**2,(1,2,3,4)))) #[1, 4, 9, 16]
        print(list(map(lambda x,y:x*y,(1,2,3,4),(5,6,7,8)))) #[5, 12, 21, 32]
        
    reduce(function, iterable[, initial])   #返回值为一个元素
        function：函数（function 必需参数只能有两个）
        iterable：可迭代对象
        initial：初始值
        在 Python2 中 reduce() 是内置函数，而在Python3中 reduce() 函数是在functools模块中的，所以在使用的时候需要先导入functools 模块
        在没有指定 initial 参数时，先把 iterable 的前两个元素作为参数调用函数，把这次函数的结果以及iterable 的下一个元素又作为参数再调用函数，以此类推
        在指定 initial 参数时，先把 initial 值和 iterable 的第一个元素作为参数调用函数，把这次函数的结果以及 iterable 的下一个元素又作为参数再调用函数，以此类推
        如果 iterable 为空，返回 initial ，此时如果没有指定 initial，则报错
        如果 iterable 只有一个元素且没有指定 initial，返回该元素
        
    递归函数 了解
        
"""


