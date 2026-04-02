from kafka import KafkaProducer
import json
import os
from xml.etree import ElementTree as ET

# Configurar Kafka Producer
kafka_brokers = "kafka:29092"
producer = KafkaProducer(
    bootstrap_servers=kafka_brokers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Função para extrair dados do XML
def extract_nfe_data(xml_file):
    """
    Extrai dados principais de uma NF-e em XML
    """
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Remove namespaces
        for elem in root.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]
        
        nfe_data = {}
        
        # Identificação
        ide = root.find('.//ide')
        if ide is not None:
            nfe_data['data_emissao'] = ide.findtext('dhEmi', '')
            nfe_data['numero_nf'] = ide.findtext('nNF', '')
        
        # Emitente
        emit = root.find('.//emit')
        if emit is not None:
            nfe_data['emitente_nome'] = emit.findtext('xNome', '')
            nfe_data['emitente_cnpj'] = emit.findtext('CNPJ', '')
        
        # Destinatário
        dest = root.find('.//dest')
        if dest is not None:
            nfe_data['destinatario_nome'] = dest.findtext('xNome', '')
        
        # Totais
        total = root.find('.//total')
        if total is not None:
            icms_tot = total.find('ICMSTot')
            if icms_tot is not None:
                nfe_data['valor_total'] = float(icms_tot.findtext('vNF', '0'))
        
        return nfe_data
    
    except Exception as e:
        print(f"Erro ao processar {xml_file}: {str(e)}")
        return None

# Caminho dos XMLs
xml_folder = "/xmls"

# Processar todos os XMLs
if os.path.exists(xml_folder):
    xml_files = [f for f in os.listdir(xml_folder) if f.endswith('.xml')]
    print(f"Encontrados {len(xml_files)} arquivos XML")
    
    for xml_file in sorted(xml_files):
        xml_path = os.path.join(xml_folder, xml_file)
        
        # Extrai dados
        nfe_data = extract_nfe_data(xml_path)
        
        if nfe_data:
            # Envia para Kafka
            producer.send(
                topic='nfe-events',
                value=nfe_data
            )
            print(f"✓ {xml_file} enviado para Kafka")
    
    producer.flush()
    producer.close()
    print(f"\n✅ Processamento concluído! {len(xml_files)} NFes enviadas para Kafka")
else:
    print(f"❌ Pasta {xml_folder} não encontrada!")