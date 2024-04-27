from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    data_info = [
        ('Валера', 0),
        ('Гришка Мотовилов', 100),
        ('Илья Сахаров', 100),
        ("Алла Михайловна", 100),
        ("Кирилл Тарасов", 100)
    ]
    return render_template('main_page.html', data=data_info)


if __name__ == '__main__':
    app.run(debug=True)
