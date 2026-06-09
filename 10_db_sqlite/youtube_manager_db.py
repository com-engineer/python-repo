import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    create table if not exists videos(
               id integer primary key,
               name text not null,
               time text not null
    )
''')



def list_videos():
    cursor.execute("select * from videos")# return tuple and cursor hold that result
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("insert into videos (name,time) values (?, ?)",(name,time))
    # we need to commit after execution
    conn.commit()

def update_video(vid_id,new_name,new_time):
    cursor.execute("update videos set name=?,time=? where id=?",(new_name,new_time,vid_id))
    conn.commit()

def delete_video(vid_id):
    cursor.execute("delete from videos where id=?",(vid_id,))#we need to add comma for single variable
    conn.commit()


def main():
    # videos=[]
    while True:
        print("\n Youtube Manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            add_video(name,time)
        elif choice=='3':
            vid_id=input("Enter video id to update: ")
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            update_video(vid_id,name,time)
        elif choice=='4':
            vid_id=input("Enter video id to delete: ")
            delete_video(vid_id)
        elif choice=='5':
            break
        else:
            print("Invalid choice")
    
    conn.close()



if __name__ == '__main__':
    main()