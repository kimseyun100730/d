from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 알림장을 저장하는 리스트 (예시)
notices = []

# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect('/notices')
        else:
            return 'Invalid username or password'
    return render_template('login.html')

# 로그아웃
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

# 알림장 목록 페이지 (인증 필요)
@app.route('/notices')
def notice_list():
    if 'username' in session:
        return render_template('notices.html', notices=notices)
    else:
        return redirect('/login')

# 알림장 작성 페이지 (인증 필요)
@app.route('/notices/create', methods=['GET', 'POST'])
def create_notice():
    if 'username' in session:
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            notice = {'title': title, 'content': content}
            notices.append(notice)
            return redirect('/notices')
        return render_template('create_notice.html')
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run()
