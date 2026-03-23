
| ETA | ETA DA RAGGIUNGERE | Cosa fare?                                                         |
| --- | ------------------ | ------------------------------------------------------------------ |
| <0  | <=0                | print("Impossibile")                                               |
| <0  | >0                 | print("Non puoi avere età negativa!")                              |
| >=0 | <=0                 | print("Non sei Benjamin Button")                                   |
| >=0 | >0                 | stampa_messaggio_giusto() |


[INT]  < [INT] ----> BOOL
[STR]  < [STR] ----> BOOL

[BOOL] [OPERATORE] [BOOL] ----> [BOOL]

and

| Bool1 | Bool2 | [BOOL1] and [BOOL2] | esempio                        |
| ----- | ----- | ------------------- | ------------------------------ |
| True  | True  | True                | (3<5) and ("a"<"b") ---> True  |
| True  | False | False               | (3<5) and ("a">"b") ---> False |
| False | True  | False               | (3>5) and ("a"<"b") ---> False |
| False | False | False               | (3>5) and ("a">"b") ---> False |

or

| Bool1 | Bool2 | [BOOL1] or [BOOL2] | esempio                        |
| ----- | ----- | ------------------ | ------------------------------ |
| True  | True  | True               | (3<5) or ("a"<"b") ---> True   |
| True  | False | True               | (3<5) or ("a">"b") ---> True   |
| False | True  | True               | (3>5) or ("a"<"b") ---> True   |
| False | False | False              | (3>5) and ("a">"b") ---> False |

not

| Bool1 | not [BOOL1] | esempio               |
| ----- | ----------- | --------------------- |
| True  | False       | not (3<5)  ---> False |
| False | True        | not (3>5)  ---> True  |


<!--

# IF [ESPRESSIONE BOOLEANA]:
#	istruzione-1
#	istruzione-2
#	istruzione-3
# ELIF [ESPRESSIONE BOOLEANA]:
#	fai quello
# ELIF C:
#	fai altro
#...
# ELSE:
# 	vai al mare

-->
