from manim import *
import numpy as np
from Dice import *


class DistributionDiceRoll(Scene):
    def construct(self):
        np.random.seed(49312188)
        count_dice = 7
        count_roll = 10**5
        distr_roll = []
      
        for i in range(count_dice):
            roll = np.sum(np.random.randint(1, 7, size = (i+1,count_roll)), axis=0)
            val = np.zeros((i+1)*6)
            for r in roll:
                val[r-1] += 1
            
            distr_roll.append(val/count_roll)

        dice = VGroup(*[create_dice(np.random.randint(1,7), 0.75, 0.2) for _ in range(count_dice)]).arrange(RIGHT,buff =0.2) 
        hist = BarChart(
            distr_roll[0],
            bar_names=[f"{i}" for i in range(1,7)],
            bar_colors=["#2F58CD" for _ in range(6)]
        ).scale(0.85)
        VGroup(hist, dice).arrange(DOWN, buff = 1)
        
        self.play(GrowFromPoint(dice[0], [dice[0].get_bottom()[0], -5, 0]))
        self.play(DrawBorderThenFill(hist[0:2]))

        for k in range(1, count_dice):
            new_hist = BarChart(
            distr_roll[k],
            bar_names = [f"{i}" for i in range(1, k*6 + 7)],
            bar_colors = ["#2F58CD" for _ in range(k*6)],
            ).move_to(hist.get_center()).scale(0.85)
            
            self.play(GrowFromPoint(dice[k], [dice[k].get_bottom()[0], -5, 0]), run_time=0.5)
            self.play(ReplacementTransform(hist[0:2], new_hist[0:2]), run_time=0.5)
            hist = new_hist

        mean = 3.5*count_dice
        std = (count_dice*35/12)**0.5   
        func = lambda t : np.exp(-0.5*((t-mean)/std)**2)/(std*(2*np.pi)**0.5)
        func = hist.plot(func, x_range=[0, 6*(count_dice)], color="#FDE910")
        self.play(Create(func), run_time=1.5, rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.5)