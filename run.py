from app import create_app

env = 'dev'
app = create_app(env)

if __name__ == '__main__':
    app.run(debug=True)