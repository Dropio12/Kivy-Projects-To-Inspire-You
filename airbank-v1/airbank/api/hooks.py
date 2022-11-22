
class Client(object):
    def __init__(self) -> None:
        pass

    def get_shared(self):
        shared = [
            {
                "id": "7790",
                "title": "Wedding Photos",
                "total": 230,
                "users": [
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/avatar.jpg",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-1.png",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-2.png",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-3.png",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-4.png",
                    },
                ]
            },
            {
                "id": "7791",
                "title": "My Awesome Fishing trip",
                "total": 210,
                "users": [
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/avatar.jpg",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-1.png",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-3.png",
                    },
                ]
            },
            {
                "id": "7795",
                "title": "Julian's Graduation",
                "total": 230,
                "users": [
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/avatar.jpg",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-1.png",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-2.png",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-4.png",
                    },
                ]
            },
            {
                "id": "7710",
                "title": "Dapware Illustrations",
                "total": 230,
                "users": [
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-3.png",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/avatar.jpg",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-4.png",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-1.png",
                    },
                    {
                        "name": "Samuel M",
                        "avatarUrl": "assets/imgs/user-2.png",
                    },
                ]
            },
        ]

        return shared

    def get_storage(self):
        store = [
            {
                "id": "one-d",
                "title": "One Drive",
                "iconUrl": "assets/icons/ic_onedrive.png",
                "total": "25GB",
                "used": "5GB",
            },
            {
                "id": "db",
                "title": "DropBox",
                "iconUrl": "assets/icons/ic_dropbox.png",
                "total": "1024GB",
                "used": "645GB",
            },
            {
                "id": "gdrive",
                "title": "Google Drive",
                "iconUrl": "assets/icons/ic_drive.png",
                "total": "250GB",
                "used": "50GB",
            },
        ]

        return store

    def get_quick_access(self):
        quick = [
            {
                "id": "q-01",
                "fileType": "pdf",
                "name": "Kivy docs - Full.pdf",
                "size": "1.5mb"
            },
            {
                "id": "q-04",
                "fileType": "mp3",
                "name": "Linkin Park - Battle Symphony.mp3",
                "size": "2.2mb"
            },
            {
                "id": "q-02",
                "fileType": "png",
                "name": "Screenshot - Dapware_2022.12.05-23:01.png",
                "size": "4.1mb"
            },
            {
                "id": "q-03",
                "fileType": "odt",
                "name": "Udemy Course-Lesson Plan.odt",
                "size": "542kb"
            },
        ]

        return quick

    def get_recents(self):
        recents = [
            {
                "id": "rc-001",
                "title": "Udemy Course-Lesson Plan.odt",
                "modified": "2022-12-06 14:56:23",
            },
            {
                "id": "rc-023",
                "title": "Gym Workout Meal Plan.odt",
                "modified": "2022-04-06 23:56:23",
            },
            {
                "id": "rc-041",
                "title": "Airbank UI Design-Dashboard_Cover.png",
                "modified": "2022-12-06 08:46:23",
            },
            {
                "id": "rc-041",
                "title": "UI Design Speedtalk - Saturday Meet.mp4",
                "modified": "2022-12-06 17:23:21",
            },
            {
                "id": "rc-041",
                "title": "Create Crypto App With Kivy Intro.mp4",
                "modified": "2022-12-06 12:04:13",
            },
            {
                "id": "rc-041",
                "title": "Saturday's Hackathon Spring Talk.mp3",
                "modified": "2022-12-06 10:23:49",
            },
        ]

        return recents
    
    def get_usage(self):
        used = [
            {
                "title": "music",
                "totalFiles": "1023",
                "used": "45GB",
                "iconName": "music",
            },
            {
                "title": "images",
                "totalFiles": "1210",
                "used": "87GB",
                "iconName": "image",
            },
            {
                "title": "videos",
                "totalFiles": "834",
                "used": "97GB",
                "iconName": "film",
            },
            {
                "title": "documents",
                "totalFiles": "5420",
                "used": "32GB",
                "iconName": "file",
            },
        ]

        return used