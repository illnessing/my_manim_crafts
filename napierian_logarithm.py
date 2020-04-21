'''
已应用于视频：https://www.bilibili.com/video/BV1HK411j79Y
欢迎各位加入我的电报群来找我玩：http://t.me/manimplayground
'''

from manimlib.imports import *
import numpy as np
import math



class Tittle(Scene):
	def construct(self):
		ask = TexMobject("ln(-1)=?")
		ask.scale(3)
		ask.set_color_by_gradient(RED, YELLOW, GREEN, BLUE)
		self.add(ask)



class Quotes(Scene):
	def construct(self):
		quotes =  TextMobject(
			"新的数学方法和概念，往往比解决数学问题本身更重要。",
			color=BLUE
		)
		author = TextMobject(
			"------华罗庚",
			color=YELLOW
		)

		quotes.move_to(UP)
		author.next_to(quotes, DOWN, aligned_edge=RIGHT)

		self.play(Write(quotes), run_time=3)
		self.play(FadeIn(author), run_time=2)
		self.wait(1)
		self.play(FadeOut(quotes), FadeOut(author), run_time=2)



class RolePlay(Scene):
	def construct(self):
		text = [TextMobject(t)for t in [
			"幼儿园时期我们就学过了对数函数ln",
			"同时，老师也告诉过你ln(-1)是没有意义",
			"ln(-1)真的没有意义吗？"
			]
		]
		formula = TexMobject(
			"e^{ln(a)} = a",
			"ln(a+b)=ln(a)+ln(b)",
		).arrange(RIGHT, buff=1)

		text[0].move_to(2*UP)
		formula.next_to(text[0], DOWN, buff=0.3)
		text[1].next_to(formula, DOWN, buff=0.3)
		text[2].scale(2)
		
		
		self.play(FadeIn(text[0]), run_time=2)
		self.play(Write(formula), run_time=2)
		self.wait(1)
		self.play(FadeIn(text[1]),run_time=2)
		self.wait(1)
		self.play(ReplacementTransform(VGroup(formula, *text[0:2]), text[2]), run_time=2)
		self.wait(3)
		self.play(FadeOut(text[2]))
		
		
		
