#!/usr/bin/env python3
"""
Script para gerar questões adicionais para expandir o banco de dados
Foco em cenários práticos e situações reais de certificação
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from src.models.user import db
from src.models.question import Question
from src.main import app
import json

def get_additional_clf_questions():
    """Questões adicionais CLF-C02 focadas em cenários práticos"""
    return [
        {
            "certification": "CLF-C02",
            "domain": "Technology",
            "question_text": "Uma startup precisa hospedar um website estático com alta disponibilidade e baixo custo. Qual combinação de serviços seria mais apropriada?",
            "question_type": "multiple_choice",
            "options": [
                "EC2 + ELB + Auto Scaling",
                "S3 + CloudFront + Route 53",
                "Lambda + API Gateway + DynamoDB",
                "Lightsail + RDS + ElastiCache"
            ],
            "correct_answers": [1],
            "explanation": "Para websites estáticos, S3 oferece hospedagem de baixo custo, CloudFront melhora performance global via CDN, e Route 53 fornece DNS confiável. Esta é a solução mais econômica e eficiente.",
            "difficulty": "medium"
        },
        {
            "certification": "CLF-C02",
            "domain": "Security and Compliance",
            "question_text": "Uma empresa precisa criptografar dados em trânsito e em repouso. Quais serviços AWS ajudam com isso? (Escolha dois)",
            "question_type": "multiple_response",
            "options": [
                "AWS KMS (Key Management Service)",
                "AWS CloudTrail",
                "SSL/TLS certificates via ACM (Certificate Manager)",
                "AWS Config",
                "Amazon Inspector"
            ],
            "correct_answers": [0, 2],
            "explanation": "AWS KMS gerencia chaves de criptografia para dados em repouso, e ACM fornece certificados SSL/TLS para criptografia em trânsito. Ambos são essenciais para uma estratégia completa de criptografia.",
            "difficulty": "medium"
        },
        {
            "certification": "CLF-C02",
            "domain": "Billing and Pricing",
            "question_text": "Uma empresa quer monitorar e controlar custos AWS proativamente. Quais ferramentas devem ser usadas? (Escolha três)",
            "question_type": "multiple_response",
            "options": [
                "AWS Budgets para alertas de custo",
                "Cost Explorer para análise de tendências",
                "AWS Pricing Calculator para estimativas",
                "CloudWatch apenas para métricas técnicas",
                "Trusted Advisor para recomendações de otimização"
            ],
            "correct_answers": [0, 1, 4],
            "explanation": "AWS Budgets monitora gastos e envia alertas, Cost Explorer analisa padrões de uso, e Trusted Advisor identifica oportunidades de economia. Pricing Calculator é para estimativas pré-implementação.",
            "difficulty": "medium"
        },
        {
            "certification": "CLF-C02",
            "domain": "Cloud Concepts",
            "question_text": "Qual das seguintes situações melhor demonstra o conceito de 'elasticidade' na nuvem?",
            "question_type": "multiple_choice",
            "options": [
                "Manter sempre 10 servidores rodando independente da demanda",
                "Aumentar automaticamente de 2 para 8 servidores durante picos de tráfego e reduzir para 2 quando o tráfego normaliza",
                "Fazer backup dos dados uma vez por semana",
                "Usar apenas uma região AWS para todos os recursos"
            ],
            "correct_answers": [1],
            "explanation": "Elasticidade é a capacidade de escalar recursos automaticamente baseado na demanda real, aumentando durante picos e diminuindo quando a demanda reduz, otimizando custos e performance.",
            "difficulty": "easy"
        },
        {
            "certification": "CLF-C02",
            "domain": "Technology",
            "question_text": "Uma aplicação precisa processar milhões de mensagens de forma assíncrona e confiável. Qual serviço seria mais apropriado?",
            "question_type": "multiple_choice",
            "options": [
                "Amazon SNS (Simple Notification Service)",
                "Amazon SQS (Simple Queue Service)",
                "Amazon SES (Simple Email Service)",
                "Amazon Kinesis"
            ],
            "correct_answers": [1],
            "explanation": "Amazon SQS é ideal para processamento assíncrono de mensagens, oferecendo durabilidade, escalabilidade e garantia de entrega. É o serviço padrão para desacoplar componentes de aplicações.",
            "difficulty": "easy"
        }
    ]

def get_additional_aif_questions():
    """Questões adicionais AIF-C01 focadas em casos de uso práticos"""
    return [
        {
            "certification": "AIF-C01",
            "domain": "AI and ML Services on AWS",
            "question_text": "Uma empresa de e-commerce quer implementar recomendações personalizadas de produtos. Qual serviço AWS seria mais apropriado?",
            "question_type": "multiple_choice",
            "options": [
                "Amazon Personalize",
                "Amazon Comprehend",
                "Amazon Textract",
                "Amazon Forecast"
            ],
            "correct_answers": [0],
            "explanation": "Amazon Personalize é especificamente projetado para criar sistemas de recomendação personalizados usando machine learning, ideal para e-commerce e plataformas de conteúdo.",
            "difficulty": "easy"
        },
        {
            "certification": "AIF-C01",
            "domain": "Fundamentals of AI and ML",
            "question_text": "Qual é a diferença entre overfitting e underfitting em machine learning?",
            "question_type": "multiple_choice",
            "options": [
                "Overfitting é quando o modelo é muito simples, underfitting é quando é muito complexo",
                "Overfitting é quando o modelo memoriza dados de treino mas falha em generalizar, underfitting é quando o modelo é muito simples para capturar padrões",
                "Ambos são sinônimos e representam o mesmo problema",
                "Overfitting só acontece com deep learning, underfitting só com algoritmos tradicionais"
            ],
            "correct_answers": [1],
            "explanation": "Overfitting ocorre quando o modelo é muito complexo e memoriza os dados de treino, falhando em generalizar. Underfitting acontece quando o modelo é muito simples para capturar os padrões nos dados.",
            "difficulty": "medium"
        },
        {
            "certification": "AIF-C01",
            "domain": "AI and ML Services on AWS",
            "question_text": "Uma empresa quer extrair texto de documentos escaneados e PDFs. Qual serviço AWS seria mais eficaz?",
            "question_type": "multiple_choice",
            "options": [
                "Amazon Comprehend",
                "Amazon Textract",
                "Amazon Translate",
                "Amazon Polly"
            ],
            "correct_answers": [1],
            "explanation": "Amazon Textract usa OCR (Optical Character Recognition) e machine learning para extrair texto, tabelas e dados de documentos escaneados e PDFs com alta precisão.",
            "difficulty": "easy"
        }
    ]

def get_additional_saa_questions():
    """Questões adicionais SAA-C03 focadas em arquiteturas complexas"""
    return [
        {
            "certification": "SAA-C03",
            "domain": "Design Resilient Architectures",
            "question_text": "Uma aplicação crítica precisa de RTO (Recovery Time Objective) de 5 minutos e RPO (Recovery Point Objective) de 1 minuto. Qual estratégia de disaster recovery seria mais apropriada?",
            "question_type": "multiple_choice",
            "options": [
                "Backup and Restore",
                "Pilot Light",
                "Warm Standby",
                "Multi-Site Active/Active"
            ],
            "correct_answers": [3],
            "explanation": "Para RTO de 5 minutos e RPO de 1 minuto, apenas Multi-Site Active/Active pode atender esses requisitos rigorosos, mantendo infraestrutura completa em múltiplas regiões.",
            "difficulty": "hard"
        },
        {
            "certification": "SAA-C03",
            "domain": "Design High-Performing Architectures",
            "question_text": "Uma aplicação de analytics precisa processar 10TB de dados diariamente com consultas ad-hoc. Qual arquitetura seria mais eficiente?",
            "question_type": "multiple_choice",
            "options": [
                "RDS MySQL com read replicas",
                "DynamoDB com GSI",
                "S3 + Athena + Glue",
                "ElastiCache + Lambda"
            ],
            "correct_answers": [2],
            "explanation": "Para analytics de grandes volumes com consultas ad-hoc, S3 para armazenamento, Athena para consultas SQL serverless e Glue para ETL formam a arquitetura mais eficiente e econômica.",
            "difficulty": "medium"
        }
    ]

def get_additional_sap_questions():
    """Questões adicionais SAP-C02 focadas em cenários enterprise"""
    return [
        {
            "certification": "SAP-C02",
            "domain": "Design Solutions for Organizational Complexity",
            "question_text": "Uma empresa multinacional precisa implementar compliance GDPR em múltiplas regiões AWS. Qual estratégia seria mais eficaz?",
            "question_type": "multiple_choice",
            "options": [
                "Usar apenas regiões europeias para todos os dados",
                "Implementar data residency com AWS Config Rules e SCPs",
                "Criptografar todos os dados com KMS",
                "Usar apenas serviços serverless"
            ],
            "correct_answers": [1],
            "explanation": "Para GDPR compliance, é essencial implementar data residency usando AWS Config Rules para monitoramento e SCPs para enforcement de políticas de localização de dados.",
            "difficulty": "hard"
        },
        {
            "certification": "SAP-C02",
            "domain": "Design for New Solutions",
            "question_text": "Uma aplicação de IoT precisa processar 1 milhão de eventos por segundo com latência sub-100ms. Qual arquitetura seria mais apropriada?",
            "question_type": "multiple_choice",
            "options": [
                "API Gateway + Lambda + DynamoDB",
                "Kinesis Data Streams + Kinesis Analytics + ElastiCache",
                "SQS + EC2 + RDS",
                "SNS + Lambda + S3"
            ],
            "correct_answers": [1],
            "explanation": "Para alta throughput e baixa latência em IoT, Kinesis Data Streams ingere dados em tempo real, Kinesis Analytics processa streams, e ElastiCache fornece acesso de baixa latência.",
            "difficulty": "hard"
        }
    ]

def main():
    """Adiciona questões adicionais ao banco de dados"""
    with app.app_context():
        # Coletar questões adicionais
        additional_questions = []
        additional_questions.extend(get_additional_clf_questions())
        additional_questions.extend(get_additional_aif_questions())
        additional_questions.extend(get_additional_saa_questions())
        additional_questions.extend(get_additional_sap_questions())
        
        print(f"Processando {len(additional_questions)} questões adicionais...")
        
        added_count = 0
        existing_count = 0
        
        for q_data in additional_questions:
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
        print(f"✅ QUESTÕES ADICIONAIS PROCESSADAS!")
        print(f"{'='*60}")
        print(f"📊 Questões adicionadas: {added_count}")
        print(f"📊 Questões já existentes: {existing_count}")
        
        # Contagem final por certificação
        for cert in ['CLF-C02', 'AIF-C01', 'SAA-C03', 'SAP-C02']:
            count = Question.query.filter_by(certification=cert).count()
            print(f"📊 {cert}: {count} questões no banco")
        
        total_questions = Question.query.count()
        print(f"📊 TOTAL GERAL: {total_questions} questões no banco de dados")

if __name__ == "__main__":
    main()

