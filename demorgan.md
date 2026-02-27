NOT (A OR B) <=> NOT-A AND NOT-B

					*							*
A	B	AorB	not(AorB)	not(A)	not(B)	not(A)andnot(B)
T	T	T		F			F		F		F
T	F	T		F			F		T		F
F	T	T		F			T		F		F
F	F	F		T			T		T		T


if numero >=1:
	stampa la tabellina
else:
	stampa errore

if not numero >=1:
	stampa errore
else:
	stampa la tabellina