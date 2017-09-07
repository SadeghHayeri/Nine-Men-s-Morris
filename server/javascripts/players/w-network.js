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
  pickPosition: function() {
      var requestAddress = this.server.address + ':' + this.server.port;
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

      var gameBoard = GAME.board;
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
    selectEnemyPiece : function() {
        requestAddress = this.server.address + ':' + this.server.port;
        requestAddress += '/selectEnemyPiece';

        var gameBoard = GAME.board;
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
    }

});