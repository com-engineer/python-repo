# first decide the entry point of the app
import json



def load_data():
    # data will be loaded from the file
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)# what is the type of this
            # print(type (test))#-->list so y why we need to enumerate
            return test# load the data from the file in json formate
    # what if file is not available
    except FileNotFoundError:
        return []
    
# to save the file in the file
def save_data_helper(videos):
    # try except is not used becaused i don't have to return any empty list unlike in load data
    with open('youtube.txt','w') as file:
        json.dump(videos,file)# used to dump the data into file so it take two arguement 1.data 2.location-where to dump


def list_all_videos(videos):
    # user is not going to give the index so it create difficulty to list the videos as per requirement
    # so enumarate help here--add indexing
    # here videos are not in the list formate it is most likely in the string formate
    # for index,video in enumerate(videos,start=1):#normaly start indexing from 0 so we can start from 1 also   
        # print(f"{vid},")
    # since the data was loaded in the list formate so we are trying this
    # for vid in videos:
    #     print(f"{vid},")
    # if we do it without enumerating then we get output like this
#     {'name': 'chai aur python', 'time': '50'},
# {'name': 'chai aur backend', 'time': '15 hours'},
# there is no key to access the individual video details but when we use enumerate we get
# (1, {'name': 'chai', 'time': '2mins'})
# (2, {'name': 'code', 'time': '3mins'})
# this makes the access very easy
    # so we will use initial wala syntax
    print("\n")
    print("*"*70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    
    print("\n")
    print("*"*70)


def add_video(videos):
    # take 2 inpupt name and video time
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video Number to update"))
    if 1<= index <=len(videos):
        name=input("Enter the new video name: ")
        time=input("Enter the new video time: ")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def delete_video(videos):
    list_all_videos(videos)
    index=int(input("ENter the video number to be delelted"))
    if 1<= index <=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager  | choose an option")
        print("1.List all youtube Videos")
        print("2.Add a youtube video")
        print("3.UPdate a youtube video details")
        print("4.Delete a youtube video")
        print("5.Exit the app")

        choice=input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")


if __name__== "__main__":# __ is known as Dunder which means double underscore..here if statement says that if there is any definition in this file with name __main__ then execute it
    # __name__ gives the name of the function
    main()