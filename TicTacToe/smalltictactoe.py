f=lambda b=0,c=0,l='8ITđĤǀ',g=format,k=input,h=int:exit()if print("\n".join([(x:=str(h(str(g(b,'b')))+2*h(str(g(c,'b')))).zfill(9)[::-1])[:3],x[3:6],x[6:]]))or b|c==511or any(chr(c&ord(x)) in l for x in l)else f(c,b+(x:=lambda:(2**(y+q) if ((b|c)>>(y:=3*h(k()))+(q:=h(k())))%2==0and 0<=y<9and 0<=q<3else x()))())

f()
