from manimlib.imports import *
import math
import numpy as np

class IntroduceQuestion(Scene):
    def construct(self):
        question_text = TextMobject("今日题目：")
        question_text2 = TextMobject("反复掷一枚硬币，直到连续掷出n次正面停下。")
        question_text3 = TextMobject("求停下时掷的次数的期望E(X)。")
        question = VGroup(question_text, question_text2, question_text3)
        known_text = TextMobject("本视频涉及以下前置知识：")
        known_tex = TexMobject(
            "E(X)=\\sum p_i X",
            "E(X+a)=",
            "\\sum p_i (X+a)",
            "\\sum p_i X + \\sum p_i a",
            "\\sum p_i X + a",
            "E(X) + a"
        )
        solution = VGroup(known_tex[0], known_tex[1], known_tex[5])
        tex_of_sum = TexMobject(
            "\\sum_{i=1}^{n}\\frac{i}{2^i}=\\frac{1}{2}+\\frac{1}{2^2}2+\\frac{1}{2^3}3+...+\\frac{1}{2^n}n",
            "2\\sum_{i=1}^{n}\\frac{i}{2^i}=1+\\frac{1}{2}2+\\frac{1}{2^2}3+...+\\frac{1}{2^{n-1}}n",
            "\\sum_{i=1}^{n}\\frac{i}{2^i}=-\\frac{n}{2^n}+1+\\frac{1}{2}+\\frac{1}{2^2}+\\frac{1}{2^3}+...+\\frac{1}{2^n}",
            "\\sum_{i=1}^{n}\\frac{i}{2^i}=-\\frac{n}{2^n}+\\frac{2^{n+1}-2}{2^i}"
        )
        history = [known_text, solution]

        question.arrange(DOWN)
        known_tex[0].move_to(ORIGIN)
        known_tex[1].move_to(DOWN+LEFT)
        for i in range(2,6):
            known_tex[i].next_to(known_tex[1], RIGHT)
        tex_of_sum.arrange(DOWN)

        for i in range(0,3):
            self.play(Write(question[i]),runtime=10)
        self.count_down()
        self.play(FadeOut(question))
        self.remove(question)
        self.play(Write(known_text))
        self.play(ApplyMethod(known_text.to_edge, UP))
        self.play(Write(known_tex[0]))
        self.play(Write(known_tex[1:3]))
        for i in range(2, 5):
            self.play(ReplacementTransform(known_tex[i], known_tex[i+1]))
            self.wait(1)
        self.play(ApplyMethod(solution.next_to, known_text, DOWN))
        self.play(*[FadeOut(i) for i in history])
        for i in range(0,2):
            self.play(Write(tex_of_sum[i]))
            self.wait(1)
        self.play(ReplacementTransform(tex_of_sum[0:2].copy(), tex_of_sum[2]))
        self.wait()
        self.play(ReplacementTransform(tex_of_sum[2].copy(), tex_of_sum[3]))
        self.play(FadeOut(tex_of_sum[0:3]))
        self.play(*[FadeIn(i) for i in history])
        self.play(ApplyMethod(tex_of_sum[3].next_to, solution, DOWN))
        self.count_down()
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


