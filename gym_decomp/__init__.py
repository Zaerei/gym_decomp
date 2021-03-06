from gym.envs.registration import register

register(
    id='MiniGridworld-v0',
    entry_point='gym_decomp.gridworld:MiniGridworldV0'
)

register(
    id='Cliffworld-v0',
    entry_point='gym_decomp.gridworld:CliffworldV0'
)

register(
    id='CliffworldDeterministic-v0',
    entry_point='gym_decomp.gridworld:CliffworldDeterministicV0'
)

register(
    id="HivSimulator-v0",
    entry_point='gym_decomp.hiv:HivSimV0'
)

register(
    id="ScaiiFourTowers-v1",
    entry_point='gym_decomp.scaii:FourTowersV1'
)
