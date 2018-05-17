from Ch07Q05_class import RegularPolygon

def main():
    pol1 =  RegularPolygon()
    pol2 =  RegularPolygon(6, 4)
    pol3 =  RegularPolygon(10, 4, 5.6, 7.8)
    
    pol1.getPrint()
    pol2.getPrint()
    pol3.getPrint()

main()