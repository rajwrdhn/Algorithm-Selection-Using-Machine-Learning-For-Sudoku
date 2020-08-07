#!usr/var/python3
from subprocess import call

for i in range(7,10):
    for j in range(0,105,5):
        for k in range(1,21):
            call(["./a.out",  "n%dexample.txt" %i,  "benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), "%f" %(j/100), "%d" %k])
