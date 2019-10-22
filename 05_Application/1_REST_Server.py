from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
app.debug = True
api = Api(app)

dvorak = '''
<!DOCTYPE HTML>
<h1>Antonin Dvorak</h1>
<p><strong>Antonín <u>Leopold</u></strong> Dvořák was a Czech composer,
one of the first to achieve worldwide recognition.
Following the Romantic-era nationalist example of
his predecessor Bedřich Smetana, Dvořák frequently
employed rhythms and other aspects of the folk music
of Moravia and his native Bohemia. Dvořák's own style
has been described as <strong>"the fullest recreation of
a national idiom with that of the symphonic tradition,
absorSbing folk influences and finding effective ways of using them".</strong></p>
<img src="piano.jpg" width="100%">
<p style="margin-top:40px;">All of Dvořák's nine operas but his first have librettos in Czech and were intended to convey Czech national spirit, as were some of his choral works. By far the most successful of the operas is Rusalka. Among his smaller works, the seventh Humoresque and the song "Songs My Mother Taught Me" are also widely performed and recorded. He has been described as "arguably the most versatile... composer of his time".[5]</p>
'''


class CreateUser(Resource):
    def get(self):
        return dvorak
api.add_resource(CreateUser, '/user')


class CreateUser2(Resource):
    def get(self):
        return {'status': 'success user2'}
api.add_resource(CreateUser2, '/user2')


class Multi(Resource):
    def get(self, num):
        return {'result': num * 10}
api.add_resource(Multi, '/Multi/<int:num>')

if __name__ == '__main__':
    app.run(host='192.168.0.5')
