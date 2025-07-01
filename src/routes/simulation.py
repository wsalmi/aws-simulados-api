from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.question import Question, SimulationSession
from datetime import datetime
import json
import random

simulation_bp = Blueprint('simulation', __name__)

@simulation_bp.route('/certifications', methods=['GET'])
def get_certifications():
    """Retorna lista de certificações disponíveis"""
    certifications = [
        {
            'code': 'CLF-C02',
            'name': 'AWS Certified Cloud Practitioner',
            'level': 'Foundational',
            'duration': 90,
            'questions': 65,
            'passing_score': 700
        },
        {
            'code': 'AIF-C01',
            'name': 'AWS Certified AI Practitioner',
            'level': 'Foundational',
            'duration': 90,
            'questions': 65,
            'passing_score': 700
        },
        {
            'code': 'SAA-C03',
            'name': 'AWS Certified Solutions Architect - Associate',
            'level': 'Associate',
            'duration': 130,
            'questions': 65,
            'passing_score': 720
        },
        {
            'code': 'SAP-C02',
            'name': 'AWS Certified Solutions Architect - Professional',
            'level': 'Professional',
            'duration': 180,
            'questions': 75,
            'passing_score': 750
        }
    ]
    return jsonify(certifications)

@simulation_bp.route('/questions/<certification>', methods=['GET'])
def get_questions_by_certification(certification):
    """Retorna questões por certificação"""
    questions = Question.query.filter_by(certification=certification).all()
    return jsonify([q.to_dict_without_answers() for q in questions])

@simulation_bp.route('/simulation/start', methods=['POST'])
def start_simulation():
    """Inicia um novo simulado"""
    data = request.get_json()
    certification = data.get('certification')
    user_name = data.get('user_name', 'Anônimo')
    num_questions = data.get('num_questions', 65)
    
    # Busca questões aleatórias da certificação
    all_questions = Question.query.filter_by(certification=certification).all()
    
    if len(all_questions) < num_questions:
        return jsonify({'error': 'Não há questões suficientes para esta certificação'}), 400
    
    # Seleciona questões aleatórias
    selected_questions = random.sample(all_questions, num_questions)
    
    # Cria sessão de simulado
    session = SimulationSession(
        certification=certification,
        user_name=user_name,
        total_questions=num_questions,
        questions_data=json.dumps([q.id for q in selected_questions])
    )
    
    db.session.add(session)
    db.session.commit()
    
    # Retorna questões sem as respostas corretas
    questions_data = [q.to_dict_without_answers() for q in selected_questions]
    
    return jsonify({
        'session_id': session.id,
        'questions': questions_data,
        'certification': certification,
        'total_questions': num_questions
    })

@simulation_bp.route('/simulation/<int:session_id>', methods=['GET'])
def get_simulation(session_id):
    """Retorna dados de um simulado em andamento"""
    session = SimulationSession.query.get_or_404(session_id)
    
    # Se já foi completado, redireciona para resultados
    if session.completed_at:
        return jsonify({'error': 'Simulado já foi concluído'}), 400
    
    # Carrega os IDs das questões
    questions_data_raw = json.loads(session.questions_data)
    
    # Verifica se é o formato novo (com question_ids e detailed_results) ou antigo (só IDs)
    if isinstance(questions_data_raw, dict) and 'question_ids' in questions_data_raw:
        # Formato novo: já foi submetido antes
        question_ids = questions_data_raw['question_ids']
    elif isinstance(questions_data_raw, list):
        # Verifica se é lista de IDs ou lista de resultados detalhados
        if questions_data_raw and isinstance(questions_data_raw[0], dict):
            # Formato antigo: lista de resultados detalhados - extrai os question_ids
            question_ids = [item['question_id'] for item in questions_data_raw]
        else:
            # Formato original: lista de IDs de questões
            question_ids = questions_data_raw
    else:
        return jsonify({'error': 'Formato de dados de questões inválido'}), 400
    
    # Busca as questões
    questions = []
    for question_id in question_ids:
        question = Question.query.get(question_id)
        if question:
            questions.append(question.to_dict_without_answers())
    
    # Busca informações da certificação para pegar a duração
    cert_info = {
        'CLF-C02': {'duration': 90, 'passing_score': 700},
        'AIF-C01': {'duration': 90, 'passing_score': 700},
        'SAA-C03': {'duration': 130, 'passing_score': 720},
        'SAP-C02': {'duration': 180, 'passing_score': 750}
    }
    
    cert_data = cert_info.get(session.certification, {'duration': 90, 'passing_score': 700})
    
    # Retorna dados do simulado
    simulation_data = {
        'id': session.id,
        'certification': session.certification,
        'user_name': session.user_name,
        'total_questions': session.total_questions,
        'duration': cert_data['duration'],
        'passing_score': cert_data['passing_score'],
        'started_at': session.started_at.isoformat() if session.started_at else None
    }
    
    return jsonify({
        'simulation': simulation_data,
        'questions': questions
    })

