from flask import Flask, render_template, url_for

app = Flask(__name__)

ADULT_IMG_URL = 'https://i.pinimg.com/originals/16/8d/17/168d17f695066e3d415a2b5e0d4c2381.jpg'
CHILD_IMG_URL = 'https://ae04.alicdn.com/kf/HTB1oKDwXZfrK1RkSmLyq6xGApXam.jpg_640x640.jpg'


@app.route('/table/<gender>/<int:age>')
def table_param(gender: str, age: int):
    params = {'gender': gender, 'age': age, 'child_img_url': CHILD_IMG_URL, 'adult_img_url': ADULT_IMG_URL,
              'style_url': url_for('static', filename='css/7.css')}
    return render_template('table_param.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
