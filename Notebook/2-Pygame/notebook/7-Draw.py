"""pygame.draw绘图函数绘制一些简单的图形状"""
"""
    pygame.draw模块的常用方法：
        pygame.draw.rect() 	    绘制矩形
        pygame.draw.polygon() 	绘制多边形
        pygame.draw.circle() 	根据圆心和半径绘制圆形
        pygame.draw.ellipse() 	绘制一个椭圆形
        pygame.draw.arc() 	    绘制弧线（挥着椭圆的一部分）
        pygame.draw.line() 	    绘制线段（直线）
        pygame.draw.lines() 	绘制多条连续的线段
        pygame.draw.aaline() 	绘制一条平滑的线段（抗锯齿）
        pygame.draw.aalines() 	绘制多条连续的线段
        
    函数使用方法大同小异，它们都可以在 Surface 对象上绘制一些简单的形状，返回值是一个 Rect 对象，表示实际绘制图形的矩形区域
    绘图函数都提供了一个 color 参数，我们可以通过以下三种方式来传递 color 参数值：
        1.使用 pygame.color 对象
        2.RGB 三元组
        3.RGBA 四元组
        
    绘制矩形
        pygame.draw.rect(surface, color, rect, width)
            surface：指主游戏窗口，无特殊情况，一般都会绘制在主屏幕上
            color：该参数用于该图形着色
            rect：绘制图形的位置和尺寸大小
            width：可选参数，指定边框的宽度，默认为 0，表示填充该矩形区域
        
    绘制多边形
        pygame.draw.polygon(surface, color, points, width)
            其中 points 一个列表参数，它表示组成多边形顶点的 3 或者多个 (x,y) 坐标
            通过元组或者列表来表示这些多边形顶点。其余参数与上述函数相同
        
    绘制圆形
        pygame.circle(surface, color, pos, radius, width=0)
            pos：该参数用来指定的圆心位置
            radius：用来指定圆的半径
            
    绘制椭圆形
        pygame.draw.ellipse(surface, color, Rect, width=0)
            绘制椭圆形的过程，其实就是在矩形区域内部（Rect）绘制一个内接椭圆形，其余参数与上述参数意思相同
            
    绘制圆弧曲线        
        pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1)    
            与 ellipse 函数相比，该函数多了两个参数：
                start_angle是该段圆弧的起始角度
                stop_angle是终止角度；
            这两个都是用弧度制来表示的，而原点就是矩形 Rect 的中心位置
            
    绘制直线
        pygame.draw.line(surface, color, start_pos, end_pos, width=1)
            start_pos 和 end_pos 表示线段的起始位置，此处使用 [x,y] 来表示起始位置
            width =1 表示直线的宽度，默认为 1
            
        如果是绘制一条消除锯齿的平滑线，此时则使用 blend = 1 参数，如下所示：
        pygame.aaline(surface, color, startpos, endpos, blend=1) 
            blend 参数表示通过绘制混合背景的阴影来实现抗锯齿功能
            
    绘制多条直线
        pygame.lines(surface, color, closed, pointlist, width=1)    
            pointlist：参数值为列表，包含了一些列点坐标的列表
            closed：布尔值参数，如果设置为 True，表示直线的第一个端点和直线的最后一个端点要首尾相连
        如果绘制抗锯齿直线，使用以下方法：    
            pygame.draw.aalines(surface, color, closed, pointlist, blend=1)
    
    
            
"""