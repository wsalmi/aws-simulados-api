from src.models.user import db
from datetime import datetime
import json

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    certification = db.Column(db.String(50), nullable=False)  # CLF-C02, AIF-C01, SAA-C03, SAP-C02
    domain = db.Column(db.String(100), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(20), nullable=False)  # multiple_choice, multiple_response
    options = db.Column(db.Text, nullable=False)  # JSON string
    correct_answers = db.Column(db.Text, nullable=False)  # JSON string
    explanation = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(20), default='medium')  # easy, medium, hard
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'certification': self.certification,
            'domain': self.domain,
            'question_text': self.question_text,
            'question_type': self.question_type,
            'options': json.loads(self.options),
            'correct_answers': json.loads(self.correct_answers),
            'explanation': self.explanation,
            'difficulty': self.difficulty
        }
    
    def to_dict_without_answers(self):
        return {
            'id': self.id,
            'certification': self.certification,
            'domain': self.domain,
            'question_text': self.question_text,
            'question_type': self.question_type,
            'options': json.loads(self.options),
            'difficulty': self.difficulty
        }

class SimulationSession(db.Model):
    __tablename__ = 'simulation_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    certification = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(100), nullable=True)
    total_questions = db.Column(db.Integer, nullable=False)
    correct_answers = db.Column(db.Integer, default=0)
    score = db.Column(db.Float, default=0.0)
    time_taken = db.Column(db.Integer, nullable=True)  # em segundos
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)
    questions_data = db.Column(db.Text, nullable=False)  # JSON com questões e respostas
    
    def to_dict(self):
        return {
            'id': self.id,
            'certification': self.certification,
            'user_name': self.user_name,
            'total_questions': self.total_questions,
            'correct_answers': self.correct_answers,
            'score': self.score,
            'time_taken': self.time_taken,
            'started_at': self.started_at.isoformat() if self.started_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'questions_data': json.loads(self.questions_data) if self.questions_data else []
        }

