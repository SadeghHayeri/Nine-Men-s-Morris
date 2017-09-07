from flask import Flask, request, abort
import random, json
from game import Game
from aiplayer import AIPlayer
app = Flask(__name__)

GAME = Game()
PLAYER = AIPlayer(GAME)

@app.route('/', methods=['GET'])
def hello():
    return 'salam!'

@app.route('/placing', methods=['POST'])
def placing():
    data = request.data
    dataDict = json.loads(data)
    print dataDict

    global GAME, PLAYER
    GAME.set_game(
        dataDict['gameBoard'],
        dataDict['phase']
    )
    selected_position = PLAYER.place()
    return json.dumps({
        'selectedPosition': selected_position
    })

@app.route('/moving', methods=['POST'])
def moving():
    data = request.data
    dataDict = json.loads(data)
    print dataDict

    global GAME, PLAYER
    GAME.set_game(
        dataDict['gameBoard'],
        dataDict['phase']
    )
    origin, destination = PLAYER.move()
    return json.dumps({
        'origin': origin,
        'destination': destination
    })

@app.route('/selectEnemyPiece', methods=['POST'])
def destroyPiece():
    data = request.data
    dataDict = json.loads(data)
    print dataDict

    global GAME, PLAYER
    GAME.set_game(
        dataDict['gameBoard'],
        dataDict['phase']
    )
    selected_piece = PLAYER.select_enemy_piece()
    return json.dumps({
        'selectedPiece': selected_piece
    })
