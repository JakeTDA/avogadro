import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture

# Entry point
def main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    pic = Picture(sys.argv[4])
    frame = BlobFinder(pic,tau)
    prevBeads = frame.getBeads(pixels)
    # Starting from sys.argv[5], finds the distances between beads of previous iteration and currnet iteation,
    # and takes the least distances of the beads.
    for i in range(5,len(sys.argv)):
        beads = BlobFinder(Picture(sys.argv[i]),tau)
        currBeads = beads.getBeads(pixels)
        for currBead in currBeads:
            closestBeadDistance = 0.0
            distance = math.inf
            for prevBead in prevBeads:
                prevBeadDistance = prevBead.distanceTo(currBead)
                if prevBeadDistance <= delta and prevBeadDistance <= distance:
                    distance = prevBeadDistance
                    closestBeadDistance = prevBeadDistance
            if closestBeadDistance != math.inf and closestBeadDistance != 0:
                stdio.writef('%.4f\n',closestBeadDistance)
        prevBeads = currBeads
        stdio.writeln()



if __name__ == "__main__":
    main()
