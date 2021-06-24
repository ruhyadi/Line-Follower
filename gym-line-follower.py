
#%%
import os
import json
import warnings
from time import time, sleep

import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
import pybullet as p

from gym_line_follower.track import Track
from gym_line_follower.track_plane_builder import build_track_plane
from gym_line_follower.bullet_client import BulletClient
from gym_line_follower.line_follower_bot import LineFollowerBot
from gym_line_follower.randomizer_dict import RandomizerDict
from gym_line_follower.envs import LineFollowerEnv
env = LineFollowerEnv(gui=False, nb_cam_pts=8, max_track_err=0.4, power_limit=0.4, max_time=600, obsv_type="points_latch")
env.reset()

for _ in range(10):
    for i in range(10):
        obsv, rew, done, info = env.step((0.5, 0.))
        sleep(0.05)
        if done:
            break
    env.reset()
env.close()

env.render(mode='human')

# %%
