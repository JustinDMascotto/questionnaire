from app import create_app

env = 'local'
app = create_app(env)

if __name__ == '__main__':
    app.run(debug=True)