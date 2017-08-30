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

      requestAddress = this.server.address + ':' + this.server.port
      switch(this.phase) {
          case PHASE.PLACING:
              requestAddress += '/placing';
              break;
          case PHASE.MOVING:
              requestAddress += '/moving';
              break;
          case PHASE.FLYING:
              requestAddress += '/flying';
              break;
          default:
              console.error('bad phase!')
      }

      var xhttp = new XMLHttpRequest();
      xhttp.open("POST", requestAddress, false);
      xhttp.send(JSON.stringify({
          'phase': this.phase,
          'gameStatus': GAME.board
      }));

      var data = JSON.parse(xhttp.responseText);
      console.log(data);
      switch(this.phase) {
          case PHASE.PLACING:
              position = data.selectedPosition;
              break;
          case PHASE.MOVING:
              pieceAndPosition = [data.selectedPiece, data.selectedPosition];

              position = _.last(pieceAndPosition);
              piecePosition = _.first(pieceAndPosition);
              break;
          case PHASE.FLYING:
              pieceAndPosition = [data.selectedPiece, data.selectedPosition];

              position = _.last(pieceAndPosition);
              piecePosition = _.first(pieceAndPosition);
              break;
          default:
              pieceAndPosition = this.findPlacingPosition();
      }
      if (piecePosition !== undefined) {
          GAME.destroyPiece(piecePosition);
      }
      GAME.setPieceOnPosition(position);

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

});