"""
3.f-strings(String Interpolation)
*f-strings Python 3 ile geldi(yeni)
*f'...string... seklinde string in basina f harfi konur
*str.format()gibi calisir ama daha dinamiktir
*{}süslü parantez ile kullanilir
"""
x=2
y=3
carpim=x*y
print(f"{x}*{y}={carpim}")
#direk {} icinden de islem yapilabilir
print(f"{x}*{y}={x*y}")

veri=["Klar Kent","Metropolis","Daily Planet"]
print(f"{veri[0]},yani Superman,kurgusal {veri[1]} sehrinde,{veri[2]} gazetesinde calisir")

