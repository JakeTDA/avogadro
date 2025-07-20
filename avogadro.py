import math
import stdio

# Entry point.
def main():
    ETA = 9.135e-4
    RHO = 0.5e-6
    T = 297.0
    R = 8.31457
    var = 0.0
    displacements = stdio.readAllFloats()
    n = len(displacements)
    # Using the results of distances/displacements gotten from bead_tracker.py, puts it in the equation
    # to calculate the variance. The pixels are also converted into meters before being put into the equation,
    # as the equation uses meters as its units.
    for i in range(0,n):
        var += (displacements[i] * 0.175 * (10**-6))**2
    var = var/(2*n)
    k = 6 * math.pi * var * ETA * RHO / T
    avogadro = R/k
    stdio.writef('%e',avogadro)
if __name__ == "__main__":
    main()
