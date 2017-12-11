import os
import dropbox
import datetime
import time
import contextlib

@contextlib.contextmanager
def stopwatch(message):
    """Context manager to print how long a block of code took."""
    t0 = time.time()
    try:
        yield
    finally:
        t1 = time.time()
        print('Total elapsed time for %s: %.3f' % (message, t1 - t0))

def check(dbx,folder):
	res = True
	path = '/' + folder
	try:
		test = dbx.files_list_folder(path).entries
	except dropbox.exceptions.ApiError:
		res = False
	return res
def create_folder(dbx,name):
	path = '/' + name
	dbx.files_create_folder(path)

def upload_to_dropbox(dbx, file, folder,timestamp, subfolder='', overwrite=False):
    """Upload a file.
    Return the request response, or None in case of error.
    """
    path = '/%s/%s/%s' % (folder, subfolder.replace(os.path.sep, '/'), file.name)
    while '//' in path:
        path = path.replace('//', '/')
    mode = (dropbox.files.WriteMode.overwrite
            if overwrite
            else dropbox.files.WriteMode.add)
    
    data = file.read()
    with stopwatch('upload %d bytes' % len(data)):
        try:
            res = dbx.files_upload(
                data, path, mode,
                client_modified=timestamp,
                mute=True)
        except dropbox.exceptions.ApiError as err:
            print('*** API error', err)
            return None
    print('uploaded as', res.name.encode('utf8'))
    return res

def list_files(dbx,course_code):
    folder = '/' + course_code
    files_list = dbx.files_list_folder(folder).entries
    for entry in files_list:
        add_time_diff(entry)
    return files_list

def add_time_diff(entry):
    entry.client_modified+=datetime.timedelta(0, 19800)

def get_download_link(dbx,folder,file,subfolder=''):
    path = os.path.join('/',folder,subfolder,file)
    try:
        res = dbx.files_get_temporary_link(path).link
    except  dropbox.exceptions.ApiError as err:
        print('API error',err)
        return None
    return res    
