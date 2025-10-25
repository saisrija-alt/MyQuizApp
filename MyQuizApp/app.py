from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "What is 5 + 7?", "options": ["10", "11", "12", "13"], "answer": "12"}
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    score = None
    if request.method == "POST":
        score = 0
        for i, q in enumerate(questions):
            selected = request.form.get(f"question-{i}")
            if selected is None:
                # If a question is unanswered, treat as 0
                continue
            if selected == q["answer"]:
                score += 1
    return render_template("quiz.html", questions=questions, score=score)

if __name__ == "__main__":
    app.run(debug=True)