from re import T
import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

def define_membership_functions():
    # Create linguistic variables
    x_temperature = np.arange(35.9, 42, 0.1)
    x_headache = np.arange(0, 10.5, 0.5)
    x_eyepain = np.arange(0, 10.5, 0.5)
    x_musclejointpain = np.arange(0, 10.5, 0.5)
    x_nausea = np.arange(0, 10.5, 0.5)
    x_vomiting = np.arange(0, 2, 1)
    x_swollenglands = np.arange(0, 2, 1)
    x_rash = np.arange(0, 2, 1)
    y_risk = np.arange(0, 46, 1)

    # Define membership functions for temperature
    temperature_normal = mf.trapmf(x_temperature, [0, 35.9, 37, 37.5])
    temperature_light_fever = mf.trapmf(x_temperature, [37, 37.5, 38.5, 40])
    temperature_high_fever = mf.trapmf(x_temperature, [38.5, 40, 42, 43])

    # Define membership functions for headache
    headache_mild = fuzz.trapmf(x_headache, [0, 2, 3, 5])
    headache_medium = fuzz.trapmf(x_headache, [3, 5, 6, 8])
    headache_severe = fuzz.trapmf(x_headache, [6, 8, 10, 11])

    # Define membership functions for eyepain
    eyepain_low = fuzz.trapmf(x_eyepain, [0, 2, 3, 5])
    eyepain_medium = fuzz.trapmf(x_eyepain, [3, 5, 6, 8])
    eyepain_severe = fuzz.trapmf(x_eyepain, [6, 8, 10, 11])

    # Define membership functions for muscle joint pain
    musclejointpain_low = fuzz.trapmf(x_musclejointpain, [0, 2, 3, 5])
    musclejointpain_medium = fuzz.trapmf(x_musclejointpain, [3, 5, 6, 8])
    musclejointpain_severe = fuzz.trapmf(x_musclejointpain, [6, 8, 10, 11])

    # Define membership functions for nausea
    nausea_low = fuzz.trapmf(x_nausea, [0, 2, 3, 5])
    nausea_medium = fuzz.trapmf(x_nausea, [3, 5, 6, 8])
    nausea_severe = fuzz.trapmf(x_nausea, [6, 8, 10, 11])

    # Define membership functions for vomiting
    vomiting_yes = fuzz.trimf(x_vomiting, [0, 1, 1])
    vomiting_no = fuzz.trimf(x_vomiting, [0, 0, 1])

    # Define membership functions for swollen glands
    swollenglands_yes = fuzz.trimf(x_swollenglands, [0, 1, 1]) 
    swollenglands_no = fuzz.trimf(x_swollenglands, [0, 0, 1]) 

    # Define membership functions for rash
    rash_yes = fuzz.trimf(x_rash, [0, 1, 1])  
    rash_no = fuzz.trimf(x_rash, [0, 0, 1]) 

    # Membership Function for Risk
    risk_not = mf.trapmf(y_risk, [0 ,0 ,5 ,10])
    risk_low = mf.trapmf(y_risk, [5 ,10 ,15 ,20])
    risk_moderate = mf.trapmf(y_risk, [15 ,20 ,25 ,30])
    risk_high = mf.trapmf(y_risk, [25 ,30 ,35 ,40])
    risk_veryHigh = mf.trapmf(y_risk, [35, 40, 45, 50])

     # Return the linguistic variables and their membership functions
    return {
        'x_temperature': x_temperature,
        'temperature_normal': temperature_normal,
        'temperature_light_fever': temperature_light_fever,
        'temperature_high_fever': temperature_high_fever,
        'x_headache': x_headache,
        'headache_mild': headache_mild,
        'headache_medium': headache_medium,
        'headache_severe': headache_severe,
        'x_eyepain': x_eyepain,
        'eyepain_low': eyepain_low,
        'eyepain_medium': eyepain_medium,
        'eyepain_severe': eyepain_severe,
        'x_musclejointpain': x_musclejointpain,
        'musclejointpain_low': musclejointpain_low,
        'musclejointpain_medium': musclejointpain_medium,
        'musclejointpain_severe': musclejointpain_severe,
        'x_nausea': x_nausea,
        'nausea_low': nausea_low,
        'nausea_medium': nausea_medium,
        'nausea_severe': nausea_severe,
        'x_vomiting': x_vomiting,
        'vomiting_yes': vomiting_yes,
        'vomiting_no': vomiting_no,
        'x_swollenglands': x_swollenglands,
        'swollenglands_yes': swollenglands_yes,
        'swollenglands_no': swollenglands_no,
        'x_rash': x_rash,
        'rash_yes': rash_yes,
        'rash_no': rash_no,
        'y_risk': y_risk,
        'risk_not': risk_not,
        'risk_low': risk_low,
        'risk_moderate': risk_moderate,
        'risk_high': risk_high,
        'risk_veryHigh': risk_veryHigh,
}

