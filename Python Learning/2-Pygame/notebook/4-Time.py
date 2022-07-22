"""pygame.time时间控制模块管理时间和游戏帧数率"""
"""
    注意，在 Pygame 中时间以毫秒为单位（1秒=1000毫秒），这样会使游戏的设计更为精细
    
    游戏暂停：
        pygame.time.get_ticks() 	以毫秒为单位获取时间
        pygame.time.wait()	        使程序暂停一段时间
        pygame.time.set_timer()	    创建一个定时器，即每隔一段时间，去执行一些动作
        pygame.time.Clock()	        创建一个时钟对象来帮我们确定游戏要以多大的帧数运行

"""
"""
    设置游戏FPS：
        pygame.time.Clock.tick()	更新clock对象
        pygame.time.Clock.get_time()	获取上一个tick中的时间
        pygame.time.Clock.get_fps()	计算clock对象的帧率
        
"""
