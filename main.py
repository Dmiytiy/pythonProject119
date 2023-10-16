from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
db = SQLAlchemy(app)

''' Создаём базу данных Question для 3 задания '''
class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, unique=True, nullable=False)
    question_text = db.Column(db.String(500), nullable=False)
    answer_text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

''' Выполняем 1 задание (questions_num = data.get('questions_num', 1). Так же выполняем  2 задание 
       response = requests.get(f'https://jservice.io/api/random?count={questions_num}') ) '''
@app.route('/api/questions', methods=['POST'])
def get_quiz_questions():
    data = request.get_json()
    questions_num = data.get('questions_num', 1)
    quiz_questions = []

    while len(quiz_questions) < questions_num:
        response = requests.get(f'https://jservice.io/api/random?count={questions_num}')
        if response.status_code == 200:
            quiz_data = response.json()
            for question_data in quiz_data:
                existing_question = Question.query.filter_by(question_id=question_data['id']).first()
                if existing_question is None:
                    new_question = Question(
                        question_id=question_data['id'],
                        question_text=question_data['question'],
                        answer_text=question_data['answer']
                    )
                    db.session.add(new_question)
                    db.session.commit()
                    quiz_questions.append({
                        'id': new_question.id,
                        'question_text': new_question.question_text,
                        'answer_text': new_question.answer_text,
                        'created_at': new_question.created_at
                    })
                else:
                    continue
        else:
            return jsonify({'message': 'Не удалось получить вопросы викторины из внешнего API'}), 500

    return jsonify(quiz_questions)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)