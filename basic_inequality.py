'''
这本来是原创出来的视频
快完工的时候突然发现有人做过了
关键还做的不错，于是就废弃了这里的代码
有兴趣可以来我的电报群玩：http://t.me/manimplayground
'''

from manimlib.imports import *
import math
import numpy as np


class Welcome(Scene):
    def construct(self):
        text = TextMobject("欢迎来到", "病态小鸽", "的数学世界")
        text[0].move_to(UP)
        text[1].move_to(LEFT).set_color("#29ABCA")
        text[2].next_to(text[1], RIGHT * 0.9, buff=0.1)

        self.play(Write(text[0]))
        self.play(ReplacementTransform(text[0].copy(), text[1:3]), run_time=2)
        self.wait()


class Introduce(Scene):
    def construct(self):
        text_list = TextMobject(
            "今天我们讲几个常用的基本不等式",
            "基本不等式涉及了\n几个常用平均",
        )
        func_name = TextMobject(
            "平方平均",
            "算数平均",
            "几何平均",
            "调和平均"
        )
        tex_list = TexMobject(
            "\\sqrt{\\frac{a^2+b^2}{2}}",
            "\\frac{a+b}{2}",
            "\\sqrt{ab}",
            "\\frac{2}{ \\frac{1}{a} + \\frac{1}{b} }",
            "\\sqrt{\\frac{a^2+b^2}{2}} \\geq \\frac{a+b}{2} \\geq \\sqrt{ab} \\geq \\frac{2}{ \\frac{1}{a} + \\frac{1}{b} }",
        )
        condition = TextMobject("对于a，b > 0, 我们有以下不等式成立：").move_to(UP*1.5)
        line = Line(np.array([-5,-3,0]), np.array([5,-3,0]))
        all_in_all = TextMobject("这便是常见基本不等式").move_to(DOWN*1.5)

        text_list.arrange(DOWN)
        tex_list.arrange(DOWN, buff=1)
        func_name.arrange(DOWN, buff=1.5).move_to(RIGHT)
        tex_list.move_to(DOWN + 2*LEFT)
        tex_list[4].move_to(ORIGIN)

        self.play(Write(text_list[0]))
        self.wait(1)
        self.play(ReplacementTransform(text_list[0], text_list[1]))
        self.wait(2)
        self.play(FadeOut(text_list))
        self.remove(text_list)
        for i in range(0,4):
            self.play(Write(tex_list[i]))
            self.play(Write(func_name[i]))
        self.play(FadeOut(func_name), ApplyMethod(tex_list[0:4].shift, 4*LEFT))
        self.play(Write(condition))
        self.play(ReplacementTransform(tex_list[0:4], tex_list[4]), runtime=5)
        self.play(Write(all_in_all))
        self.wait(2)