class EulerFormula(Scene):
	def construct(self):
		#引入
		introduce = TextMobject("在开始之前，我们先引进一个著名公式")
		euler_formula = TexMobject("e^{\\theta i}=cos(\\theta)+sin(\\theta)i").next_to(introduce, DOWN)
		
		self.play(FadeIn(introduce), run_time=2)
		self.play(Write(euler_formula), run_time=2)
		self.wait(1)
		
		chance = TextMobject("这个公式非常好证").next_to(euler_formula, DOWN)
		
		
		self.play(FadeIn(chance), run_time=2)
		self.wait(2)
		self.play(FadeOut(VGroup(introduce, euler_formula, chance)),run_time=2)
		
		
		#随便证明一下
		func_cos = TexMobject("cos(x)", "=","1", "-\\frac{x^2}{2!}", "+...", "+(-1)^n\\frac{x^{2n}}{(2n)!}", "+...").arrange(RIGHT).scale(0.75)
		func_sin = TexMobject("sin(x)", "=", "x", "-\\frac{x^3}{3!}", "+...", "+(-1)^n\\frac{x^{2n+1}}{(2n+1)!}", "+...").arrange(RIGHT).scale(0.75)
		func_sin_i = TexMobject("sin(x)i", "=", "xi", "-\\frac{x^3}{3!}i", "+...", "+(-1)^n\\frac{x^{2n+1}}{(2n+1)!}i", "+...").arrange(RIGHT).scale(0.75)
		func_e = TexMobject("e^x=1+x+\\frac{x^2}{2!}+\\frac{x^3}{3!}+...+\\frac{x^{n}}{n!}+...").to_edge(LEFT, buff=2).shift(UP*2)
		func_ei = TexMobject("e^{\\pi i}", "=", "1+xi-\\frac{x^2}{2!}-\\frac{x^3}{3!}i+...+(-1)^n\\frac{x^{2n}}{(2n)!}+\\frac{x^{2n+1}}{(2n+1)!}+...").arrange(RIGHT).to_edge(LEFT, buff=2).shift(UP*2)
		
		align_point = Dot()
		
		
		functions = VGroup(func_cos, func_sin, func_e)
		func_sin.next_to(func_ei[1], DOWN, submobject_to_align=func_sin[1], aligned_edge=LEFT, buff=1)
		func_sin_i.next_to(func_sin[1], ORIGIN, submobject_to_align=func_sin_i[1], aligned_edge=LEFT, buff=1)
		func_cos.next_to(func_sin[1], DOWN, submobject_to_align=func_cos[1], aligned_edge=LEFT, buff=1)
		euler_formula.to_edge(DOWN)
		
		
		self.play(Write(functions), run_time=6)
		self.wait(1)
		self.play(Transform(func_sin, func_sin_i), run_time=2)
		self.play(Transform(func_e, func_ei), run_time=2)
		self.wait(2)
		#开始对齐
		align_point.next_to(func_sin[0], LEFT, buff=0.1)
		self.play(func_cos[0].align_to, align_point, RIGHT, run_time=1)
		align_point.next_to(func_cos[2], RIGHT)
		self.play(func_sin[2:].align_to, align_point, LEFTrun_time=1)
		for i in range(3,6):
			align_point.next_to(func_sin[i-1], RIGHT)
			self.play(func_cos[i:].align_to, align_point, LEFT, run_time=1)
			align_point.next_to(func_cos[i], RIGHT)
			self.play(func_sin[i:].align_to, align_point, LEFT, run_time=1)
		#结束对齐
		self.wait(2)
		self.play(TransformFromCopy(functions, euler_formula))
		self.play(FadeOut(functions), run_time=2)
		self.remove(functions)
		
		
		#开始计算ln(-1)
		special_text = VGroup(*[TextMobject(t) for t in [
												  "特别的，当x取$$\\pi$$的时候，就是大家所熟知的欧拉公式",
												  "对着这个式子变一下形",
												  "便得到了ln(-1)的值"
												]]).arrange(DOWN).to_edge(UP)
		euler_formula_special = TexMobject("e^{\\pi i}=-1").move_to(DOWN)
		change = TexMobject("e^{ln(-1)}=e^{\\pi i}").next_to(euler_formula_special, ORIGIN)
		logarithm = TexMobject("ln(-1)=\\pi i").next_to(euler_formula_special, ORIGIN)
		
		
		self.play(FadeIn(special_text[0]), ApplyMethod(euler_formula.next_to, logarithm, ORIGIN), run_time=2)
		self.play(ReplacementTransform(euler_formula, euler_formula_special), run_time=2)
		self.wait(1)
		self.play(FadeIn(special_text[1]), ReplacementTransform(euler_formula_special, change), run_time=2)
		self.wait(1)
		self.play(FadeIn(special_text[2]), ReplacementTransform(change, logarithm), run_time=2)
		self.wait(2)
		self.play(FadeOut(special_text), FadeOut(logarithm), run_time=2)
		
		
		summarize = TextMobject("稍微推广一下就可以得到ln(x) x<0的情况")
		proccess = TexMobject("ln(x)=ln(-1*(-x))",
									  "ln(x)=ln(-1)+ln(-x)",
									  "ln(x)=ln(-x)+\\pi i").arrange(DOWN)
		
		
		self.play(FadeIn(summarize), run_time=2)
		self.play(summarize.to_edge, UP, run_time=2)
		self.play(Write(proccess[0]))
		self.wait(1)
		self.play(ReplacementTransform(proccess[0], proccess[1]), run_time=2)
		self.wait(1)
		self.play(ReplacementTransform(proccess[1], proccess[2]), run_time=2)
		self.wait(1)
		self.play(FadeOut(proccess[2]), FadeOut(summarize))



class RToC(Scene):
	#从实数到虚数的转场
	
	def construct(self):
		texts = TexMobject(
		"ln(a)= ln(a) (a>0)",
		"ln(|a|)+\\pi i (a<0)",
		#"$f(x) =\\begin{cases} x - 1 & x\\leqslant 3 \\\\x ^ 2 + 3 x - 1 & x > 3 \\end{cases}$",
		"ln(z)=? \\,(z\\in C)",
			)
		texts[0:2].arrange(DOWN, buff=0.3)
		texts[2].next_to(texts[0:2], ORIGIN)

		self.play(FadeIn(texts[0:2]), run_time=2)
		self.wait(0.5)
		self.play(Transform(texts[0:2], texts[2]), run_time=2)
		self.wait(0.5)
		self.play(FadeOut(texts[2]), run_time=2)
		self.wait(1)



