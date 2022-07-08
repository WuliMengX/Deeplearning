"""pygame.Surface创建图像对象"""
"""
    Surface = pygame.Surface(size=(width,height),flags,depth)
        size：表示 Surface 对象的矩形区域大小，默认大小与主游戏屏幕一致
        flags：功能标志位，有两个可选参数值 HWSURFACE 和 SPCALPHA，前者代表将创建的 Surface 对象存放于显存中，后者表示让图像的每一个像素都包含一个 alpha 通道
        depth：指定像素的颜色深度，默认为自适应模式，由 Pygame 自动调节
    
    Surface模块还提供了处理图像的其他方法：
    
        pygame.Surface.blit() 	        将一个图像（Surface对象）绘制到另一个图像上
        pygame.Surface.convert() 	    修改图像（Surface对象）的像素格式
        pygame.Surface.fill()  	        使用纯色填充 Surface 对象
        pygame.Surface.scroll() 	    复制并移动 Surface 对象
        pygame.Surface.set_alpha() 	    设置整个图像的透明度
        pygame.Surface.get_at() 	    获取一个像素的颜色值
        pygame.Surface.set_at() 	    设置一个像素的颜色值
        pygame.Surface.get_palette()	获取 Surface 对象 8 位索引的调色板
        pygame.Surface.map_rgb()  	    将一个 RGBA 颜色转换为映射的颜色值
        pygame.Surface.set_clip() 	    设置该 Surface 对象的当前剪切区域
        pygame.Surface.subsurface()  	根据父对象创建一个新的子 Surface 对象
        pygame.Surface.get_offset()	    获取子 Surface 对象在父对象中的偏移位置
        pygame.Surface.get_size()	    获取 Surface 对象的尺寸
        
        
    除了使用Surface模块新建图像外，还有另一种方法从外部加载图像作为Surface对象来使用：
    
        pygame.image.load("图片路径").convert()
            注意，此处之所以使用 convert(）来转换被加载图片的像素格式，是为了提升 Pygame 对图片的处理速度，该操作能够保证图像的像素格式与图片的显示格式是相同的
    通过 image.load() 方法可以加载游戏的背景图，或者游戏中使用的其他元素，比如的人物、道具等等
"""