def calc_freq():
    c = 3*(10**8) #speed of light
    wave_len = float(input("Enter wavelength in nanometers"))
    wave_len_in_m = 1/(10**9)
    freq = c/wave_len_in_m
    print(freq , "Hz")
calc_freq()
    