import time
from os import scandir
from os.path import splitext, exists, join
from shutil import move
from time import sleep 
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


source_dir = "/Users/eunahjung/Downloads"
dest_dir_pdf = "/Users/eunahjung/Desktop/pdf" #pdf 
dest_dir_pptx = "/Users/eunahjung/Desktop/pptx" #pptx, key
dest_dir_image = "/Users/eunahjung/Desktop/img" #jpg, png, jpeg
dest_dir_documents = "/Users/eunahjung/Desktop/docs" #docx, pages, xslx, numbers
dest_dir_video = "/Users/eunahjung/Desktop/video" #mp4, mov, avi, wmv

# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"]
# ? supported pdf types
pdf_extensions = [".pdf"]
# ? supported pptx types
pptx_extensions = [".ppt", ".pptx"]

# #this prints out all the filenames in Downloads folder 
# with os.scandir(source_dir) as entries: 
#     for entry in entries: 
#         print(entry.name)

#entry = file name itself without paths
def move_file(dest, entry):
    """
    why do we need to rename the file? bc
    ie. filename: /path/to/current/file.txt -> "path/to/destination/file.txt" 
    """
    move(entry, dest)

class MovingFiles(FileSystemEventHandler):
    #step1: categorize by file types 
    def on_modified(self, event): 
        for entry in scandir(source_dir): 
            name = entry.name
            self.check_pdf_files(entry, name)
            self.check_pptx_files(entry, name)
            self.check_image_files(entry, name)
            self.check_documents_files(entry, name)
            self.check_video_files(entry, name)
    
    #step2: move files to designated folders
    def check_pdf_files(self, entry, name): 
        for pdf_extension in pdf_extensions:
            if name.endswith(pdf_extension) or name.endswith(pdf_extension.upper()):
                move_file(dest_dir_pdf, entry, name)
                logging.info(f"Moved {name} to {dest_dir_pdf}")
    
    def check_pptx_files(self, entry, name):
        for pptx_extension in pptx_extensions:
            if name.endswith(pptx_extension) or name.endswith(pptx_extension.upper()):
                move_file(dest_dir_pptx, entry, name)
                logging.info(f"Moved {name} to {dest_dir_pptx}")

    def check_image_files(self, entry, name):
        for image_extension in image_extensions: 
            if name.endswith(image_extension) or name.endswith(image_extension.upper()): 
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved {name} to {dest_dir_image}")

    def check_documents_files(self, entry, name):
        for document_extension in document_extensions: 
            if name.endswith(document_extension) or name.endswith(document_extension.upper()): 
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved {name} to {dest_dir_documents}")

    def check_video_files(self, entry, name):
        for video_extension in video_extensions: 
            if name.endswith(video_extension) or name.endswith(video_extension.upper()): 
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved {name} to {dest_dir_video}")
            


#initiator 
    #whenever there's a change in the source directory (path), this will trigger the event handler
if __name__ == "__main__": 
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MovingFiles()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
