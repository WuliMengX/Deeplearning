"""pygame.display显示模块中的方法创建游戏主窗口"""
"""
    screen = pygame.display.set_mode(size=(),flags=0)
        size:元组参数，设置窗口大小
        flags:功能标志位，表示创建的窗口样式，参数如下
            pygame.FULLSCREEN   全屏
            pygame.HWSURFACE    硬件加速窗口，必须同时与全屏使用
            pygame.OPENGL       OPENGL渲染窗口
            pygame.RESIZABLE    可以改变大小的窗口
            pygame.DOUBLEBUF    双缓冲区窗口，建议与 HWSURFACE 或 OPENGL 同时使用
            pygame.NOFRAME      无边框窗口

    主窗口screen相当于游戏程序中尺寸最大的Surface对象，我们可以添加其他的Surface对象以矩阵形式存在于主窗口中
    比如通过以下方法：
    screen.blit(source, dest, area=None, special_flags = 0)
        source：表示要添加的 Surface 对象
        dest：主窗口中的一个标识的坐标位置，可以接受一个 (x,y) 元组，或者 (x,y,width,height) 元组，也可以是一个 Rect 对象；
        area：接受一个 Rect 对象，默认为 None，如果提供该参数则相当于抠图操作，即在屏幕的指定区域显示想要的内容；
        special_flags：可选参数，用于指定对应位置颜色的混合方式，参数值有 BLEND_RGBA_ADD、BLEND_SUB 等。
                       如果不提供该参数的情况下，默认使用 source 的颜色覆盖 screen 的颜色。
                       
    其他与"显示"有关的方法：
        screen.fill((R,G,B))    填充主窗口的背景颜色，参数值RGB是一个颜色元组，也可以是"color"或者color="pink"的形式
    
        pygame.display.set_caption(text)    设置窗口标题
    
    刷新界面显示的方法：
        pygame.display.flip()   更新整个待显示的 Surface 对象到屏幕上
        pygame.display.update() 可以根据选定的区域更新部分内容，未提供区域位置参数则作用与flip相同
    
        pygame.display.get_surface()	获取当前显示的 Surface 对象。
    
        pygame.display.Info()	产生一个 VideoInfo 对象，包含了显示界面的相关信息
    
        pygame.display.set_icon()	设置左上角的游戏图标，图标尺寸大小为 32*32
    
        pygame.display.iconify()	将显示的主窗口即 Surface 对象最小化，或者隐藏
    
        pygame.display.get_active()	当前显示界面显示在屏幕上时返回 True，如果窗口被隐藏和最小化则返回 False。
    
    主循环代码：
    
        while True:                                 # 循环获取事件，监听事件        
            for event in pygame.event.get():                  
                if event.type == pygame.QUIT:       # 判断用户是否点了关闭按钮
                    pygame.quit()                   # 卸载所有模块                           
                    sys.exit()                      # 终止程序                         
            pygame.display.flip()                   # 更新屏幕内容
            
        
"""