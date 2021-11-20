#



def echofilter(input, output, delay, atten):
    entrada=input
    saida=output
    
    print(entrada + saida * delay + atten)
