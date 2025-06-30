#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

# Configuração da aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'src', 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do banco
db = SQLAlchemy(app)

# Modelo Question
class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    certification = db.Column(db.String(50), nullable=False)
    domain = db.Column(db.String(100), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(20), nullable=False)
    options = db.Column(db.Text, nullable=False)
    correct_answers = db.Column(db.Text, nullable=False)
    explanation = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(20), default='medium')

def add_clf_questions():
    """Adiciona mais questões CLF-C02 baseadas no formato real"""
    
    questions = [
        # Domínio 1: Cloud Concepts (26% - ~17 questões)
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Concepts',
            'question_text': 'Which of the following are benefits of cloud computing? (Choose two.)',
            'question_type': 'multiple_response',
            'options': [
                'Increased speed and agility',
                'Elimination of all security risks',
                'Variable expense instead of capital expense',
                'Guaranteed 100% uptime',
                'Requirement for extensive hardware knowledge'
            ],
            'correct_answers': [0, 2],
            'explanation': 'Os principais benefícios da computação em nuvem incluem maior velocidade e agilidade (deploy rápido de recursos) e modelo de despesas variáveis em vez de despesas de capital (pague apenas pelo que usar).',
            'difficulty': 'easy'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Concepts',
            'question_text': 'What is the AWS Well-Architected Framework?',
            'question_type': 'multiple_choice',
            'options': [
                'A set of questions to review architectures',
                'A certification program for AWS architects',
                'A tool for automated infrastructure deployment',
                'A pricing calculator for AWS services'
            ],
            'correct_answers': [0],
            'explanation': 'O AWS Well-Architected Framework é um conjunto de perguntas e melhores práticas para revisar e melhorar arquiteturas na nuvem, baseado em cinco pilares: excelência operacional, segurança, confiabilidade, eficiência de performance e otimização de custos.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Concepts',
            'question_text': 'Which AWS service provides a hybrid cloud storage solution?',
            'question_type': 'multiple_choice',
            'options': [
                'Amazon EBS',
                'Amazon S3',
                'AWS Storage Gateway',
                'Amazon EFS'
            ],
            'correct_answers': [2],
            'explanation': 'AWS Storage Gateway é um serviço de armazenamento híbrido que conecta ambientes on-premises à nuvem AWS, permitindo integração perfeita entre infraestrutura local e serviços de armazenamento da AWS.',
            'difficulty': 'medium'
        },
        
        # Domínio 2: Security and Compliance (25% - ~16 questões)
        {
            'certification': 'CLF-C02',
            'domain': 'Security and Compliance',
            'question_text': 'Which AWS service helps protect against DDoS attacks?',
            'question_type': 'multiple_choice',
            'options': [
                'AWS WAF',
                'AWS Shield',
                'Amazon GuardDuty',
                'AWS Config'
            ],
            'correct_answers': [1],
            'explanation': 'AWS Shield é um serviço gerenciado de proteção contra DDoS que protege aplicações executadas na AWS. O Shield Standard é gratuito e fornece proteção contra ataques DDoS mais comuns.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Security and Compliance',
            'question_text': 'What is the principle of least privilege in AWS IAM?',
            'question_type': 'multiple_choice',
            'options': [
                'Users should have maximum permissions for flexibility',
                'Users should have only the minimum permissions necessary to perform their job',
                'All users should share the same permissions',
                'Permissions should be granted permanently'
            ],
            'correct_answers': [1],
            'explanation': 'O princípio do menor privilégio significa conceder apenas as permissões mínimas necessárias para que um usuário ou serviço execute suas funções. Isso reduz o risco de segurança limitando o acesso desnecessário.',
            'difficulty': 'easy'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Security and Compliance',
            'question_text': 'Which AWS service provides centralized logging for security analysis?',
            'question_type': 'multiple_choice',
            'options': [
                'Amazon CloudWatch',
                'AWS CloudTrail',
                'AWS Config',
                'Amazon Inspector'
            ],
            'correct_answers': [1],
            'explanation': 'AWS CloudTrail fornece logs centralizados de todas as chamadas de API feitas na conta AWS, essencial para auditoria de segurança, conformidade e análise de atividades suspeitas.',
            'difficulty': 'medium'
        },
        
        # Domínio 3: Cloud Technology and Services (33% - ~21 questões)
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Technology and Services',
            'question_text': 'Which Amazon EC2 instance type is optimized for compute-intensive applications?',
            'question_type': 'multiple_choice',
            'options': [
                'Memory optimized (R5)',
                'Compute optimized (C5)',
                'Storage optimized (I3)',
                'General purpose (T3)'
            ],
            'correct_answers': [1],
            'explanation': 'Instâncias compute optimized (família C) são projetadas para aplicações que se beneficiam de processadores de alta performance, como computação científica, modelagem e análise de dados.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Technology and Services',
            'question_text': 'What is Amazon RDS?',
            'question_type': 'multiple_choice',
            'options': [
                'A NoSQL database service',
                'A relational database service',
                'A data warehouse service',
                'A file storage service'
            ],
            'correct_answers': [1],
            'explanation': 'Amazon RDS (Relational Database Service) é um serviço gerenciado que facilita a configuração, operação e escalabilidade de bancos de dados relacionais na nuvem, suportando MySQL, PostgreSQL, Oracle, SQL Server e outros.',
            'difficulty': 'easy'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Technology and Services',
            'question_text': 'Which AWS service is used for content delivery and caching?',
            'question_type': 'multiple_choice',
            'options': [
                'Amazon S3',
                'Amazon CloudFront',
                'Amazon Route 53',
                'AWS Direct Connect'
            ],
            'correct_answers': [1],
            'explanation': 'Amazon CloudFront é um serviço de rede de entrega de conteúdo (CDN) que entrega dados, vídeos, aplicações e APIs para clientes globalmente com baixa latência e altas velocidades de transferência.',
            'difficulty': 'easy'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Technology and Services',
            'question_text': 'What is the difference between Amazon S3 and Amazon EBS?',
            'question_type': 'multiple_choice',
            'options': [
                'S3 is object storage, EBS is block storage',
                'S3 is block storage, EBS is object storage',
                'Both are the same type of storage',
                'S3 is only for backup, EBS is for active data'
            ],
            'correct_answers': [0],
            'explanation': 'Amazon S3 é um serviço de armazenamento de objetos para dados não estruturados, enquanto Amazon EBS fornece armazenamento de blocos persistente para instâncias EC2, similar a um disco rígido virtual.',
            'difficulty': 'medium'
        },
        
        # Domínio 4: Billing, Pricing, and Support (16% - ~11 questões)
        {
            'certification': 'CLF-C02',
            'domain': 'Billing, Pricing, and Support',
            'question_text': 'Which AWS support plan provides 24/7 access to Cloud Support Engineers?',
            'question_type': 'multiple_choice',
            'options': [
                'Basic',
                'Developer',
                'Business',
                'Enterprise'
            ],
            'correct_answers': [2],
            'explanation': 'O plano Business Support fornece acesso 24/7 aos Cloud Support Engineers via telefone, chat e email. Os planos Basic e Developer têm suporte limitado, enquanto Enterprise oferece recursos adicionais.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Billing, Pricing, and Support',
            'question_text': 'What is AWS Free Tier?',
            'question_type': 'multiple_choice',
            'options': [
                'A permanent free service for all AWS resources',
                'A 12-month free trial for new AWS customers',
                'Free usage limits for certain AWS services',
                'A discount program for enterprise customers'
            ],
            'correct_answers': [2],
            'explanation': 'AWS Free Tier oferece limites de uso gratuito para determinados serviços AWS, incluindo ofertas sempre gratuitas, 12 meses gratuitos para novos clientes e testes gratuitos de curto prazo.',
            'difficulty': 'easy'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Billing, Pricing, and Support',
            'question_text': 'Which tool helps estimate AWS costs before deployment?',
            'question_type': 'multiple_choice',
            'options': [
                'AWS Cost Explorer',
                'AWS Pricing Calculator',
                'AWS Budgets',
                'AWS Cost and Usage Report'
            ],
            'correct_answers': [1],
            'explanation': 'AWS Pricing Calculator permite estimar custos de serviços AWS antes da implantação, ajudando no planejamento orçamentário e comparação de diferentes configurações.',
            'difficulty': 'easy'
        }
    ]
    
    with app.app_context():
        for q_data in questions:
            # Verifica se a questão já existe
            existing = Question.query.filter_by(
                certification=q_data['certification'],
                question_text=q_data['question_text']
            ).first()
            
            if not existing:
                question = Question(
                    certification=q_data['certification'],
                    domain=q_data['domain'],
                    question_text=q_data['question_text'],
                    question_type=q_data['question_type'],
                    options=json.dumps(q_data['options']),
                    correct_answers=json.dumps(q_data['correct_answers']),
                    explanation=q_data['explanation'],
                    difficulty=q_data['difficulty']
                )
                db.session.add(question)
        
        db.session.commit()
        print(f"Adicionadas {len(questions)} novas questões CLF-C02")

if __name__ == '__main__':
    print("Adicionando mais questões CLF-C02...")
    add_clf_questions()
    
    # Verifica total de questões
    with app.app_context():
        total = Question.query.filter_by(certification='CLF-C02').count()
        print(f"Total de questões CLF-C02 no banco: {total}")
    
    print("Questões adicionadas com sucesso!")

