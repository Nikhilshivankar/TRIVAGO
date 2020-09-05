import os
import shutil

from datetime import date

from data.config import projectPath


def zip_screen_shot_folder():
    today_date = date.today()
    zip_path = os.path.join(projectPath, "output_zip_folder//"+"ScreenShots_"+str(today_date))
    source_folder = os.path.join(projectPath, "screenshots")
    print("Source folder::", source_folder)
    folder_to_attach = shutil.make_archive(zip_path, 'zip', source_folder)
    return folder_to_attach


def delete_zip_file():
    """Method to delete the te batch file if it already exsits at the start of the run """
    print("Inside deleting Batch")
    path_test_data = os.path.join(projectPath)
    text_counter = 0
    for filename in os.listdir(path=path_test_data):
        if filename.endswith('.zip'):
            file_to_delete = filename
            os.remove(path_test_data + file_to_delete)
            text_counter += 1