class Generalize(Scene):
	def construct(self):
		complex_plane = NumberPlane()
		radius = ValueTracker(1)
		theta = ValueTracker(0)
		complex_z = Vector(np.array((radius.get_value()*math.cos(theta.get_value()),
											radius.get_value()*math.sin(theta.get_value()), 0)))
		complex_z.add_updater(lambda z:z.become(Vector(np.array((radius.get_value()*math.cos(theta.get_value()),
									radius.get_value()*math.sin(theta.get_value()), 0)))))
		angle_theta = Arc(
				color=RED,
				radius=0.5,
				angle=theta.get_value()
			)
		angle_theta.add_updater(lambda a:a.become(Arc(
				color=RED,
				fill_color=RED,
				fill_opacity=0.3,
				radius=0.5,
				angle=theta.get_value()
			)))
		def get_log_z():
			return VGroup(*[Dot(i) for i in [
				np.array((radius.get_value(), theta.get_value(), 0)),
				np.array((radius.get_value(), theta.get_value() - 2*math.pi, 0)),
				np.array((radius.get_value(), theta.get_value() + 2*math.pi, 0))
			]])
		log_z = Dot(np.array((radius.get_value(), theta.get_value(), 0)))
		log_z_label = TexMobject("ln(z)")
		log_z.add_updater(lambda z:z.become(Dot(np.array((radius.get_value(), theta.get_value(), 0)))))
		log_z_label.add_updater(lambda z:z.next_to(log_z, UR))
		label_x = TexMobject("R").to_edge(RIGHT).shift(UP/2)
		label_y = TexMobject("i").to_edge(UP).shift(RIGHT/2)
		transition = [TextMobject(t) for t in [
			"可能有的观众已经发现了",
			"利用欧拉公式的一般形式$e^{\\theta i}=cos(\\theta)+sin(\\theta)i$",
			"将z表示为$|z|*e^{\\theta}$我们可以轻松求出|z|=1时的ln(z)",
			"而且不难发现不止一个值$a=\\theta+2k*\\pi$满足$e^a=z$",
			"这时候就会有观众问了",
			"这不是函数吗怎么会有多个值呢？",
			"所以一般来说我们取$\\theta\\in (-\\pi,\\pi]$作为ln的定义域",
			"于是乎我们也可以得到$ln(z)=ln(|z|)+\\theta i$",
			"嗯，看起来这个函数把复平面变得有亿点点扭曲"
		]]
		for i in range(0, 9):
			transition[i].to_edge(DOWN)
		unit_circle = Circle(radius=1)
		dots = []
		for i in range(-7, 8):
			for j in range(-4, 5):
				if i != 0 or j != 0:
					dots.append(Dot(RIGHT*i + UP*j))

		def get_theta(p):
			x = p[0]
			y = p[1]
			if x == 0:
				if y == 0:
					return 0
				elif y > 0:
					return math.pi
				else:
					return -math.pi
			elif x > 0:
				return math.atan(y/x)
			elif x < 0:
				if y >= 0:
					return math.pi + math.atan(y/x)
				else:
					return math.atan(y/x) - math.pi

		ln_dots = [Dot(RIGHT*math.log(math.sqrt(d.get_center()[0]**2+d.get_center()[1]**2)) + UP*get_theta(d.get_center())) for d in dots]
		

		#先创造一个复数
		self.play(ShowCreation(complex_plane), Write(label_x), Write(label_y), run_time=2)
		self.play(ShowCreation(complex_z), run_time=1)
		self.play(theta.increment_value, 7*math.pi/3, run_time=2)
		theta.set_value(math.pi/3)
		self.wait(0.5)
		#开始陈述
		self.play(FadeIn(transition[0]), run_time=2)
		self.wait(0.5)
		self.play(FadeOut(transition[0]), FadeIn(transition[1]), run_time=2)
		self.wait(0.5)
		self.play(ShowCreation(angle_theta), run_time=2)
		self.play(FadeOut(transition[1]), FadeIn(transition[2]), ShowCreation(log_z), ShowCreation(log_z_label), run_time=2)
		self.wait(0.5)
		self.play(FadeOut(transition[2]), FadeIn(transition[3]), run_time=2)
		self.wait(0.5)
		self.play(radius.increment_value, 1, run_time=2)
		self.play(theta.increment_value, -math.pi/2, rate_func=there_and_back, run_time=2)
		self.wait(0.5)
		self.play(FadeOut(transition[3]), FadeIn(transition[4]), run_time=2)
		self.wait(0.5)
		self.play(FadeOut(transition[4]), FadeIn(transition[5]), run_time=2)
		self.wait(0.5)
		self.play(FadeOut(transition[5]), FadeIn(transition[6]), run_time=2)
		self.wait(0.5)
		self.play(*[ShowCreation(d) for d in dots], run_time=2)
		self.wait(1)
		self.play(FadeOut(transition[6]), FadeIn(transition[7]), *[Transform(d, nd) for d, nd in zip(dots, ln_dots)], run_time=2)
		'''		
		self.play(
			FadeOut(transition[6]),
			FadeIn(transition[7]),
			ApplyMethod(
				complex_plane.apply_function,
            	lambda p: np.array([
                	np.log(np.sqrt(p[0]**2+p[1]**2)),
                	get_theta(p),
                	0,
            	]), run_time=2))
        '''
		self.wait(0.5)
		self.play(FadeOut(transition[7]), FadeIn(transition[8]), run_time=2)
		self.wait()



