"""pygame.event事件模块"""
"""
    事件类型：   Pygame 定义了一个专门用来处理事件的结构，即事件队列
                该结构遵循遵循队列“先到先处理”的基本原则
                通过事件队列，我们可以有序的、逐一的处理用户的操作（触发事件）
    
    Pygame 中常用的游戏事件：
        QUIT	        用户按下窗口的关闭按钮	          成员属性：none
        ATIVEEVENT	    Pygame被激活或者隐藏             成员属性：gain,state
        KEYDOWN	        键盘按下	                    成员属性：unicode、key、mod
        KEYUP	        键盘放开	                    成员属性：key、mod
        MOUSEMOTION	    鼠标移动  	                    成员属性：pos, rel, buttons
        MOUSEBUTTONDOWN	鼠标按下 	                    成员属性：pos, button
        MOUSEBUTTONUP	鼠标放开 	                    成员属性：pos, button
        JOYAXISMOTION	游戏手柄(Joystick or pad) 移动 	成员属性：joy, axis, value
        JOYBALLMOTION 	游戏球(Joy ball) 移动  	        成员属性：joy, axis, value
        JOYHATMOTION	游戏手柄(Joystick) 移动    	    成员属性：joy, axis, value
        JOYBUTTONDOWN	游戏手柄按下	                成员属性：joy, button
        JOYBUTTONUP	    游戏手柄放开    	            成员属性：joy, button
        VIDEORESIZE	    Pygame窗口缩放  	            成员属性：size, w, h
        VIDEOEXPOSE	    Pygame窗口部分公开(expose) 	    成员属性：none
        USEREVENT	    触发一个用户事件  	             成员属性：事件代码
    
    事件处理方法：
        pygame.event.get()	        从事件队列中获取一个事件，并从队列中删除该事件
        pygame.event.wait() 	    阻塞直至事件发生才会继续执行，若没有事件发生将一直处于阻塞状态
        pygame.event.set_blocked() 	控制哪些事件禁止进入队列，如果参数值为None，则表示禁止所有事件进入
        pygame.event.set_allowed()  控制哪些事件允许进入队列
        pygame.event.pump() 	    调用该方法后，Pygame 会自动处理事件队列
        pygame.event.poll() 	    会根据实际情形返回一个真实的事件，或者一个None
        pygame.event.peek()  	    检测某类型事件是否在队列中
        pygame.event.clear()	    从队列中清除所有的事件
        pygame.event.get_blocked() 	检测某一类型的事件是否被禁止进入队列
        pygame.event.post()  	    放置一个新的事件到队列中
        pygame.event.Event()  	    创建一个用户自定义的新事件
        
    处理键盘事件：
        K_BACKSPACE	退格键（Backspace）
        K_TAB	制表键（Tab）
        K_CLEAR	清除键（Clear）
        K_RETURN	回车键（Enter）
        K_PAUSE	暂停键（Pause）
        K_ESCAPE	退出键（Escape）
        K_SPACE	空格键（Space）
        K_0...K_9	0...9
        K_a...Kz	a...z
        K_DELETE	删除键（delete）
        K_KP0...K_KP9	0（小键盘）...9（小键盘）
        K_F1...K_F15	F1...F15
        K_UP	向上箭头（up arrow）
        K_DOWN	向下箭头（down arrow）
        K_RIGHT	向右箭头（right arrow）
        K_LEFT	向左箭头（left arrow）
        KMOD_ALT	同时按下Alt键

    处理鼠标事件：
        Pygame 提供了三个鼠标事件，分别是鼠标移动（MOUSEMOTION）、鼠标按下（MOUSEBUTTONDOWN）、鼠标释放（MOUSEBUTTONUP）
        
        pygame.event.MOUSEMOTION鼠标移动事件

            event.pos 相对于窗口左上角，鼠标的当前坐标值(x,y)
            event.rel 鼠标相对运动距离(X,Y)，相对于上次事件
            event.buttons 鼠标按钮初始状态(0,0,0)，分别对应(左键,滑轮,右键)，移动过程中点击那个键，相应位置变会为1

        pygame.event.MOUSEBUTTONUP鼠标键释放事件

            event.pos 相对于窗口左上角，鼠标的当前坐标值(x,y)
            event.button 鼠标释放键编号（整数）左键为1，按下滚动轮2、右键为3

        pygame.event.MOUSEBUTTONDOWN 鼠标键按下事件

            event.pos 相对于窗口左上角，鼠标的当前坐标值(x,y)
            event.button 鼠标按下键编号（整数），左键为1，按下滚动轮2、右键为3，向前滚动滑轮4、向后滚动滑轮5
            
            
            
            
            
"""