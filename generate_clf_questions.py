#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from src.models.user import db
from src.models.question import Question
from src.main import app
import json

def create_clf_questions():
    """Cria questões detalhadas para CLF-C02"""
    
    questions = [
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
            "correct_answer": "C",
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
            "correct_answer": "A",
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
            "correct_answer": "B",
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
            "correct_answer": "C", 
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
            "correct_answer": "B",
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
            "correct_answer": "C",
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
            "correct_answer": "C",
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
            "correct_answer": "B",
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
            "correct_answer": "C",
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
            "correct_answer": "B", 
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
            "correct_answer": "B",
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
            "correct_answer": "B",
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
            "correct_answer": "B",
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
            "correct_answer": "B",
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
            "correct_answer": "B",
            "explanation": "Alta disponibilidade refere-se à capacidade de um sistema permanecer operacional por longos períodos, minimizando o tempo de inatividade. A AWS oferece múltiplas AZs e regiões para implementar arquiteturas altamente disponíveis.",
            "difficulty": "medium"
        }
    ]
    
    return questions

def main():
    with app.app_context():
        # Criar tabelas se não existirem
        db.create_all()
        
        # Gerar questões CLF-C02
        questions = create_clf_questions()
        
        print(f"Adicionando {len(questions)} questões CLF-C02...")
        
        for q_data in questions:
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
                    correct_answers=json.dumps([q_data["correct_answer"]]),  # Lista para compatibilidade
                    explanation=q_data["explanation"],
                    difficulty=q_data["difficulty"]
                )
                db.session.add(question)
                print(f"✓ Adicionada: {q_data['question_text'][:50]}...")
            else:
                print(f"- Já existe: {q_data['question_text'][:50]}...")
        
        db.session.commit()
        print(f"\n✅ Processo concluído! Total de questões CLF-C02 no banco: {Question.query.filter_by(certification='CLF-C02').count()}")

if __name__ == "__main__":
    main()