class Final(Scene):
	def construct(self):
		texts = [TextMobject(t) for t in [
			"就在刚才我们完成了对好奇心的一次探索",
			"事实上数学的发展正是一次次的好奇而探索的过程",
			"分形",
			"数论",
			"欧拉公式(复变函数)",
			"和欧拉公式（拓扑）",
			"以及欧拉公式（三角公式）",
			"这些都是源自于一些非常简单甚至有些可笑的问题",
			"正是这一次次的好奇才有了数学这个美妙的世界",
			"数学不仅是形式科学,数学更是一门艺术"
		]]
		texts[9].set_color(BLUE).scale(1.5)
		for i in range(0,10):
			texts[i].to_corner(UL)

		self.play(Write(texts[0]), run_time=2)
		self.wait(0.5)
		self.play(ReplacementTransform(texts[0], texts[1]), run_time=2)
		self.wait(0.5)

		#分型
		self.play(ReplacementTransform(texts[1], texts[2]))

		def next_branch(branches):  # 利用上一次的枝桠生成下一层枝桠
				theta = 2 * math.pi / 3
				rote_left = np.array(
					((math.cos(theta), math.sin(theta), 0),
					 (-math.sin(theta), math.cos(theta), 0),
					 (0, 0, 1))
				)
				rote_right = np.array(
					((math.cos(theta), -math.sin(theta), 0),
					 (math.sin(theta), math.cos(theta), 0),
					 (0, 0, 1))
				)
				new_branches = []
				for branch in branches:
					branch1 = branch[0]
					branch2 = branch[1]

					middle = 2 * (branch1 - branch2) / 3
					right = middle @ rote_right + branch2
					left = middle @ rote_left + branch2

					new_branches.append((branch2, left))
					new_branches.append((branch2, right))

				return new_branches
		branches = [(4 * DOWN, 1 * DOWN)]
		tree = VGroup(*[Line(branches[0][0], branches[0][1])])
		self.play(ShowCreation(tree))
		for i in range(0, 5 ):
			branches = next_branch(branches)
			Vbranches = [Line(branch[0], branch[1]) for branch in branches]
			tree.add(*Vbranches)
			self.play(*[ShowCreation(branch) for branch in Vbranches])
		self.wait()


		#数论
		tabo_func = TexMobject(
			"\\frac{1}{2}<\\lfloor mod(\\lfloor\\tfrac{y}{5}\\rfloor 2^{-5\\lfloor x \\rfloor-mod(\\lfloor y \\rfloor,5)},2)\\rfloor"
		)
		self.play(ReplacementTransform(tree, tabo_func), ReplacementTransform(texts[2], texts[3]))
		self.wait(1)

		#欧拉(木大)公式
		euler_formula = TexMobject(
			"e^{\\pi i}+1=0",
			"V+F-E=2",
			"d^2=R^2-2Rr"
		)
		for i in range(0,3):
			euler_formula[i].to_corner(UR, buff=2)
		#1
		complane = NumberPlane()
		unit_circle = Circle(color=BLUE)
		complex_z = Vector(np.array((-1, 0, 0)), color=GREEN)
		euler_1 = VGroup(complane, unit_circle, complex_z)
		self.play(ReplacementTransform(tabo_func, euler_1), ReplacementTransform(texts[3], texts[4]), Write(euler_formula[0]), run_time=2)
		self.wait(1)
		#2
		euler_2 = TextMobject("V顶点数 F面数 E棱数")
		self.play(
			ReplacementTransform(euler_1, euler_2),
			ReplacementTransform(texts[4], texts[5]),
			ReplacementTransform(euler_formula[0], euler_formula[1]), run_time=2
		)
		self.wait(1)
		#3
		self.play(FadeOut(euler_2), ReplacementTransform(texts[5], texts[6]), ReplacementTransform(euler_formula[1], euler_formula[2]), run_time=2)
		points = (
			UP,
			3*DOWN+4*LEFT,
			2*DOWN+3*RIGHT
		)
		dots = [Dot(point) for point in points]
		lines = [
			Line(points[1], points[2]),
			Line(points[0], points[2]),
			Line(points[0], points[1])
		]
		euler_3 = VGroup(*dots, *lines)
		self.play(ShowCreation(euler_3), run_time=2)

		def get_length(m, n):
			p = m-n
			return math.sqrt(p[0]**2+p[1]**2)
		a = get_length(points[1], points[2])
		b = get_length(points[0], points[2])
		c = get_length(points[0], points[1])
		incentre= Dot((a*points[0] + b*points[1] + c*points[2])/(a+b+c))
		v_a = (points[1]-points[2])
		v_b = (points[0]-points[2])
		r = abs(v_a[0]*v_b[1]-v_a[1]*v_b[0])/(a+b+c)
		euler_3.add(incentre)
		circle_1 = Circle(arc_center=incentre.get_center(), radius=r)
		#euler_3.add(circle_1)
		euler_3.add(incentre)
		self.play(ShowCreation(circle_1), ShowCreation(incentre), run_time=2)
		vector_r = Vector(RIGHT*r).shift(incentre.get_center())
		self.play(ShowCreation(vector_r))
		euler_3.add(vector_r)

		A1=2*(points[1][0]-points[0][0])
		B1=2*(points[1][1]-points[0][1])
		C1 = points[1][0]**2 + points[1][1]**2 - points[0][0]**2 - points[0][1]**2
		A2 = 2 * (points[2][0] - points[1][0])
		B2 = 2 * (points[2][1] - points[1][1])
		C2 = points[2][0]**2 + points[2][1]**2 - points[1][0]**2 - points[1][1]**2
		circumcenter = Dot(np.array(
			(((C1*B2)-(C2*B1))/((A1*B2)-(A2*B1)),
			((A1*C2) - (A2 * C1)) / ((A1 * B2) - (A2 * B1)),
			0)
		))
		v_R = circumcenter.get_center()-points[0]
		R = math.sqrt(v_R[0]**2 + v_R[1]**2)
		circle_2 = Circle(arc_center=circumcenter.get_center(), radius=R, color=GREEN)
		#euler_3.add(circle_2)
		euler_3.add(circumcenter)
		self.play(ShowCreation(circle_2), ShowCreation(circumcenter), run_time=2)
		vector_R = Vector(UP * R).shift(circumcenter.get_center())
		self.play(ShowCreation(vector_R))
		euler_3.add(vector_R)
		d = Line(incentre.get_center(), circumcenter.get_center())
		self.play(ShowCreation(d))
		euler_3.add(d)
		self.wait(1)

		#求币
		coin = SVGMobject("C:\\manim-master\\crafts\\svg\\一笔画的svg素材\\svg_icon\\coin.svg", fill_color=YELLOW).scale(1.2)
		good = SVGMobject("C:\\manim-master\\crafts\\svg\\一笔画的svg素材\\svg_icon\\good.svg", fill_color=GREEN).move_to(5*LEFT).scale(1.2)
		share = SVGMobject("C:\\manim-master\\crafts\\svg\\一笔画的svg素材\\svg_icon\\favo.svg", fill_color=PURPLE).move_to(5*RIGHT).scale(1.2)
		self.play(
			FadeOut(euler_3),
			ReplacementTransform(texts[6], texts[7]),
			FadeOut(euler_formula[2]),
			ApplyMethod(circle_2.next_to, good, ORIGIN),
			ApplyMethod(circle_1.next_to, share, ORIGIN),
			run_time=2
		)
		self.remove(euler_3)
		self.play(
			ReplacementTransform(texts[7], texts[8]),
			Transform(circle_2, good),
			ShowCreation(coin),
			Transform(circle_1, share),
			run_time=2
		)
		self.wait(1)
		self.play(ReplacementTransform(texts[8], texts[9]), run_time=2)
		self.wait(2)