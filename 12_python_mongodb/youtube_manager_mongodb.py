# import pymongo instead of importing complete pymongo we can just import MongoClient from pymongo
from pymongo import MongoClient
from bson import ObjectId

# create client
client = MongoClient("mongodb+srv://gaurav0207vesit_db_user:K0XZweTua6IzWiil@cluster0.nggldjw.mongodb.net/?appName=Cluster0")# this should not be pushed on the github so recommended to keep in .env file  git ignore
# not a good practice to include id and password in the file

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)


def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})


def list_videos():
    for vid in video_collection.find():# return iteratable
        print(f"ID: {vid['_id']}, Name: {vid["name"]}, Time: {vid["time"]}")
    

def update_video(video_id,new_name,new_time):
    # print( type(video_id))
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set":{"name": new_name,"time":new_time}}
        )

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})

def main():
    while True:
        # here after while no need to close the connection it do not create any prblm like sql
        print("\n Youtube Manager App | Choose your Options")
        print("1. List all Videos")
        print("2. Add a Video")
        print("3. Update the Video")
        print("4. Delete the Video")
        print("5. Exit the App")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter the video_id: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter the video_id: ")
            
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")



if __name__ == "__main__":
    main()