class ProveGraph(Scene):
    def construct(self):
        average = VGroup(*[TexMobject(t, color=c) for t,c in zip(
            [
                "a",
                "b",
                "\\sqrt{ab}",
                "\\frac{a+b}{2}",
                "\\sqrt{\\frac{a^2+b^2}{2}}",
                "\\frac{2}{ \\frac{1}{a} + \\frac{1}{b} }",
                #"\\sqrt{\\frac{a^2+b^2}{2}} \\geq \\frac{a+b}{2} \\geq \\sqrt{ab} \\geq \\frac{2}{ \\frac{1}{a} + \\frac{1}{b} }",
             ],
            [
                BLUE,
                RED,
                ORANGE,
                GREEN,
                PURPLE,
                YELLOW,
            ]
        )])
        inequal = TexMobject("\\geq", "\\geq", "\\geq").set_color(GOLD)
        inequality = VGroup(average[4], inequal[0], average[3], inequal[1], average[2], inequal[2], average[5]).arrange(RIGHT, buff=0.2)
        inequality.to_edge(DOWN).scale(1.2)

        r = 3
        dot_0 = Dot(2*LEFT, color=YELLOW)
        line_a = Line(r*LEFT, dot_0.get_center(), color=BLUE)
        line_a.add_updater(lambda a:a.become(Line(r*LEFT, dot_0.get_center(), color=BLUE)))
        average[0].next_to(line_a, DOWN)
        line_b = Line(dot_0.get_center(), r*RIGHT, color=RED)
        line_b.add_updater(lambda b:b.become(Line(dot_0.get_center(), r*RIGHT, color=RED)))
        average[1].next_to(line_b, DOWN)
        circle = Circle(radius=r, color=WHITE)

        abvalue_text = TexMobject("\\frac{a}{b}=").to_corner(UL)
        abvalue = DecimalNumber((dot_0.get_center()[0]+r)/(r-dot_0.get_center()[0]),
                                show_ellipsis=True,
                                num_decimal_places=3,
                                #include_sign=True,
                                ).next_to(abvalue_text, RIGHT)
        abvalue.add_updater(lambda ab:ab.set_value((dot_0.get_center()[0]+r)/(r-dot_0.get_center()[0])))

        arithmetic1 = Line(ORIGIN, r*UP, color=GREEN)
        arithmetic2 = Line(ORIGIN, dot_0.get_center() + UP*math.sqrt(r**2 - dot_0.get_center()[0]**2), color=GREEN)
        arithmetic2.add_updater(lambda a:a.become(Line(ORIGIN,
                                                    dot_0.get_center() + UP*math.sqrt(r**2 - dot_0.get_center()[0]**2),
                                                    color=GREEN
                                                    )))
        #average[3].next_to(arithmetic1, RIGHT)
        geometric = Line(dot_0.get_center(), dot_0.get_center() + UP*math.sqrt(r**2 - dot_0.get_center()[0]**2), color=ORANGE)
        geometric.add_updater(lambda h:h.become(Line(dot_0.get_center(),
                                                    dot_0.get_center() + UP*math.sqrt(r**2 - dot_0.get_center()[0]**2),
                                                    color=ORANGE
                                                    )))
        #average[2].next_to(geometric, LEFT)
        square = Line(dot_0.get_center(), r*UP, color=PURPLE)
        square.add_updater(lambda s:s.become(Line(dot_0.get_center(), r*UP, color=PURPLE)))
        harmonic1 = Line(
                        dot_0.get_center(),
                        RIGHT*(dot_0.get_center()[0]**3/r**2)
                        + UP*((dot_0.get_center()[0]**2)*math.sqrt(1-(dot_0.get_center()[0]/r)**2)/r),
                        color=WHITE
                        )
        harmonic1.add_updater(lambda h:h.become(
            Line(
                dot_0.get_center(),
                RIGHT * (dot_0.get_center()[0] ** 3 / r ** 2)
                + UP * ((dot_0.get_center()[0] ** 2) * math.sqrt(1 - (dot_0.get_center()[0] / r) ** 2)/r),
                color=WHITE
            )))
        harmonic2 = Line(
            dot_0.get_center() + UP*math.sqrt(r**2 - dot_0.get_center()[0]**2),
            RIGHT * (dot_0.get_center()[0] ** 3 / r ** 2)
            + UP * ((dot_0.get_center()[0] ** 2) * math.sqrt(1 - (dot_0.get_center()[0] / r) ** 2) / r),
            color=YELLOW
        )
        harmonic2.add_updater(lambda h: h.become(
            Line(
                dot_0.get_center() + UP*math.sqrt(r**2 - dot_0.get_center()[0]**2),
                RIGHT * (dot_0.get_center()[0] ** 3 / r ** 2)
                + UP * ((dot_0.get_center()[0] ** 2) * math.sqrt(1 - (dot_0.get_center()[0] / r) ** 2) / r),
                color=YELLOW
            )
        ))
        harmonic = VGroup(harmonic1, harmonic2)

        process = TexMobject("\\frac{|a-b|}{2}").next_to(dot_0, DR)


        sequence = [geometric, VGroup(arithmetic1, arithmetic2), square, harmonic]

        #self.add(dot_0, line_a, line_b, circle, arithmetic1, arithmetic2, geometric, square, harmonic)
        self.play(ShowCreation(dot_0))
        self.play(ShowCreation(line_a), Write(average[0]))
        self.play(ShowCreation(line_b), Write(average[1]))
        self.play(FadeInFromLarge(abvalue), FadeInFromLarge(abvalue_text))
        self.play(dot_0.shift, 3.9 * RIGHT, rate_func=there_and_back, run_time=4)
        self.play(ShowCreation(circle), ShowCreation(Dot(ORIGIN, color=WHITE)))
        self.average_born(average, sequence, process)
        self.play(dot_0.shift, 3.9 * RIGHT, rate_func=there_and_back, run_time=4)
        self.play(*[Write(inequal[i]) for i in range(0,3)])
        self.play(dot_0.move_to, 2.9 * LEFT, run_time=2)
        a = ValueTracker(-2.9)
        dot_0.add_updater(lambda d:d.become(Dot(a.get_value()*RIGHT)))
        self.play(a.increment_value, 5, rate_func=linear, run_time=8)
        #self.count_down()
        self.wait()

    def average_born(self, average, sequence, process):
        #for i in range(0,4):
        #    self.play(ShowCreation(sequence[i]), Write(average[i+2]))
        #    self.wait()

        #self.play(ShowCreation(average[]))
        #self.play(Write(process))

        for i in range(0,4):
            self.play(ShowCreation(sequence[i]))
            self.wait(1)
            self.play(ReplacementTransform(sequence[i].copy(), average[i+2]))
            self.wait()


    def count_down(self):
        count_down = TexMobject(
            "\\sqrt{25}",
            "2^2",
            "\\lfloor\\pi\\rfloor",
            "\\sum_{n=0}^{\\infty} \\frac{1}{2^n}",
            "-e^{\\pi i}"
        )
        for i in range(0,len(count_down)):
            count_down[i].to_corner(DR)
        self.play(Write(count_down[0]))
        for i in range(0,len(count_down)-1):
            self.play(ReplacementTransform(count_down[i],count_down[i+1]))
            self.wait(0.5)
        self.play(FadeOut(count_down[len(count_down)-1]))


