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
        self.tk_label_extent_up = self.__tk_label_extent_up( self.tk_label_frame_draw_extent_frame)
        self.tk_label_extent_down = self.__tk_label_extent_down( self.tk_label_frame_draw_extent_frame)
        self.tk_label_extent_left = self.__tk_label_extent_left( self.tk_label_frame_draw_extent_frame)
        self.tk_label_extent_right = self.__tk_label_extent_right( self.tk_label_frame_draw_extent_frame)
        self.tk_input_extent_up = self.__tk_input_extent_up( self.tk_label_frame_draw_extent_frame)
        self.tk_input_extent_down = self.__tk_input_extent_down( self.tk_label_frame_draw_extent_frame)
        self.tk_input_extent_left = self.__tk_input_extent_left( self.tk_label_frame_draw_extent_frame)
        self.tk_input_extent_right = self.__tk_input_extent_right( self.tk_label_frame_draw_extent_frame)
        self.tk_button_reg_button = self.__tk_button_reg_button( self.tk_tabs_edges_0)
        self.tk_label_frame_draw_kwarg = self.__tk_label_frame_draw_kwarg( self.tk_tabs_edges_0)
        self.tk_label_frame_significance = self.__tk_label_frame_significance( self.tk_label_frame_draw_kwarg)
        self.tk_input_p_value = self.__tk_input_p_value( self.tk_label_frame_significance)
        self.tk_label_p_value_units = self.__tk_label_p_value_units( self.tk_label_frame_significance)
        self.tk_select_box_significance_para = self.__tk_select_box_significance_para( self.tk_label_frame_significance)
        self.tk_select_box_significance_style = self.__tk_select_box_significance_style( self.tk_label_frame_significance)
        self.tk_label_significance_style = self.__tk_label_significance_style( self.tk_label_frame_significance)
        self.tk_input_significance_style_color = self.__tk_input_significance_style_color( self.tk_label_frame_significance)
        self.tk_select_box_mfh1xf0z = self.__tk_select_box_mfh1xf0z( self.tk_label_frame_draw_kwarg)
        self.tk_label_frame_cont = self.__tk_label_frame_cont( self.tk_label_frame_draw_kwarg)
        self.tk_input_cont_lw = self.__tk_input_cont_lw( self.tk_label_frame_cont)
        self.tk_select_box_mfi0d4db = self.__tk_select_box_mfi0d4db( self.tk_label_frame_cont)
        self.tk_label_cont_lw = self.__tk_label_cont_lw( self.tk_label_frame_cont)
        self.tk_select_box_mfi1psry = self.__tk_select_box_mfi1psry( self.tk_label_frame_cont)
        self.tk_label_cont_postive = self.__tk_label_cont_postive( self.tk_label_frame_cont)
        self.tk_input_cont_postive_ls = self.__tk_input_cont_postive_ls( self.tk_label_frame_cont)
        self.tk_label_cont_postive_ls = self.__tk_label_cont_postive_ls( self.tk_label_frame_cont)
        self.tk_input_cont_postive_color = self.__tk_input_cont_postive_color( self.tk_label_frame_cont)
        self.tk_label_cont_postive_color = self.__tk_label_cont_postive_color( self.tk_label_frame_cont)
        self.tk_label_cont_negative = self.__tk_label_cont_negative( self.tk_label_frame_cont)
        self.tk_label_cont_negative_ls = self.__tk_label_cont_negative_ls( self.tk_label_frame_cont)
        self.tk_input_cont_negative_ls = self.__tk_input_cont_negative_ls( self.tk_label_frame_cont)
        self.tk_label_cont_negative_color = self.__tk_label_cont_negative_color( self.tk_label_frame_cont)
        self.tk_input_cont_negative_color = self.__tk_input_cont_negative_color( self.tk_label_frame_cont)
        self.tk_input_mfi2hfcp = self.__tk_input_mfi2hfcp( self.tk_label_frame_cont)
        self.tk_label_cont_level = self.__tk_label_cont_level( self.tk_label_frame_cont)
        self.tk_input_time_series_0 = self.__tk_input_time_series_0( self.tk_tabs_edges_0)
        self.tk_label_time_series_0 = self.__tk_label_time_series_0( self.tk_tabs_edges_0)
        self.tk_frame_data_select = self.__tk_frame_data_select( self.tk_tabs_edges_0)
        self.tk_check_button_data_hor_wind = self.__tk_check_button_data_hor_wind( self.tk_frame_data_select)
        self.tk_select_box_data_level = self.__tk_select_box_data_level( self.tk_frame_data_select)
        self.tk_check_button_data_t = self.__tk_check_button_data_t( self.tk_frame_data_select)
        self.tk_check_button_data_omega = self.__tk_check_button_data_omega( self.tk_frame_data_select)
        self.tk_check_button_data_geo = self.__tk_check_button_data_geo( self.tk_frame_data_select)
        self.tk_label_hPa = self.__tk_label_hPa( self.tk_frame_data_select)
        self.tk_check_button_data_ols = self.__tk_check_button_data_ols( self.tk_frame_data_select)
        self.tk_check_button_data_shf = self.__tk_check_button_data_shf( self.tk_frame_data_select)
        self.tk_check_button_data_lhf = self.__tk_check_button_data_lhf( self.tk_frame_data_select)
        self.tk_check_button_data_sst = self.__tk_check_button_data_sst( self.tk_frame_data_select)
        self.tk_check_button_data_slp = self.__tk_check_button_data_slp( self.tk_frame_data_select)
        self.tk_check_button_data_pre = self.__tk_check_button_data_pre( self.tk_frame_data_select)
        self.tk_check_button_data_t2m = self.__tk_check_button_data_t2m( self.tk_frame_data_select)
        self.tk_check_button_data_tcc = self.__tk_check_button_data_tcc( self.tk_frame_data_select)
        self.tk_check_button_interp = self.__tk_check_button_interp( self.tk_frame_data_select)
        self.tk_input_interp_x = self.__tk_input_interp_x( self.tk_frame_data_select)
        self.tk_input_interp_y = self.__tk_input_interp_y( self.tk_frame_data_select)
        self.tk_label_interp_x = self.__tk_label_interp_x( self.tk_frame_data_select)
        self.tk_label_interp_grid = self.__tk_label_interp_grid( self.tk_frame_data_select)
        self.tk_check_button_data_waf = self.__tk_check_button_data_waf( self.tk_frame_data_select)
        self.tk_check_button_data_mf = self.__tk_check_button_data_mf( self.tk_frame_data_select)
        self.tk_button_draw = self.__tk_button_draw( self.tk_tabs_edges_0)
        self.tk_button_saveas = self.__tk_button_saveas( self.tk_tabs_edges_0)
        self.tk_select_box_fig_save = self.__tk_select_box_fig_save( self.tk_tabs_edges_0)
        self.tk_input_fig_save_address = self.__tk_input_fig_save_address( self.tk_tabs_edges_0)
        self.tk_label_saveas_address = self.__tk_label_saveas_address( self.tk_tabs_edges_0)
    def __win(self):
        self.title("Climate Analyze")
        # 设置窗口大小、居中
        width = 604
        height = 670
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
        frame.place(x=0, y=0, width=602, height=670)
        return frame
    def __tk_tabs_edges(self,parent):
        frame = Notebook(parent)
        self.tk_tabs_edges_0 = self.__tk_frame_edges_0(frame)
        frame.add(self.tk_tabs_edges_0, text="回归分析")
        self.tk_tabs_edges_1 = self.__tk_frame_edges_1(frame)
        frame.add(self.tk_tabs_edges_1, text="数据路径配置")
        self.tk_tabs_edges_2 = self.__tk_frame_edges_2(frame)
        frame.add(self.tk_tabs_edges_2, text="功率谱分析")
        self.tk_tabs_edges_3 = self.__tk_frame_edges_3(frame)
        frame.add(self.tk_tabs_edges_3, text="非绝热加热率计算")
        frame.place(x=0, y=0, width=602, height=670)
        return frame
    def __tk_frame_edges_0(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=602, height=670)
        return frame
    def __tk_frame_edges_1(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=602, height=670)
        return frame
    def __tk_frame_edges_2(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=602, height=670)
        return frame
    def __tk_frame_edges_3(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=602, height=670)
        return frame
    def __tk_progressbar_reg_progress(self,parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL,)
        progressbar.place(x=4, y=33, width=168, height=22)
        return progressbar
    def __tk_canvas_figure_zone(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(x=1, y=306, width=599, height=337)
        return canvas
    def __tk_label_frame_draw_extent_frame(self,parent):
        frame = LabelFrame(parent,text="绘制范围",)
        frame.place(x=399, y=89, width=139, height=130)
        return frame
    def __tk_label_extent_up(self,parent):
        label = Label(parent,text="上",anchor="center", )
        label.place(x=0, y=0, width=30, height=22)
        return label
    def __tk_label_extent_down(self,parent):
        label = Label(parent,text="下",anchor="center", )
        label.place(x=0, y=27, width=30, height=22)
        return label
    def __tk_label_extent_left(self,parent):
        label = Label(parent,text="左",anchor="center", )
        label.place(x=0, y=54, width=30, height=22)
        return label
    def __tk_label_extent_right(self,parent):
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
        btn.place(x=4, y=60, width=168, height=27)
        return btn
    def __tk_label_frame_draw_kwarg(self,parent):
        frame = LabelFrame(parent,text="绘图参数",)
        frame.place(x=0, y=89, width=388, height=214)
        return frame
    def __tk_label_frame_significance(self,parent):
        frame = LabelFrame(parent,text="显著性检验",)
        frame.place(x=138, y=142, width=244, height=50)
        return frame
    def __tk_input_p_value(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=59, y=1, width=25, height=25)
        return ipt
    def __tk_label_p_value_units(self,parent):
        label = Label(parent,text="%",anchor="center", )
        label.place(x=85, y=1, width=25, height=25)
        return label
    def __tk_select_box_significance_para(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("sst","pre","z","t2m","t","w","tcc","ols","shf","lhf")
        cb.place(x=4, y=1, width=50, height=25)
        return cb
    def __tk_select_box_significance_style(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("dot","line")
        cb.place(x=188, y=1, width=50, height=25)
        return cb
    def __tk_label_significance_style(self,parent):
        label = Label(parent,text="样式",anchor="center", )
        label.place(x=110, y=1, width=35, height=25)
        return label
    def __tk_input_significance_style_color(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=144, y=1, width=39, height=25)
        return ipt
    def __tk_select_box_mfh1xf0z(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("回归图","相关图")
        cb.place(x=4, y=0, width=78, height=25)
        return cb
    def __tk_label_frame_cont(self,parent):
        frame = LabelFrame(parent,text="等值线",)
        frame.place(x=138, y=0, width=244, height=141)
        return frame
    def __tk_input_cont_lw(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=85, y=1, width=48, height=25)
        return ipt
    def __tk_select_box_mfi0d4db(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("sst","pre","z","t2m","t","w","tcc","ols","shf","lhf")
        cb.place(x=4, y=1, width=50, height=25)
        return cb
    def __tk_label_cont_lw(self,parent):
        label = Label(parent,text="lw",anchor="center", )
        label.place(x=59, y=1, width=25, height=25)
        return label
    def __tk_select_box_mfi1psry(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("无线标","有线标","有线标（白底）")
        cb.place(x=134, y=1, width=108, height=25)
        return cb
    def __tk_label_cont_postive(self,parent):
        label = Label(parent,text="正等值线:",anchor="center", )
        label.place(x=0, y=36, width=58, height=25)
        return label
    def __tk_input_cont_postive_ls(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=85, y=36, width=48, height=25)
        return ipt
    def __tk_label_cont_postive_ls(self,parent):
        label = Label(parent,text="ls",anchor="center", )
        label.place(x=59, y=36, width=25, height=25)
        return label
    def __tk_input_cont_postive_color(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=177, y=36, width=63, height=25)
        return ipt
    def __tk_label_cont_postive_color(self,parent):
        label = Label(parent,text="color",anchor="center", )
        label.place(x=135, y=36, width=39, height=25)
        return label
    def __tk_label_cont_negative(self,parent):
        label = Label(parent,text="负等值线:",anchor="center", )
        label.place(x=0, y=65, width=58, height=25)
        return label
    def __tk_label_cont_negative_ls(self,parent):
        label = Label(parent,text="ls",anchor="center", )
        label.place(x=59, y=65, width=25, height=25)
        return label
    def __tk_input_cont_negative_ls(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=85, y=65, width=48, height=25)
        return ipt
    def __tk_label_cont_negative_color(self,parent):
        label = Label(parent,text="color",anchor="center", )
        label.place(x=135, y=65, width=39, height=25)
        return label
    def __tk_input_cont_negative_color(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=177, y=65, width=63, height=25)
        return ipt
    def __tk_input_mfi2hfcp(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=59, y=94, width=181, height=25)
        return ipt
    def __tk_label_cont_level(self,parent):
        label = Label(parent,text="等值层级:",anchor="center", )
        label.place(x=0, y=94, width=58, height=25)
        return label
    def __tk_input_time_series_0(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=71, y=6, width=101, height=22)
        return ipt
    def __tk_label_time_series_0(self,parent):
        label = Label(parent,text="序列路径",anchor="center", )
        label.place(x=4, y=6, width=60, height=22)
        return label
    def __tk_frame_data_select(self,parent):
        frame = Frame(parent,)
        frame.place(x=180, y=6, width=416, height=81)
        return frame
    def __tk_check_button_data_hor_wind(self,parent):
        cb = Checkbutton(parent,text="UV",)
        cb.place(x=101, y=4, width=49, height=25)
        return cb
    def __tk_select_box_data_level(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("200","300","500","650","750","850","900","925","975")
        cb.place(x=4, y=4, width=59, height=25)
        return cb
    def __tk_check_button_data_t(self,parent):
        cb = Checkbutton(parent,text="T",)
        cb.place(x=207, y=4, width=40, height=25)
        return cb
    def __tk_check_button_data_omega(self,parent):
        cb = Checkbutton(parent,text="Omega",)
        cb.place(x=248, y=4, width=72, height=25)
        return cb
    def __tk_check_button_data_geo(self,parent):
        cb = Checkbutton(parent,text="H",)
        cb.place(x=321, y=4, width=41, height=25)
        return cb
    def __tk_label_hPa(self,parent):
        label = Label(parent,text="hPa",anchor="center", )
        label.place(x=70, y=4, width=30, height=25)
        return label
    def __tk_check_button_data_ols(self,parent):
        cb = Checkbutton(parent,text="OLS",)
        cb.place(x=0, y=30, width=55, height=25)
        return cb
    def __tk_check_button_data_shf(self,parent):
        cb = Checkbutton(parent,text="SHF",)
        cb.place(x=56, y=30, width=55, height=25)
        return cb
    def __tk_check_button_data_lhf(self,parent):
        cb = Checkbutton(parent,text="LHF",)
        cb.place(x=112, y=30, width=55, height=25)
        return cb
    def __tk_check_button_data_sst(self,parent):
        cb = Checkbutton(parent,text="SST",)
        cb.place(x=168, y=30, width=55, height=25)
        return cb
    def __tk_check_button_data_slp(self,parent):
        cb = Checkbutton(parent,text="SLP",)
        cb.place(x=224, y=30, width=55, height=25)
        return cb
    def __tk_check_button_data_pre(self,parent):
        cb = Checkbutton(parent,text="PRE",)
        cb.place(x=280, y=30, width=55, height=25)
        return cb
    def __tk_check_button_data_t2m(self,parent):
        cb = Checkbutton(parent,text="2-m T",)
        cb.place(x=336, y=30, width=62, height=25)
        return cb
    def __tk_check_button_data_tcc(self,parent):
        cb = Checkbutton(parent,text="TCC",)
        cb.place(x=0, y=56, width=55, height=25)
        return cb
    def __tk_check_button_interp(self,parent):
        cb = Checkbutton(parent,text="插值到",)
        cb.place(x=235, y=56, width=66, height=25)
        return cb
    def __tk_input_interp_x(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=302, y=56, width=30, height=25)
        return ipt
    def __tk_input_interp_y(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=350, y=56, width=30, height=25)
        return ipt
    def __tk_label_interp_x(self,parent):
        label = Label(parent,text="×",anchor="center", )
        label.place(x=333, y=56, width=15, height=25)
        return label
    def __tk_label_interp_grid(self,parent):
        label = Label(parent,text="网格",anchor="center", )
        label.place(x=381, y=56, width=35, height=25)
        return label
    def __tk_check_button_data_waf(self,parent):
        cb = Checkbutton(parent,text="WAF",)
        cb.place(x=151, y=4, width=55, height=25)
        return cb
    def __tk_check_button_data_mf(self,parent):
        cb = Checkbutton(parent,text="MF",)
        cb.place(x=363, y=4, width=49, height=25)
        return cb
    def __tk_button_draw(self,parent):
        btn = Button(parent, text="绘制", takefocus=False,)
        btn.place(x=400, y=234, width=60, height=25)
        return btn
    def __tk_button_saveas(self,parent):
        btn = Button(parent, text="另存为", takefocus=False,)
        btn.place(x=479, y=234, width=60, height=25)
        return btn
    def __tk_select_box_fig_save(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = (".png",".pdf")
        cb.place(x=546, y=271, width=51, height=27)
        return cb
    def __tk_input_fig_save_address(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=456, y=271, width=88, height=25)
        return ipt
    def __tk_label_saveas_address(self,parent):
        label = Label(parent,text="另存地址",anchor="center", )
        label.place(x=392, y=271, width=60, height=25)
        return label
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_reg_button.bind('<Button-1>',self.ctl.reg_start)
        self.tk_button_draw.bind('<Button-1>',self.ctl.draw_start)
        self.tk_button_saveas.bind('<Button-1>',self.ctl.fig_save)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()