"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_frame_main_frame = self.__tk_frame_main_frame(self)
        self.tk_tabs_edges = self.__tk_tabs_edges( self.tk_frame_main_frame) 
        self.tk_progressbar_reg_progress = self.__tk_progressbar_reg_progress( self.tk_tabs_edges_0)
        self.tk_canvas_figure_zone = self.__tk_canvas_figure_zone( self.tk_tabs_edges_0)
        self.tk_label_frame_draw_extent_frame = self.__tk_label_frame_draw_extent_frame( self.tk_tabs_edges_0)
        self.tk_label_extent_up_label = self.__tk_label_extent_up_label( self.tk_label_frame_draw_extent_frame) 
        self.tk_label_extent_down_label = self.__tk_label_extent_down_label( self.tk_label_frame_draw_extent_frame) 
        self.tk_label_extent_left_label = self.__tk_label_extent_left_label( self.tk_label_frame_draw_extent_frame) 
        self.tk_label_extent_right_label = self.__tk_label_extent_right_label( self.tk_label_frame_draw_extent_frame) 
        self.tk_input_extent_up = self.__tk_input_extent_up( self.tk_label_frame_draw_extent_frame) 
        self.tk_input_extent_down = self.__tk_input_extent_down( self.tk_label_frame_draw_extent_frame) 
        self.tk_input_extent_left = self.__tk_input_extent_left( self.tk_label_frame_draw_extent_frame) 
        self.tk_input_extent_right = self.__tk_input_extent_right( self.tk_label_frame_draw_extent_frame) 
        self.tk_button_reg_button = self.__tk_button_reg_button( self.tk_tabs_edges_0)
    def __win(self):
        self.title("Climate Analyze")
        # 设置窗口大小、居中
        width = 604
        height = 502
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_frame_main_frame(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=0, width=602, height=502)
        return frame
    def __tk_tabs_edges(self,parent):
        frame = Notebook(parent)
        self.tk_tabs_edges_0 = self.__tk_frame_edges_0(frame)
        frame.add(self.tk_tabs_edges_0, text="回归分析")
        self.tk_tabs_edges_1 = self.__tk_frame_edges_1(frame)
        frame.add(self.tk_tabs_edges_1, text="相关分析")
        self.tk_tabs_edges_2 = self.__tk_frame_edges_2(frame)
        frame.add(self.tk_tabs_edges_2, text="合成分析")
        frame.place(x=0, y=0, width=602, height=502)
        return frame
    def __tk_frame_edges_0(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=602, height=502)
        return frame
    def __tk_frame_edges_1(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=602, height=502)
        return frame
    def __tk_frame_edges_2(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=602, height=502)
        return frame
    def __tk_progressbar_reg_progress(self,parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL,)
        progressbar.place(x=440, y=11, width=150, height=15)
        return progressbar
    def __tk_canvas_figure_zone(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(x=0, y=216, width=602, height=286)
        return canvas
    def __tk_label_frame_draw_extent_frame(self,parent):
        frame = LabelFrame(parent,text="绘制范围",)
        frame.place(x=11, y=72, width=139, height=130)
        return frame
    def __tk_label_extent_up_label(self,parent):
        label = Label(parent,text="上",anchor="center", )
        label.place(x=0, y=0, width=30, height=22)
        return label
    def __tk_label_extent_down_label(self,parent):
        label = Label(parent,text="下",anchor="center", )
        label.place(x=0, y=27, width=30, height=22)
        return label
    def __tk_label_extent_left_label(self,parent):
        label = Label(parent,text="左",anchor="center", )
        label.place(x=0, y=54, width=30, height=22)
        return label
    def __tk_label_extent_right_label(self,parent):
        label = Label(parent,text="右",anchor="center", )
        label.place(x=0, y=82, width=30, height=22)
        return label
    def __tk_input_extent_up(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=44, y=0, width=80, height=22)
        return ipt
    def __tk_input_extent_down(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=44, y=27, width=80, height=22)
        return ipt
    def __tk_input_extent_left(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=44, y=54, width=80, height=22)
        return ipt
    def __tk_input_extent_right(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=44, y=82, width=80, height=22)
        return ipt
    def __tk_button_reg_button(self,parent):
        btn = Button(parent, text="计算", takefocus=False,)
        btn.place(x=440, y=35, width=150, height=30)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_reg_button.bind('<Button-1>',self.ctl.reg_start)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()