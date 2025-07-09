#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from src.models.user import db
from src.models.question import Question
from src.main import app
import json

def populate_clf_c02_questions():
    """Popula questões do CLF-C02"""
    questions = [
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
            'explanation': 'Amazon Inspector é um serviço de avaliação de segurança automatizada que ajuda a melhorar a segurança e conformidade de aplicações implantadas na AWS. Ele avalia automaticamente aplicações quanto a vulnerabilidades ou desvios das melhores práticas.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Technology and Services',
            'question_text': 'A company has a centralized group of users with large file storage requirements that have exceeded the space available on premises. The company wants to extend its file storage capabilities for this group while retaining the performance benefit of sharing content locally. What is the MOST operationally efficient AWS solution for this scenario?',
            'question_type': 'multiple_choice',
            'options': [
                'Create an Amazon S3 bucket for each user. Mount each bucket by using an S3 file system mounting utility.',
                'Configure and deploy an AWS Storage Gateway file gateway. Connect each user\'s workstation to the file gateway.',
                'Move each user\'s working environment to Amazon WorkSpaces. Set up an Amazon WorkDocs account for each user.',
                'Deploy an Amazon EC2 instance and attach an Amazon Elastic Block Store (Amazon EBS) Provisioned IOPS volume. Share the EBS volume directly with the users.'
            ],
            'correct_answers': [1],
            'explanation': 'AWS Storage Gateway file gateway permite que você armazene arquivos como objetos no Amazon S3, enquanto mantém acesso local através de protocolos de arquivo padrão (NFS/SMB). Isso fornece a extensão de armazenamento necessária mantendo o desempenho local.',
            'difficulty': 'hard'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Security and Compliance',
            'question_text': 'According to security best practices, how should an Amazon EC2 instance be given access to an Amazon S3 bucket?',
            'question_type': 'multiple_choice',
            'options': [
                'Hard code an IAM user\'s secret key and access key directly in the application, and upload the file.',
                'Store the IAM user\'s secret key and access key in a text file on the EC2 instance, read the keys, then upload the file.',
                'Have the EC2 instance assume a role to obtain the privileges to upload the file.',
                'Modify the S3 bucket policy so that any service can upload to it at any time.'
            ],
            'correct_answers': [2],
            'explanation': 'A melhor prática de segurança é usar IAM roles para instâncias EC2. Isso elimina a necessidade de armazenar credenciais de longo prazo na instância e fornece credenciais temporárias automaticamente rotacionadas.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Concepts',
            'question_text': 'Which option is a customer responsibility when using Amazon DynamoDB under the AWS Shared Responsibility Model?',
            'question_type': 'multiple_choice',
            'options': [
                'Physical security of DynamoDB',
                'Patching of DynamoDB',
                'Access to DynamoDB tables',
                'Encryption of data at rest in DynamoDB'
            ],
            'correct_answers': [2],
            'explanation': 'No modelo de responsabilidade compartilhada, o cliente é responsável pelo controle de acesso aos recursos, incluindo tabelas do DynamoDB. A AWS é responsável pela segurança física, patches e criptografia da infraestrutura.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Concepts',
            'question_text': 'Which option is a perspective that includes foundational capabilities of the AWS Cloud Adoption Framework (AWS CAF)?',
            'question_type': 'multiple_choice',
            'options': [
                'Sustainability',
                'Performance efficiency',
                'Governance',
                'Reliability'
            ],
            'correct_answers': [2],
            'explanation': 'Governance é uma das seis perspectivas fundamentais do AWS CAF. As perspectivas são: Business, People, Governance, Platform, Security e Operations.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Technology and Services',
            'question_text': 'A company is running and managing its own Docker environment on Amazon EC2 instances. The company wants an alternative to help manage cluster size, scheduling, and environment maintenance. Which AWS service meets these requirements?',
            'question_type': 'multiple_choice',
            'options': [
                'AWS Lambda',
                'Amazon RDS',
                'AWS Fargate',
                'Amazon Athena'
            ],
            'correct_answers': [2],
            'explanation': 'AWS Fargate é um mecanismo de computação serverless para containers que funciona com Amazon ECS e EKS. Ele remove a necessidade de gerenciar servidores, permitindo que você se concentre no design e construção de suas aplicações.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Cloud Concepts',
            'question_text': 'A company wants to run a NoSQL database on Amazon EC2 instances. Which task is the responsibility of AWS in this scenario?',
            'question_type': 'multiple_choice',
            'options': [
                'Update the guest operating system of the EC2 instances.',
                'Maintain high availability at the database layer.',
                'Patch the physical infrastructure that hosts the EC2 instances.',
                'Configure the security group firewall.'
            ],
            'correct_answers': [2],
            'explanation': 'No modelo de responsabilidade compartilhada, a AWS é responsável pela infraestrutura física, incluindo patches do hardware e hypervisor. O cliente é responsável pelo sistema operacional guest, aplicações e configurações.',
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
            'explanation': 'AWS Cost Explorer e AWS Compute Optimizer podem identificar oportunidades de rightsizing. O Cost Explorer fornece recomendações de rightsizing baseadas em uso histórico, enquanto o Compute Optimizer usa machine learning para analisar métricas e recomendar recursos otimais.',
            'difficulty': 'medium'
        },
        {
            'certification': 'CLF-C02',
            'domain': 'Security and Compliance',
            'question_text': 'Which of the following are benefits of using AWS Trusted Advisor? (Choose two.)',
            'question_type': 'multiple_response',
            'options': [
                'Providing high-performance container orchestration',
                'Creating and rotating encryption keys',
                'Detecting underutilized resources to save costs',
                'Improving security by proactively monitoring the AWS environment',
                'Implementing enforced tagging across AWS resources'
            ],
            'correct_answers': [2, 3],
            'explanation': 'AWS Trusted Advisor fornece recomendações em cinco categorias: otimização de custos, performance, segurança, tolerância a falhas e limites de serviço. Ele detecta recursos subutilizados para economia de custos e monitora proativamente o ambiente para melhorar a segurança.',
            'difficulty': 'medium'
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
        print(f"Adicionadas {len(questions)} questões CLF-C02")

def populate_sample_questions():
    """Popula questões de exemplo para outras certificações"""
    
    # Questões AIF-C01
    aif_questions = [
        {
            'certification': 'AIF-C01',
            'domain': 'Fundamentals of AI and ML',
            'question_text': 'What is the primary difference between supervised and unsupervised machine learning?',
            'question_type': 'multiple_choice',
            'options': [
                'Supervised learning uses labeled data, while unsupervised learning uses unlabeled data',
                'Supervised learning is faster than unsupervised learning',
                'Supervised learning requires more computational power',
                'Supervised learning only works with numerical data'
            ],
            'correct_answers': [0],
            'explanation': 'A principal diferença é que o aprendizado supervisionado usa dados rotulados (com respostas conhecidas) para treinar o modelo, enquanto o aprendizado não supervisionado encontra padrões em dados não rotulados.',
            'difficulty': 'easy'
        },
        {
            'certification': 'AIF-C01',
            'domain': 'Fundamentals of Generative AI',
            'question_text': 'Which AWS service provides pre-trained foundation models for generative AI applications?',
            'question_type': 'multiple_choice',
            'options': [
                'Amazon SageMaker',
                'Amazon Bedrock',
                'Amazon Comprehend',
                'Amazon Rekognition'
            ],
            'correct_answers': [1],
            'explanation': 'Amazon Bedrock é o serviço da AWS que fornece acesso a modelos de fundação pré-treinados de várias empresas através de uma API unificada, facilitando a construção de aplicações de IA generativa.',
            'difficulty': 'medium'
        }
    ]
    
    # Questões SAA-C03
    saa_questions = [
        {
            'certification': 'SAA-C03',
            'domain': 'Design Secure Architectures',
            'question_text': 'A company needs to ensure that data stored in Amazon S3 is encrypted at rest. Which approach provides the MOST operational efficiency?',
            'question_type': 'multiple_choice',
            'options': [
                'Use client-side encryption before uploading to S3',
                'Enable S3 default encryption with SSE-S3',
                'Use AWS KMS keys for every object',
                'Implement application-level encryption'
            ],
            'correct_answers': [1],
            'explanation': 'Habilitar a criptografia padrão do S3 com SSE-S3 é a abordagem mais eficiente operacionalmente, pois criptografa automaticamente todos os objetos sem necessidade de configuração adicional por objeto.',
            'difficulty': 'medium'
        }
    ]
    
    # Questões SAP-C02
    sap_questions = [
        {
            'certification': 'SAP-C02',
            'domain': 'Design for Organizational Complexity',
            'question_text': 'A large enterprise wants to implement a multi-account strategy with centralized billing and governance. Which AWS service combination would be MOST appropriate?',
            'question_type': 'multiple_choice',
            'options': [
                'AWS Control Tower and AWS Organizations',
                'AWS Config and AWS CloudTrail',
                'AWS IAM and AWS CloudFormation',
                'AWS Systems Manager and AWS Service Catalog'
            ],
            'correct_answers': [0],
            'explanation': 'AWS Control Tower e AWS Organizations fornecem a melhor combinação para estratégia multi-conta com governança centralizada, billing consolidado e implementação automatizada de guardrails de segurança.',
            'difficulty': 'hard'
        }
    ]
    
    all_questions = aif_questions + saa_questions + sap_questions
    
    with app.app_context():
        for q_data in all_questions:
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
        print(f"Adicionadas {len(all_questions)} questões de exemplo para outras certificações")

if __name__ == '__main__':
    print("Populando banco de dados com questões...")
    populate_clf_c02_questions()
    populate_sample_questions()
    print("Banco de dados populado com sucesso!")

