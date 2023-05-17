"""
    Hora : 18:35
    
"""
def whole2half(hour: str):
    hour = [int(x) for x in hour.split(":")]
    if(hour[0] > 11):
        hour[0] -= 12
    return hour
def app(hour: str):
    reloj = whole2half(hour)
    # ":".join([str(x) for x in reloj])
    punto1 = (reloj[0]/12)*360
    punto2 = (reloj[1]/60)*360
    angulo = abs(punto1-punto2)
    print(f"Será un ángulo de {min(360-angulo,angulo)}°")
def main():
    hour = input("¿Qué hora buscas? ")
    if(hour.count(":") == 1):
        for x in hour.split(":"):
            if not (x.isnumeric() and len(x) == 2):
                raise TypeError
        return app(hour)
                
    raise TypeError
if __name__ == '__main__':
    main()