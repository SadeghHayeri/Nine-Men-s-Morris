#include "client.h"
#include "game.h"
#include "AIPlayer.h"

Game game = Game();
AIPlayer player = AIPlayer(game);


int client::placing(int phase, std::vector<int> board) {
    game.set_game(board, phase);
    int selected_position = player.place();

    // validation
    vector<int> empty_positions = game.get_empty_positions();
    bool is_selected_position_valid = false;
    for (int empty_position : empty_positions)
        if(selected_position == empty_position) {
            is_selected_position_valid = true;
            break;
        }
    if(!is_selected_position_valid)
        throw "selected_position is not empty!";

    return selected_position;
}

vector<int> client::moving(int phase, vector<int> board) {
    game.set_game(board, phase);
    pair<int, int> selected_movement = player.move();

    // validation
    vector< pair<int, int> > valid_movements = game.get_valid_movements();
    bool is_movement_valid = false;
    for (pair<int, int> valid_movement : valid_movements)
        if(selected_movement == valid_movement) {
            is_movement_valid = true;
            break;
        }
    if(!is_movement_valid)
        throw "selected_movement is not a valid movement!";

    vector<int> response;
    response.push_back(selected_movement.first);
    response.push_back(selected_movement.second);
    return response;
}

int client::destroyPiece(int phase, std::vector<int> board) {
    game.set_game(board, phase);
    int selected_position = player.select_enemy_piece();

    // validation
    vector<int> enemy_positions = game.get_enemy_positions();
    bool is_selected_position_valid = false;
    for (int enemy_position : enemy_positions)
        if(selected_position == enemy_position) {
            is_selected_position_valid = true;
            break;
        }
    if(!is_selected_position_valid)
        throw "selected_position is not valid enemy position!";

    return selected_position;
}
