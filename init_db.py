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

# Modelo SimulationSession
class SimulationSession(db.Model):
    __tablename__ = 'simulation_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    certification = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(100), nullable=True)
    total_questions = db.Column(db.Integer, nullable=False)
    correct_answers = db.Column(db.Integer, default=0)
    score = db.Column(db.Float, default=0.0)
    time_taken = db.Column(db.Integer, nullable=True)
    started_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    completed_at = db.Column(db.DateTime, nullable=True)
    questions_data = db.Column(db.Text, nullable=False)

def create_tables():
    """Cria as tabelas do banco de dados"""
    with app.app_context():
        db.create_all()
        print("Tabelas criadas com sucesso!")

def populate_questions():
    """Popula o banco com questões de exemplo"""
    questions_data = [
        {
            'certification': 'CLF-C02',
            'domain': 'Billing, Pricing, and Support',
            'question_text': 'A company plans to use an Amazon Snowball Edge device to transfer files to the AWS Cloud. Which activities related to a Snowball Edge device are available to the company at no cost?',
            'question_type': 'multiple_choice',
            'options': [
                'Use of the Snowball Edge appliance for a 10-day period',
                'The transfer of data out of Amazon S3 and to the Snowball Edge appliance',
                'The transfer of data from the Snowball Edge appliance into Amazon S3',
                'Daily use of the Snowball Edge appliance after 10 days'
            ],
            'correct_answers': [2],
            'explanation': 'A transferência de dados do dispositivo Snowball Edge para o Amazon S3 é gratuita. Você paga apenas pelo dispositivo e pelo transporte, mas não pela transferência de dados para dentro da AWS.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Security and Compliance',
            'question_text': 'A company has deployed applications on Amazon EC2 instances. The company needs to assess application vulnerabilities and must identify infrastructure deployments that do not meet best practices. Which AWS service can the company use to meet these requirements?',
            'question_type': 'multiple_choice',
            'options': [
                'AWS Trusted Advisor',
                'Amazon Inspector',
                'AWS Config',
                'Amazon GuardDuty'
            ],
            'correct_answers': [1],
            'explanation': 'Amazon Inspector é um serviço de avaliação de segurança automatizada que ajuda a melhorar a segurança e conformidade de aplicações implantadas na AWS.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Billing, Pricing, and Support',
            'question_text': 'Which AWS services or tools can identify rightsizing opportunities for Amazon EC2 instances? (Choose two.)',
            'question_type': 'multiple_response',
            'options': [
                'AWS Cost Explorer',
                'AWS Billing Conductor',
                'Amazon CodeGuru',
                'Amazon SageMaker',
                'AWS Compute Optimizer'
            ],
            'correct_answers': [0, 4],
            'explanation': 'AWS Cost Explorer e AWS Compute Optimizer podem identificar oportunidades de rightsizing para instâncias EC2.',
            'difficulty': 'medium'
        }
    ]
    
    with app.app_context():
        for q_data in questions_data:
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
        print(f"Adicionadas {len(questions_data)} questões de exemplo!")

if __name__ == '__main__':
    print("Inicializando banco de dados...")
    create_tables()
    populate_questions()
    print("Banco de dados inicializado com sucesso!")