def perform_fuzzy_logic(temperature, headache, eyepain, musclejointpain, nausea, vomiting, swollenglands, rash):
    variables = define_membership_functions()

    # Extract linguistic variables and membership functions from the dictionary
    x_temperature = variables['x_temperature']
    mem_normal_temperature = variables['temperature_normal']
    mem_light_fever_temperature = variables['temperature_light_fever']
    mem_high_fever_temperature = variables['temperature_high_fever']

    x_headache = variables['x_headache']
    mem_mild_headache = variables['headache_mild']
    mem_medium_headache = variables['headache_medium']
    mem_severe_headache = variables['headache_severe']

    x_eyepain = variables['x_eyepain']
    mem_low_eyepain  = variables['eyepain_low']
    mem_medium_eyepain = variables['eyepain_medium']
    mem_severe_eyepain = variables['eyepain_severe']

    x_musclejointpain = variables['x_musclejointpain']
    musclejointpain_low_degree = variables['musclejointpain_low']
    musclejointpain_medium_degree = variables['musclejointpain_medium']
    musclejointpain_severe_degree  = variables['musclejointpain_severe']

    x_nausea = variables['x_nausea']
    mem_low_nausea = variables['nausea_low']
    mem_medium_nausea = variables['nausea_medium']
    mem_severe_nausea = variables['nausea_severe']

    x_vomiting = variables['x_vomiting']
    mem_yes_vomiting = variables['vomiting_yes']
    mem_no_vomiting = variables['vomiting_no']

    x_swollenglands = variables['x_swollenglands']
    mem_yes_swollenglands = variables['swollenglands_yes']
    mem_no_swollenglands = variables['swollenglands_no']

    x_rash = variables['x_rash']
    mem_yes_rash = variables['rash_yes']
    mem_no_rash = variables['rash_no']

    y_risk = variables['y_risk']
    risk_not = variables['risk_not']
    risk_low = variables['risk_low']
    risk_moderate = variables['risk_moderate']
    risk_high = variables['risk_high']
    risk_veryHigh = variables['risk_veryHigh']

    # Fuzzify input variables
    temperature_membership = {
        'normal': fuzz.interp_membership(x_temperature, mem_normal_temperature, temperature),
        'light_fever': fuzz.interp_membership(x_temperature, mem_light_fever_temperature, temperature),
        'high_fever': fuzz.interp_membership(x_temperature, mem_high_fever_temperature, temperature),
    }

    headache_membership = {
        'mild': fuzz.interp_membership(x_headache, mem_mild_headache, headache),
        'medium': fuzz.interp_membership(x_headache, mem_medium_headache, headache),
        'severe': fuzz.interp_membership(x_headache, mem_severe_headache, headache),
    }

    eyepain_membership = {
        'low': fuzz.interp_membership(x_eyepain, mem_low_eyepain, eyepain),
        'medium': fuzz.interp_membership(x_eyepain, mem_medium_eyepain, eyepain),
        'severe': fuzz.interp_membership(x_eyepain, mem_severe_eyepain, eyepain),
    }

    musclejointpain_membership = {
        'low': fuzz.interp_membership(x_musclejointpain, musclejointpain_low_degree, musclejointpain),
        'medium': fuzz.interp_membership(x_musclejointpain, musclejointpain_medium_degree, musclejointpain),
        'severe': fuzz.interp_membership(x_musclejointpain, musclejointpain_severe_degree, musclejointpain),
    }

    nausea_membership = {
        'low': fuzz.interp_membership(x_nausea, mem_low_nausea, nausea),
        'medium': fuzz.interp_membership(x_nausea, mem_medium_nausea, nausea),
        'severe': fuzz.interp_membership(x_nausea, mem_severe_nausea, nausea),
    }

    vomiting_membership = {
        'yes': fuzz.interp_membership(x_vomiting, mem_yes_vomiting, vomiting),
        'no': fuzz.interp_membership(x_vomiting, mem_no_vomiting, vomiting),
    }

    swollenglands_membership = {
        'yes': fuzz.interp_membership(x_swollenglands, mem_yes_swollenglands, swollenglands),
        'no': fuzz.interp_membership(x_swollenglands, mem_no_swollenglands, swollenglands),
    }

    rash_membership = {
        'yes': fuzz.interp_membership(x_rash, mem_yes_rash, rash),
        'no': fuzz.interp_membership(x_rash, mem_no_rash, rash),
    }

    # Apply rules (using the min operator)
    rule1 = np.fmin(temperature_membership['normal'], risk_not)
    rule2 = np.fmin(np.fmin(eyepain_membership['low'], nausea_membership['low']), risk_not)
    rule3 = np.fmin(np.fmin(np.fmin(temperature_membership['normal'], headache_membership['mild']), musclejointpain_membership['low']), risk_not)
    rule4 = np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], headache_membership['mild']), musclejointpain_membership['low']), risk_low)
    rule5 = np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], headache_membership['medium']), swollenglands_membership['yes']), risk_moderate)
    rule6 = np.fmin(np.fmin(temperature_membership['light_fever'], musclejointpain_membership['medium']), risk_moderate)
    rule7 = np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], vomiting_membership['yes']), rash_membership['yes']), risk_high)
    rule8 = np.fmin(np.fmin(np.fmin(temperature_membership['normal'], headache_membership['mild']), musclejointpain_membership['low']), risk_low)
    rule9 = np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], headache_membership['severe']), vomiting_membership['yes']), risk_moderate)
    rule10 = np.fmin(np.fmin(temperature_membership['normal'], nausea_membership['severe']), risk_low)
    rule11 = np.fmin(np.fmin(temperature_membership['normal'], eyepain_membership['medium']), risk_not)
    rule12 = np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], headache_membership['severe']), vomiting_membership['yes']), risk_moderate)
    rule13 = np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], headache_membership['severe']), rash_membership['yes']), risk_high)
    rule14 = np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['severe']), risk_veryHigh)
    rule15 = np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], musclejointpain_membership['severe']), rash_membership['yes']), risk_veryHigh)
    rule16 = np.fmin(np.fmin(np.fmin(temperature_membership['normal'], headache_membership['mild']), eyepain_membership['low']), risk_not)
    rule17 = np.fmin(np.fmin(np.fmin(temperature_membership['normal'], nausea_membership['low']), swollenglands_membership['yes']), risk_low)
    rule18 = np.fmin(np.fmin(np.fmin(headache_membership['severe'], musclejointpain_membership['severe']), vomiting_membership['yes']), risk_veryHigh)
    rule19 = np.fmin(np.fmin(np.fmin(eyepain_membership['severe'], nausea_membership['severe']), swollenglands_membership['yes']), risk_veryHigh)
    rule20 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['severe']), musclejointpain_membership['severe']), nausea_membership['severe']), vomiting_membership['yes']), swollenglands_membership['yes']), rash_membership['yes']), risk_veryHigh)
    rule21 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), nausea_membership['severe']), nausea_membership['medium']), musclejointpain_membership['severe']), vomiting_membership['yes']), swollenglands_membership['yes']), rash_membership['yes']), risk_veryHigh)
    rule22 = np.fmin(np.fmin(np.fmin(temperature_membership['normal'], headache_membership['mild']), musclejointpain_membership['medium']), risk_low)
    rule23 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['severe']), musclejointpain_membership['severe']), rash_membership['yes']), risk_veryHigh)
    rule24 = np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], headache_membership['medium']), eyepain_membership['medium']), risk_low)
    rule25 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['normal'], headache_membership['severe']), eyepain_membership['medium']), musclejointpain_membership['medium']), vomiting_membership['yes']), risk_moderate)
    rule26 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], headache_membership['mild']), eyepain_membership['medium']), nausea_membership['medium']), vomiting_membership['yes']), swollenglands_membership['yes']), risk_high)
    rule27 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], headache_membership['mild']), musclejointpain_membership['medium']), nausea_membership['medium']), swollenglands_membership['yes']), risk_moderate)
    rule28 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], headache_membership['medium']), eyepain_membership['low']), musclejointpain_membership['medium']), swollenglands_membership['yes']), risk_high)
    rule29 = np.fmin(np.fmin(np.fmin(temperature_membership['normal'], musclejointpain_membership['low']), swollenglands_membership['yes']), risk_not)
    rule30 = np.fmin(np.fmin(np.fmin(temperature_membership['normal'], musclejointpain_membership['medium']), rash_membership['yes']), risk_not)
    rule31 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['low']), musclejointpain_membership['low']), nausea_membership['low']), vomiting_membership['yes']), swollenglands_membership['yes']), rash_membership['no']), risk_moderate)
    rule32 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['medium']), eyepain_membership['severe']), musclejointpain_membership['severe']), nausea_membership['severe']), vomiting_membership['yes']), swollenglands_membership['no']), rash_membership['yes']), risk_veryHigh)
    rule33 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['medium']), eyepain_membership['medium']), musclejointpain_membership['medium']), nausea_membership['medium']), vomiting_membership['no']), swollenglands_membership['yes']), rash_membership['yes']), risk_high)
    rule34 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['light_fever'], headache_membership['severe']), eyepain_membership['severe']), musclejointpain_membership['low']), nausea_membership['severe']), vomiting_membership['yes']), swollenglands_membership['no']), rash_membership['no']), risk_low)
    rule35 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['low']), musclejointpain_membership['low']), nausea_membership['low']), vomiting_membership['no']), swollenglands_membership['no']), rash_membership['yes']), risk_high)
    rule36 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['medium']), musclejointpain_membership['medium']), nausea_membership['medium']), vomiting_membership['no']), swollenglands_membership['no']), rash_membership['yes']), risk_high)
    rule37 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['low']), musclejointpain_membership['medium']), nausea_membership['severe']), vomiting_membership['yes']), swollenglands_membership['yes']), rash_membership['yes']), risk_veryHigh)
    rule38 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['low']), musclejointpain_membership['severe']), nausea_membership['medium']), vomiting_membership['yes']), swollenglands_membership['yes']), rash_membership['no']), risk_high)
    rule39 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['severe']), musclejointpain_membership['medium']), nausea_membership['severe']), vomiting_membership['no']), swollenglands_membership['no']), rash_membership['yes']), risk_high)
    rule40 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['severe']), musclejointpain_membership['low']), nausea_membership['medium']), vomiting_membership['yes']), swollenglands_membership['yes']), rash_membership['yes']), risk_veryHigh)
    rule41 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['medium']), musclejointpain_membership['medium']), nausea_membership['medium']), vomiting_membership['yes']), swollenglands_membership['yes']), rash_membership['yes']), risk_veryHigh)
    rule42 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['severe']), musclejointpain_membership['severe']), rash_membership['yes']), risk_veryHigh)
    rule43 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['severe']), eyepain_membership['severe']), musclejointpain_membership['medium']), vomiting_membership['yes']), rash_membership['yes']), risk_veryHigh)
    rule44 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(temperature_membership['high_fever'], headache_membership['medium']), eyepain_membership['medium']), musclejointpain_membership['medium']), nausea_membership['severe']), rash_membership['yes']), risk_high)

    out_not = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule1, rule2),rule3),rule11),rule16),rule29), rule30)
    out_low = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule4,rule8),rule10), rule17), rule22), rule24), rule34)
    out_moderate = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule5, rule6),rule9), rule12), rule25), rule27),rule31)
    out_high = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule7, rule13),rule26),rule28), rule33), rule35), rule36), rule38), rule39),rule44)
    out_veryHigh = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule14,rule15),rule18),rule19),rule20),rule21),rule23),rule32),rule37),rule40), rule41),rule42),rule43)

    # risk0 = np.zeros_like(y_risk)

    out_risk = np.fmax(np.fmax(np.fmax(np.fmax(out_not, out_low), out_moderate), out_high), out_veryHigh)

    defuzzified  = fuzz.defuzz(y_risk, out_risk, 'centroid')

    result = fuzz.interp_membership(y_risk, out_risk, defuzzified)
    
    rounded_result = round(result, 5)
    
    text = "default"
    
    if(rounded_result > 0.5):
        text = "Anda berisiko tinggi terkena demam berdarah!"
    elif(rounded_result <= 0.5 and rounded_result > 0.25):
        text = "Anda kemungkinan terkena demam berdarah!"
    elif(rounded_result > 0 and rounded_result < 0.25): 
        text = "Anda kemungkinan sangat kecil terkena demam berdarah!"
    else: 
        text = "Anda tidak terkena demam berdarah!"
        
    data = "Temperature: {}, Headache: {}, Eye Pain: {}, " \
            "Muscle and Joint Pain: {}, Nausea: {}, Vomiting: {}, " \
            "Swollen Glands: {}, Rash: {}".format(temperature, headache, eyepain,
                                                  musclejointpain, nausea, vomiting,
                                                  swollenglands, rash)
    
    return text, data