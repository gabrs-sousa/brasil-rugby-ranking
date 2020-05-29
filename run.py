import openpyxl

from utils import export_output_file
from functions import map_team_names, format_and_map_games_data, calculate_scores


def run(filename: str, calculate_pre_score: bool, output_file_name: str):
    workbook = openpyxl.load_workbook(filename)
    name_sheet = workbook['Mapeamento']
    teams_dict = map_team_names(name_sheet)

    games_sheet = workbook['Dados']
    games_dict = format_and_map_games_data(games_sheet, teams_dict)
    calculate_scores(teams_dict, games_dict, calculate_pre_score)
    export_output_file(teams_dict, output_file_name)


if __name__ == "__main__":
    filename = r'C:\Users\Gabriel\Documents\Graduação\Projeto-PUB-EPUSP\Ranking\documents\Dados.xlsx'
    run(filename=filename, calculate_pre_score=False, output_file_name='test.xlsx')

