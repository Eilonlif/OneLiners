f=lambda b=0,c=0,l='8ITđĤǀ',g=format,k=input,h=int:exit if print((x:=str(h(str(g(b,'b')))+2*h(str(g(c,'b')))).zfill(9)[::-1])[:3],x[3:6],x[6:],sep='\n')or b|c==511or any(chr(c&ord(x))in l for x in l)else f(c,b+(x:=lambda:(2**(y+q)if 9>(y:=3*h(k()))>=((b|c)>>y+(q:=h(k())))%2==0<=q<3else x()))())

f()
