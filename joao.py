import sqlite3

conexao = sqlite3.connect("cadastroAluno.db")
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE `aluno` (
        `matricula` varchar(8) NOT NULL,
        `nome` varchar(120) NOT NULL,
        `curso` varchar(60) NOT NULL,
        `turma` varchar(6) NOT NULL,
        `np1` float DEFAULT NULL,
        `np2` float DEFAULT NULL,
        `ms` float DEFAULT NULL,
        `ex` float DEFAULT NULL,
        `mf` float DEFAULT NULL,
        `situacao` varchar(10) DEFAULT NULL,
        `md` float DEFAULT NULL)
        ''')
cursor.execute('''
            INSERT INTO 'aluno' ('matricula', 'nome', 'curso', 'turma', 'np1', 'np2', 'ms', 'ex', 'mf','situacao','md') VALUES
('G0826C-7', 'BARTOLOMEU DIAS', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G0881C-7', 'DAMASCENO ARAUJO', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G08405-0', 'WELLINGTON PRACIANO', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G07HDC-6', 'ALVES FORTE', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G0748E-9', 'PINHEIRO DE MORAIS', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G707DG-9', 'FEITOSA CUNHA', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G89BHC-2', 'HENRIQUE SEVERINO', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G00JGH-7', 'RICARDO DIAS', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N0212J-1', 'PARENTE NETO', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G091CB-3', 'BATISTA NASCIMENTO', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G01152-8', 'REIS SANTOS', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G71047-3', 'MATEUS PENHA', 'Análise e desenvolvimento de sistemas', 'DS4P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N81928-0', 'JOSE JUNIOR', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G51549-0', 'CERQUEIRA DE ANDRADE', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N7120E-0', 'SANTOS SOUZA', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G4144E-3', 'FELICIANO SILVA', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N91224-0', 'DIAS MARTINS', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N31257-0', 'FELIPE CAVALCANTI', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G41ACA-0', 'SILVEIRA NEVES', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N8102H-0', 'VIEIRA DE ARAUJO', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G4106C-9', 'ESTRELA DE ALBUQUERQUE', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N7386D-0', 'RESENDE SANTIAGO', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N91184-3', 'FARKAS DA SILVA', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N78183-0', 'FERREIRA DE CASTRO', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G511EB-2', 'RIBEIRO DORNELAS', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('F34186-2', 'SOUZA ROCHA', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N80185-7', 'SANTOS LOPES', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G50183-0', 'SOUSA DA SILVA', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G451DB-9', 'GOMES DE OLIVEIRA', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL , NULL, NULL),
('G49185-6', 'MATOS FIGUEIREDO', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G6217F-0', 'BEZERRA DA SILVA', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N56176-5', 'SOUZA TAVARES', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N7016H-4', 'RODRIGUES CARDOSO', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G481AE-0', 'RAMOS RIBEIRO', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N75141-1', 'ANDRADE DO NASCIMENTO', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N81105-4', 'OLIVEIRA SOARES', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G4419E-5', 'GONCALVES FARIAS', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N92126-0', 'MEDEIROS DE MORAIS', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G51HFF-2', 'MALTA GOMES', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G4144C-0', 'COIMBRA LOPES', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('G6157D-4', 'FERNANDES DE ARAÚJO', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('F3167G-9', 'GABRIEL FERREIRA', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N81398-2', 'HENRIQUE DOS SANTOS', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('F31962-4', 'OLIVEIRA VIEIRA', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('F31422-3', 'OLIVEIRA MARTINS', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('N71892-0', 'PEREIRA DA SILVA', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('F31475-4', 'OLIVEIRA DE ANDRADE', 'Análise e desenvolvimento de sistemas', 'DS3P30', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
''')
conexao.commit()
cursor.close()
conexao.close()