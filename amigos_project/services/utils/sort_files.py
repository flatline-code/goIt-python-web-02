import os
import zipfile


def sort_files(path: str) -> str:
    original_path = os.path.join(path)
    all_folders = {
      'images': ['jpeg', 'png', 'jpg', 'svg'],
      'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
      'audio': ['mp3', 'ogg', 'wav', 'amr'],
      'video': ['avi', 'mp4', 'mov', 'mkv'],
      'archives': ['zip'],
    }

    all_files = os.listdir(original_path)

    for file in all_files:
        file_path = os.path.join(original_path, file)

        if os.path.isdir(file_path):
            
            if file in all_folders:
                continue

            if not os.listdir(file_path):
                os.rmdir(file_path)
                continue

            sort_files(file_path)

        file_type = file.split('.')[-1]

        if file_type in all_folders['images']:
            if not os.path.exists(os.path.join(original_path, 'images')):
                os.makedirs(os.path.join(original_path, 'images'))      
            
            new_file_path = os.path.join(os.path.join(original_path, 'images'), file)
            os.replace(file_path, new_file_path)

        if file_type in all_folders['documents']:
            if not os.path.exists(os.path.join(original_path, 'documents')):
                os.makedirs(os.path.join(original_path, 'documents'))      
            
            new_file_path = os.path.join(os.path.join(original_path, 'documents'), file)
            os.replace(file_path, new_file_path)

        if file_type in all_folders['audio']:
            if not os.path.exists(os.path.join(original_path, 'audio')):
                os.makedirs(os.path.join(original_path, 'audio'))      
            
            new_file_path = os.path.join(os.path.join(original_path, 'audio'), file)
            os.replace(file_path, new_file_path)
        
        if file_type in all_folders['video']:
            if not os.path.exists(os.path.join(original_path, 'video')):
                os.makedirs(os.path.join(original_path, 'video'))      
            
            new_file_path = os.path.join(os.path.join(original_path, 'video'), file)
            os.replace(file_path, new_file_path)

        if file_type in all_folders['archives']:
            if not os.path.exists(os.path.join(original_path, 'archives')):
                os.makedirs(os.path.join(original_path, 'archives'))      
            
            new_file_path = os.path.join(os.path.join(original_path, 'archives'), file)
            os.replace(file_path, new_file_path)
            
            unzip_folder = file.removesuffix(f'.{file_type}')
            unzip_folder_path = os.path.join(os.path.join(original_path, 'archives'), unzip_folder)
            archive = zipfile.ZipFile(new_file_path)
            archive.extractall(unzip_folder_path)

    return 'files sorted'
