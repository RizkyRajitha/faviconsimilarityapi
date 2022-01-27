import traceback
from .imageutil import getDominentColor , get_favicon_from_google , dominent_dataset , get_image_data_from_path_cv , compareFavs , image_data_dict

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)

dir_path.split('/')

dirarr = dir_path.split('/')
dirarr.pop()
dirarr.append('favicons')

favicons_path = '/'.join(dirarr)

# print('favicons path - '+favicons_path)

mode='MSE'

def find_image(url):

    img_path = get_favicon_from_google(url)

    print(img_path)
    if img_path :
        dominentcolor = getDominentColor(img_path)
        print(dominentcolor)
        try:
            print(dominentcolor['color'])
            icons = dominent_dataset[dominentcolor['color']]
            print(icons)
            for icon in icons:
                candidate_img_path = favicons_path+'/'+icon+".ico"
                query_img_path = img_path
                print("can - "+candidate_img_path)
                print("query - "+query_img_path)

                # candidateImg = image_data_dict get_image_data_from_path_cv(candidate_img_path)
                
                candidateImg = image_data_dict[icon+".ico"]
                queryImg = get_image_data_from_path_cv(query_img_path)

                res = compareFavs( mode, 10 , candidateImg ,queryImg)
                print(res)
                if res:
                    print(res)
                    return icon
        except KeyError:
            print("dominentcolor not found")
        except FileNotFoundError : 
            print("FileNotFoundError occurred ")        
            print(traceback.format_exc())
        finally:
            os.remove(img_path)


    else:
        print("favicon not found")
        return False



# def findImage(imgPath , mode):
#   dominentcolor = getDominentColor(imgPath)
#   try:
#     print(dominentcolor['color'])
#     icons = dominentdatadict[dominentcolor['color']]
#     print(icons)
#     for icon in icons:
#       candidateImg = getImageDataFromName('favicons/'+icon+".ico")
#       queryImg = getImageDataFromName(imgPath)

#       res = compareFavs( mode, 10 , candidateImg ,queryImg  )
#       print(res)
#       if res:
#         print(res)
#         return icon
#   except KeyError:
#     print("dominentcolor not found")
#   except FileNotFoundError : 
#     print("FileNotFoundError occurred "+imgPath)        
#     print(traceback.format_exc())
    # print("dominentcolor not found")
    

    # datadict[datapoint['color']] = [datapoint['name']]

  # print(dominentcolor)
  # dominentdatadict