from CursoPythonPOO.classe_abstrata.classes.conta_poupanca import ContaPoupanca
from CursoPythonPOO.classe_abstrata.classes.conta_corrente import ContaCorrente


cp = ContaPoupanca(1160, 1234, 0)
cp.depositar(100)
cp.sacar(50)
cp.sacar(50)
cp.sacar(1)

print('------------------------------------------------------------')

cc = ContaCorrente(1150, 4321, 0, 5000)
cc.depositar(1000)
cc.sacar(2500)
cc.sacar(5000)
cc.depositar(10000)
