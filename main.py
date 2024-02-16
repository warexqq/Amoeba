from src.interface import terminal

def main():
    term = terminal.SimpleTerminalIF()

    adding_players = True
    while adding_players:
        try:
            term.add_player()
            adding_players = terminal.survey.routines.inquire('Want to add more players? ', default=True)
        except ValueError as e:
            print(e)
            continue



if __name__ == "__main__":
    main()