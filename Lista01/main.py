import tkinter as tk, re




#Exercício 1
def regraDeNegocioContratacao(idade):
    if 0  <= idade <= 15:
        print("Não empregar")
    if 16 <= idade <= 17:
        print("Pode ser empregado tempo parcial")
    if 18 <= idade <= 54:
        print("Pode ser empregado tempo integral")
    if 55 <= idade <= 99:
        print("Não empregar")
regraDeNegocioContratacao(int(input("Digite uma idade: ")))



#Exercício 2
def verificarSeSenhaForte(senha):
    if len(senha) >= 8:
        print("OK oito caracteres ")
    if any(i.isupper() for i in senha):
        print("OK possui maiuscula")
    if any(i.islower() for i in senha):
        print("OK possui minuscula")
    if any(i.isdigit() for i in senha):
        print("OK possui um numero")
    if any(i in "@#$%" for i in senha):
        print("OK possui especial ")
verificarSeSenhaForte(input("Digite uma senha: "))



#Exercício 3
def verificarSeSenhaForteNovo(senha):
    if 6 <= len(senha) <= 10:
        print("OK caracteres 6 a 10")
    if senha[0].isalpha() or senha[0].isdigit() or senha[0] == "?":
        print("OK primeiro caracter alfabetico, digito ou ?")
    if senha.isalpha():
        print("OK sem caracter de controle")
    if senha not in {"admin123", "123", "senha"}:
        print("OK senha não é proíbida")
verificarSeSenhaForteNovo(input("Digite uma senha: "))


#Exercício 4
def criarInterfaceGraficaBanco():
    def validar():
        a,p,s,sen,o = e1.get(),e2.get(),e3.get(),e4.get(),e5.get()
        ok = (a=="" or re.fullmatch(r"0\d{2}",a)) and \
             re.fullmatch(r"[1-9]\d{2}",p) and \
             re.fullmatch(r"\d{4}",s) and \
             re.fullmatch(r"[A-Za-z0-9]{6}",sen) and \
             o in "cde"
        r.config(text="✔ Válido" if ok else "✖ Inválido", fg="green" if ok else "red")

    j=tk.Tk(); j.title("Banco")
    for i,t in enumerate(["Cód. Área","Prefixo","Sufixo","Senha","Operação"]):
        tk.Label(j,text=t).grid(row=i,column=0,padx=5,pady=5)

    e1,e2,e3,e4,e5=[tk.Entry(j) for _ in range(5)]
    for i,e in enumerate([e1,e2,e3,e4,e5]): e.grid(row=i,column=1,padx=5)

    tk.Button(j,text="Validar",command=validar).grid(row=5,column=0,columnspan=2,pady=8)
    r=tk.Label(j,font=("Arial",10,"bold")); r.grid(row=6,column=0,columnspan=2)

    j.mainloop()
criarInterfaceGraficaBanco()