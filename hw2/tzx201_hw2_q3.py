"""
tzx201_hw1_q3
"""

def factors(num):
    if num == 0:
        yield 0
    #factors less than sqrt
    for i in range(1,int(num**0.5)):
        if num%i == 0:
            yield i
    #other factors 
    for i in range(int(num**0.5),0,-1):
        if num%i == 0:
            yield num//i
        
    
    
def main():
    for fac in factors(23):
        print(fac, end = " ")
        
main()