@simulation_bp.route('/simulation/<int:session_id>/submit', methods=['POST'])
def submit_simulation(session_id):
    """Submete respostas do simulado e calcula resultado"""
    data = request.get_json()
    answers = data.get('answers', {})  # {question_id: [selected_options]}
    time_taken = data.get('time_taken', 0)
    
    session = SimulationSession.query.get_or_404(session_id)
    questions_data_raw = json.loads(session.questions_data)
    
    # Verifica se é o formato novo (com question_ids e detailed_results) ou antigo (só IDs)
    if isinstance(questions_data_raw, dict) and 'question_ids' in questions_data_raw:
        # Formato novo: já foi submetido antes
        question_ids = questions_data_raw['question_ids']
    elif isinstance(questions_data_raw, list):
        # Verifica se é lista de IDs ou lista de resultados detalhados
        if questions_data_raw and isinstance(questions_data_raw[0], dict):
            # Formato antigo: lista de resultados detalhados - extrai os question_ids
            question_ids = [item['question_id'] for item in questions_data_raw]
        else:
            # Formato original: lista de IDs de questões
            question_ids = questions_data_raw
    else:
        return jsonify({'error': 'Formato de dados de questões inválido'}), 400
    
    correct_count = 0
    detailed_results = []
    
    # Itera sobre as questões usando o índice para mapear as respostas do frontend
    for index, question_id in enumerate(question_ids):
        question = Question.query.get(question_id)
        if question is None:
            continue
            
        # Frontend envia respostas usando índice da questão (0, 1, 2, etc.)
        user_answer = answers.get(str(index), [])
        correct_answers = json.loads(question.correct_answers)
        
        is_correct = set(user_answer) == set(correct_answers)
        if is_correct:
            correct_count += 1
            
        detailed_results.append({
            'question_id': question_id,
            'question_text': question.question_text,
            'options': json.loads(question.options),
            'user_answer': user_answer,
            'correct_answers': correct_answers,
            'is_correct': is_correct,
            'explanation': question.explanation,
            'domain': question.domain
        })
    
    # Calcula pontuação (escala 100-1000)
    percentage = (correct_count / session.total_questions) * 100
    scaled_score = int(100 + (percentage / 100) * 900)
    
    # Atualiza sessão
    session.correct_answers = correct_count
    session.score = scaled_score
    session.time_taken = time_taken
    session.completed_at = datetime.utcnow()
    
    # Preserva a estrutura original: mantém IDs das questões e adiciona os resultados detalhados
    original_questions_data = {
        'question_ids': question_ids,  # IDs originais das questões
        'detailed_results': detailed_results  # Resultados detalhados
    }
    session.questions_data = json.dumps(original_questions_data)
    
    db.session.commit()
    
    # Determina se passou
    cert_info = {
        'CLF-C02': 700,
        'AIF-C01': 700,
        'SAA-C03': 720,
        'SAP-C02': 750
    }
    
    passing_score = cert_info.get(session.certification, 700)
    passed = scaled_score >= passing_score
    
    return jsonify({
        'session_id': session_id,
        'score': scaled_score,
        'percentage': percentage,
        'correct_answers': correct_count,
        'total_questions': session.total_questions,
        'passed': passed,
        'passing_score': passing_score,
        'time_taken': time_taken,
        'detailed_results': detailed_results
    })

