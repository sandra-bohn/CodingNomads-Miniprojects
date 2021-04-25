import os

# assign directory
folder = '/home/sandra/Downloads'
# get list of files in directory
jpgs = []
extensions = []
for root, directories, filenames in os.walk(folder):
    for filename in filenames:
        # find file extensions in directory
        if len(filename.split('.')) > 1:
            extensions.append(filename.split('.')[-1])
        # select jpgs
        if filename.find('.jpg') > -1:
            jpgs.append(os.path.join(root, filename))
# print results
print(f"The JPGs in {folder} are:")
print('\n'.join(jpgs))
print(f"The extensions found in {folder} are:")
print(', '.join(set(extensions)))
