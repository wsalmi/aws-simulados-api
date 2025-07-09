#!/usr/bin/env python3
"""
Script para gerar questões abrangentes para todas as certificações AWS
Baseado nos formatos reais das provas e domínios oficiais
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from src.models.user import db
from src.models.question import Question
from src.main import app
import json

def get_clf_c02_questions():
    """Questões CLF-C02 - AWS Certified Cloud Practitioner"""
    return [
        {
            "certification": "CLF-C02",
            "domain": "Cloud Concepts",
            "question_text": "Uma empresa está considerando migrar para a AWS. Qual das seguintes opções melhor descreve o modelo de responsabilidade compartilhada da AWS?",
            "question_type": "multiple_choice",
            "options": [
                "A AWS é responsável pela segurança NA nuvem, e o cliente é responsável pela segurança DA nuvem",
                "O cliente é responsável pela segurança NA nuvem, e a AWS é responsável pela segurança DA nuvem", 
                "A AWS é responsável pela segurança DA nuvem, e o cliente é responsável pela segurança NA nuvem",
                "Tanto a AWS quanto o cliente compartilham igualmente todas as responsabilidades de segurança"
            ],
            "correct_answers": [2],
            "explanation": "No modelo de responsabilidade compartilhada: AWS é responsável pela segurança DA nuvem (infraestrutura física, rede, hipervisor, serviços gerenciados) e o cliente é responsável pela segurança NA nuvem (dados, aplicações, configurações de segurança, patches do SO, configuração de firewall).",
            "difficulty": "medium"
        },
        {
            "certification": "CLF-C02",
            "domain": "Cloud Concepts", 
            "question_text": "Quais são os principais benefícios da computação em nuvem? (Escolha três)",
            "question_type": "multiple_response",
            "options": [
                "Agilidade e velocidade de implantação",
                "Elasticidade e escalabilidade",
                "Economia de custos com modelo pay-as-you-use",
                "Eliminação completa de todos os riscos de segurança",
                "Garantia de 100% de uptime para todas as aplicações"
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "Os principais benefícios da nuvem são: Agilidade (rapidez para provisionar recursos), Elasticidade (escalar conforme demanda), e Economia de custos (pagar apenas pelo que usa). A nuvem não elimina todos os riscos de segurança nem garante 100% de uptime.",
            "difficulty": "easy"
        },
        {
            "certification": "CLF-C02",
            "domain": "Security and Compliance",
            "question_text": "Uma empresa precisa implementar autenticação multifator (MFA) para usuários que acessam recursos AWS. Qual serviço deve ser usado?",
            "question_type": "multiple_choice", 
            "options": [
                "AWS CloudTrail",
                "AWS IAM (Identity and Access Management)",
                "AWS Config",
                "Amazon Cognito"
            ],
            "correct_answers": [1],
            "explanation": "AWS IAM permite configurar MFA para usuários, adicionando uma camada extra de segurança. O MFA pode ser configurado usando dispositivos virtuais, hardware ou SMS.",
            "difficulty": "easy"
        },
        {
            "certification": "CLF-C02",
            "domain": "Technology",
            "question_text": "Uma aplicação web precisa de um banco de dados NoSQL totalmente gerenciado com latência de milissegundos. Qual serviço seria mais apropriado?",
            "question_type": "multiple_choice",
            "options": [
                "Amazon RDS",
                "Amazon DynamoDB", 
                "Amazon Redshift",
                "Amazon Aurora"
            ],
            "correct_answers": [1],
            "explanation": "Amazon DynamoDB é um banco NoSQL totalmente gerenciado que oferece latência de milissegundos em qualquer escala. É ideal para aplicações que precisam de performance consistente e alta disponibilidade.",
            "difficulty": "easy"
        },
        {
            "certification": "CLF-C02",
            "domain": "Billing and Pricing",
            "question_text": "Uma empresa quer reduzir custos de instâncias EC2 que executam cargas de trabalho previsíveis por 24/7. Qual opção de compra oferece maior economia?",
            "question_type": "multiple_choice", 
            "options": [
                "On-Demand Instances",
                "Spot Instances",
                "Reserved Instances",
                "Dedicated Instances"
            ],
            "correct_answers": [2],
            "explanation": "Reserved Instances oferecem até 75% de desconto comparado a On-Demand para cargas previsíveis com compromisso de 1 ou 3 anos. São ideais para workloads estáveis e previsíveis.",
            "difficulty": "medium"
        }
    ]

def get_aif_c01_questions():
    """Questões AIF-C01 - AWS Certified AI Practitioner"""
    return [
        {
            "certification": "AIF-C01",
            "domain": "Fundamentals of AI and ML",
            "question_text": "Qual é a principal diferença entre Inteligência Artificial (AI), Machine Learning (ML) e Deep Learning (DL)?",
            "question_type": "multiple_choice",
            "options": [
                "AI é um subconjunto de ML, que é um subconjunto de DL",
                "ML é um subconjunto de AI, e DL é um subconjunto de ML",
                "DL é um subconjunto de AI, e ML é um subconjunto de DL", 
                "AI, ML e DL são termos intercambiáveis"
            ],
            "correct_answers": [1],
            "explanation": "AI é o campo mais amplo que busca criar máquinas inteligentes. ML é um subconjunto de AI que usa algoritmos para aprender com dados. DL é um subconjunto de ML que usa redes neurais profundas.",
            "difficulty": "medium"
        },
        {
            "certification": "AIF-C01",
            "domain": "Fundamentals of AI and ML",
            "question_text": "Quais são os três principais tipos de aprendizado de máquina?",
            "question_type": "multiple_choice",
            "options": [
                "Supervisionado, Não-supervisionado e Por reforço",
                "Classificação, Regressão e Clustering",
                "Treinamento, Validação e Teste",
                "Linear, Não-linear e Probabilístico"
            ],
            "correct_answers": [0],
            "explanation": "Os três tipos principais são: Supervisionado (com dados rotulados), Não-supervisionado (sem rótulos, encontra padrões) e Por reforço (aprende através de recompensas/punições).",
            "difficulty": "easy"
        },
        {
            "certification": "AIF-C01",
            "domain": "AI and ML Services on AWS",
            "question_text": "Uma empresa quer adicionar capacidades de reconhecimento de fala em tempo real à sua aplicação. Qual serviço AWS seria mais apropriado?",
            "question_type": "multiple_choice",
            "options": [
                "Amazon Polly",
                "Amazon Transcribe",
                "Amazon Translate",
                "Amazon Comprehend"
            ],
            "correct_answers": [1],
            "explanation": "Amazon Transcribe converte fala em texto em tempo real. Amazon Polly faz o contrário (texto para fala), Translate traduz idiomas e Comprehend analisa sentimentos em texto.",
            "difficulty": "easy"
        },
        {
            "certification": "AIF-C01",
            "domain": "Responsible AI",
            "question_text": "Quais são as principais considerações éticas ao implementar sistemas de AI? (Escolha três)",
            "question_type": "multiple_response",
            "options": [
                "Transparência e explicabilidade dos modelos",
                "Prevenção de viés e discriminação",
                "Privacidade e proteção de dados",
                "Maximização de lucros a qualquer custo",
                "Substituição completa de trabalhadores humanos"
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "AI responsável requer: transparência (entender como decisões são tomadas), prevenção de viés (fairness), e proteção de privacidade. Maximizar lucros sem ética e substituir humanos indiscriminadamente não são práticas responsáveis.",
            "difficulty": "medium"
        },
        {
            "certification": "AIF-C01",
            "domain": "AI and ML Services on AWS",
            "question_text": "Uma empresa quer implementar um chatbot inteligente para atendimento ao cliente. Qual serviço AWS seria mais apropriado?",
            "question_type": "multiple_choice",
            "options": [
                "Amazon Lex",
                "Amazon Kendra",
                "Amazon Textract",
                "Amazon Rekognition"
            ],
            "correct_answers": [0],
            "explanation": "Amazon Lex é o serviço para construir interfaces de conversação (chatbots) usando voz e texto. Inclui processamento de linguagem natural e reconhecimento automático de fala.",
            "difficulty": "easy"
        }
    ]

def get_saa_c03_questions():
    """Questões SAA-C03 - AWS Certified Solutions Architect Associate"""
    return [
        {
            "certification": "SAA-C03",
            "domain": "Design Resilient Architectures",
            "question_text": "Uma aplicação crítica precisa de 99.99% de disponibilidade. Como deve ser projetada a arquitetura para atender esse requisito?",
            "question_type": "multiple_choice",
            "options": [
                "Implantar em uma única AZ com instâncias redundantes",
                "Implantar em múltiplas AZs dentro de uma região com load balancer",
                "Implantar em uma única região com backup em outra região",
                "Usar apenas instâncias Spot para reduzir custos"
            ],
            "correct_answers": [1],
            "explanation": "Para alta disponibilidade, deve-se usar múltiplas AZs com load balancer. Isso garante que se uma AZ falhar, a aplicação continue funcionando nas outras AZs.",
            "difficulty": "medium"
        },
        {
            "certification": "SAA-C03",
            "domain": "Design High-Performing Architectures",
            "question_text": "Uma aplicação web tem picos de tráfego imprevisíveis. Qual estratégia de auto scaling seria mais eficiente?",
            "question_type": "multiple_choice",
            "options": [
                "Scaling baseado apenas em CPU",
                "Scaling baseado em múltiplas métricas (CPU, memória, requests)",
                "Scaling manual durante horários de pico",
                "Manter sempre o número máximo de instâncias"
            ],
            "correct_answers": [1],
            "explanation": "Usar múltiplas métricas fornece uma visão mais completa da demanda e permite scaling mais preciso e eficiente, evitando over ou under-provisioning.",
            "difficulty": "medium"
        },
        {
            "certification": "SAA-C03",
            "domain": "Design Secure Architectures",
            "question_text": "Uma empresa precisa permitir acesso temporário a recursos AWS para usuários externos. Qual é a melhor prática?",
            "question_type": "multiple_choice",
            "options": [
                "Criar usuários IAM permanentes para cada usuário externo",
                "Compartilhar credenciais de um usuário IAM existente",
                "Usar IAM Roles com AssumeRole para acesso temporário",
                "Dar acesso root para simplificar o processo"
            ],
            "correct_answers": [2],
            "explanation": "IAM Roles com AssumeRole permitem acesso temporário e seguro sem compartilhar credenciais permanentes. É a prática recomendada para acesso externo ou cross-account.",
            "difficulty": "medium"
        },
        {
            "certification": "SAA-C03",
            "domain": "Design Cost-Optimized Architectures",
            "question_text": "Uma aplicação tem workloads que podem tolerar interrupções e têm flexibilidade de horário. Qual estratégia de instâncias EC2 seria mais econômica?",
            "question_type": "multiple_choice",
            "options": [
                "On-Demand Instances",
                "Reserved Instances",
                "Spot Instances",
                "Dedicated Hosts"
            ],
            "correct_answers": [2],
            "explanation": "Spot Instances oferecem até 90% de desconto para workloads que podem tolerar interrupções. São ideais para processamento em lote, análise de dados e outras tarefas flexíveis.",
            "difficulty": "easy"
        },
        {
            "certification": "SAA-C03",
            "domain": "Design Resilient Architectures",
            "question_text": "Uma aplicação precisa de um banco de dados que possa automaticamente fazer failover para outra região em caso de falha. Qual solução seria mais apropriada?",
            "question_type": "multiple_choice",
            "options": [
                "Amazon RDS com Multi-AZ",
                "Amazon RDS com Read Replicas cross-region",
                "Amazon Aurora Global Database",
                "DynamoDB com backup manual"
            ],
            "correct_answers": [2],
            "explanation": "Aurora Global Database permite replicação cross-region com failover automático em menos de 1 minuto, oferecendo a melhor solução para disaster recovery global.",
            "difficulty": "hard"
        }
    ]

def get_sap_c02_questions():
    """Questões SAP-C02 - AWS Certified Solutions Architect Professional"""
    return [
        {
            "certification": "SAP-C02",
            "domain": "Design Solutions for Organizational Complexity",
            "question_text": "Uma organização multinacional precisa implementar uma estratégia de múltiplas contas AWS com governança centralizada. Qual abordagem seria mais eficaz?",
            "question_type": "multiple_choice",
            "options": [
                "Usar uma única conta AWS com IAM para separação",
                "Implementar AWS Organizations com SCPs (Service Control Policies)",
                "Criar contas separadas sem integração",
                "Usar apenas AWS Config para governança"
            ],
            "correct_answers": [1],
            "explanation": "AWS Organizations com SCPs permite governança centralizada, billing consolidado e controle granular de permissões across múltiplas contas, sendo a solução enterprise recomendada.",
            "difficulty": "hard"
        },
        {
            "certification": "SAP-C02",
            "domain": "Design for New Solutions",
            "question_text": "Uma aplicação de machine learning precisa processar grandes volumes de dados com baixa latência e alta throughput. Qual arquitetura seria mais eficiente?",
            "question_type": "multiple_choice",
            "options": [
                "EC2 com EBS gp2",
                "EC2 com instance store e EBS io2",
                "Lambda com S3",
                "Fargate com EFS"
            ],
            "correct_answers": [1],
            "explanation": "Para ML com alta performance, EC2 com instance store (NVMe SSD local) para dados temporários e EBS io2 para dados persistentes oferece a melhor combinação de latência e throughput.",
            "difficulty": "hard"
        },
        {
            "certification": "SAP-C02",
            "domain": "Migration Planning",
            "question_text": "Uma empresa precisa migrar um data center completo para AWS com mínimo downtime. Qual estratégia de migração seria mais apropriada?",
            "question_type": "multiple_choice",
            "options": [
                "Lift and shift de todos os sistemas simultaneamente",
                "Migração faseada com AWS Application Migration Service",
                "Reescrever todas as aplicações como cloud-native",
                "Manter tudo on-premises e usar apenas AWS para backup"
            ],
            "correct_answers": [1],
            "explanation": "Migração faseada com AWS Application Migration Service permite migração com mínimo downtime, testando cada workload antes da cutover final, reduzindo riscos.",
            "difficulty": "medium"
        },
        {
            "certification": "SAP-C02",
            "domain": "Cost Control",
            "question_text": "Uma empresa tem custos AWS crescendo rapidamente e precisa implementar governança financeira. Quais estratégias devem ser implementadas? (Escolha três)",
            "question_type": "multiple_response",
            "options": [
                "Implementar AWS Budgets com alertas automáticos",
                "Usar Cost Allocation Tags para rastreamento detalhado",
                "Implementar políticas de auto-shutdown para recursos não utilizados",
                "Migrar tudo para instâncias mais caras para garantir performance",
                "Ignorar custos de desenvolvimento e focar apenas em produção"
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "Governança financeira eficaz requer: Budgets para controle proativo, Tags para visibilidade de custos por projeto/departamento, e automação para eliminar desperdícios.",
            "difficulty": "medium"
        },
        {
            "certification": "SAP-C02",
            "domain": "Continuous Improvement for Existing Solutions",
            "question_text": "Uma aplicação legacy tem problemas de performance e escalabilidade. Qual abordagem de modernização seria mais eficaz?",
            "question_type": "multiple_choice",
            "options": [
                "Migrar para instâncias maiores sem mudanças",
                "Implementar microserviços com containers e API Gateway",
                "Adicionar mais servidores com a mesma arquitetura",
                "Mover para serverless sem análise prévia"
            ],
            "correct_answers": [1],
            "explanation": "Modernização com microserviços permite escalabilidade independente, melhor manutenibilidade e uso de serviços gerenciados AWS, resolvendo problemas de arquiteturas monolíticas.",
            "difficulty": "hard"
        }
    ]

def main():
    """Função principal para popular o banco com questões de todas as certificações"""
    with app.app_context():
        # Criar tabelas se não existirem
        db.create_all()
        
        # Coletar todas as questões
        all_questions = []
        all_questions.extend(get_clf_c02_questions())
        all_questions.extend(get_aif_c01_questions())
        all_questions.extend(get_saa_c03_questions())
        all_questions.extend(get_sap_c02_questions())
        
        print(f"Processando {len(all_questions)} questões...")
        
        added_count = 0
        existing_count = 0
        
        for q_data in all_questions:
            # Verificar se a questão já existe
            existing = Question.query.filter_by(
                certification=q_data["certification"],
                question_text=q_data["question_text"]
            ).first()
            
            if not existing:
                question = Question(
                    certification=q_data["certification"],
                    domain=q_data["domain"],
                    question_text=q_data["question_text"],
                    question_type=q_data["question_type"],
                    options=json.dumps(q_data["options"]),
                    correct_answers=json.dumps(q_data["correct_answers"]),
                    explanation=q_data["explanation"],
                    difficulty=q_data["difficulty"]
                )
                db.session.add(question)
                added_count += 1
                print(f"✓ Adicionada [{q_data['certification']}]: {q_data['question_text'][:60]}...")
            else:
                existing_count += 1
                print(f"- Já existe [{q_data['certification']}]: {q_data['question_text'][:60]}...")
        
        db.session.commit()
        
        # Estatísticas finais
        print(f"\n{'='*60}")
        print(f"✅ PROCESSO CONCLUÍDO!")
        print(f"{'='*60}")
        print(f"📊 Questões adicionadas: {added_count}")
        print(f"📊 Questões já existentes: {existing_count}")
        print(f"📊 Total processadas: {len(all_questions)}")
        
        # Contagem por certificação
        for cert in ['CLF-C02', 'AIF-C01', 'SAA-C03', 'SAP-C02']:
            count = Question.query.filter_by(certification=cert).count()
            print(f"📊 {cert}: {count} questões no banco")
        
        total_questions = Question.query.count()
        print(f"📊 TOTAL GERAL: {total_questions} questões no banco de dados")

if __name__ == "__main__":
    main()

