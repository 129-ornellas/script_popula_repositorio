SELECT
	agrup.ds_agrupamento,
	rel.nm_relatorio,
	rel.me_relatorio_config,
	rel.me_relatorio_view
	
FROM
	rgo_relatorios rel
INNER JOIN rgo_agrupamentos agrup
	on (agrup.cd_agrupamento = rel.cd_agrupamento)
WHERE
	me_relatorio_index IS NOT NULL and me_relatorio_index != ''