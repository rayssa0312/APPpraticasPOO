#Curso: Informática
#Ano: 2ª A
#Disciplina: Programação Orientada a Objetos
#Alunos:
#Álvaro Brígido
#Jhenifer dos Santos
#Isac de Jesus Holanda
#Samantha Beatriz
#Rayssa de Castro

import datetime


class Pessoa:
    def __init__(self, id_pessoa, nome, cpf, telefone):
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

class Credencial:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

class LocalizacaoGPS:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.dataHoraLeitura = datetime.datetime.now()
    def capturarCoordenadas(self):
        hora = self.dataHoraLeitura.strftime("%H:%M:%S")
        return f"Lat: {self.latitude}, Lon: {self.longitude} (às {hora})"


class ProfissionalSuporte(Pessoa):
    def __init__(self, id_pessoa, nome, cpf, telefone, registro_profissional, especialidade):
        super().__init__(id_pessoa, nome, cpf, telefone)
        self.registro_profissional = registro_profissional
        self.especialidade = especialidade

    def receberSolicitacao(self, motivo):
        print(f"[REDE DE APOIO] O(a) profissional {self.nome} ({self.especialidade}) recebeu o seu pedido.")
        print(f"   -> Motivo registrado: {motivo}")

class Autoridade: 
    def __init__(self, id_autoridade, nome_orgao):
        
        self.id_autoridade = id_autoridade
        self.nome_orgao = nome_orgao

    def despacharViatura(self):
        print(f"   -> [RADIO {self.nome_orgao}] Viatura a caminho do local!")

class MedidaProtetiva:
    def __init__(self, numero, validade, ativa):
        self.numero = numero
        self.validade = validade
        self.ativa = ativa

    def verificar_validade(self):
        if self.ativa:
            print("[MEDIDA] Medida protetiva válida.")
        else:
            print("[MEDIDA] Medida protetiva inválida.")

    def anexar_documento(self):
        print("[MEDIDA] Documento anexado com sucesso.")

class SolicitacaoApoio:
    def __init__(self, motivo):
        self.motivo = motivo
        self.status = "Pendente"

    def criar_solicitacao(self):
        self.status = "Aberta"
        print("[SOLICITAÇÃO] Solicitação criada.")

    def cancelar_solicitacao(self):
        self.status = "Cancelada"
        print("[SOLICITAÇÃO] Solicitação cancelada.")

class Alerta:
    def __init__(self, latitude, longitude):
        self.localizacao = LocalizacaoGPS(latitude, longitude)
    def acionarAutoridade(self, autoridade):
        local = self.localizacao.capturarCoordenadas()
        print(f"[SISTEMA] Notificando {autoridade.nome_orgao} para o local: {local}")
        autoridade.despacharViatura()

class Guardiao(Pessoa):
    def __init__(self, id_pessoa, nome, cpf, telefone, vinculo):
        super().__init__(id_pessoa, nome, cpf, telefone)
        self.vinculo = vinculo
    def alertarGuardiao(self):
        print(f"   -> [SMS Enviado] Para {self.nome} ({self.vinculo}): A usuária acionou o pânico!")

class Usuario(Pessoa):
    def __init__(self, id_pessoa, nome, cpf, telefone, endereco, email, senha):
        super().__init__(id_pessoa, nome, cpf, telefone)
        self.endereco = endereco
        self.credencial = Credencial(email, senha)
        self.guardioes = []
        self.medidas = []
    
    def gerenciarGuardiao(self, guardiao):
        self.guardioes.append(guardiao)
        print(f"\n[APP] Guardião {guardiao.nome} adicionado com sucesso!")

    def acionarBotaoPanico(self, autoridade_local):
        print(f"\n{'='*50}\n[ALERTA MÁXIMO] BOTÃO DE PÂNICO ACIONADO POR {self.nome.upper()}!\n{'='*50}")
        novo_alerta = Alerta(-8.7611, -63.9004)
        novo_alerta.acionarAutoridade(autoridade_local)
        for guardiao in self.guardioes:
            guardiao.alertarGuardiao()
        print(f"{'='*50}\n")


if __name__ == "__main__":
    deam = Autoridade(1, "DEAM - Polícia Civil")
    psicologa = ProfissionalSuporte(201, "Dra. Ana", "000.000.000-00", "3333-3333", "CRP-99", "Psicóloga")
    
    print("=== BEM-VINDA AO SOS MARIA DA PENHA ===")
    nome_usuaria = input("Digite seu nome: ")
    tel_usuaria = input("Digite seu telefone: ")
    
    vitima = Usuario(101, nome_usuaria, "000.000.000-00", tel_usuaria, "Centro", "email@teste.com", "123")
    print(f"\nConta criada com sucesso, {vitima.nome}!")

    while True:
        print("\n--- TELA INICIAL ---")
        print("1. Adicionar um Guardião")
        print("2. Solicitar Apoio Psicológico/Jurídico")
        print("3. Verificar Medida Protetiva")
        print("4. ACIONAR BOTÃO DE PÂNICO")
        print("0. Fechar Aplicativo")
        
        opcao = input("Escolha uma opção (0 a 4): ")

        if opcao == "1":
            print("\n-- Cadastro de Guardião --")
            nome_g = input("Nome do guardião: ")
            vinc_g = input("Qual o vínculo (ex: Irmão, Amiga): ")
            tel_g = input("Telefone do guardião: ")
            novo_guardiao = Guardiao(len(vitima.guardioes)+1, nome_g, "000", tel_g, vinc_g)
            vitima.gerenciarGuardiao(novo_guardiao)
            
        elif opcao == "2":
            print("\n-- Rede de Apoio --")
            motivo = input("Descreva o motivo do pedido de apoio: ")
            psicologa.receberSolicitacao(motivo)
            
        elif opcao == "3":
            print("\n-- Consulta de Medida Protetiva --")
            num_m = input("Número da medida protetiva: ")
            medida = MedidaProtetiva(num_m, "2027-12-31", True)
            medida.verificar_validade()
            medida.anexar_documento()
            
        elif opcao == "4":
            vitima.acionarBotaoPanico(deam)
            
        elif opcao == "0":
            print("Fechando aplicativo. Fique segura!")
            break
            
        else:
            print("Opção inválida, tente novamente.")

#Álvaro Brígido
#Jhenifer dos Santos
#Isac de Jesus Holanda
#Samantha Beatriz
#Rayssa de Castro