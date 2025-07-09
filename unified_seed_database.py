#!/usr/bin/env python3
"""
Unified Database Seeding Script for AWS Simulados
=================================================

This script unifies all database seeding functionality for the AWS Simulados project.
It combines question generation and population logic from all existing seed scripts:
- generate_300_questions.py
- generate_additional_questions.py
- generate_clf_questions.py
- generate_comprehensive_questions.py
- init_db.py
- populate_questions.py

Usage:
    python unified_seed_database.py [options]

Options:
    --cert CERT     Seed only specific certification (CLF-C02, AIF-C01, SAA-C03, SAP-C02)
    --reset         Clear existing questions before seeding
    --verbose       Enable verbose output
    --help          Show this help message

Examples:
    python unified_seed_database.py                    # Seed all certifications
    python unified_seed_database.py --cert CLF-C02     # Seed only CLF-C02
    python unified_seed_database.py --reset            # Clear DB and seed all
"""

import os
import sys
import json
import argparse
from datetime import datetime

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

from src.models.user import db
from src.models.question import Question, SimulationSession
from src.main import app

class UnifiedDatabaseSeeder:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.added_count = 0
        self.existing_count = 0
        self.error_count = 0
        
    def log(self, message, level="INFO"):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
        
    def verbose_log(self, message):
        """Log message only if verbose mode is enabled"""
        if self.verbose:
            self.log(message, "DEBUG")
    
    def get_clf_c02_questions(self):
        """Generate CLF-C02 questions from all sources"""
        questions = []
        
        # Questions from generate_300_questions.py - 100 questions distributed across domains
        # Cloud Concepts (25 questions)
        for i in range(25):
            questions.append({
                "certification": "CLF-C02",
                "domain": "Cloud Concepts",
                "question_text": f"Uma empresa está avaliando migração para nuvem. Questão {i+1}: Qual é o benefício de {['elasticidade', 'agilidade', 'economia de escala', 'alcance global', 'alta disponibilidade'][i%5]} na AWS?",
                "question_type": "multiple_choice",
                "options": [
                    f"Permite redução de custos através de {['otimização automática', 'recursos compartilhados', 'pagamento por uso', 'eliminação de CapEx'][i%4]}",
                    f"Oferece {['escalabilidade instantânea', 'deploy global rápido', 'redundância automática', 'performance otimizada'][i%4]}",
                    f"Garante {['segurança avançada', 'compliance automático', 'backup contínuo', 'monitoramento 24/7'][i%4]}",
                    f"Facilita {['inovação rápida', 'time-to-market', 'experimentação', 'prototipagem'][i%4]}"
                ],
                "correct_answers": [str(i%4)],
                "explanation": f"Explicação detalhada sobre {['elasticidade', 'agilidade', 'economia de escala', 'alcance global', 'alta disponibilidade'][i%5]} como benefício fundamental da computação em nuvem AWS.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # Security and Compliance (25 questions)
        for i in range(25):
            questions.append({
                "certification": "CLF-C02",
                "domain": "Security and Compliance",
                "question_text": f"Questão de Segurança {i+1}: Como implementar {['MFA', 'IAM Roles', 'CloudTrail', 'GuardDuty', 'Shield'][i%5]} para melhorar a postura de segurança?",
                "question_type": "multiple_choice",
                "options": [
                    f"Configurar {['autenticação dupla', 'permissões temporárias', 'auditoria de API', 'detecção de ameaças', 'proteção DDoS'][i%5]} adequadamente",
                    f"Implementar {['tokens seguros', 'assume role', 'logs centralizados', 'ML para anomalias', 'WAF integrado'][i%5]} corretamente",
                    f"Estabelecer {['políticas rígidas', 'acesso mínimo', 'monitoramento contínuo', 'alertas automáticos', 'filtros de tráfego'][i%5]} efetivamente",
                    f"Manter {['credenciais seguras', 'rotação de chaves', 'compliance ativo', 'visibilidade total', 'defesa em camadas'][i%5]} constantemente"
                ],
                "correct_answers": [str(i%4)],
                "explanation": f"Explicação sobre implementação adequada de {['MFA', 'IAM Roles', 'CloudTrail', 'GuardDuty', 'Shield'][i%5]} seguindo melhores práticas de segurança AWS.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # Technology (25 questions)
        for i in range(25):
            questions.append({
                "certification": "CLF-C02",
                "domain": "Technology",
                "question_text": f"Questão de Tecnologia {i+1}: Uma aplicação precisa de {['armazenamento de objetos', 'banco relacional', 'computação serverless', 'CDN global', 'DNS gerenciado'][i%5]}. Qual serviço AWS é mais apropriado?",
                "question_type": "multiple_choice",
                "options": [
                    f"Amazon {['S3', 'RDS', 'Lambda', 'CloudFront', 'Route 53'][i%5]}",
                    f"Amazon {['EBS', 'DynamoDB', 'EC2', 'API Gateway', 'VPC'][i%5]}",
                    f"Amazon {['EFS', 'Aurora', 'ECS', 'ElastiCache', 'Direct Connect'][i%5]}",
                    f"Amazon {['Glacier', 'Redshift', 'Batch', 'Global Accelerator', 'Transit Gateway'][i%5]}"
                ],
                "correct_answers": ["A"],
                "explanation": f"Amazon {['S3', 'RDS', 'Lambda', 'CloudFront', 'Route 53'][i%5]} é o serviço mais apropriado para {['armazenamento de objetos', 'banco relacional', 'computação serverless', 'CDN global', 'DNS gerenciado'][i%5]} devido às suas características específicas.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # Billing and Pricing (25 questions)
        for i in range(25):
            questions.append({
                "certification": "CLF-C02",
                "domain": "Billing and Pricing",
                "question_text": f"Questão de Billing {i+1}: Para otimizar custos de {['instâncias EC2', 'armazenamento S3', 'transferência de dados', 'banco RDS', 'Lambda executions'][i%5]}, qual estratégia é mais eficaz?",
                "question_type": "multiple_choice",
                "options": [
                    f"Usar {['Reserved Instances', 'Intelligent Tiering', 'CloudFront', 'Reserved Instances', 'Provisioned Concurrency'][i%5]}",
                    f"Implementar {['Spot Instances', 'Lifecycle Policies', 'VPC Endpoints', 'Aurora Serverless', 'Pay-per-request'][i%5]}",
                    f"Configurar {['Savings Plans', 'Storage Classes', 'Data Compression', 'Read Replicas', 'Memory Optimization'][i%5]}",
                    f"Aplicar {['Right Sizing', 'Cross-Region Replication', 'Edge Locations', 'Multi-AZ', 'Concurrent Executions'][i%5]}"
                ],
                "correct_answers": [str(i%4)],
                "explanation": f"Para otimizar custos de {['instâncias EC2', 'armazenamento S3', 'transferência de dados', 'banco RDS', 'Lambda executions'][i%5]}, a estratégia mais eficaz considera padrões de uso e características específicas do serviço.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # Questions from generate_clf_questions.py
        questions.extend([
            {
                "certification": "CLF-C02",
                "domain": "Cloud Concepts",
                "question_text": "Uma empresa está migrando sua infraestrutura para a AWS. Qual das seguintes opções melhor descreve o modelo de responsabilidade compartilhada da AWS?",
                "question_type": "multiple_choice",
                "options": [
                    "A AWS é responsável pela segurança NA nuvem, e o cliente é responsável pela segurança DA nuvem",
                    "O cliente é responsável pela segurança NA nuvem, e a AWS é responsável pela segurança DA nuvem", 
                    "A AWS é responsável pela segurança DA nuvem, e o cliente é responsável pela segurança NA nuvem",
                    "Tanto a AWS quanto o cliente compartilham igualmente todas as responsabilidades de segurança"
                ],
                "correct_answers": ["C"],
                "explanation": "No modelo de responsabilidade compartilhada da AWS: AWS é responsável pela segurança DA nuvem (infraestrutura física, rede, hipervisor) e o cliente é responsável pela segurança NA nuvem (dados, aplicações, configurações de segurança, patches do SO).",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Cloud Concepts", 
                "question_text": "Quais são os três principais benefícios da computação em nuvem que a AWS oferece?",
                "question_type": "multiple_choice",
                "options": [
                    "Agilidade, elasticidade e economia de custos",
                    "Segurança, compliance e auditoria",
                    "Backup, recuperação e arquivamento", 
                    "Monitoramento, logging e alertas"
                ],
                "correct_answers": ["A"],
                "explanation": "Os três principais benefícios da computação em nuvem são: Agilidade (rapidez para provisionar recursos), Elasticidade (capacidade de escalar recursos conforme demanda) e Economia de custos (modelo pay-as-you-use sem investimento inicial em hardware).",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Security and Compliance",
                "question_text": "Uma empresa precisa garantir que apenas usuários autorizados tenham acesso aos recursos da AWS. Qual serviço da AWS deve ser usado para gerenciar identidades e acessos?",
                "question_type": "multiple_choice", 
                "options": [
                    "AWS CloudTrail",
                    "AWS IAM (Identity and Access Management)",
                    "AWS Config",
                    "AWS Inspector"
                ],
                "correct_answers": ["B"],
                "explanation": "AWS IAM (Identity and Access Management) é o serviço responsável por gerenciar identidades, usuários, grupos, roles e políticas de acesso aos recursos da AWS. Permite controlar quem pode acessar quais recursos e quais ações podem ser executadas.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Security and Compliance",
                "question_text": "Qual das seguintes práticas de segurança é recomendada para a conta root da AWS?",
                "question_type": "multiple_choice",
                "options": [
                    "Usar a conta root para todas as atividades administrativas diárias",
                    "Compartilhar as credenciais da conta root com a equipe de TI",
                    "Habilitar MFA (Multi-Factor Authentication) e usar a conta root apenas quando necessário",
                    "Desabilitar a conta root após criar usuários IAM"
                ],
                "correct_answers": ["C"],
                "explanation": "A conta root deve ter MFA habilitado e ser usada apenas para tarefas que requerem especificamente privilégios de root (como alterar plano de suporte ou fechar conta). Para atividades diárias, devem ser usados usuários IAM com permissões apropriadas.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Technology",
                "question_text": "Uma aplicação web precisa de um banco de dados relacional totalmente gerenciado na AWS. Qual serviço seria mais apropriado?",
                "question_type": "multiple_choice",
                "options": [
                    "Amazon DynamoDB",
                    "Amazon RDS (Relational Database Service)", 
                    "Amazon Redshift",
                    "Amazon ElastiCache"
                ],
                "correct_answers": ["B"],
                "explanation": "Amazon RDS é o serviço de banco de dados relacional totalmente gerenciado da AWS, suportando engines como MySQL, PostgreSQL, Oracle, SQL Server e MariaDB. A AWS gerencia backups, patches, monitoramento e alta disponibilidade.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02", 
                "domain": "Technology",
                "question_text": "Qual serviço da AWS fornece armazenamento de objetos escalável e durável?",
                "question_type": "multiple_choice",
                "options": [
                    "Amazon EBS (Elastic Block Store)",
                    "Amazon EFS (Elastic File System)",
                    "Amazon S3 (Simple Storage Service)",
                    "Amazon FSx"
                ],
                "correct_answers": ["C"],
                "explanation": "Amazon S3 é o serviço de armazenamento de objetos da AWS, oferecendo 99.999999999% (11 9's) de durabilidade e escalabilidade virtualmente ilimitada. É ideal para backup, arquivamento, websites estáticos e data lakes.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Technology", 
                "question_text": "Uma empresa quer executar aplicações em contêineres na AWS sem gerenciar a infraestrutura subjacente. Qual serviço seria mais apropriado?",
                "question_type": "multiple_choice",
                "options": [
                    "Amazon EC2",
                    "AWS Lambda",
                    "Amazon ECS com Fargate",
                    "Amazon Lightsail"
                ],
                "correct_answers": ["C"],
                "explanation": "Amazon ECS (Elastic Container Service) com Fargate permite executar contêineres sem gerenciar servidores. O Fargate é um mecanismo de computação serverless que elimina a necessidade de provisionar e gerenciar instâncias EC2.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Billing and Pricing",
                "question_text": "Qual ferramenta da AWS ajuda a estimar os custos antes de implementar recursos na nuvem?",
                "question_type": "multiple_choice",
                "options": [
                    "AWS Cost Explorer",
                    "AWS Pricing Calculator", 
                    "AWS Budgets",
                    "AWS Cost and Usage Report"
                ],
                "correct_answers": ["B"],
                "explanation": "AWS Pricing Calculator é uma ferramenta gratuita que permite estimar custos de serviços AWS antes da implementação. Você pode modelar suas soluções, explorar preços e criar estimativas que podem ser salvas e compartilhadas.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Billing and Pricing",
                "question_text": "Uma empresa quer reduzir custos de instâncias EC2 que executam cargas de trabalho previsíveis. Qual opção de compra seria mais econômica?",
                "question_type": "multiple_choice", 
                "options": [
                    "On-Demand Instances",
                    "Spot Instances",
                    "Reserved Instances",
                    "Dedicated Hosts"
                ],
                "correct_answers": ["C"],
                "explanation": "Reserved Instances oferecem desconto significativo (até 75%) comparado a On-Demand para cargas de trabalho previsíveis com compromisso de 1 ou 3 anos. São ideais quando você pode prever o uso e se comprometer com um período específico.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Billing and Pricing",
                "question_text": "Qual das seguintes opções descreve corretamente o modelo de preços 'pay-as-you-go' da AWS?",
                "question_type": "multiple_choice",
                "options": [
                    "Pagamento fixo mensal independente do uso",
                    "Pagamento apenas pelos recursos que você usa, quando usa",
                    "Pagamento antecipado com desconto por volume",
                    "Pagamento baseado no número de usuários"
                ],
                "correct_answers": ["B"],
                "explanation": "O modelo 'pay-as-you-go' significa que você paga apenas pelos recursos que consome, quando os consome, sem contratos de longo prazo ou taxas antecipadas. Isso permite flexibilidade e otimização de custos baseada no uso real.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Cloud Concepts",
                "question_text": "Qual das seguintes opções melhor descreve a 'elasticidade' na computação em nuvem?",
                "question_type": "multiple_choice",
                "options": [
                    "A capacidade de mover aplicações entre diferentes provedores de nuvem",
                    "A capacidade de aumentar ou diminuir recursos automaticamente baseado na demanda",
                    "A capacidade de executar aplicações em múltiplas regiões simultaneamente", 
                    "A capacidade de fazer backup automático de dados"
                ],
                "correct_answers": ["B"],
                "explanation": "Elasticidade é a capacidade de escalar recursos (aumentar ou diminuir) automaticamente baseado na demanda atual. Isso permite otimizar custos e performance, provisionando recursos apenas quando necessário.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02", 
                "domain": "Technology",
                "question_text": "Uma empresa precisa de uma solução de CDN (Content Delivery Network) para melhorar a performance de seu website global. Qual serviço da AWS deve ser usado?",
                "question_type": "multiple_choice",
                "options": [
                    "Amazon Route 53",
                    "Amazon CloudFront",
                    "AWS Global Accelerator", 
                    "Amazon API Gateway"
                ],
                "correct_answers": ["B"],
                "explanation": "Amazon CloudFront é o serviço de CDN da AWS que distribui conteúdo globalmente através de edge locations, reduzindo latência e melhorando a experiência do usuário ao servir conteúdo do local mais próximo geograficamente.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Security and Compliance", 
                "question_text": "Qual serviço da AWS fornece auditoria e logging de chamadas de API para compliance e segurança?",
                "question_type": "multiple_choice",
                "options": [
                    "AWS CloudWatch",
                    "AWS CloudTrail",
                    "AWS Config",
                    "AWS Inspector"
                ],
                "correct_answers": ["B"],
                "explanation": "AWS CloudTrail registra todas as chamadas de API feitas na sua conta AWS, fornecendo logs detalhados para auditoria, compliance e análise de segurança. É essencial para rastrear quem fez o quê e quando na sua infraestrutura AWS.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Technology",
                "question_text": "Uma aplicação precisa executar código sem provisionar ou gerenciar servidores. Qual serviço da AWS seria mais apropriado?",
                "question_type": "multiple_choice",
                "options": [
                    "Amazon EC2",
                    "AWS Lambda", 
                    "Amazon ECS",
                    "AWS Batch"
                ],
                "correct_answers": ["B"],
                "explanation": "AWS Lambda é um serviço de computação serverless que executa código em resposta a eventos sem necessidade de provisionar ou gerenciar servidores. Você paga apenas pelo tempo de computação consumido.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Cloud Concepts",
                "question_text": "Qual das seguintes opções é um benefício da alta disponibilidade na AWS?",
                "question_type": "multiple_choice",
                "options": [
                    "Redução de custos operacionais",
                    "Minimização do tempo de inatividade do sistema",
                    "Aumento da velocidade de processamento",
                    "Simplificação da arquitetura de aplicações"
                ],
                "correct_answers": ["B"],
                "explanation": "Alta disponibilidade refere-se à capacidade de um sistema permanecer operacional por longos períodos, minimizando o tempo de inatividade. A AWS oferece múltiplas AZs e regiões para implementar arquiteturas altamente disponíveis.",
                "difficulty": "medium"
            }
        ])
        
        # Additional questions from generate_additional_questions.py
        questions.extend([
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
                "correct_answers": ["B"],
                "explanation": "Para websites estáticos, S3 oferece hospedagem de baixo custo, CloudFront melhora performance global via CDN, e Route 53 fornece DNS confiável. Esta é a solução mais econômica e eficiente.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Security and Compliance",
                "question_text": "Uma empresa precisa criptografar dados em trânsito e em repouso. Quais serviços AWS ajudam com isso?",
                "question_type": "multiple_response",
                "options": [
                    "AWS KMS (Key Management Service)",
                    "AWS CloudTrail",
                    "SSL/TLS certificates via ACM (Certificate Manager)",
                    "AWS Config",
                    "Amazon Inspector"
                ],
                "correct_answers": ["A", "C"],
                "explanation": "AWS KMS gerencia chaves de criptografia para dados em repouso, e ACM fornece certificados SSL/TLS para criptografia em trânsito. Ambos são essenciais para uma estratégia completa de criptografia.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Billing and Pricing",
                "question_text": "Uma empresa quer monitorar e controlar custos AWS proativamente. Quais ferramentas devem ser usadas?",
                "question_type": "multiple_response",
                "options": [
                    "AWS Budgets para alertas de custo",
                    "Cost Explorer para análise de tendências",
                    "AWS Pricing Calculator para estimativas",
                    "CloudWatch apenas para métricas técnicas",
                    "Trusted Advisor para recomendações de otimização"
                ],
                "correct_answers": ["A", "B", "E"],
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
                "correct_answers": ["B"],
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
                "correct_answers": ["B"],
                "explanation": "Amazon SQS é ideal para processamento assíncrono de mensagens, oferecendo durabilidade, escalabilidade e garantia de entrega. É o serviço padrão para desacoplar componentes de aplicações.",
                "difficulty": "easy"
            }
        ])
        
        # Additional questions from generate_300_questions.py pattern
        questions.extend([
            {
                "certification": "CLF-C02",
                "domain": "Cloud Concepts",
                "question_text": "Uma empresa está considerando os benefícios da migração para a AWS. Qual das seguintes opções NÃO é um benefício direto da computação em nuvem?",
                "question_type": "multiple_choice",
                "options": [
                    "Redução de gastos de capital (CapEx)",
                    "Aumento da agilidade e velocidade de inovação",
                    "Eliminação completa de todos os custos de TI",
                    "Capacidade de escalar globalmente em minutos"
                ],
                "correct_answers": ["C"],
                "explanation": "A computação em nuvem oferece muitos benefícios, mas não elimina completamente os custos de TI. Há custos operacionais (OpEx) contínuos baseados no uso dos recursos.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Technology",
                "question_text": "Uma startup precisa de uma solução de banco de dados que possa escalar automaticamente conforme o crescimento da aplicação. Qual serviço seria mais apropriado?",
                "question_type": "multiple_choice",
                "options": [
                    "Amazon RDS com Multi-AZ",
                    "Amazon DynamoDB",
                    "Amazon Redshift",
                    "Amazon DocumentDB"
                ],
                "correct_answers": ["B"],
                "explanation": "Amazon DynamoDB é um banco NoSQL totalmente gerenciado que escala automaticamente conforme a demanda, sendo ideal para aplicações com crescimento imprevisível.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Security and Compliance",
                "question_text": "Qual das seguintes práticas de segurança é fundamental para proteger dados em trânsito na AWS?",
                "question_type": "multiple_choice",
                "options": [
                    "Usar apenas HTTP para todas as comunicações",
                    "Implementar SSL/TLS para criptografia",
                    "Armazenar senhas em texto plano",
                    "Desabilitar logs de auditoria"
                ],
                "correct_answers": ["B"],
                "explanation": "SSL/TLS é fundamental para criptografar dados em trânsito, protegendo informações sensíveis durante a transmissão entre cliente e servidor.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Billing and Pricing",
                "question_text": "Uma empresa executa workloads de desenvolvimento que só funcionam durante horário comercial. Qual estratégia de custo seria mais eficiente?",
                "question_type": "multiple_choice",
                "options": [
                    "Reserved Instances para 3 anos",
                    "Dedicated Hosts 24/7",
                    "Scheduled Reserved Instances ou automação para start/stop",
                    "On-Demand Instances executando continuamente"
                ],
                "correct_answers": ["C"],
                "explanation": "Para workloads previsíveis com horários específicos, Scheduled Reserved Instances ou automação para iniciar/parar recursos oferece maior economia de custos.",
                "difficulty": "medium"
            }
        ])
        
        return questions
    
    def get_aif_c01_questions(self):
        """Generate AIF-C01 questions from all sources"""
        questions = []
        
        # Questions from generate_300_questions.py - 100 questions distributed across domains
        # Fundamentals of AI and ML (35 questions)
        for i in range(35):
            questions.append({
                "certification": "AIF-C01",
                "domain": "Fundamentals of AI and ML",
                "question_text": f"Questão AI Fundamentals {i+1}: Qual é a principal diferença entre {['supervised learning', 'unsupervised learning', 'reinforcement learning', 'deep learning', 'transfer learning'][i%5]} e outros tipos de aprendizado?",
                "question_type": "multiple_choice",
                "options": [
                    f"Usa {['dados rotulados', 'dados não rotulados', 'sistema de recompensas', 'redes neurais profundas', 'modelos pré-treinados'][i%5]} para treinamento",
                    f"Aplica {['algoritmos supervisionados', 'clustering e associação', 'trial and error', 'múltiplas camadas', 'conhecimento transferido'][i%5]} como metodologia",
                    f"Requer {['targets conhecidos', 'descoberta de padrões', 'ambiente interativo', 'grande volume de dados', 'domínio similar'][i%5]} como pré-requisito",
                    f"Produz {['predições precisas', 'insights ocultos', 'decisões otimizadas', 'representações complexas', 'adaptação rápida'][i%5]} como resultado"
                ],
                "correct_answers": ["A"],
                "explanation": f"A principal característica de {['supervised learning', 'unsupervised learning', 'reinforcement learning', 'deep learning', 'transfer learning'][i%5]} é o uso de {['dados rotulados', 'dados não rotulados', 'sistema de recompensas', 'redes neurais profundas', 'modelos pré-treinados'][i%5]}, diferenciando-o dos outros tipos de aprendizado.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # AI and ML Services on AWS (40 questions)
        for i in range(40):
            questions.append({
                "certification": "AIF-C01",
                "domain": "AI and ML Services on AWS",
                "question_text": f"Questão AWS AI Services {i+1}: Uma empresa precisa implementar {['reconhecimento de imagens', 'análise de sentimentos', 'extração de texto', 'tradução automática', 'síntese de voz', 'transcrição de áudio'][i%6]}. Qual serviço AWS é mais apropriado?",
                "question_type": "multiple_choice",
                "options": [
                    f"Amazon {['Rekognition', 'Comprehend', 'Textract', 'Translate', 'Polly', 'Transcribe'][i%6]}",
                    f"Amazon {['SageMaker', 'Lex', 'Personalize', 'Forecast', 'Kendra', 'CodeGuru'][i%6]}",
                    f"Amazon {['Bedrock', 'Q', 'Augmented AI', 'Lookout', 'Monitron', 'HealthLake'][i%6]}",
                    f"Amazon {['DeepLens', 'DeepRacer', 'Braket', 'Fraud Detector', 'DevOps Guru', 'Detective'][i%6]}"
                ],
                "correct_answers": ["A"],
                "explanation": f"Amazon {['Rekognition', 'Comprehend', 'Textract', 'Translate', 'Polly', 'Transcribe'][i%6]} é especificamente projetado para {['reconhecimento de imagens', 'análise de sentimentos', 'extração de texto', 'tradução automática', 'síntese de voz', 'transcrição de áudio'][i%6]}, oferecendo APIs prontas para uso.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # Responsible AI (25 questions)
        for i in range(25):
            questions.append({
                "certification": "AIF-C01",
                "domain": "Responsible AI",
                "question_text": f"Questão Responsible AI {i+1}: Como garantir {['transparência', 'fairness', 'accountability', 'privacy', 'explainability'][i%5]} em sistemas de AI?",
                "question_type": "multiple_choice",
                "options": [
                    f"Implementar {['documentação clara', 'algoritmos imparciais', 'auditoria contínua', 'proteção de dados', 'modelos interpretáveis'][i%5]}",
                    f"Estabelecer {['processos abertos', 'datasets balanceados', 'responsabilidades definidas', 'anonimização', 'explicações automáticas'][i%5]}",
                    f"Manter {['comunicação transparente', 'métricas de equidade', 'logs detalhados', 'consentimento informado', 'simplicidade de modelo'][i%5]}",
                    f"Garantir {['acesso público', 'representatividade', 'rastreabilidade', 'minimização de dados', 'interpretabilidade humana'][i%5]}"
                ],
                "correct_answers": [str(i%4)],
                "explanation": f"Para garantir {['transparência', 'fairness', 'accountability', 'privacy', 'explainability'][i%5]} em AI, é essencial implementar práticas que promovam confiança e responsabilidade no desenvolvimento e deployment de sistemas inteligentes.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # Additional questions from generate_additional_questions.py
        questions.extend([
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
                "correct_answers": ["A"],
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
                "correct_answers": ["B"],
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
                "correct_answers": ["B"],
                "explanation": "Amazon Textract usa OCR (Optical Character Recognition) e machine learning para extrair texto, tabelas e dados de documentos escaneados e PDFs com alta precisão.",
                "difficulty": "easy"
            }
        ])
        
        return questions
    
    def get_saa_c03_questions(self):
        """Generate SAA-C03 questions from all sources"""
        questions = []
        
        # Questions from generate_300_questions.py - 100 questions distributed across domains
        # Design Resilient Architectures (30 questions)
        for i in range(30):
            questions.append({
                "certification": "SAA-C03",
                "domain": "Design Resilient Architectures",
                "question_text": f"Questão Resilient Architecture {i+1}: Para garantir alta disponibilidade de {['aplicação web crítica', 'banco de dados transacional', 'API de pagamentos', 'sistema de autenticação'][i%4]}, qual arquitetura é mais apropriada?",
                "question_type": "multiple_choice",
                "options": [
                    f"Multi-AZ com {['Load Balancer', 'RDS Multi-AZ', 'API Gateway', 'Cognito Multi-Region'][i%4]}",
                    f"Single-AZ com {['Auto Scaling', 'Read Replicas', 'CloudFront', 'IAM Roles'][i%4]}",
                    f"Cross-Region com {['Route 53 Failover', 'Cross-Region Replication', 'Global Load Balancer', 'Global Tables'][i%4]}",
                    f"Hybrid com {['Direct Connect', 'Storage Gateway', 'VPN Backup', 'Directory Service'][i%4]}"
                ],
                "correct_answers": ["A"],
                "explanation": f"Para alta disponibilidade de {['aplicação web crítica', 'banco de dados transacional', 'API de pagamentos', 'sistema de autenticação'][i%4]}, arquitetura Multi-AZ com {['Load Balancer', 'RDS Multi-AZ', 'API Gateway', 'Cognito Multi-Region'][i%4]} oferece redundância automática.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # Design High-Performing Architectures (25 questions)
        for i in range(25):
            questions.append({
                "certification": "SAA-C03",
                "domain": "Design High-Performing Architectures",
                "question_text": f"Questão Performance {i+1}: Para otimizar performance de {['consultas de banco', 'entrega de conteúdo', 'processamento de dados', 'APIs REST'][i%4]}, qual solução é mais eficaz?",
                "question_type": "multiple_choice",
                "options": [
                    f"Implementar {['ElastiCache', 'CloudFront', 'EMR', 'API Gateway Caching'][i%4]}",
                    f"Usar {['Read Replicas', 'Edge Locations', 'Spark Clusters', 'Lambda@Edge'][i%4]}",
                    f"Configurar {['Connection Pooling', 'Origin Shield', 'Partitioning', 'Throttling'][i%4]}",
                    f"Aplicar {['Query Optimization', 'Compression', 'Parallel Processing', 'Response Caching'][i%4]}"
                ],
                "correct_answers": ["A"],
                "explanation": f"Para otimizar performance de {['consultas de banco', 'entrega de conteúdo', 'processamento de dados', 'APIs REST'][i%4]}, {['ElastiCache', 'CloudFront', 'EMR', 'API Gateway Caching'][i%4]} oferece a solução mais eficaz e direta.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # Design Secure Architectures (25 questions)
        for i in range(25):
            questions.append({
                "certification": "SAA-C03",
                "domain": "Design Secure Architectures",
                "question_text": f"Questão Security {i+1}: Para implementar segurança em {['VPC networking', 'data encryption', 'access control', 'application security'][i%4]}, qual abordagem é mais robusta?",
                "question_type": "multiple_choice",
                "options": [
                    f"Usar {['Security Groups + NACLs', 'KMS + CloudHSM', 'IAM Policies + Roles', 'WAF + Shield'][i%4]}",
                    f"Implementar {['Private Subnets', 'Encryption at Rest', 'MFA + SAML', 'API Rate Limiting'][i%4]}",
                    f"Configurar {['VPC Flow Logs', 'Encryption in Transit', 'Least Privilege', 'Input Validation'][i%4]}",
                    f"Aplicar {['Network Segmentation', 'Key Rotation', 'Zero Trust', 'Security Headers'][i%4]}"
                ],
                "correct_answers": ["A"],
                "explanation": f"Para segurança robusta em {['VPC networking', 'data encryption', 'access control', 'application security'][i%4]}, usar {['Security Groups + NACLs', 'KMS + CloudHSM', 'IAM Policies + Roles', 'WAF + Shield'][i%4]} fornece proteção em múltiplas camadas.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # Design Cost-Optimized Architectures (20 questions)
        for i in range(20):
            questions.append({
                "certification": "SAA-C03",
                "domain": "Design Cost-Optimized Architectures",
                "question_text": f"Questão Cost Optimization {i+1}: Para reduzir custos de {['compute workloads', 'storage solutions', 'data transfer', 'monitoring services'][i%4]}, qual estratégia oferece maior economia?",
                "question_type": "multiple_choice",
                "options": [
                    f"Usar {['Spot Instances', 'S3 Intelligent Tiering', 'VPC Endpoints', 'CloudWatch Logs Insights'][i%4]}",
                    f"Implementar {['Reserved Instances', 'Lifecycle Policies', 'CloudFront', 'Custom Metrics'][i%4]}",
                    f"Configurar {['Auto Scaling', 'Storage Classes', 'Direct Connect', 'Log Aggregation'][i%4]}",
                    f"Aplicar {['Right Sizing', 'Compression', 'Regional Optimization', 'Metric Filters'][i%4]}"
                ],
                "correct_answers": [str(i%4)],
                "explanation": f"Para otimização de custos em {['compute workloads', 'storage solutions', 'data transfer', 'monitoring services'][i%4]}, a estratégia escolhida deve considerar padrões de uso e características específicas da carga de trabalho.",
                "difficulty": ["easy", "medium", "hard"][i%3]
            })
        
        # Additional questions from generate_additional_questions.py
        questions.extend([
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
                "correct_answers": ["D"],
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
                "correct_answers": ["C"],
                "explanation": "Para analytics de grandes volumes com consultas ad-hoc, S3 para armazenamento, Athena para consultas SQL serverless e Glue para ETL formam a arquitetura mais eficiente e econômica.",
                "difficulty": "medium"
            }
        ])
        
        # Original questions from comprehensive questions
        questions.extend([
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
                "correct_answers": ["B"],
                "explanation": "Para alta disponibilidade, deve-se usar múltiplas AZs com load balancer. Isso garante que se uma AZ falhar, a aplicação continue funcionando nas outras AZs.",
                "difficulty": "medium"
            },
            {
                "certification": "SAA-C03",
                "domain": "Design High-Performing Architectures",
                "question_text": "Uma aplicação web tem picos de tráfego imprevisíveis. Qual estratégia de auto scaling seria mais eficiente?",
                "question_type": "multiple_choice",
                "options": [
                    "Scaling manual baseado em cronograma",
                    "Target tracking scaling baseado em CPU",
                    "Predictive scaling baseado em histórico",
                    "Scaling reativo baseado apenas em memória"
                ],
                "correct_answers": ["B"],
                "explanation": "Para tráfego imprevisível, target tracking scaling baseado em CPU é eficiente, pois ajusta automaticamente baseado na utilização real, mantendo a performance desejada.",
                "difficulty": "medium"
            },
            {
                "certification": "SAA-C03",
                "domain": "Design Secure Architectures",
                "question_text": "Uma empresa precisa implementar isolamento de rede para diferentes ambientes (dev, staging, prod). Qual abordagem seria mais eficaz?",
                "question_type": "multiple_choice",
                "options": [
                    "Usar diferentes subnets na mesma VPC",
                    "Implementar VPCs separadas para cada ambiente",
                    "Usar apenas Security Groups para isolamento",
                    "Implementar uma única VPC com diferentes IAM roles"
                ],
                "correct_answers": ["B"],
                "explanation": "VPCs separadas fornecem isolamento completo de rede entre ambientes, eliminando riscos de comunicação acidental entre dev, staging e produção.",
                "difficulty": "medium"
            },
            {
                "certification": "SAA-C03",
                "domain": "Design Cost-Optimized Architectures",
                "question_text": "Uma aplicação tem workloads que podem ser interrompidos e retomados sem perda de dados. Qual estratégia de instâncias seria mais econômica?",
                "question_type": "multiple_choice",
                "options": [
                    "On-Demand Instances exclusivamente",
                    "Reserved Instances para toda a carga",
                    "Spot Instances com estratégias de recuperação",
                    "Dedicated Hosts para controle total"
                ],
                "correct_answers": ["C"],
                "explanation": "Spot Instances podem oferecer até 90% de desconto para workloads fault-tolerant. Com estratégias adequadas de recuperação, são ideais para processamento que pode ser interrompido.",
                "difficulty": "medium"
            },
            {
                "certification": "SAA-C03",
                "domain": "Design Resilient Architectures",
                "question_text": "Uma empresa precisa implementar backup e recuperação de dados com RTO de 4 horas e RPO de 1 hora. Qual estratégia seria apropriada?",
                "question_type": "multiple_choice",
                "options": [
                    "Backup diário para S3 Glacier",
                    "Snapshots automatizados a cada hora com restore procedures",
                    "Replicação síncrona para outra região",
                    "Backup manual semanal"
                ],
                "correct_answers": ["B"],
                "explanation": "Snapshots automatizados a cada hora garantem RPO de 1 hora, e procedures de restore bem definidos podem atender RTO de 4 horas.",
                "difficulty": "hard"
            }
        ])
        
        return questions
    
    def get_sap_c02_questions(self):
        """Generate SAP-C02 questions from all sources"""
        questions = []
        
        # Additional questions from generate_additional_questions.py
        questions.extend([
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
                "correct_answers": ["B"],
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
                "correct_answers": ["B"],
                "explanation": "Para alta throughput e baixa latência em IoT, Kinesis Data Streams ingere dados em tempo real, Kinesis Analytics processa streams, e ElastiCache fornece acesso de baixa latência.",
                "difficulty": "hard"
            }
        ])
        
        # Original questions from comprehensive questions
        questions.extend([
            {
                "certification": "SAP-C02",
                "domain": "Design Solutions for Organizational Complexity",
                "question_text": "Uma empresa multinacional precisa implementar governança de custos em múltiplas contas AWS. Qual abordagem seria mais eficaz?",
                "question_type": "multiple_choice",
                "options": [
                    "Usar uma única conta AWS com tags detalhadas",
                    "Implementar AWS Organizations com políticas de billing",
                    "Gerenciar cada conta independentemente",
                    "Usar apenas Reserved Instances para controle de custos"
                ],
                "correct_answers": ["B"],
                "explanation": "AWS Organizations permite gerenciamento centralizado de múltiplas contas, com políticas de billing, consolidated billing e governança centralizada.",
                "difficulty": "medium"
            },
            {
                "certification": "SAP-C02",
                "domain": "Design for New Solutions",
                "question_text": "Uma aplicação requer processamento de dados em tempo real com latência sub-milissegundo. Qual arquitetura seria mais apropriada?",
                "question_type": "multiple_choice",
                "options": [
                    "Lambda functions com SQS",
                    "EC2 instances com ElastiCache Redis",
                    "Kinesis Data Streams com Lambda",
                    "RDS com read replicas"
                ],
                "correct_answers": ["B"],
                "explanation": "EC2 instances com ElastiCache Redis podem fornecer latência sub-milissegundo para processamento em tempo real, com controle total sobre a performance.",
                "difficulty": "hard"
            },
            {
                "certification": "SAP-C02",
                "domain": "Migration Planning",
                "question_text": "Uma empresa precisa migrar 500 aplicações legacy para AWS com mínimo downtime. Qual estratégia seria mais eficaz?",
                "question_type": "multiple_choice",
                "options": [
                    "Big bang migration em um fim de semana",
                    "Migração faseada com AWS Application Migration Service",
                    "Reconstruir todas as aplicações do zero",
                    "Manter tudo on-premises"
                ],
                "correct_answers": ["B"],
                "explanation": "Migração faseada com AWS Application Migration Service permite migração com mínimo downtime, testando cada workload antes da cutover final, reduzindo riscos.",
                "difficulty": "medium"
            },
            {
                "certification": "SAP-C02",
                "domain": "Cost Control",
                "question_text": "Uma empresa tem custos AWS crescendo rapidamente e precisa implementar governança financeira. Quais estratégias devem ser implementadas?",
                "question_type": "multiple_response",
                "options": [
                    "Implementar AWS Budgets com alertas automáticos",
                    "Usar Cost Allocation Tags para rastreamento detalhado",
                    "Implementar políticas de auto-shutdown para recursos não utilizados",
                    "Migrar tudo para instâncias mais caras para garantir performance",
                    "Ignorar custos de desenvolvimento e focar apenas em produção"
                ],
                "correct_answers": ["A", "B", "C"],
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
                "correct_answers": ["B"],
                "explanation": "Modernização com microserviços permite escalabilidade independente, melhor manutenibilidade e uso de serviços gerenciados AWS, resolvendo problemas de arquiteturas monolíticas.",
                "difficulty": "hard"
            }
        ])
        
        return questions
    
    def get_sample_questions(self):
        """Get sample questions from populate_questions.py and init_db.py"""
        return [
            {
                "certification": "CLF-C02",
                "domain": "Billing, Pricing, and Support",
                "question_text": "A company plans to use an Amazon Snowball Edge device to transfer files to the AWS Cloud. Which activities related to a Snowball Edge device are available to the company at no cost?",
                "question_type": "multiple_choice",
                "options": [
                    "Use of the Snowball Edge appliance for a 10-day period",
                    "The transfer of data out of Amazon S3 and to the Snowball Edge appliance",
                    "The transfer of data from the Snowball Edge appliance into Amazon S3",
                    "Daily use of the Snowball Edge appliance after 10 days"
                ],
                "correct_answers": ["C"],
                "explanation": "A transferência de dados do dispositivo Snowball Edge para o Amazon S3 é gratuita. Você paga apenas pelo dispositivo e pelo transporte, mas não pela transferência de dados para dentro da AWS.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Security and Compliance",
                "question_text": "A company has deployed applications on Amazon EC2 instances. The company needs to assess application vulnerabilities and must identify infrastructure deployments that do not meet best practices. Which AWS service can the company use to meet these requirements?",
                "question_type": "multiple_choice",
                "options": [
                    "AWS Trusted Advisor",
                    "Amazon Inspector",
                    "AWS Config",
                    "Amazon GuardDuty"
                ],
                "correct_answers": ["B"],
                "explanation": "Amazon Inspector é um serviço de avaliação de segurança automatizada que ajuda a melhorar a segurança e conformidade de aplicações implantadas na AWS. Ele avalia automaticamente aplicações quanto a vulnerabilidades ou desvios das melhores práticas.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Cloud Technology and Services",
                "question_text": "A company has a centralized group of users with large file storage requirements that have exceeded the space available on premises. The company wants to extend its file storage capabilities for this group while retaining the performance benefit of sharing content locally. What is the MOST operationally efficient AWS solution for this scenario?",
                "question_type": "multiple_choice",
                "options": [
                    "Create an Amazon S3 bucket for each user. Mount each bucket by using an S3 file system mounting utility.",
                    "Configure and deploy an AWS Storage Gateway file gateway. Connect each user's workstation to the file gateway.",
                    "Move each user's working environment to Amazon WorkSpaces. Set up an Amazon WorkDocs account for each user.",
                    "Deploy an Amazon EC2 instance and attach an Amazon Elastic Block Store (Amazon EBS) Provisioned IOPS volume. Share the EBS volume directly with the users."
                ],
                "correct_answers": ["B"],
                "explanation": "AWS Storage Gateway file gateway permite que você armazene arquivos como objetos no Amazon S3, enquanto mantém acesso local através de protocolos de arquivo padrão (NFS/SMB). Isso fornece a extensão de armazenamento necessária mantendo o desempenho local.",
                "difficulty": "hard"
            },
            {
                "certification": "CLF-C02",
                "domain": "Security and Compliance",
                "question_text": "According to security best practices, how should an Amazon EC2 instance be given access to an Amazon S3 bucket?",
                "question_type": "multiple_choice",
                "options": [
                    "Hard code an IAM user's secret key and access key directly in the application, and upload the file.",
                    "Store the IAM user's secret key and access key in a text file on the EC2 instance, read the keys, then upload the file.",
                    "Have the EC2 instance assume a role to obtain the privileges to upload the file.",
                    "Modify the S3 bucket policy so that any service can upload to it at any time."
                ],
                "correct_answers": ["C"],
                "explanation": "A melhor prática de segurança é usar IAM roles para instâncias EC2. Isso elimina a necessidade de armazenar credenciais de longo prazo na instância e fornece credenciais temporárias automaticamente rotacionadas.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Cloud Concepts",
                "question_text": "Which option is a customer responsibility when using Amazon DynamoDB under the AWS Shared Responsibility Model?",
                "question_type": "multiple_choice",
                "options": [
                    "Physical security of DynamoDB",
                    "Patching of DynamoDB",
                    "Access to DynamoDB tables",
                    "Encryption of data at rest in DynamoDB"
                ],
                "correct_answers": ["C"],
                "explanation": "No modelo de responsabilidade compartilhada, o cliente é responsável pelo controle de acesso aos recursos, incluindo tabelas do DynamoDB. A AWS é responsável pela segurança física, patches e criptografia da infraestrutura.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Cloud Concepts",
                "question_text": "Which option is a perspective that includes foundational capabilities of the AWS Cloud Adoption Framework (AWS CAF)?",
                "question_type": "multiple_choice",
                "options": [
                    "Sustainability",
                    "Performance efficiency",
                    "Governance",
                    "Reliability"
                ],
                "correct_answers": ["C"],
                "explanation": "Governance é uma das seis perspectivas fundamentais do AWS CAF. As perspectivas são: Business, People, Governance, Platform, Security e Operations.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Cloud Technology and Services",
                "question_text": "A company is running and managing its own Docker environment on Amazon EC2 instances. The company wants an alternative to help manage cluster size, scheduling, and environment maintenance. Which AWS service meets these requirements?",
                "question_type": "multiple_choice",
                "options": [
                    "AWS Lambda",
                    "Amazon RDS",
                    "AWS Fargate",
                    "Amazon Athena"
                ],
                "correct_answers": ["C"],
                "explanation": "AWS Fargate é um mecanismo de computação serverless para containers que funciona com Amazon ECS e EKS. Ele remove a necessidade de gerenciar servidores, permitindo que você se concentre no design e construção de suas aplicações.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Cloud Concepts",
                "question_text": "A company wants to run a NoSQL database on Amazon EC2 instances. Which task is the responsibility of AWS in this scenario?",
                "question_type": "multiple_choice",
                "options": [
                    "Update the guest operating system of the EC2 instances.",
                    "Maintain high availability at the database layer.",
                    "Patch the physical infrastructure that hosts the EC2 instances.",
                    "Configure the security group firewall."
                ],
                "correct_answers": ["C"],
                "explanation": "No modelo de responsabilidade compartilhada, a AWS é responsável pela infraestrutura física, incluindo patches do hardware e hypervisor. O cliente é responsável pelo sistema operacional guest, aplicações e configurações.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Billing, Pricing, and Support",
                "question_text": "Which AWS services or tools can identify rightsizing opportunities for Amazon EC2 instances?",
                "question_type": "multiple_response",
                "options": [
                    "AWS Cost Explorer",
                    "AWS Billing Conductor",
                    "Amazon CodeGuru",
                    "Amazon SageMaker",
                    "AWS Compute Optimizer"
                ],
                "correct_answers": ["A", "E"],
                "explanation": "AWS Cost Explorer e AWS Compute Optimizer podem identificar oportunidades de rightsizing. O Cost Explorer fornece recomendações de rightsizing baseadas em uso histórico, enquanto o Compute Optimizer usa machine learning para analisar métricas e recomendar recursos otimais.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Security and Compliance",
                "question_text": "Which of the following are benefits of using AWS Trusted Advisor?",
                "question_type": "multiple_response",
                "options": [
                    "Providing high-performance container orchestration",
                    "Creating and rotating encryption keys",
                    "Detecting underutilized resources to save costs",
                    "Improving security by proactively monitoring the AWS environment",
                    "Implementing enforced tagging across AWS resources"
                ],
                "correct_answers": ["C", "D"],
                "explanation": "AWS Trusted Advisor fornece recomendações em cinco categorias: otimização de custos, performance, segurança, tolerância a falhas e limites de serviço. Ele detecta recursos subutilizados para economia de custos e monitora proativamente o ambiente para melhorar a segurança.",
                "difficulty": "medium"
            },
            {
                "certification": "CLF-C02",
                "domain": "Cloud Concepts",
                "question_text": "Qual é o principal benefício da computação em nuvem?",
                "question_type": "multiple_choice",
                "options": [
                    "Redução de custos operacionais",
                    "Escalabilidade sob demanda",
                    "Segurança aprimorada",
                    "Backup automático"
                ],
                "correct_answers": ["B"],
                "explanation": "A escalabilidade sob demanda permite ajustar recursos conforme necessário, otimizando custos e performance.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Security and Compliance",
                "question_text": "Qual serviço AWS é usado para gerenciar identidades e acessos?",
                "question_type": "multiple_choice",
                "options": [
                    "Amazon S3",
                    "AWS IAM",
                    "Amazon EC2",
                    "AWS CloudTrail"
                ],
                "correct_answers": ["B"],
                "explanation": "AWS IAM (Identity and Access Management) é o serviço responsável por gerenciar usuários, grupos e permissões na AWS.",
                "difficulty": "easy"
            },
            {
                "certification": "CLF-C02",
                "domain": "Technology",
                "question_text": "Qual serviço AWS oferece armazenamento de objetos?",
                "question_type": "multiple_choice",
                "options": [
                    "Amazon EBS",
                    "Amazon S3",
                    "Amazon RDS",
                    "Amazon EC2"
                ],
                "correct_answers": ["B"],
                "explanation": "Amazon S3 (Simple Storage Service) é o serviço de armazenamento de objetos da AWS, oferecendo alta durabilidade e disponibilidade.",
                "difficulty": "easy"
            }
        ]
    
    def get_additional_questions(self):
        """Get additional practical questions"""
        return [
            {
                "certification": "CLF-C02",
                "domain": "Technology",
                "question_text": "Uma empresa precisa executar uma aplicação web que requer alta disponibilidade e escalabilidade automática. Qual combinação de serviços AWS seria mais apropriada?",
                "question_type": "multiple_choice",
                "options": [
                    "EC2 + Auto Scaling Group + Application Load Balancer",
                    "Lambda + API Gateway + DynamoDB",
                    "S3 + CloudFront + Route 53",
                    "RDS + ElastiCache + CloudWatch"
                ],
                "correct_answers": ["A"],
                "explanation": "EC2 com Auto Scaling Group e Application Load Balancer fornece alta disponibilidade e escalabilidade automática para aplicações web tradicionais.",
                "difficulty": "medium"
            },
            {
                "certification": "SAA-C03",
                "domain": "Design Resilient Architectures",
                "question_text": "Uma aplicação crítica precisa de um RTO (Recovery Time Objective) de 15 minutos e RPO (Recovery Point Objective) de 5 minutos. Qual estratégia de DR seria mais apropriada?",
                "question_type": "multiple_choice",
                "options": [
                    "Backup and restore com snapshots diários",
                    "Pilot light com dados replicados",
                    "Warm standby com instâncias em standby",
                    "Multi-site ativo/ativo"
                ],
                "correct_answers": ["C"],
                "explanation": "Warm standby com instâncias em standby pode atender RTO de 15 minutos, e replicação frequente pode garantir RPO de 5 minutos.",
                "difficulty": "hard"
            },
            {
                "certification": "AIF-C01",
                "domain": "AI and ML Services on AWS",
                "question_text": "Uma empresa quer implementar análise de sentimentos em tempo real para comentários de clientes. Qual combinação de serviços AWS seria mais eficaz?",
                "question_type": "multiple_choice",
                "options": [
                    "Kinesis Data Streams + Lambda + Comprehend",
                    "SQS + EC2 + Rekognition",
                    "S3 + Glue + SageMaker",
                    "API Gateway + Lambda + Translate"
                ],
                "correct_answers": ["A"],
                "explanation": "Kinesis para streaming de dados, Lambda para processamento e Comprehend para análise de sentimentos fornecem uma solução completa em tempo real.",
                "difficulty": "medium"
            }
        ]
    
    def normalize_answers(self, answers):
        """Normalize answers to ensure consistency"""
        if isinstance(answers, list):
            return answers
        elif isinstance(answers, str):
            return [answers]
        else:
            return [str(answers)]
    
    def add_questions_to_db(self, questions):
        """Add questions to database with duplicate checking"""
        for q_data in questions:
            try:
                # Check if question already exists
                existing = Question.query.filter_by(
                    certification=q_data["certification"],
                    question_text=q_data["question_text"]
                ).first()
                
                if not existing:
                    # Normalize correct_answers format
                    correct_answers = self.normalize_answers(q_data["correct_answers"])
                    
                    question = Question(
                        certification=q_data["certification"],
                        domain=q_data["domain"],
                        question_text=q_data["question_text"],
                        question_type=q_data["question_type"],
                        options=json.dumps(q_data["options"]),
                        correct_answers=json.dumps(correct_answers),
                        explanation=q_data["explanation"],
                        difficulty=q_data["difficulty"]
                    )
                    db.session.add(question)
                    self.added_count += 1
                    self.verbose_log(f"Added [{q_data['certification']}]: {q_data['question_text'][:60]}...")
                else:
                    self.existing_count += 1
                    self.verbose_log(f"Exists [{q_data['certification']}]: {q_data['question_text'][:60]}...")
                    
            except Exception as e:
                self.error_count += 1
                self.log(f"Error adding question: {str(e)}", "ERROR")
                continue
    
    def seed_database(self, target_cert=None, reset=False):
        """Main seeding function"""
        with app.app_context():
            # Create tables if they don't exist
            db.create_all()
            self.log("Database tables created/verified")
            
            # Reset database if requested
            if reset:
                self.log("Resetting database...")
                Question.query.delete()
                SimulationSession.query.delete()
                db.session.commit()
                self.log("Database reset completed")
            
            # Collect all questions
            all_questions = []
            
            if not target_cert or target_cert == "CLF-C02":
                self.log("Collecting CLF-C02 questions...")
                all_questions.extend(self.get_clf_c02_questions())
                all_questions.extend(self.get_sample_questions())
                all_questions.extend([q for q in self.get_additional_questions() if q["certification"] == "CLF-C02"])
            
            if not target_cert or target_cert == "AIF-C01":
                self.log("Collecting AIF-C01 questions...")
                all_questions.extend(self.get_aif_c01_questions())
                all_questions.extend([q for q in self.get_additional_questions() if q["certification"] == "AIF-C01"])
            
            if not target_cert or target_cert == "SAA-C03":
                self.log("Collecting SAA-C03 questions...")
                all_questions.extend(self.get_saa_c03_questions())
                all_questions.extend([q for q in self.get_additional_questions() if q["certification"] == "SAA-C03"])
            
            if not target_cert or target_cert == "SAP-C02":
                self.log("Collecting SAP-C02 questions...")
                all_questions.extend(self.get_sap_c02_questions())
            
            self.log(f"Total questions collected: {len(all_questions)}")
            
            # Add questions to database
            self.log("Adding questions to database...")
            self.add_questions_to_db(all_questions)
            
            # Commit changes
            db.session.commit()
            self.log("Database changes committed")
            
            # Print statistics
            self.print_statistics()
    
    def print_statistics(self):
        """Print final statistics"""
        print(f"\n{'='*80}")
        print(f"🚀 DATABASE SEEDING COMPLETED!")
        print(f"{'='*80}")
        print(f"📊 Questions added: {self.added_count}")
        print(f"📊 Questions already existing: {self.existing_count}")
        print(f"📊 Errors encountered: {self.error_count}")
        print(f"📊 Total processed: {self.added_count + self.existing_count + self.error_count}")
        
        # Count by certification
        print(f"\n{'='*80}")
        print(f"📈 QUESTIONS BY CERTIFICATION:")
        print(f"{'='*80}")
        
        for cert in ['CLF-C02', 'AIF-C01', 'SAA-C03', 'SAP-C02']:
            count = Question.query.filter_by(certification=cert).count()
            print(f"📊 {cert}: {count} questions")
        
        total_questions = Question.query.count()
        print(f"📊 TOTAL IN DATABASE: {total_questions} questions")
        
        print(f"\n{'='*80}")
        print(f"✅ SUCCESS: Database seeding completed successfully!")
        print(f"{'='*80}")

def main():
    """Main function with command line argument parsing"""
    parser = argparse.ArgumentParser(
        description="Unified Database Seeding Script for AWS Simulados",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python unified_seed_database.py                    # Seed all certifications
    python unified_seed_database.py --cert CLF-C02     # Seed only CLF-C02
    python unified_seed_database.py --reset            # Clear DB and seed all
    python unified_seed_database.py --verbose          # Enable verbose output
        """
    )
    
    parser.add_argument(
        '--cert', 
        choices=['CLF-C02', 'AIF-C01', 'SAA-C03', 'SAP-C02'],
        help='Seed only specific certification'
    )
    
    parser.add_argument(
        '--reset',
        action='store_true',
        help='Clear existing questions before seeding'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Create seeder instance
    seeder = UnifiedDatabaseSeeder(verbose=args.verbose)
    
    # Welcome message
    print(f"{'='*80}")
    print(f"🚀 AWS SIMULADOS - UNIFIED DATABASE SEEDER")
    print(f"{'='*80}")
    print(f"📅 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if args.cert:
        print(f"🎯 Target certification: {args.cert}")
    else:
        print(f"🎯 Target: ALL certifications")
    
    if args.reset:
        print(f"⚠️  Reset mode: ENABLED (will clear existing questions)")
    
    if args.verbose:
        print(f"🔍 Verbose mode: ENABLED")
    
    print(f"{'='*80}")
    
    # Run seeding
    try:
        seeder.seed_database(target_cert=args.cert, reset=args.reset)
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
