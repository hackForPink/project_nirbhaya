from flask import Flask
from flask import request
from flask_restful import Resource, Api
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
api = Api(app)

class Quotes(Resource):
    def get(self):
        input_text = request.args['text']
        resp = my_bot.get_response(input_text)
        print(resp)
        return jsons.dumps(resp)
api.add_resource(Quotes, '/chat')

my_bot = ChatBot(name='PyBot', read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])


corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')


if __name__ == '__main__':
    app.run(debug=True)
