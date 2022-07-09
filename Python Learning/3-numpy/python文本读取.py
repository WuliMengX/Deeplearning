"""文本读取"""
"""
    文本读取的模式：
        r   读取文件，返回的是字符串类型
        rb  二进制形式读取文件
        
    文本对象的读取方法：file.method()
        read        全部读取，返回整个文件的字符串
        readlines   每一行分割成列表，返回文件列表
        readline    一次返回一行，返回文件中的一行
        mode        调用返回当前文件模式
        name        返回文件名称
        closed      返回bool类型，知道文件是否关闭
        
    使用readlines方法时，处理每一行的空白符：
    _data = []
    for i in data:
        temp = i.strip()
        if temp != '':
            _data.append(temp)
    
    使用readline方法时，避免繁琐引入with语句自动调用close()方法：
    with open('file_path','r/rb') as file:
        print(file.read())
        
"""



