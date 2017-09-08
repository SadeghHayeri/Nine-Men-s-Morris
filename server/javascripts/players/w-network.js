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
  createBoard: function () {
      var marker = this.marker;
      return _.map(GAME.board, function (cell) {
          if (cell === true) {
              if(marker === false)
                  return -1;
              else
                  return 1;
          }
          else if (cell === false) {
              if(marker === false)
                  return 1;
              else
                  return -1;
          }
          else
              return 0;
      });
  },
  pickPosition: function() {
      var requestAddress = this.server.address + ':' + this.server.port + '/client';
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

      var gameBoard = this.createBoard();

      headers = {'Content-Type': 'application/json'};
      body = JSON.stringify({
          'phase': this.phase.value,
          'gameBoard': gameBoard
      });


      var request = new XMLHttpRequest();
      request.open('POST', requestAddress, false);
      for (var name in headers)
          request.setRequestHeader(name, headers[name]);
      request.send(body);
      console.log(request.responseText);


      var data = JSON.parse(request.responseText);
      console.log(this.username + ' Destroy ' + JSON.stringify(data));
      switch(this.phase) {
          case PHASE.PLACING:
              GAME.setPieceOnPosition(data.result);
              break;
          case PHASE.MOVING:
          case PHASE.FLYING:
              GAME.destroyPiece(data.result[0]);
              GAME.setPieceOnPosition(data.result[1]);
              break;
          default:
              console.error('bad phase!')
      }
  },
    selectEnemyPiece : function() {
        requestAddress = this.server.address + ':' + this.server.port;
        requestAddress += '/selectEnemyPiece';

        var gameBoard = this.createBoard();

        var xhttp = new XMLHttpRequest();
        xhttp.open("POST", requestAddress, false);
        xhttp.send(JSON.stringify({
            'phase': this.phase.value,
            'gameBoard': gameBoard
        }));

        var data = JSON.parse(xhttp.responseText);
        return data.result
    }

});