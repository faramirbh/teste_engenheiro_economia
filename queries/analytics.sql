-- ============================================
-- CONSULTAS ANALÍTICAS SOBRE NOTAS FISCAIS
-- ============================================

-- 1. CONTAGEM TOTAL DE NOTAS FISCAIS
SELECT 
    COUNT(*) as total_nfes
FROM nfe_events;

-- 2. VALOR TOTAL DE TODAS AS NOTAS FISCAIS
SELECT 
    SUM(valor_total) as valor_total_nfes,
    COUNT(*) as quantidade_nfes,
    AVG(valor_total) as valor_medio_nfe,
    MIN(valor_total) as valor_minimo,
    MAX(valor_total) as valor_maximo
FROM nfe_events;

-- 3. ANÁLISE POR EMITENTE (TOP 10)
SELECT 
    emitente_nome,
    emitente_cnpj,
    COUNT(*) as quantidade_nfes,
    SUM(valor_total) as valor_total_emitente,
    AVG(valor_total) as valor_medio_emitente
FROM nfe_events
GROUP BY emitente_nome, emitente_cnpj
ORDER BY valor_total_emitente DESC
LIMIT 10;

-- 4. ANÁLISE POR DATA DE EMISSÃO
SELECT 
    DATE(data_emissao) as data_emissao,
    COUNT(*) as quantidade_nfes,
    SUM(valor_total) as valor_total_dia,
    AVG(valor_total) as valor_medio_dia
FROM nfe_events
GROUP BY DATE(data_emissao)
ORDER BY data_emissao DESC;

-- 5. ANÁLISE POR DESTINATÁRIO (TOP 10)
SELECT 
    destinatario_nome,
    COUNT(*) as quantidade_nfes_recebidas,
    SUM(valor_total) as valor_total_recebido,
    AVG(valor_total) as valor_medio_recebido
FROM nfe_events
WHERE destinatario_nome IS NOT NULL
GROUP BY destinatario_nome
ORDER BY valor_total_recebido DESC
LIMIT 10;

-- 6. DISTRIBUIÇÃO DE VALOR POR RANGE
SELECT 
    CASE 
        WHEN valor_total < 50 THEN 'Até R$ 50'
        WHEN valor_total >= 50 AND valor_total < 100 THEN 'R$ 50 a R$ 100'
        WHEN valor_total >= 100 AND valor_total < 500 THEN 'R$ 100 a R$ 500'
        WHEN valor_total >= 500 AND valor_total < 1000 THEN 'R$ 500 a R$ 1.000'
        ELSE 'Acima de R$ 1.000'
    END as range_valor,
    COUNT(*) as quantidade_nfes,
    SUM(valor_total) as valor_total,
    AVG(valor_total) as valor_medio
FROM nfe_events
GROUP BY 
    CASE 
        WHEN valor_total < 50 THEN 'Até R$ 50'
        WHEN valor_total >= 50 AND valor_total < 100 THEN 'R$ 50 a R$ 100'
        WHEN valor_total >= 100 AND valor_total < 500 THEN 'R$ 100 a R$ 500'
        WHEN valor_total >= 500 AND valor_total < 1000 THEN 'R$ 500 a R$ 1.000'
        ELSE 'Acima de R$ 1.000'
    END
ORDER BY valor_total DESC;

-- 7. RESUMO EXECUTIVO
SELECT 
    'Total de NFes' as metrica,
    CAST(COUNT(*) as STRING) as valor
FROM nfe_events
UNION ALL
SELECT 
    'Valor Total (R$)',
    CAST(SUM(valor_total) as STRING)
FROM nfe_events
UNION ALL
SELECT 
    'Valor Médio (R$)',
    CAST(AVG(valor_total) as STRING)
FROM nfe_events
UNION ALL
SELECT 
    'Total de Emitentes',
    CAST(COUNT(DISTINCT emitente_cnpj) as STRING)
FROM nfe_events
UNION ALL
SELECT 
    'Total de Destinatários',
    CAST(COUNT(DISTINCT destinatario_nome) as STRING)
FROM nfe_events;
