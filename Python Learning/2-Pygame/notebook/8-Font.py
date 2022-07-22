"""pygame.font创建字体对象"""
"""
    pygame.font.init()	            初始化字体模块
    pygame.font.quit() 	            取消初始化字体模块
    pygame.font.get_init() 	        检查字体模块是否被初始化，返回一个布尔值。
    pygame.font.get_default_font() 	获得默认字体的文件名。返回系统中字体的文件名
    pygame.font.get_fonts() 	    获取所有可使用的字体，返回值是所有可用的字体列表
    pygame.font.match_font() 	    从系统的字体库中匹配字体文件，返回值是完整的字体文件路径
    pygame.font.SysFont() 	        从系统的字体库中创建一个 Font 对象
    pygame.font.Font()	            从一个字体文件创建一个 Font 对象
    
    Font 模块提供了两种创建字体（Font）对象的方法，分别是：
        SysFont（从系统中加载字体文件创建字体对象）
        Font（通过文件路径创建字体对象）
        
    直接从系统中加载字体:
        pygame.font.SysFont(name, size, bold=False, italic=False)
            name：列表参数值，表示要从系统中加载的字体名称，它会按照列表中的元素顺序依次搜索，如果系统中没有列表中的字体，将使用 Pygame 默认的字体
            size：表示字体的大小
            bold：字体是否加粗
            italic：字体是否为斜体
    注意，如果要显示中文，那么一定要使用中文字体文件
    
    从外部加载字体文件来绘制文本:
        my_font = pygame.font.Font(filename, size) 
            filename：字符串格式，表示字体文件的所在路径
            size：设置字体的大小
    
    字体对象方法：
        pygame.font.Font.render() 	        该函数创建一个渲染了文本的 Surface 对象
        pygame.font.Font.size() 	        该函数返回渲染文本所需的尺寸大小，返回值是一个一元组 (width,height)
        pygame.font.Font.set_underline() 	是否为文本内容绘制下划线
        pygame.font.Font.get_underline() 	检查文本是否绘制了下划线
        pygame.font.Font.set_bold() 	    启动粗体字渲染
        pygame.font.Font.get_bold() 	    检查文本是否使用粗体渲染
        pygame.font.Font.set_italic() 	    启动斜体字渲染
        pygame.font.Font.metrics() 	        获取字符串中每一个字符的详细参数
        pygame.font.Font.get_italic() 	    检查文本是否使用斜体渲染
        pygame.font.Font.get_linesize() 	获取字体文本的行高
        pygame.font.Font.get_height() 	    获取字体的高度
        pygame.font.Font.get_ascent() 	    获取字体顶端到基准线的距离
        pygame.font.Font.get_descent() 	    获取字体底端到基准线的距离
    
    使用最多的方法：
    render(text, antialias, color, background=None)
        text：要绘制的文本内容
        antialias：布尔值参数，是否是平滑字体（抗锯齿）
        color：设置字体颜色
        background：可选参数，默认为 None，该参数用来设置字体的背景颜色
    
"""