class Ask(Scene):
    def construct(self):
        text = [
            #"为什么?",
            "因为a和b是可以缩放的",
            "所以我们现在研究a和b的比值",
        ]
        text_writer = VGroup(*[TextMobject(t) for t in text]).arrange(DOWN)
        title = TextMobject("几何证法")


        for i in range(0,2):
            self.play(Write(text_writer[i]))
        self.wait(2)
        self.play(FadeOut(text_writer))
        self.play(Write(title))
        self.wait()


class ArithmeticSolution(Scene):
    def construct(self):
        basic_inequal = TexMobject("a>0,b>0", "(a-b)^2 \\geq 0", "a^2-2ab+b^2 \\geq 0").arrange(RIGHT, buff=1)
        first = TexMobject(
            "2a^2+2b^2 \\geq a^2+2ab+b^2",
            "\\frac{a^2+b^2}{2} \\geq \\frac{(a+b)^2}{4}",
            "\\sqrt{\\frac{a^2+b^2}{2}} \\geq \\frac{a+b}{2}"
        ).arrange(DOWN).scale(0.7)
        second = TexMobject(
            "a^2+2ab+b^2 \\geq 4ab",
            "\\frac{(a+b)^2}{4} \\geq ab",
            "\\frac{a+b}{2} \\geq \\sqrt{ab}"
        ).arrange(DOWN).scale(0.7)
        third = TexMobject(
            "\\sqrt{\\frac{a^2+b^2}{2}} \\geq \\frac{a+b}{2}",
            "\\sqrt{ab} \\geq \\frac{2ab}{a+b}",
            "\\sqrt{ab} \\geq \\frac{2}{\\frac{1}{a}+\\frac{1}{b}}"
        ).arrange(DOWN).scale(0.7)
        all_in_all = TexMobject("\\sqrt{\\frac{a^2+b^2}{2}} \\geq \\frac{a+b}{2} \\geq \\sqrt{ab} \\geq \\frac{2}{ \\frac{1}{a} + \\frac{1}{b} }")


        basic_inequal.to_corner(UL)
        basic_inequal[2].next_to(basic_inequal[1], DOWN)
        first.next_to(second, LEFT, buff=0.5)
        third.next_to(third, RIGHT, buff=0.5)
        all_in_all.to_edge(DOWN)


        self.play(Write(basic_inequal[0:2]))
        self.play(ReplacementTransform(basic_inequal[1].copy(), basic_inequal[2]))
        self.wait(1)
        for tex in [first, second]:
            self.play(ReplacementTransform(basic_inequal[2].copy(), tex[0]))
            self.play(ReplacementTransform(tex[0].copy(), tex[1]))
            self.play(ReplacementTransform(tex[1].copy(), tex[2]))
            self.wait(1)
        self.play(ReplacementTransform(second[2].copy(), third[0]))
        self.play(ReplacementTransform(third[0].copy(), third[1]))
        self.play(ReplacementTransform(third[1].copy(), third[2]))
        self.wait(1)
        self.play(ReplacementTransform(VGroup(first[2], second[2], third[2]).copy(), all_in_all))
        self.count_down()


    def count_down(self):
        count_down = TexMobject(
            "\\sqrt{25}",
            "2^2",
            "\\lfloor\\pi\\rfloor",
            "\\sum_{n=0}^{\\infty} \\frac{1}{2^n}",
            "-e^{\\pi i}"
        )
        for i in range(0,len(count_down)):
            count_down[i].to_corner(DR)
        self.play(Write(count_down[0]))
        for i in range(0,len(count_down)-1):
            self.play(ReplacementTransform(count_down[i],count_down[i+1]))
            self.wait(0.5)
        self.play(FadeOut(count_down[len(count_down)-1]))


class change(Scene):
    def construct(self):
        text_list = []