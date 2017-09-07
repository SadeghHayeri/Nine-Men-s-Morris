from flask import Flask, request, abort
import random, json
from game import Game
from aiplayer import AIPlayer
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

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
    if selected_position not in GAME.get_empty_positions():
        raise Exception('%d is not empty!' % selected_position)
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
    if (origin, destination) not in GAME.get_valid_movements():
        raise Exception('%d -> %d is not a valid movement!' % (origin, destination))
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
    if selected_piece not in GAME.get_enemy_positions():
        raise Exception('%d is not valid enemy position!' % selected_piece)
    return json.dumps({
        'selectedPiece': selected_piece
    })
