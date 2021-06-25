from gym_line_follower.envs import LineFollowerEnv
import matplotlib.pyplot as plt

from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, Concatenate, Input, Dropout
from keras.optimizers import Adam, RMSprop
from keras.callbacks import TensorBoard
from rl.agents import DDPGAgent
from rl.random import OrnsteinUhlenbeckProcess
from rl.memory import SequentialMemory
from rl.callbacks import ModelIntervalCheckpoint
import gym
import cv2
from PIL import Image

window_length = 5

env = LineFollowerEnv(gui=False, nb_cam_pts=1, max_track_err=0.4, 
                    power_limit=0.4, max_time=600, obsv_type="camera")

nb_actions = env.action_space.shape[0]
obs = env.reset()
space = env.observation_space
print(space.shape)
plt.imshow(obs)
plt.show()
# print(obs.shape)
# input_shape=(window_length,) + env.observation_space.shape
# print(input_shape)

# print("nb_actions:", nb_actions)
# print(space.shape)
# print(space)
# print(obs.shape)
# image = cv2.imwrite('image-2.jpg', obs)
# image = cv2.imwrite('image-3.jpg', image)
# print(image.shape)
# plt.imshow(image)
# plt.show()

# # Actor model
# actor = Sequential()
# actor.add(Flatten(input_shape=(window_length,) + env.observation_space.shape))
# actor.add(Dense(128, activation="relu"))
# actor.add(Dense(128, activation="relu"))
# actor.add(Dense(64, activation="relu"))
# actor.add(Dense(nb_actions, activation="tanh"))
# actor.summary()

# # Critic model
# action_input = Input(shape=(nb_actions,), name='action_input')
# observation_input = Input(shape=(window_length,) + env.observation_space.shape, name='observation_input')
# flattened_observation = Flatten()(observation_input)
# x = Concatenate()([action_input, flattened_observation])
# x = Dense(256, activation="relu")(x)
# x = Dense(256, activation="relu")(x)
# x = Dense(128, activation="relu")(x)
# x = Dense(1, activation="linear")(x)
# critic = Model(inputs=[action_input, observation_input], outputs=x)
# critic.summary()


# print(obs.shape)
# plt.imshow(obs)
# plt.show()