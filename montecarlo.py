import numpy as np

# Base parameters
ukraine_forces = np.array([1155, 14372, 783, 658, 319])  # Tanks, combat vehicles, self-propelled artillery, towed artillery, MLRS
russia_forces = np.array([10000, 25000, 5000, 3500, 3000])  # Tanks, combat vehicles, self-propelled artillery, towed artillery, MLRS
simulation_count = 10000

# Support range
support_start = 1.1  # 10% support
support_stop = 1.9    # 90% support
support_step = 0.01 

results = []

for support in np.arange(support_start, support_stop + support_step, support_step):
    ukraine_support = np.random.uniform(support, support, simulation_count)
    russia_support = np.random.uniform(1.0, 1.0, simulation_count)
    ukraine_variability = np.random.uniform(0.9, 1.7, simulation_count)
    russia_variability = np.random.uniform(0.9, 1.0, simulation_count)
    
    ukraine_results = 0
    russia_results = 0
    
    for i in range(simulation_count):
        ukraine_effectiveness = (ukraine_forces * ukraine_support[i] * ukraine_variability[i]).sum()
        russia_effectiveness = (russia_forces * russia_support[i] * russia_variability[i]).sum()
        
        if ukraine_effectiveness > russia_effectiveness:
            ukraine_results += 1
        elif ukraine_effectiveness < russia_effectiveness:
            russia_results += 1

    ukraine_win_percentage = ukraine_results / simulation_count * 100
    russia_win_percentage = russia_results / simulation_count * 100
    
    results.append((support, ukraine_win_percentage, russia_win_percentage))

for support, ukraine, russia in results:
    print(f"Support: {support:.1f}, Ukraine Wins: {ukraine:.2f}%, Russia Wins: {russia:.2f}%")
