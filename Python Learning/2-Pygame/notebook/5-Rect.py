"""pygame.Rect创建指定位置和大小的矩形区域"""
"""
    rect = pygame.Rect(left,top,width,height) 
        (left,top)即坐标(x,y)，指定矩形位置
        (width,height)为矩形的宽和高，指定矩形大小
        Rect 表示的区域必须位于一个 Surface 对象之上，比如游戏的主窗口（screen）
        注意：在 Pygame 中以游戏主窗口的左上角为坐标原点
        
    Rect（矩形区域）对象还提供了一些常用方法：
        pygame.Rect.copy()	        复制矩形
        pygame.Rect.move()	        移动矩形区域，接受一个列表参数
        pygame.Rect.move_ip()	    移动矩形（无返回）
        pygame.Rect.inflate()	    增大或缩小矩形大小
        pygame.Rect.clamp()	        将矩形移到另一个矩形内
        pygame.Rect.union()	        返回一个两个矩形合并后的矩形。
        pygame.Rect.fit()	        按纵横比调整矩形的大小或移动矩形。
        pygame.Rect.contains()	    测试一个矩形是否在另一个矩形内
        pygame.Rect.collidepoint() 	测试点是否在矩形内
        pygame.Rect.colliderect()	测试两个矩形是否重叠
        
    同时 Rect 对象也提供了一些关于矩形大小的常用的属性：
        x,y  表示矩形距离 x、y 轴的距离
        top, left, bottom, right                    #在坐标系内描述矩形的大小
        topleft, bottomleft, topright, bottomright  #返回一个描述矩形大小的元组
        midtop, midleft, midbottom, midright        #返回一个描述矩形大小的元组
        center, centerx, centery                    #(centerx，centery)表示矩形中央坐标(x,y)的值
        size, width, height
        w,h  #用于描述矩形的width、height
        
"""