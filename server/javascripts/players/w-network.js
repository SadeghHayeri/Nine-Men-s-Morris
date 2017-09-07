/**
 * Define a network player
 * @type {Object}
 */
 var Network = Player.extend({
  init: function(address, port, username, marker) {
    this._super('network', username, marker);
    this.pieceSelected = undefined;
    this.server = {
        address: address,
        port: port
    }
  },
  pickPosition: function(position) {
      var position, piecePosition, pieceAndPosition;

      requestAddress = this.server.address + ':' + this.server.port;
      switch(this.phase) {
          case PHASE.PLACING:
              requestAddress += '/placing';
              break;
          case PHASE.MOVING:
          case PHASE.FLYING:
              requestAddress += '/moving';
              break;
          default:
              console.error('bad phase!')
      }

      var gameBoard = GAME.board
      if(this.marker === false) {
          gameBoard = _.map(GAME.board, function (x) {
              if (x === true) {
                  return false;
              }
              else if (x === false) {
                  return true;
              }
              return x
          });
      }

      var xhttp = new XMLHttpRequest();
      xhttp.open("POST", requestAddress, false);
      xhttp.send(JSON.stringify({
          'phase': this.phase,
          'gameBoard': gameBoard
      }));

      var data = JSON.parse(xhttp.responseText);
      console.log(this.username + ' Destroy ' + JSON.stringify(data));
      switch(this.phase) {
          case PHASE.PLACING:
              GAME.setPieceOnPosition(data.selectedPosition);
              break;
          case PHASE.MOVING:
          case PHASE.FLYING:
              GAME.destroyPiece(data.origin);
              GAME.setPieceOnPosition(data.destination);
              break;
          default:
              console.error('bad phase!')
      }
  },
    findPlacingPosition : function() {
        var selectedPosition, dangerPosition;
        var weightedLines = this.setLinesWeight();

        var dangerLine = this.dangerousEnemyLine();
        if (dangerLine !== undefined) {
            dangerPosition = this.pickEmptyPositionFromLine(dangerLine);
        }

        if (!_.isEmpty(weightedLines)) {
            weightedLines = _.sortBy(weightedLines, function(line) { return -line[1]; });
            if (_.first(weightedLines)[1] === 2) {
                selectedPosition = this.pickEmptyPositionFromLine(_.first(weightedLines)[0]);
            } else if (dangerPosition !== undefined) {
                selectedPosition = dangerPosition;
            } else {
                selectedPosition = this.pickEmptyPositionFromLine(_.first(weightedLines)[0]);
            }
        }

        if (selectedPosition === undefined) {
            if (dangerPosition !== undefined) {
                selectedPosition = dangerPosition;
            } else {
                var emptyLine = this.getEmptyLine();
                if (emptyLine !== undefined) {
                    selectedPosition = _.shuffle(emptyLine)[0];
                } else {
                    selectedPosition = _.random(GAME.boardSize - 1);
                }
            }
        }
        return selectedPosition;
    },
    selectEnemyPiece : function() {
        requestAddress = this.server.address + ':' + this.server.port;
        requestAddress += '/selectEnemyPiece';

        var gameBoard = GAME.board
        if(this.marker === false) {
            gameBoard = _.map(GAME.board, function (x) {
                if (x === true) {
                    return false;
                }
                else if (x === false) {
                    return true;
                }
                return x
            });
        }

        var xhttp = new XMLHttpRequest();
        xhttp.open("POST", requestAddress, false);
        xhttp.send(JSON.stringify({
            'phase': this.phase,
            'gameBoard': gameBoard
        }));

        var data = JSON.parse(xhttp.responseText);
        return data.selectedPiece
    },

});