@simulation_bp.route('/simulation/<int:session_id>/results', methods=['GET'])
def get_simulation_results(session_id):
    """Retorna resultados detalhados de um simulado"""
    session = SimulationSession.query.get_or_404(session_id)
    
    # Busca informações da certificação para pegar passing_score
    cert_info = {
        'CLF-C02': {'duration': 90, 'passing_score': 700},
        'AIF-C01': {'duration': 90, 'passing_score': 700},
        'SAA-C03': {'duration': 130, 'passing_score': 720},
        'SAP-C02': {'duration': 180, 'passing_score': 750}
    }
    
    cert_data = cert_info.get(session.certification, {'duration': 90, 'passing_score': 700})
    
    # Calcula percentual
    percentage = (session.correct_answers / session.total_questions) * 100 if session.total_questions > 0 else 0
    
    # Estrutura dados do simulado
    simulation_data = {
        'id': session.id,
        'certification': session.certification,
        'user_name': session.user_name,
        'total_questions': session.total_questions,
        'passing_score': cert_data['passing_score'],
        'started_at': session.started_at.isoformat() if session.started_at else None,
        'completed_at': session.completed_at.isoformat() if session.completed_at else None
    }
    
    # Carrega questões com respostas do JSON armazenado
    questions_data_raw = json.loads(session.questions_data) if session.questions_data else []
    
    # Verifica o formato dos dados
    if isinstance(questions_data_raw, dict) and 'detailed_results' in questions_data_raw:
        # Formato novo: extrai os resultados detalhados
        questions_with_answers = questions_data_raw['detailed_results']
    elif isinstance(questions_data_raw, list) and questions_data_raw and isinstance(questions_data_raw[0], dict):
        # Formato antigo: os dados já são os resultados detalhados
        questions_with_answers = questions_data_raw
    else:
        # Nenhum resultado encontrado
        questions_with_answers = []
    
    # Renomeia campos para compatibilidade com frontend
    for q in questions_with_answers:
        if 'user_answer' in q:
            q['user_answers'] = q['user_answer']
    
    return jsonify({
        'simulation': simulation_data,
        'score': session.score,
        'percentage': percentage,
        'correct_count': session.correct_answers,
        'total_questions': session.total_questions,
        'questions_with_answers': questions_with_answers
    })

@simulation_bp.route('/questions', methods=['POST'])
def add_question():
    """Adiciona uma nova questão"""
    data = request.get_json()
    
    question = Question(
        certification=data['certification'],
        domain=data['domain'],
        question_text=data['question_text'],
        question_type=data['question_type'],
        options=json.dumps(data['options']),
        correct_answers=json.dumps(data['correct_answers']),
        explanation=data['explanation'],
        difficulty=data.get('difficulty', 'medium')
    )
    
    db.session.add(question)
    db.session.commit()
    
    return jsonify({'message': 'Questão adicionada com sucesso', 'id': question.id}), 201

@simulation_bp.route('/stats/<certification>', methods=['GET'])
def get_certification_stats(certification):
    """Retorna estatísticas de uma certificação"""
    total_questions = Question.query.filter_by(certification=certification).count()
    total_sessions = SimulationSession.query.filter_by(certification=certification).count()
    completed_sessions = SimulationSession.query.filter_by(certification=certification).filter(
        SimulationSession.completed_at.isnot(None)
    ).count()
    
    if completed_sessions > 0:
        avg_score = db.session.query(db.func.avg(SimulationSession.score)).filter_by(
            certification=certification
        ).filter(SimulationSession.completed_at.isnot(None)).scalar()
        
        pass_rate = db.session.query(SimulationSession).filter_by(
            certification=certification
        ).filter(SimulationSession.score >= 700).count() / completed_sessions * 100
    else:
        avg_score = 0
        pass_rate = 0
    
    return jsonify({
        'certification': certification,
        'total_questions': total_questions,
        'total_sessions': total_sessions,
        'completed_sessions': completed_sessions,
        'average_score': round(avg_score, 1) if avg_score else 0,
        'pass_rate': round(pass_rate, 1)
    })