class Special_case(Scene):
    def construct(self):
        introduce = TextMobject(
            "先研究一下简单的情况总是很有必要",
            "现在我们使n=2"
        )
        text = [
            "先分析一下抛硬币的过程",
            "在连续掷出2次正面之前",
            "只要掷出了一次反面就要在已掷出的次数的基础上重新掷",
            "设E(X)=T,于是我们可以列出方程"
        ]
        solve_text = VGroup(*[TextMobject(t) for t in text]).arrange(DOWN)
        equality = TextMobject(
                                "1",
                               "+0.5*T",
                               "+0.5*",
                               "(1+0.5*0",
                               "+0.5*T)",
                                "T=").arrange(RIGHT)
        explain_text =[
            "先掷一次",
            "若为反面则重新开始",
            "若为正面则继续接着掷第二次",
            "若为正面则结束",
            "若为反面则重新开始",
            "于是我们得到了方程",
            "解得T=6"
        ]
        explain = VGroup(*[TextMobject(t) for t in explain_text])

        introduce.arrange(DOWN)
        #solvetion.next_to(equality, DOWN)
        equality[5].next_to(equality[0], LEFT)
        for i in range(0,len(explain_text)):
            explain[i].move_to(UP*1)
        explain[len(explain_text)-1].move_to(2*DOWN)

        self.play(Write(introduce[0]))
        self.wait(2)
        self.play(Write(introduce[1]))
        self.wait(2)
        self.play(FadeOut(introduce[0]),
                  ApplyMethod(introduce[1].to_edge, UP))
        for i in range(0,len(text)):
            self.play(Write(solve_text[i]),runtime=2)
            self.wait(0.5)
        self.play(FadeOut(solve_text[0:len(text)-1]),
                  ApplyMethod(solve_text[len(text)-1].next_to, introduce[1], DOWN))
        self.play(Write(explain[0]))
        for i in range(0,len(explain_text)-1):
            self.play(Write(equality[i]))
            self.wait(1)
            self.play(ReplacementTransform(explain[i], explain[i+1]))
        self.wait(1)
        self.play(Write(TextMobject("这就是n=2时的情况").to_edge(DOWN)))
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


class normal_case(Scene):
    def construct(self):
        text = [
            "现在，我们把n还原回来",
            "在连续掷出n次正面的过程中",
            "只要掷出了一次反面就要在已掷出的次数的基础上重新掷",
            "设E(X)=T,参考n=2的特殊情况可以列出方程",
        ]
        solve_text = VGroup(*[TextMobject(t) for t in text])
        equalities = TexMobject(
            "T=",
            "(1-\\sum_{i=1}^{n}\\frac{1}{2})T=",
            "\\frac{T}{2^n}=",
            "1+0.5*T+0.5(1+0.5*T+0.5(1+0.5*T+0.5(...)))",
            "\\frac{n}{2^n}+\\sum_{i=1}^{n}\\frac{x+i}{2^i}",
            "\\frac{n}{2^n}+\\sum_{i=1}^{n}\\frac{x}{2^i}+\\sum_{i=1}^{n}\\frac{i}{2^i}",
            "\\frac{n}{2^n}+\\sum_{i=1}^{n}\\frac{i}{2^i}",
            "\\frac{n}{2^n}-\\frac{n}{2^n}+\\frac{2^{n+1}-2}{2^n}",
            "\\frac{2^{n+1}-2}{2^n}",
            "2^{n+1}-2"
        )
        middle = Dot(LEFT*3)
        all_in_all = TextMobject("于是我们就得到了通解").to_edge(UP,buff=2)
        final = TexMobject("T=").next_to(middle, LEFT)
        equalities[3].scale(0.72)
        solve_text.arrange(DOWN)
        for i in range(0,3):
            equalities[i].next_to(middle, LEFT)
        for i in range(3,10):
            equalities[i].next_to(middle, RIGHT)
        solvetion = VGroup(final, equalities[9])

        for i in range(0,len(text)):
            self.play(Write(solve_text[i]))
            self.wait(0.5)
        self.play(FadeOut(solve_text[0:3]), ApplyMethod(solve_text[3].to_edge, UP))
        self.play(Write(equalities[0]))
        self.play(Write(equalities[3]))
        self.wait(2)
        self.play(Write(TextMobject("整理一下").next_to(solve_text[3], DOWN).scale(0.8)))
        for i in range(3,5):
            self.play(ReplacementTransform(equalities[i], equalities[i+1]))
            self.wait(1)
        self.play(ReplacementTransform(equalities[0], equalities[1]),
                  ReplacementTransform(equalities[5],equalities[6]))
        self.remove(equalities[0])
        self.wait(1)
        self.play(ReplacementTransform(equalities[1], equalities[2]))
        self.wait(1)
        for i in range(6,8):
            self.play(ReplacementTransform(equalities[i], equalities[i+1]))
            self.wait(1)
        self.play(ReplacementTransform(equalities[2], final),
                  ReplacementTransform(equalities[8], equalities[9]))
        self.play(Write(all_in_all))
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