SET SESSION group_concat_max_len = 5000;

SELECT
	agrup.ds_agrupamento,

	rel.nm_relatorio,-- 	arquivos da rgo_relatorios à serem criados :
	rel.me_relatorio_config,
	rel.me_relatorio_view,
	rel.me_relatorio_index,
	rel.ds_filtro,-- 	inser do relatorio sem os campos acima:
	rel.cd_relatorio,
	(
		SELECT 
		 GROUP_CONCAT( distinct "INSERT IGNORE INTO rgo_opcoes_tipos (
								cd_opcao_tipo,
								ds_opcao_tipo,
								ds_tag_opcao,
								dt_base
						)
				VALUES (
								NULL,",
								IF(opct.ds_opcao_tipo IS NOT NULL, CONCAT('"',opct.ds_opcao_tipo, '"' ), 'NULL'),
								',',
								IF(opct.ds_tag_opcao IS NOT NULL,  CONCAT('"',opct.ds_tag_opcao, '"'), 'NULL'),
								',',
								IF(opct.dt_base IS NOT NULL, CONCAT('"', opct.dt_base, '"'), 'NULL'), ')'
						SEPARATOR '; \n')
		FROM rgo_opcoes opc
		INNER JOIN rgo_opcoes_tipos opct ON (opc.cd_opcao_tipo = opct.cd_opcao_tipo)
		WHERE opc.cd_relatorio = rel.cd_relatorio

	) as opcao_tipo_impressao,
	
	
	
	CONCAT(
		"INSERT IGNORE INTO rgo_relatorios (
		cd_relatorio,
		cd_tipo,
		cd_agrupamento,
		sn_ativo,
		nm_relatorio,
		sn_padrao,
		ds_filtro,
		nm_arquivo,
		me_relatorio_index,
		me_relatorio_config,
		me_relatorio_view,
		cd_relatorio_template,
		cd_formato,
		me_documentacao_padrao,
		me_documentacao_cliente,
		ds_chave,
		dt_base,
		sn_autentique,
		ds_autentique_config
    )
		VALUES (
		NULL,
		",
		IFNULL( rel.cd_tipo, ' NULL' ),
		',',
		IFNULL( rel.cd_agrupamento, ' NULL' ),
		',',
		IFNULL( rel.sn_ativo, ' NULL' ),
		',',
		IF( rel.nm_relatorio IS NOT NULL, CONCAT( '"', rel.nm_relatorio , '"'), ' NULL' ),
		',',
		IFNULL( rel.sn_padrao, ' NULL' ),
		',',
		"
		NULL,
		NULL,
		NULL,
		NULL,
		NULL,
		",
		IFNULL( rel.cd_relatorio_template, ' NULL' ),
		',',
		IFNULL( rel.cd_formato, ' NULL' ),
		',',
		IF( rel.me_documentacao_padrao IS NOT NULL, CONCAT('"' , rel.me_documentacao_padrao ,'"' ) ,' NULL' ),
		',',
		IF( rel.me_documentacao_cliente IS NOT NULL, CONCAT('"', rel.me_documentacao_cliente, '"'), ' NULL' ),
		',',
		IF( rel.ds_chave IS NOT NULL, CONCAT('"', rel.ds_chave, '"'), ' NULL' ),
		',',
		IF( rel.dt_base IS NOT NULL, CONCAT('"', rel.dt_base, '"') ,' NULL' ),
		',',
		IFNULL( rel.sn_autentique, ' NULL' ),
		',',
		IF( rel.ds_autentique_config IS NOT NULL, CONCAT('"', rel.ds_autentique_config, '"') , ' NULL' ), ')' -- 				FALTA TRATAR CASO UM DOS CAMPOS FOR NULO
		

	) AS insert_statement,
	(
	
	SELECT GROUP_CONCAT(
"INSERT IGNORE INTO rgo_opcoes (cd_opcao, cd_relatorio,cd_opcao_tipo,sn_padrao,sn_ativo,ds_opcao,me_configuracao,ds_chave,dt_base)
VALUES (NULL,NULL,NULL,",IFNULL( opc.sn_padrao, 'NULL' ),',',IFNULL( opc.sn_ativo, 'NULL' ),',',IF( opc.ds_opcao IS NOT NULL, CONCAT('"', opc.ds_opcao, '"'), 'NULL' ),',',IF( opc.me_configuracao IS NOT NULL, CONCAT('"', opc.me_configuracao, '"') ,'NULL' ),',',IF( opc.ds_chave IS NOT NULL, CONCAT('"', opc.ds_chave ,'"') ,'NULL' ),',',IF( opc.dt_base IS NOT NULL, CONCAT('"' , dt_base , '"'), 'NULL' ),'\n )' SEPARATOR '; \n' 	)	
FROM rgo_opcoes opc 	WHERE		opc.cd_relatorio = rel.cd_relatorio 	) AS opcoes_impressao,

	IF( rel.cd_tipo = 2, 
		(SELECT opc.me_configuracao FROM rgo_opcoes opc WHERE rel.cd_relatorio = opc.cd_relatorio ), NULL
	) AS me_config

FROM
	rgo_relatorios rel
	INNER JOIN rgo_agrupamentos agrup ON ( agrup.cd_agrupamento = rel.cd_agrupamento ) 
	
WHERE
	me_relatorio_index IS NOT NULL 
	AND me_relatorio_index != '' 
	AND sn_ativo = 1 
	AND (rel.nm_arquivo IS NULL OR rel.nm_arquivo != '')