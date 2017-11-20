#Will produce the solutions to an elliptic curve within a given range,
def ellipiticCurve(ff,b):  #finite field (range), the b bit of  |y**2 = x**3 + ax + b|   , in BTCs case this is 7.
	for x in range(1,ff):
	    for y in range(1,ff):
	        if (y**2) % ff == (x**3 + b) % ff:
	            print(x,y)

ellipiticCurve(2400,7)