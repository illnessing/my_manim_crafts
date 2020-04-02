from manimlib.imports import *
import math
import numpy as np

class CountDown(Scene):
    def construct(self):
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


class ForCoins(Scene):
    def construct(self):
        self.for_coins()

    def for_coins(self):
        text = [
            "如果你觉得不错就点个三连吧",
            "你的三连是对我最好的支持",
            "我是病态小鸽",
            "我们下期再见~~~~"
        ]
        texts = VGroup(*[TextMobject(t) for t in text])
        texts.arrange(DOWN, buff=1)
        texts.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        for i in range(0,len(text)):
            self.play(Write(texts[i]))
            self.wait(0.7)
        self.wait()