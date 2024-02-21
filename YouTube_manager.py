import json
def load_data():
    try:
        with open('youtube.txt','r') as  file:
           return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    print("\n")
    print("*" * 90)
    for index,video in enumerate(videos,start=1):
     print(f"{index}.{video['name']},Duration:{video['time']}")
    print("\n")
    print("*" * 90)
def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
def update_video(videos):
   list_all_videos(videos)
   index=int(input("Enter the video number to update: "))
   if 1<=index<=len(videos):
       name=input("Enter the new video name: ")
       time=input("Enter the new video time: ")
       videos[index-1]={'name':name,'time':time}
       save_data_helper(videos)
   else:
       print("Invalid index selected")

def delete_video(videos):
   list_all_videos(videos)
   index=int(input("Enter the video number to be deleted: "))
   if 1<=index<=len(videos):
       del videos[index-1]
       save_data_helper(videos)
   else:
       print("Invalid video index selected")


def main():


 videos = load_data()

 while True:
    print("\n YouTube Manager | Choose your option")
    print("1.List all YouTube videos")
    print("2. Add a YouTube video")
    print("3.Update a YouTube video details")
    print("4.Delete a YouTube video")
    print("5.Exit the App")
    choice = input("Enter your choice: ")
    print(videos)

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
            print("Invalid choice:) ,please choice a correct choice")

#dunder method
if __name__=="__main__":
    main()
