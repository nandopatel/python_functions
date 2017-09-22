class Fraction:
    numerator = 0
    denominator = 1

    def get_numerator(numerator):
        return numerator

    def get_denominator(denominator):
        return denominator

    def print_fraction(numerator, denominator):
        print(numerator+"/"+denominator)

    def print_type(numerator, denominator):
        if numerator <= denominator:
            print("Proper Fraction")

        else:
            print("Improper Fraction")

    def set_numerator(new_numerator):
        numerator = new_numerator

    def set_denominator(new_denominator):
        denominator = new_denominator

    def inverse(numerator, denominator):
        numer1 = numerator
        deno1 = denominator
        if numeraror == 0:
            print("The numerator is 0")

        elif numerator != denominator:
            numerator = deno1
            denominator = numer1


fraction1 = Fraction()

fraction1.print_fraction()

fractoin2 = Fraction()

fraction2.set_numerator(2)

fraction2.set_denominator(6)
