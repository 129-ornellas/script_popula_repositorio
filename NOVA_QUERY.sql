SELECT
	agrup.ds_agrupamento,
	rel.nm_arquivo,
	rel.nm_relatorio,-- 	arquivos da rgo_relatorios à serem criados :
	rel.me_relatorio_config,
	rel.me_relatorio_view,
	rel.me_relatorio_index,
	rel.ds_filtro,-- 	inser do relatorio sem os campos acima:
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
        ",IFNULL(rel.cd_tipo, ' NULL') ,','
        ,IFNULL(rel.cd_agrupamento, ' NULL'),','
        ,IFNULL(rel.sn_ativo, ' NULL'),','
        ,IFNULL(rel.nm_relatorio, ' NULL'),','
        ,IFNULL(rel.sn_padrao, ' NULL'),',',"
				 NULL,
				 NULL,
				 NULL,
				 NULL,
				 NULL,
				"
				, IFNULL(rel.cd_relatorio_template, ' NULL'),','
        , IFNULL(rel.cd_formato, ' NULL'), ','
        , IFNULL(rel.me_documentacao_padrao, ' NULL'), ','
        , IFNULL(rel.me_documentacao_cliente, ' NULL'),','
        , IFNULL(rel.ds_chave, ' NULL'),','
        , IFNULL(rel.dt_base, ' NULL'), ','
        , IFNULL(rel.sn_autentique, ' NULL'),','
        , IFNULL(rel.ds_autentique_config, ' NULL')
				
-- 				FALTA TRATAR CASO UM DOS CAMPOS FOR NULO
        
	) AS insert_statement 
FROM
	rgo_relatorios rel
	INNER JOIN rgo_agrupamentos agrup ON ( agrup.cd_agrupamento = rel.cd_agrupamento ) 
WHERE
	me_relatorio_index IS NOT NULL 
	AND me_relatorio_index != '' 
	AND sn_ativo = 1 
	LIMIT 2