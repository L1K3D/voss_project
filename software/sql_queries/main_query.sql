USE b_voss_br_instrucoes_embalagem_mbb;

-------------------

DROP TABLE mntg_lnh_mercedes_benz

CREATE TABLE mntg_lnh_mercedes_benz (

	NR_ITEM INT IDENTITY(1,1) PRIMARY KEY
	,CD_CLIE VARCHAR(50)
	,CD_VOSS VARCHAR(50)
	,QT_SAC_PLAST INT
	,TP_EMBL_INT_CD_MICR_SIG VARCHAR(300)
	,QT_CAIXA INT
	,TP_CAIXA_CD_MICR_SIG VARCHAR(300)
	,MD_ETQ_SAC_PLAST VARCHAR(300)
	,MD_ETQ_CAIXA VARCHAR(300)
	,DT_ELB DATE
	,DT_REV DATE
	,CD_IE VARCHAR(30)
	,DT_CRGA DATE

);

-------------------

DROP TABLE usua_cadr

CREATE TABLE usua_cadr (

	NR_USUA INT IDENTITY(1,1) PRIMARY KEY
	,LOGIN_USUA VARCHAR(30)
	,SENHA_USUA VARCHAR(30)
	,DT_CADR DATE

);

-------------------

CREATE TABLE log_alteracoes (

    NR_ALT INT IDENTITY(1,1) PRIMARY KEY,  -- Número da alteração de maneira ordenada
    NR_USUA INT NOT NULL,                  -- Número do usuário que realizou a alteração
    DT_ALTR DATETIME NOT NULL,             -- Data da alteração
    NM_TABL_ALTR NVARCHAR(128) NOT NULL,   -- Nome da tabela que sofreu a alteração
    TP_OPER NVARCHAR(10) NOT NULL,         -- Tipo da operação (INSERT, DELETE, etc.)
    QT_LNH_ALTR INT NOT NULL               -- Número de linhas que foram alteradas

);

-------------------

CREATE TRIGGER trg_after_insert_usua_cadr
ON usua_cadr
AFTER INSERT
AS
BEGIN
    DECLARE @NumLinhas INT
    SET @NumLinhas = (SELECT COUNT(*) FROM inserted)
    
    INSERT INTO log_alteracoes (NR_USUA, DT_ALTR, NM_TABL_ALTR, TP_OPER, QT_LNH_ALTR)
    VALUES (SUSER_SID(), GETDATE(), 'usua_cadr', 'INSERT', @NumLinhas)
END;

-------------------

CREATE TRIGGER trg_after_delete_usua_cadr
ON usua_cadr
AFTER DELETE
AS
BEGIN
    DECLARE @NumLinhas INT
    SET @NumLinhas = (SELECT COUNT(*) FROM deleted)
    
    INSERT INTO log_alteracoes (NR_USUA, DT_ALTR, NM_TABL_ALTR, TP_OPER, QT_LNH_ALTR)
    VALUES (SUSER_SID(), GETDATE(), 'usua_cadr', 'DELETE', @NumLinhas)
END;

-------------------

CREATE TRIGGER trg_after_insert_mntg_lnh_mercedes_benz
ON mntg_lnh_mercedes_benz
AFTER INSERT
AS
BEGIN
    DECLARE @NumLinhas INT
    SET @NumLinhas = (SELECT COUNT(*) FROM inserted)
    
    INSERT INTO log_alteracoes (NR_USUA, DT_ALTR, NM_TABL_ALTR, TP_OPER, QT_LNH_ALTR)
    VALUES (SUSER_SID(), GETDATE(), 'mntg_lnh_mercedes_benz', 'INSERT', @NumLinhas)
END;

-------------------

CREATE TRIGGER trg_after_delete_mntg_lnh_mercedes_benz
ON mntg_lnh_mercedes_benz
AFTER DELETE
AS
BEGIN
    DECLARE @NumLinhas INT
    SET @NumLinhas = (SELECT COUNT(*) FROM deleted)
    
    INSERT INTO log_alteracoes (NR_USUA, DT_ALTR, NM_TABL_ALTR, TP_OPER, QT_LNH_ALTR)
    VALUES (SUSER_SID(), GETDATE(), 'mntg_lnh_mercedes_benz', 'DELETE', @NumLinhas)
END;