try:
    from cv_ml import main
except ImportError:
    print('you do not have the required files in the script directory')
    quit()
try:
    import cv2
except ImportError:
    import subprocess
    res = input(print('It seems that you dont have OpenCV installed, do you wish to install it? (Y/N)'))
    if res.upper == 'Y':
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python'])
    elif res.upper == 'N':
        print('aborting install, run cancelled!')
        quit()
    else:
        print('please give a valid response')
print('starting program', 'press ESC to quit', sep='\n')
main()
