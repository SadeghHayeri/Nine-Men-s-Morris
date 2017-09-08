//
// Created by Sadegh on 9/7/2017 AD.
//

#include "game.h"

Game::Game() {
    phase = 0;

    board = vector<int>(24, 0);

    graph.push_back(make_pair(0, 1));
    graph.push_back(make_pair(1, 2));
    graph.push_back(make_pair(2, 3));
    graph.push_back(make_pair(3, 4));
    graph.push_back(make_pair(4, 5));
    graph.push_back(make_pair(5, 6));
    graph.push_back(make_pair(6, 7));
    graph.push_back(make_pair(7, 0));
    graph.push_back(make_pair(1, 9));
    graph.push_back(make_pair(3, 11));
    graph.push_back(make_pair(5, 13));
    graph.push_back(make_pair(7, 15));
    graph.push_back(make_pair(8, 9));
    graph.push_back(make_pair(9, 19));
    graph.push_back(make_pair(10, 11));
    graph.push_back(make_pair(11, 12));
    graph.push_back(make_pair(12, 13));
    graph.push_back(make_pair(13, 14));
    graph.push_back(make_pair(14, 15));
    graph.push_back(make_pair(15, 8));
    graph.push_back(make_pair(8, 9));
    graph.push_back(make_pair(9, 10));
    graph.push_back(make_pair(10, 11));
    graph.push_back(make_pair(11, 12));
    graph.push_back(make_pair(12, 13));
    graph.push_back(make_pair(13, 14));
    graph.push_back(make_pair(14, 15));
    graph.push_back(make_pair(15, 8));
    graph.push_back(make_pair(9, 17));
    graph.push_back(make_pair(11, 19));
    graph.push_back(make_pair(13, 21));
    graph.push_back(make_pair(15, 23));
    graph.push_back(make_pair(16, 17));
    graph.push_back(make_pair(17, 18));
    graph.push_back(make_pair(18, 19));
    graph.push_back(make_pair(19, 20));
    graph.push_back(make_pair(20, 21));
    graph.push_back(make_pair(21, 22));
    graph.push_back(make_pair(22, 23));
    graph.push_back(make_pair(23, 16));
}

void Game::set_game(vector<int>& new_board, int new_phase) {
    board = new_board;
    phase = new_phase;
    empty_positions.clear();
    insider_positions.clear();
    enemy_positions.clear();
    valid_movements.clear();

    for (int i = 0; i < board.size(); ++i) {
        if(board[i] == 0)
            empty_positions.push_back(i);
        else if(board[i] == 1)
            insider_positions.push_back(i);
        else if(board[i] == -1)
            enemy_positions.push_back(i);
        else
            throw "bad phase!";
    }

    for (int &insider_position : insider_positions) {
        for (int &empty_position : empty_positions) {
            bool is_neighbor = is_neighbor_position(insider_position, empty_position);
            if(is_neighbor || can_fly())
                valid_movements.push_back(make_pair(insider_position, empty_position));
        }
    }
}

bool Game::can_fly() {
    return phase == 2;
}

bool Game::is_neighbor_position(int a, int b) {
    for (auto &i : graph) {
        if(a == i.first && b == i.second)
            return true;
        if(b == i.first && a == i.second)
            return true;
    }
    return false;
}

vector<int> Game::get_board() { return board; }

vector<int> Game::get_empty_positions() { return empty_positions; }

vector<int> Game::get_insider_positions() { return insider_positions; }

vector<int> Game::get_enemy_positions() { return enemy_positions; }

vector< pair<int, int> > Game::get_valid_movements() { return valid_movements; }
