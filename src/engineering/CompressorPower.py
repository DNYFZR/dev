'''Compressor Power Calculator'''

def compressor_power(target_flow, target_pressure, inlet_pressure = 101.325, motor_eff = 0.95, gamma = 1.4):
    compression_ratio = target_pressure / inlet_pressure
    power = (1 / (gamma-1)) * inlet_pressure * target_flow * (compression_ratio ** ((gamma - 1) / gamma) - 1)

    return round(power / motor_eff)

def power_calculator(flow, p_out, p_in, motor_eff, annual_hrs, cost_per_unit, print_output = False):
    flow = flow / 3600 # m3/s
    power = compressor_power(flow, p_out, p_in, motor_eff=motor_eff) # kW
    annual = power * annual_hrs / 1000 
    cost = round(annual * cost_per_unit, 1)

    if print_output == True:
        print(f'> This system would need a motor capacity of {round(power)} kW.')
        print(f'> Annually it would require {round(annual)} MWh, at a cost of ${cost}k.')
    else:
        return (power, annual, cost)


if __name__ == '__main__':
    import matplotlib.pyplot as plt, seaborn as sns
    sns.set()
    power_calculator(5000, 160, 100, 0.95, 8760, 0.135, print_output=True)

    x = [i for i in range(1000, 5000, 250)]
    y = [] 
    for i in x:
        y.append(power_calculator(i, 160, 100, 0.95, 8760, 0.15)[2])
    
    plt.plot(x, y)
    plt.xlabel('Air Flow')
    plt.ylabel('Annual Cost (thousands)')
    plt.title('Compressor Calculator')
    plt.show()
