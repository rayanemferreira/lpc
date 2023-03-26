
# Flask is used to handle the web requests
from flask import Flask, jsonify, request, render_template

# Sql alchemy handles all SQL interactions, but rather than using and overly relying on the ORM,
# Ill use raw SQL commands. The SQL server is running on RDS (AWS) with PostgreSQL
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Allow CORS - so it will work from both the webserver and python
from flask_cors import CORS
from waitress import serve
# This is used to hash passwords and validate them - could of used a different tool, or built it myself, but
# But this is prebuilt and purpose designed
import bcrypt
import secrets
# This starts the App
app = Flask(__name__)
# Allow the cors to work
CORS(app)
# Gets the database URL, creates the connection

engine = create_engine(
'sqlite:///test.db',
connect_args={'check_same_thread': False}
)

db = scoped_session(sessionmaker(bind=engine))


db.execute('''
CREATE TABLE IF NOT EXISTS leaderboard (
    id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
    initials VARCHAR(255),
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255)
)''')
db.commit()
db.execute('''
CREATE TABLE IF NOT EXISTS scores(
    id INT,
    scores INT
)
''')
db.commit()
db.execute('''
CREATE TABLE IF NOT EXISTS tokens (
    id INT,
    token VARCHAR
    )
''')
db.commit()

@app.route('/test', methods=['GET'])
def test():
    return render_template('error.html')

@app.route('/', methods=['GET'])
def index():
    leaders = db.execute('''SELECT leaderboard.initials, scores
    FROM leaderboard
    LEFT JOIN scores
    ON leaderboard.id = scores.id
    ORDER BY scores DESC
    LIMIT 10;''')
    # ...so we convert it into a dictionary
    a, d = [], {}
    for lead in leaders:
        a.append({"initials":lead[0],"scores":lead[1] })
    return render_template('index.html', a=a)


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html')


@app.route('/robo/leaderboard', methods=['GET'])
def leader():
    """
    This route fetches the top 10 results from the server, allowing the page to display the leaderbaord
    :return:
    """
    # This returns a Result Proxy object...
    leaders = db.execute('''SELECT leaderboard.initials, scores
        FROM leaderboard
        LEFT JOIN scores
        ON leaderboard.id = scores.id
        ORDER BY scores DESC
        LIMIT 10;''')
    # ...so we convert it into a dictionary
    a, d = [], {}
    for lead in leaders:
        a.append({"initials": lead[0], "scores": lead[1]})
    return jsonify(a)


@app.route('/robo/user/<string:userid>', methods=['GET'])
def user(userid):
    """
    This returns a users high score, given their ID - this means that the API will have to fetch the ID first
    Could it have used the username? probably.
    :param userid:
    :return:
    """
    score = list(db.execute(f'''SELECT score
FROM leaderboard
LEFT JOIN scores
ON leaderboard.id = scores.id
WHERE leaderboard.id = {userid}
ORDER BY scores DESC
LIMIT 1;'''))[0][0]
    return jsonify({'score': score})


@app.route('/robo/userid/<string:username>', methods=['GET'])
def useridget(username):

    """
    This is used to get the id of a user, from their username (which has to be unique)
    Returns a 0 if the username is not unique
    :param username:
    :return:
    """
    userid = list(db.execute(f"""SELECT leaderboard.id
FROM leaderboard
WHERE leaderboard.username = '{username}'
LIMIT 1;"""))
    try:
        print(userid)
        return jsonify({'id': userid[0][0]})
    except IndexError:
        return jsonify({'id': 0})


@app.route('/login', methods=['POST'])
def login():
    """
    Used to login to the game, returns a  token which is used to verify the user.
    :return:
    """

    userid = request.values.get('userid')
    password = request.values.get('password')
    print(userid)
    hashed = list(db.execute(f'''SELECT password
        FROM leaderboard
        WHERE leaderboard.id = {userid}
        LIMIT 1;'''))[0][0]
    valid = bcrypt.checkpw(password.encode(), hashed.encode())
    if not valid:
        return jsonify({'message': 'password fail'})
    else:
        try:
            token = list(db.execute(f'''SELECT token
            FROM tokens
            WHERE id = {userid}
            LIMIT 1;'''))[0][0]
            return jsonify({'token': token})
        except:
            token = secrets.token_urlsafe(30)
            db.execute(f"""INSERT INTO tokens (id, token)
                VALUES ('{userid}','{token}');""")
            db.commit()
            return jsonify({'token': token})


@app.route('/robo/addscore', methods=['POST'])
def add():
    """
    Used to add scores to the database, uses a post request. Must provide a password to add a score.
    This might be slightly annoying, but adding in functionality for tokens and storing them in python
    feels like a lot of work, maybe I will, but I probably wont invest my time there, I could always cache the
    password inputted in the python code instead.
    :return:
    """
    userid = request.values.get('userid')
    score = int(request.values.get('score'))
    token = request.values.get('token')

    tokenDB = list(db.execute(f'''SELECT token
    FROM tokens
    WHERE id = {userid}
    LIMIT 1;'''))[0][0]
    valid = token == tokenDB

    if not valid:
        return jsonify({'message': 'password fail'})
    try:
        db.execute(f'''INSERT INTO scores (id, scores)
    VALUES ({userid},{score});''')
        db.commit()

        return jsonify({'message': 'success'})
    except:
        return jsonify({'message': 'fail'})


@app.route('/robo/adduser', methods=['POST'])
def adduser():
    """
    This is the API used to add a user to the database, users provide a username, initials and their password.
    Password validation will be done client side, need to keep this app as lightweight as possible.
    :return:
    """
    username = request.values.get('username')
    initials = request.values.get('initials')
    password = request.values.get('password')

    tostore = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    db.execute(f"""INSERT INTO leaderboard (initials, username, password)
    VALUES ('{initials}','{username}','{tostore}');""")
    db.commit()

    return jsonify({'message': 'success'})


if __name__ == '__main__':
    app.run()
